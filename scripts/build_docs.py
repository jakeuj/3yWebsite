#!/usr/bin/env python3
"""Extract structured data from the Sango3838 mirrored site for docs."""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Dict, List

try:
    from bs4 import BeautifulSoup  # type: ignore
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Missing dependency beautifulsoup4. Install via `pip install beautifulsoup4`." ) from exc

ROOT = Path(__file__).resolve().parent.parent
CATEGORY_ORDER = ["武器技能", "法術技能", "職業技能", "其他技能"]
CATEGORY_DESCRIPTIONS = {
    "武器技能": "劍、刀、弓、槍、棍、斧、鞭、扇、短兵、拳法、氣功。",
    "法術技能": "火、風、光、聖、雷、水、土、暗、邪、毒系。",
    "職業技能": "格鬥、暗殺、法師、鑄造、吟唱、醫療、盜賊。",
    "其他技能": "步法、技能總覽、技能熟練度。",
}


def read_html(path: Path) -> BeautifulSoup:
    text = path.read_text(encoding="utf-8", errors="ignore")
    return BeautifulSoup(text, "html.parser")


def clean_text(text: str) -> str:
    rows = [re.sub(r"\s+", " ", line.strip()) for line in text.splitlines()]
    return " ".join([r for r in rows if r])


def parse_labeled_block(text: str) -> Dict[str, str]:
    info: Dict[str, str] = {}
    current_key = ""
    current_parts: List[str] = []

    for raw in text.splitlines():
        normalized = re.sub(r"\s+", " ", raw.strip()).replace("﹕", "：")
        if not normalized:
            continue

        if "：" in normalized:
            if current_key:
                info[current_key] = " ".join(current_parts).strip()
            key, value = normalized.split("：", 1)
            current_key = key.strip()
            current_parts = [value.strip()] if value.strip() else []
            continue

        if current_key:
            current_parts.append(normalized)

    if current_key:
        info[current_key] = " ".join(current_parts).strip()

    return info


