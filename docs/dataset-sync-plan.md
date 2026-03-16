---
layout: default
title: 資料同步計畫
---

# 3yWebsite Dataset Sync Plan

此文件定義 `docs/data/players.json` 與 `docs/data/skills.json` 的同步流程，避免只改 JSON 而遺漏技能說明、README 或首頁索引。

## 目標

- 維持 `players.json`、`skills.json` 與來源 HTML 的對應關係清楚可驗證。
- 維持 `sango-docs-service` 技能與 README 對這兩份資料的描述同步。
- 讓後續代理在收到「更新相關技能與說明文件和計畫」時，有固定的落點與驗收標準。

## 目前基線

| 檔案 | 預期基線 |
| --- | --- |
| `docs/data/skills.json` | `31` 筆；分類 `武器技能 11 / 法術技能 10 / 職業技能 7 / 其他技能 3`；`skill/learnlv.html` 為特殊參照頁。 |
| `docs/data/players.json` | `26` 筆；分類 `bard 2 / bravo 8 / general 7 / mage 2 / newplayer 7`；副檔名分布 `25` 筆 `.html`、`1` 筆 `.htm`。 |

## 觸發條件

出現下列任一情況時，執行完整同步：

1. `skill/*.html`、`skill/index.html` 有新增、刪除或欄位變更。
2. `newhand/players/*/*.htm*` 有新增、刪除或標題結構變更。
3. `scripts/build_docs.py` 調整了 `parse_skills()` 或 `parse_player_guides()`。
4. 任務明確提到更新 `players.json`、`skills.json`、相關技能、說明文件或計畫。

## 同步步驟

1. 先執行 `python -X utf8 scripts/build_docs.py`。
2. 再執行 `python -X utf8 scripts/check_coverage.py`。
3. 核對 `docs/data/skills.json` 是否仍符合 `31` 與 `11/10/7/3` 基線，或記錄為何變動。
4. 核對 `docs/data/players.json` 是否仍符合 `26` 與 `2/8/7/2/7` 基線，並確認 `.htm` 舊檔沒有漏抓。
5. 若基線或規則變動，回寫下列文件：
   - `docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md`
   - `docs/3yWebsite/README.md`
   - `docs/3yWebsite/docs/index.md`
   - `docs/3yWebsite/docs/newbie.md` 或 `docs/3yWebsite/docs/skills.md`
6. 若技能文件有實質更新，檢查 `docs/3yWebsite/.agents/skills/sango-docs-service/agents/openai.yaml` 是否仍符合內容。

## 驗收標準

- `players.json` 與 `skills.json` 都能被 `json.loads()` 正常解析。
- 文件中提到的筆數、分類與特殊例外和實際資料一致。
- `README.md`、`docs/index.md`、技能文件至少有一處明確提到這兩份資料的用途與基線。
- 若只變更其中一份資料，仍要確認另一份的文件描述沒有被順手寫壞。

## 備註

- `doctor`、`other`、`smith`、`thief` 目前只有玩家心得分類首頁，沒有文章明細；`players.json` 沒有這些分類屬正常。
- `skill/learnlv.html` 屬技能熟練度參照頁，應納入 `skills.json`，但不可用一般技能欄位規則強制驗證。
