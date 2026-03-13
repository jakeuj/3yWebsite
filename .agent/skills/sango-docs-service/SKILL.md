---
name: sango-docs-service
description: 使用 /Users/jakeuj/codex/3yWebsite/docs 內的 Sango3838 GitHub Pages 資料與 JSON，提供給 merc-area-builder 技能工作流程需要的世界觀、技能、國家、交通與下載資訊時使用。
---

# Sango3838 Docs Service

此技能提供一組流程，協助你把 `/Users/jakeuj/codex/3yWebsite/docs` 中整理好的 Markdown 與 `docs/data/*.json` 轉化為 merc-area-builder 相關任務可直接引用的回答或資料。遇到需要說明 Sango3838 世界觀、公告、技能、國家系統或地圖交通時，優先依照下列步驟行事。

## 1. 決定資訊來源層級
1. **主題導覽**：若使用者尚未指定細節，先閱讀 `docs/index.md` 了解章節位置與資料涵蓋範圍。
2. **主題檔案**：依請求對應主題開啟 Markdown，例如：
   - 系統／公告 → `docs/system.md`
   - 新手／規則 → `docs/newbie.md`
   - 技能 → `docs/skills.md`
   - 國家系統 → `docs/realm.md`
   - 地圖交通 → `docs/maps.md`
   - 下載／撰寫手冊 → `docs/download.md`
   - 外部連結 → `docs/links.md`
3. **資料集 JSON**：需批次查詢（例如列出所有公告或技能欄位）時，讀取對應 `docs/data/*.json`：`news.json`, `skills.json`, `realm_commands.json`, `maps.json`, `downloads.json`, `links.json`, `commands.json`, `immortals.json`。

## 2. 常見任務映射（面向 merc-area-builder）
- **規劃新區域故事/Serial**：
  1. 讀 `docs/system.md` 找背景、Immortal 名單與公告時間線。
  2. 若需事件日期，直接引用 `docs/data/news.json` 內的日期與摘要。
- **新手/行為規則**：
  1. 由 `docs/newbie.md` 擷取對應規則。
  2. 需具體條款可引用 `newhand/rule/index.html` 路徑。
- **技能掉落或 NPC 設定**：
  1. 用 `docs/skills.md` 整體說明；
  2. 需要完整欄位時從 `docs/data/skills.json` 過濾（可用 `jq`）。
- **國家／政體互動**：查看 `docs/realm.md` 內指令表；若要撰寫 MUDProg，利用 `realm_commands.json` 取得原文敘述。
- **交通／地圖**：`docs/maps.md` + `maps.json`；需要巴士價格時引用 `map/bus.html` 路徑。
- **下載與區域撰寫手冊**：`docs/download.md`；如需提醒匯入 merc-fju-2.0 資料，可指出對應 `.tar.gz` 檔案大小。

## 3. 引用與來源標註
- 以「> 原文：相對路徑」標示來源（遵循 docs 內的慣例），確保回答可追溯。
- 當回答與 merc-area-builder 流程直接相關，補充如何更新 `area/directory.lst` 或 `scripts/check-data.py`，並說明該資訊在 docs 哪一節。

## 4. 資料更新 / 驗證
1. 若 doc 內容需要重生或新增資料，先執行：
   ```bash
   python3 scripts/build_docs.py
   python3 scripts/check_coverage.py
   ```
2. 需要 GitHub Pages 預覽時，使用：
   ```bash
   ./scripts/serve_docs.sh
   ```
   （需先 `bundle install --gemfile docs/Gemfile`）

## 5. 回答格式建議
- 確保回覆保持台灣繁體中文；第一次出現的英文術語以括號補充中文。
- 對 merc-area-builder 提供 actionable 建議，如「依公告 2002/01/25 調整百幻身法掉落 → 參考 `news/200201251.html`」。
- 當引用 JSON 提供列表時，若過多可提供篩選條件或建議指令（示例：`jq '.[] | select(.category=="武器技能")' docs/data/skills.json`）。

## 6. 故障排除
- 找不到資料：
  1. 確認 `docs/data/*.json` 是否缺少對應主題，如無則回到原 HTML（例如 `news/*.html`）補摘要。
  2. 若 JSON 為空（如初次執行前），先跑 `scripts/build_docs.py`。
- GitHub Pages build 失敗：執行 `bundle exec jekyll build --source docs` 以取得錯誤訊息，並檢查 Markdown 語法。

> 使用此技能時，始終思考「merc-area-builder 的哪一步需要這段資料？」並在回覆中顯式說明目的與後續動作。
