---
name: sango-docs-service
description: 使用目前 repo 內 docs/3yWebsite/docs 的 Sango3838 GitHub Pages Markdown 與 JSON 資料集，提供給 merc-area-builder、merc-source-explainer 等工作流程查詢世界觀、技能、玩家攻略、國家、交通與下載資訊時使用；當任務明確提到 docs/3yWebsite、players.json、skills.json 或舊站鏡像資料同步時也使用。
---

# Sango3838 Docs Service

把 `docs/3yWebsite/docs/*.md` 與 `docs/3yWebsite/docs/data/*.json` 轉成可直接給 `merc-area-builder`、`merc-source-explainer` 使用的世界觀、技能、國家、交通與下載資訊。只在任務明確需要 Sango3838 舊站資料時使用。

## 快速流程

1. 先決定層級：
   - 主題導覽：`docs/index.md`
   - 主題文檔：`docs/system.md`、`docs/newbie.md`、`docs/skills.md`、`docs/realm.md`、`docs/maps.md`、`docs/download.md`、`docs/links.md`
   - 批次查詢：`docs/data/*.json`
2. 再決定用途：
   - 世界觀 / 公告：`docs/system.md`、`docs/data/news.json`
   - 技能 / 掉落 / NPC：`docs/skills.md`、`docs/data/skills.json`
   - 國家指令：`docs/realm.md`、`docs/data/realm_commands.json`
   - 地圖 / 巴士：`docs/maps.md`、`docs/data/maps.json`、`map/bus.html`
   - 玩家攻略：`docs/newbie.md`、`docs/data/players.json`
   - 下載 / 手冊：`docs/download.md`、`docs/data/downloads.json`
3. 回答時：
   - 用繁體中文
   - 以 `> 原文：相對路徑` 標示來源
   - 說清楚這份資料會影響 Merc-FJU 3.0 的哪一步

## `skills.json` 規則

- `docs/data/skills.json` 是合法的 UTF-8 JSON array；驗證優先用 Python `json.loads()`。
- 它的 `31` 筆來自 `skill/index.html`，分類基線應是：
  - 武器技能 `11`
  - 法術技能 `10`
  - 職業技能 `7`
  - 其他技能 `3`
- `skill/learnlv.html` 是「技能熟練度」參照頁，算在分類統計內，但不是一般技能明細頁。
- 若要驗證 `skills.json` 是否仍符合來源頁，先比 `skill/index.html` 的分類與筆數，再抽查 `skill/*.html`。
- 一般技能頁應有 `英文名稱 / 中文名稱 / 領悟技能` 區塊；`learnlv.html` 例外。

## `players.json` 規則

- `docs/data/players.json` 是合法的 UTF-8 JSON array；驗證優先用 Python `json.loads()`。
- 它的 `26` 筆來自 `newhand/players/*/*.htm*`，分類基線應是：
  - `bard` `2`
  - `bravo` `8`
  - `general` `7`
  - `mage` `2`
  - `newplayer` `7`
- 目前副檔名基線是 `25` 筆 `.html` 加 `1` 筆 `.htm`；不要把 `newhand/players/newplayer/9907151.htm` 當成漏抓。
- 目前 `doctor`、`other`、`smith`、`thief` 只有分類首頁，沒有文章明細；`players.json` 缺少這些分類是正常現象。
- 每筆資料至少應有 `path / category / title / summary`；`summary` 是從原頁首個可讀段落擷取的摘要，不要求完整攻略全文。
- 若要驗證 `players.json` 是否仍符合來源頁，先比 `newhand/players/*/index.html` 與實際文章檔數，再抽查各職業文章標題是否正確落到 `title`。

## 同步規則

- `skills.json` 有結構或筆數變動時，除了重生 JSON，還要同步確認 `docs/skills.md`、`docs/index.md` 與本技能中的基線描述。
- `players.json` 有結構或筆數變動時，除了重生 JSON，還要同步確認 `docs/newbie.md`、`docs/index.md` 與本技能中的基線描述。
- 若只是調整來源 HTML 摘要文字但沒有改 JSON schema，可只更新資料與對應 Markdown，不必擴大修改其他 docs。
- 若需要交接或規劃後續工作，優先參考 `docs/3yWebsite/docs/dataset-sync-plan.md`。

## 更新 / 驗證

若 docs JSON 需要重生：

```bash
python3 scripts/build_docs.py
python3 scripts/check_coverage.py
```

- `scripts/build_docs.py` 依賴 `beautifulsoup4`。
- 重生 `docs/data/skills.json` 後，特別檢查多行英文名稱是否正確合併，例如 `hua sword`、`young gun`、`dragon phoenix`。
- 重生 `docs/data/players.json` 後，特別檢查舊副檔名 `.htm` 是否仍被收錄，以及 `newplayer / bravo / general` 這三類的大宗文章數是否異常。

需要本機預覽時：

```bash
./scripts/serve_docs.sh
```

## 故障排除

- 找不到資料：先看 `docs/data/*.json` 是否已有對應主題；沒有再回原 HTML。
- `skills.json` 看起來壞掉：
  1. 先用 Python 確認是否真是非法 JSON。
  2. 若筆數或分類不對，先比 `skill/index.html` 的 `11 / 10 / 7 / 3`。
  3. 若只有少數 `英文名稱` 不對，優先檢查 `build_docs.py` 是否漏合併 HTML 續行欄位。
  4. 不要把 `skill/learnlv.html` 當成一般技能明細抽取失敗。
- `players.json` 看起來壞掉：
  1. 先用 Python 確認是否真是非法 JSON。
  2. 若筆數不對，先確認是否誤排除了 `.htm` 或把 `index.html` 算進文章。
  3. 若分類不對，先比 `newhand/players/` 底下各子目錄實際文章數，而不是首頁連結數。
  4. 若標題怪異，優先檢查頁面是否缺少 `span.text2`，再退回 `<title>`。
- GitHub Pages build 失敗：跑 `bundle exec jekyll build --source docs` 看錯誤。

> 使用此技能時，始終思考「目前 Merc-FJU 3.0 任務的哪一步需要這段資料？」並在回覆中顯式說明目的與後續動作。