def relpath(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def markdown_link(path: str) -> str:
    return f"[`{path}`]({{{{ '/{path}' | relative_url }}}})"


def markdown_text(value: str) -> str:
    return value.replace("|", "\\|").strip()


def extract_first_paragraph(soup: BeautifulSoup) -> str:
    for tag in soup.find_all(["p", "td", "div"]):
        text = clean_text(tag.get_text(" ", strip=True))
        if text:
            return text
    return ""


def parse_news(data_root: Path) -> List[Dict[str, str]]:
    news_index = ROOT / "news" / "index.html"
    soup = read_html(news_index)
    entries: List[Dict[str, str]] = []

    for row in soup.find_all("tr"):
        link = row.find("a")
        cols = row.find_all("td")
        if not link or len(cols) < 2:
            continue
        href = link.get("href")
        if not href:
            continue
        article_path = (news_index.parent / href).resolve()
        if not article_path.exists():
            continue
        article_soup = read_html(article_path)
        entries.append(
            {
                "title": link.get_text(strip=True),
                "date": cols[-1].get_text(strip=True),
                "path": relpath(article_path),
                "summary": extract_first_paragraph(article_soup)[:260],
            }
        )
    entries.sort(key=lambda item: item["date"], reverse=True)
    return entries


def parse_skill_index() -> Dict[str, str]:
    index_path = ROOT / "skill" / "index.html"
    soup = read_html(index_path)
    table = soup.find("table", attrs={"width": "450"})
    mapping: Dict[str, str] = {}
    current_category = ""
    if not table:
        return mapping
    for row in table.find_all("tr"):
        header_cell = row.find("td", attrs={"colspan": True})
        if header_cell and header_cell.get_text(strip=True):
            current_category = header_cell.get_text(strip=True)
            continue
        for anchor in row.find_all("a"):
            href = anchor.get("href")
            if href:
                mapping[href] = current_category or "其他"
    return mapping


def parse_skills(mapping: Dict[str, str]) -> List[Dict[str, str]]:
    skill_dir = ROOT / "skill"
    entries: List[Dict[str, str]] = []
    for html_file in sorted(skill_dir.glob("*.html")):
        if html_file.name in {"index.html"} or html_file.name.endswith("-m.html"):
            continue
        soup = read_html(html_file)
        info: Dict[str, str] = {
            "path": relpath(html_file),
            "category": mapping.get(html_file.name, "未分類"),
        }
        target = None
        for p in soup.find_all("p"):
            text = p.get_text("\n", strip=True)
            if "英文名稱" in text:
                target = text
                break
        if target:
            info.update(parse_labeled_block(target))
        title_tag = soup.find("div", align="center")
        if title_tag and "img" not in title_tag.decode_contents():
            info.setdefault("display_name", clean_text(title_tag.get_text()))
        entries.append(info)
    return entries


def parse_realm_docs() -> List[Dict[str, str]]:
    docs = []
    realm_dir = ROOT / "realm" / "doc"
    pattern = re.compile(
        r"指令[：:﹕]\s*(?P<cmd>.+?)(?:\s+說明[：:﹕]\s*(?P<desc>.+?))?(?=指令[：:﹕]|$)",
        re.S,
    )
    for html_file in sorted(realm_dir.glob("*.html")):
        soup = read_html(html_file)
        text = soup.get_text("\n", strip=True)
        commands = []
        for match in pattern.finditer(text):
            cmd = clean_text(match.group("cmd"))
            desc = match.group("desc")
            commands.append(
                {
                    "command": cmd,
                    "description": clean_text(desc) if desc else "",
                }
            )
        docs.append(
            {
                "path": relpath(html_file),
                "commands": [c for c in commands if c.get("command")],
            }
        )
    return docs


def parse_maps() -> List[Dict[str, str]]:
    maps = []
    for html_file in sorted((ROOT / "map").glob("*.html")):
        soup = read_html(html_file)
        title = soup.title.get_text(strip=True) if soup.title else html_file.stem
        summary = extract_first_paragraph(soup)
        maps.append(
            {
                "path": relpath(html_file),
                "title": title,
                "summary": summary[:240],
            }
        )
    return maps


def parse_downloads() -> List[Dict[str, str]]:
    downloads = []
    download_dir = ROOT / "download"
    for html_file in sorted(download_dir.glob("*.html")):
        if html_file.name not in {"index.html"}:
            soup = read_html(html_file)
            summary = extract_first_paragraph(soup)
        else:
            soup = read_html(html_file)
            summary = "鏡像的官方下載入口索引"
        title = soup.title.get_text(strip=True) if soup.title else html_file.stem
        downloads.append(
            {
                "path": relpath(html_file),
                "title": title,
                "summary": summary[:240],
            }
        )
    binaries = []
    for file in download_dir.glob("*.tar.gz"):
        size = file.stat().st_size
        binaries.append(
            {
                "file": relpath(file),
                "size": size,
            }
        )
    return [
        {"pages": downloads},
        {"archives": binaries},
    ]


def parse_links() -> List[Dict[str, str]]:
    candidates = [
        ROOT / "links.html",
        ROOT / "phorum.html",
        ROOT / "link" / "index.html",
    ]
    entries = []
    for html_file in candidates:
        if not html_file.exists():
            continue
        soup = read_html(html_file)
        for anchor in soup.find_all("a"):
            href = anchor.get("href")
            label = anchor.get_text(strip=True)
            if not href or not label:
                continue
            entries.append(
                {
                    "label": label,
                    "href": href,
                    "source": relpath(html_file),
                }
            )
    return entries


def parse_commands() -> List[Dict[str, str]]:
    command_dir = ROOT / "newhand" / "commands"
    entries = []
    for html_file in sorted(command_dir.glob("*.html")):
        soup = read_html(html_file)
        first = extract_first_paragraph(soup)
        entries.append(
            {
                "path": relpath(html_file),
                "title": soup.title.get_text(strip=True) if soup.title else html_file.stem,
                "summary": first[:240],
            }
        )
    return entries


def parse_player_guides() -> List[Dict[str, str]]:
    base = ROOT / "newhand" / "players"
    entries: List[Dict[str, str]] = []
    for html_file in sorted(base.rglob("*")):
        if not html_file.suffix.lower().startswith(".htm"):
            continue
        if html_file.name.startswith("index."):
            continue
        soup = read_html(html_file)
        heading = soup.find("span", class_="text2")
        title = heading.get_text(strip=True) if heading else (
            soup.title.get_text(strip=True) if soup.title else html_file.stem
        )
        entries.append(
            {
                "path": relpath(html_file),
                "category": html_file.relative_to(base).parts[0],
                "title": title,
                "summary": extract_first_paragraph(soup)[:280],
            }
        )
    return entries


def parse_imm_list() -> List[Dict[str, str]]:
    imm_dir = ROOT / "imm"
    entries = []
    for html_file in sorted(imm_dir.glob("*.html")):
        if html_file.name == "index.html":
            continue
        soup = read_html(html_file)
        text = extract_first_paragraph(soup)
        title = soup.title.get_text(strip=True) if soup.title else html_file.stem
        email_match = re.search(r"[\w.-]+@[\w.-]+", text)
        entries.append(
            {
                "path": relpath(html_file),
                "title": title,
                "summary": text[:200],
                "email": email_match.group(0) if email_match else "",
            }
        )
    return entries


def write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_markdown(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def generate_skills_markdown(skills: List[Dict[str, str]]) -> str:
    grouped: Dict[str, List[Dict[str, str]]] = {category: [] for category in CATEGORY_ORDER}
    for skill in skills:
        grouped.setdefault(skill.get("category", "未分類"), []).append(skill)

    lines: List[str] = [
        "---",
        "layout: default",
        "title: 技能資料庫",
        "---",
        "",
        "# 技能資料庫與職業設定",
        "",
        "> 與區域開發的關聯：技能決定 NPC 能力、掉落秘笈、任務獎勵與訓練場內容。此頁依 `docs/data/skills.json` 與 `skill/index.html` 生成，方便在 GitHub Pages 直接查看分類與詳細欄位。",
        "",
        "## 類別統計",
        "",
        "| 類別 | 檔案數 | 說明 |",
        "| --- | --- | --- |",
    ]

    for category in CATEGORY_ORDER:
        lines.append(
            f"| {category} | {len(grouped.get(category, []))} | {CATEGORY_DESCRIPTIONS[category]} |"
        )

    lines.extend(
        [
            "",
            "- `scripts/build_docs.py` 會根據 `skill/index.html` 重建 `docs/data/skills.json` 與本頁；若新增類別或技能頁，請更新來源 HTML 後重跑腳本。",
            "- `skill/learnlv.html` 屬於「技能熟練度」參照頁；它應計入 `skill/index.html` 的分類統計，但不應和一般技能明細頁等量看待。",
            "",
            "## 展開詳細資料",
            "",
            "以下內容可直接在 GitHub Pages 展開查看，不必回到原始 HTML 逐頁翻找。",
        ]
    )

    for category in CATEGORY_ORDER:
        items = grouped.get(category, [])
        if not items:
            continue
        lines.extend(["", f"## {category}", ""])
        for skill in items:
            path = skill["path"]
            is_special = path == "skill/learnlv.html"
            cname = skill.get("中文名稱") or skill.get("display_name") or Path(path).stem
            ename = skill.get("英文名稱", "")
            summary_parts = [f"<strong>{markdown_text(cname)}</strong>"]
            if ename:
                summary_parts.append(f"(`{markdown_text(ename)}`)")
            if is_special:
                summary_parts.append(" - 特殊參照頁")
            lines.append(f"<details><summary>{''.join(summary_parts)}</summary>")
            lines.append("")
            lines.append(f"- 原文頁面：{markdown_link(path)}")
            lines.append(f"- 類別：{category}")
            if is_special:
                lines.append("- 說明：這頁是技能熟練度參照，不是一般技能明細頁，因此不一定會有 `英文名稱 / 中文名稱 / 領悟技能` 等欄位。")
            else:
                for key in [
                    "英文名稱",
                    "中文名稱",
                    "攻擊武器",
                    "互相教導",
                    "技能功能",
                    "技能分類",
                    "浪費數值",
                    "領悟技能",
                    "領悟機率",
                    "預備功夫",
                    "職業限制",
                    "限 制",
                    "教 導",
                ]:
                    value = skill.get(key, "").strip()
                    if value:
                        lines.append(f"- {key}：{markdown_text(value)}")
            lines.append("")
            lines.append("</details>")

    lines.extend(
        [
            "",
            "## 區域設計建議",
            "",
            "1. **掉落／習得來源**：於 `res` 檔內安排 NPC 擁有特定技能，並在 `mob` 描述中註記「可教導」或「僅領悟」。",
            "2. **熟練度上限**：技能頁面常以「馬馬虎虎」、「神乎其技」描述各職業上限，請在 NPC 對話或任務條件中引用這些詞彙，避免與英文 Rank 混用。",
            "3. **資源消耗**：資料欄位中的「浪費數值」可直接映射成戰鬥節奏；例如步法技能多耗體力，在山地或長途區域可安排更多休息節點。",
            "4. **秘笈／study**：任何 `study` 互動都需在區域 `obj` 檔設計對應書籍，並在 `help` 或 `notes` 中補足說明。",
            "",
            "## 與公告／國家系統的連動",
            "",
            "- 請對照 `system.md` 的公告時間線；例如某步法在特定日期後才開放時，區域掉落或 NPC 教學也應標註版本時點。",
            "- 國家系統指令如 `realm !join` 會查技能欄位（權限），因此 `realm.md` 的資料應與此頁交叉檢查。",
            "",
            "> 原文：skill/index.html 及所有 `skill/*.html`",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build structured data for docs")
    parser.add_argument("--out", default=ROOT / "docs" / "data", type=Path)
    args = parser.parse_args()

    skill_mapping = parse_skill_index()
    skills = parse_skills(skill_mapping)
    datasets = {
        "news.json": parse_news(args.out),
        "skills.json": skills,
        "realm_commands.json": parse_realm_docs(),
        "maps.json": parse_maps(),
        "downloads.json": parse_downloads(),
        "links.json": parse_links(),
        "commands.json": parse_commands(),
        "players.json": parse_player_guides(),
        "immortals.json": parse_imm_list(),
    }
    for name, payload in datasets.items():
        write_json(args.out / name, payload)
    write_markdown(ROOT / "docs" / "skills.md", generate_skills_markdown(skills))
    print(f"Generated {len(datasets)} datasets into {args.out}")


if __name__ == "__main__":
    main()
