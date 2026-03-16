---
layout: default
title: 首頁 Portal
---

# 三國歪傳之降龍伏虎 GitHub Pages 入口

> 目的：將鏡像網站轉成 **merc-area-builder** 技能可直接引用的知識庫，協助區域規劃、技能平衡、故事考據與交通銜接。

<div class="callout">
<strong>如何使用：</strong> 先執行 `python3 scripts/build_docs.py` 產生 JSON，再閱讀下表各章節的 Markdown。需要更動時，可在 docs/ 檔案中直接編輯，或擴充 JSON → Markdown 的流程。
</div>

## 導覽

| 章節 | 來源目錄 | 內容用途 |
| --- | --- | --- |
| [系統資訊](system.md) | `news/`, `intro/`, `config/`, `imm/`, `announce/` | 版本沿革、Immortal 名冊、版權條款，支援系統級調整。 |
| [新手/規則](newbie.md) | `newhand/` | 玩家行為規範、常用命令、FAQ，對應 merc-area-builder 第 1 步「規劃故事與玩法」。 |
| [技能資料庫](skills.md) | `skill/` | 各職業/法術/武器的授權條件與資源消耗，供場景掉落、NPC 教學使用。 |
| [國家系統](realm.md) | `realm/` | `realm !*` 指令、國家故事、廣告範本，利於設計政體任務與首都。 |
| [地圖 / 交通](maps.md) | `map/`, `map/bus.html` | 城鎮地圖、推薦等級、巴士/船航點，支援 Serial/Capital 規劃。 |
| [下載 / 區域寫作](download.md) | `download/` | 官方釋出檔案、區域編寫手冊，同步 merc-area-builder 的資料來源。 |
| [外部連結](links.md) | `link/`, `links.html`, `phorum.html`, `telnet` | 歷史論壇、Telnet 端點、支援工具參照。 |

## merc-area-builder 對應

| merc-area-builder 步驟 | 本站對應資源 |
| --- | --- |
| 規劃 slug / VNUM / Serial | `system.md` 內的故事背景、Capital 設定與公告。 |
| 建立骨架與載入清單 | `download.md` 的寫作手冊；`maps.md` 的交通勾稽。 |
| 整備關鍵資料（技能、NPC） | `skills.md`, `realm.md`, `newbie.md` 的命令條列。 |
| 驗證/測試 | `scripts/check_coverage.py`（HTML → docs 對應）、GitHub Pages build 指南。 |

## 自動化資料集

| 檔案 | 說明 |
| --- | --- |
| `docs/data/news.json` | 系統公告（日期、標題、摘要、原始 HTML）。 |
| `docs/data/skills.json` | 各技能的分類、英文名、資源消耗。 |
| `docs/data/players.json` | 玩家攻略摘要、職業分類與歷史心得入口。 |
| `docs/data/realm_commands.json` | `realm/doc/*.html` 解析後的指令與說明。 |
| `docs/data/maps.json` | 每張地圖的標題、首段摘要。 |
| `docs/data/downloads.json` | 下載頁面摘要＋ `.tar.gz` 檔案大小。 |
| `docs/data/links.json` | 外部連結與來源頁。 |
| `docs/data/commands.json` | `newhand/commands` 目錄的條目摘要。 |
| `docs/data/immortals.json` | Immortal 名冊（頁面、摘要、Email）。 |

目前資料基線：

- `docs/data/skills.json`：`31` 筆，分類應為武器 `11` / 法術 `10` / 職業 `7` / 其他 `3`。
- `docs/data/players.json`：`26` 筆，分類應為 `bard 2 / bravo 8 / general 7 / mage 2 / newplayer 7`，且包含 `1` 筆 `.htm` 舊檔。
- 若任一基線改變，除了重跑 `scripts/build_docs.py`，也要同步檢查 `README.md`、`docs/newbie.md`、`docs/skills.md` 與 `docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md`。

> 維護流程請見 [資料同步計畫](dataset-sync-plan.md)

## 部署與預覽

1. 安裝 Ruby/Bundler 後，在 repo 根目錄執行 `bundle install --gemfile docs/Gemfile`。
2. 重新擷取資料：`python3 scripts/build_docs.py`。若需確認 coverage，執行 `python3 scripts/check_coverage.py`。
3. 本機預覽：`./scripts/serve_docs.sh`，預設以 `docs/` 為 source 並啟用 livereload。
4. GitHub Pages：於 Settings → Pages 選 `Deploy from a branch`，Branch 選 `main`、資料夾 `docs/`。

> 若 Pages build 失敗，可在本機執行 `bundle exec jekyll build --source docs` 以重現錯誤。

## 風格指南

- 文件使用台灣繁體中文，第一次出現的英文術語需加括號簡註，如「Serial（區域序號）」。
- 引述原文時，以 `> 原文：path` 標記來源，避免逐字全文轉錄。
- 表格欄位盡量保持 Merc-FJU 相關性（例如加入「區域影響」、「建置提示」），讓資料直接反饋到 `merc-area-builder` 的 checklist。
