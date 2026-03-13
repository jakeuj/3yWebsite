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
| `docs/newbie.md` | 新手規則、指令、玩家心得。 |
| `docs/skills.md` | 技能/職業/法術統整。 |
| `docs/realm.md` | 國家系統、權限與廣告。 |
| `docs/maps.md` | 地圖交通、推薦等級、區域鉤點。 |
| `docs/download.md` | 下載檔案與區域撰寫手冊索引。 |
| `docs/links.md` | 外部連結、phorum、telnet 資訊。 |
| `scripts/build_docs.py` | 解析 HTML → JSON 的主要工具。 |
| `scripts/check_coverage.py` | 確認網站所有 HTML 均分派到 docs 章節。 |
| `scripts/serve_docs.sh` | 包裝 `bundle exec jekyll serve --source docs` 的便利指令。 |

## GitHub Pages 建置

1. 於 repo 的 **Settings → Pages**，Source 選擇 `Deploy from a branch`。
2. Branch 設為 `main`、資料夾為 `/docs`。
3. 儲存後等待建置，若失敗可使用 `jekyll build --source docs` 在本機重現並修正。
