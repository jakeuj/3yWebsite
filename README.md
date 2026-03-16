# Sango3838 Website Mirror

這個倉庫保留「三國歪傳之降龍伏虎」舊站鏡像，並提供 `docs/` 目錄的 GitHub Pages 站台，將遊戲資訊整理成適用於 Merc-FJU 開發流程（參考 `merc-area-builder` 技能）的服務手冊。

## 快速開始

```bash
# 產生最新的 JSON 資料集
python3 scripts/build_docs.py

# 確認每個 HTML 都對應到某個 docs 章節
python3 scripts/check_coverage.py

# 啟動 Jekyll 開發伺服器（需先 bundle install）
./scripts/serve_docs.sh
```

- `docs/_config.yml` 已設定 `theme: minima`，直接在 GitHub Pages 選擇「Deploy from a branch」並指定 `main` / `docs` 即可發布。
- 所有自動擷取結果放在 `docs/data/*.json`，Markdown 內容以摘要/表格方式引用這些資料。
- 若要調整樣式，可編輯 `docs/assets/styles.css` 或擴充 `_includes/`。

## 組織

| 目錄/檔案 | 說明 |
| --- | --- |
| `docs/index.md` | 首頁 Portal：背景、導覽、部署步驟與 merc-area-builder 對應。 |
| `docs/system.md` | 系統公告、世界觀、Immortal 名冊。 |
| `docs/newbie.md` | 新手規則、指令、玩家心得、職業攻略與 NPC/掉落對照。 |
| `docs/skills.md` | 技能/職業/法術統整。 |
| `docs/realm.md` | 國家系統、權限與廣告。 |
| `docs/maps.md` | 地圖交通、推薦等級、區域鉤點。 |
| `docs/download.md` | 下載檔案與區域撰寫手冊索引。 |
| `docs/links.md` | 外部連結、phorum、telnet 資訊。 |
| `scripts/build_docs.py` | 解析 HTML → JSON 的主要工具（需 `beautifulsoup4`）。 |
| `scripts/check_coverage.py` | 確認網站所有 HTML 均分派到 docs 章節。 |
| `scripts/serve_docs.sh` | 包裝 `bundle exec jekyll serve --source docs` 的便利指令。 |

> 若第一次執行 `scripts/build_docs.py` 遇到缺少套件，可使用 `pip3 install --user --break-system-packages beautifulsoup4` 安裝依賴。

## 技能支援

`docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md` 為專用技能，協助其他代理在回答 merc-area-builder 相關問題時，快速定位 `docs/*.md` 與 `docs/data/*.json`（包含職業攻略 `players.json` 與技能資料 `skills.json`）中的資訊。當需求涉及 Sango3838 世界觀、公告、技能、玩家攻略或交通資料時，該技能會指引：

1. 先查 `docs/index.md` 判斷章節。
2. 依主題開啟對應 Markdown。
3. 需要批次資料時讀取 JSON 檔（如 `news.json`, `skills.json`）。
4. 回覆內標註「> 原文：相對路徑」以利追溯。

若更新 docs 內容，記得同步執行 `python3 scripts/build_docs.py` 以重建資料集，與 `python3 scripts/check_coverage.py` 檢查是否仍然覆蓋所有 HTML。

## 資料集基線

目前維護 `players.json` 與 `skills.json` 時，預期基線如下：

| 檔案 | 目前筆數 | 核對重點 |
| --- | --- | --- |
| `docs/data/skills.json` | `31` | 類別分佈應為武器 `11`、法術 `10`、職業 `7`、其他 `3`；`skill/learnlv.html` 是特殊參照頁。 |
| `docs/data/players.json` | `26` | 類別分佈應為 `bard 2 / bravo 8 / general 7 / mage 2 / newplayer 7`；其中 `newhand/players/newplayer/9907151.htm` 是唯一 `.htm` 舊檔，仍應被收錄。 |

若這些數字改變，先確認是否是來源 HTML 真的新增/刪除，而不是 parser 漏抓。

## 維護計畫

`[docs/dataset-sync-plan.md](docs/dataset-sync-plan.md)` 整理了 `players.json` / `skills.json` 的同步節點、驗證步驟與文件回寫規則。當任務是「更新相關技能與說明文件和計畫」時，預設應一起檢查：

1. `docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md`
2. `docs/3yWebsite/README.md`
3. `docs/3yWebsite/docs/index.md`
4. `docs/3yWebsite/docs/newbie.md` 或 `docs/3yWebsite/docs/skills.md`
5. `docs/3yWebsite/docs/dataset-sync-plan.md`

## GitHub Pages 建置

1. 於 repo 的 **Settings → Pages**，Source 選擇 `Deploy from a branch`。
2. Branch 設為 `main`、資料夾為 `/docs`。
3. 儲存後等待建置，若失敗可使用 `jekyll build --source docs` 在本機重現並修正。

## docs 內容概述

`docs/` 目錄是一份靜態知識庫，可直接部署為 GitHub Pages。內容分成兩層：

1. **Markdown 主題檔**：對應網站主題（系統公告、技能、國家、交通等）。每篇除了描述，也列出「如何支援 merc-area-builder」的指引，並提供原文路徑供追溯。
2. **JSON 資料集（`docs/data/*.json`）**：由 `scripts/build_docs.py` 產生，可用於批次查詢：
   - `news.json`：公告日期、標題、摘要、檔案路徑。
   - `skills.json`：每個技能的分類、中文/英文名、資源消耗、職業限制等欄位。
   - `realm_commands.json`：`realm/doc/*.html` 中的指令與說明。
   - `maps.json`、`downloads.json`、`links.json`、`commands.json`、`immortals.json`：對應地圖、下載、外部資源、指令索引、Immortal 名單。
   - `players.json`：`newhand/players/*/*.html` 摘要，包含分類（如 newplayer/bravo）、標題與首段內容，可快速搜尋歷史心得。
   - 搭配 `docs/newbie.md` 的「玩家心得」「職業心得」「NPC/掉落對照」，可迅速查到攻略提到的 NPC（例：程昱、蒯越、襄平主廚）或交通節點後續動作。

當需要補強內容時，建議流程：

```bash
# 1. 重新擷取資料（若有新增 HTML/內容）
python3 scripts/build_docs.py

# 2. 確認是否所有 HTML 仍有對應章節
python3 scripts/check_coverage.py

# 3. 在 docs/*.md 中補充說明或插入表格/引用
```

完成後可使用 `./scripts/serve_docs.sh`（livereload）檢查樣式，再 push 供 GitHub Pages 重建。
