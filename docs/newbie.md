---
layout: default
title: 新手／規則／指令
---

# 新手、玩家規則與常用指令

> 與區域開發的關聯：透過玩家規範可得知哪些行為必須在區域描述中強調（如禁止濫殺、robot 偵測）、從新手指南理解教學節奏，再依命令/引導內容設計 NPC、告示或教學房間。

## 玩家規則（`newhand/rule/index.html` 摘要）

1. **Robot 防範**：允許巨集/自動化，但系統會提問驗證；違規者送入天牢且紀錄影響技能提升。→ 在新手區設計 `tick/alias` 教程。
2. **文明用語**：公共頻道、名稱、信件不得出現不雅字，違規者禁言甚至刪國家。→ 在 NPC 對話中加入「公告板」提醒。
3. **衝突處理**：PK 事件鼓勵私下協調；濫殺 3 名以上將禁線或清除技能。→ 區域任務如懸賞/罪惡島需強調後果。
4. **多重連線**：頻寬受限，multi 指令可查詢；神族不介入，要求玩家自律。→ 交通/旅店描述可引導玩家流量分配。
5. **程式錯誤**：通報可得獎勵；惡意利用會沒收。
6. **謎題/法器**：神族不公開解法；鼓勵玩家整理分享。→ 區域內 puzzle 需留提示但不直接給答案。
7. **神族支援範圍**：僅處理系統事務，不提供經濟援助。
8. **回報渠道**：透過 `note` 寄信給大神。
9. **非牟利**：不接受捐贈，檔案保護自行負責；停電時僅協助恢復備份。
10. **規則更新**：改動會寫入 MOTD，需持續關注。

## 新手指南節奏（`newhand/newbies/index.html`）

| 節點 | 內容 | 區域開發建議 |
| --- | --- | --- |
| 經驗值 (`help experience`) | 等級差 ±3 內才有經驗、逃跑扣經驗。 | 在新手怪/房描述寫明推薦等級與 `area` 指令。 |
| 技能 (`help skills`) | 攻擊、步法、逃跑、法術、雜項分類。 | NPC 需提供 `leftskill`/`pry` 的解說或範例。 |
| 學習 (`help learnskill`) | 可向怪、玩家、秘笈或任務學習。 | 區域中 NPC 需要 `learn <mob> !list` 對話與回應。 |
| 致能 (`help enableskill`) | `enable 'two sword'` 式開關，建議攻擊/步法/逃跑各一。 | 在訓練場加入 `enable` 互動與 UI 提示。 |
| 戰鬥 (`help killmob`) | 使用 `score`、`rest`、`lore`、`area`、`group`。 | MUD Prog 可根據 `group` 提示結隊優勢。 |
| 職業與轉職 (`help classes`, `help classrebirth`) | 平民 → 文官/武官/道士 → 進階職 | 在新主城 NPC 內安排轉職說明與 `attribution` 服務。 |
| 屬性/升級 (`help trainattr`, `help upgrade`) | 升級後分配屬性；`attribution` 查官職。 | `realm.md` 指令 1:1 對應; 需在地圖/建築內標示官署位置。 |

## 常用指令與範例（依 `newhand/commands/index.html`）

| 類別 | 指令 | 說明 | 區域互動 |
| --- | --- | --- | --- |
| 移動 | `help direction` | 八方位移動、`recall` 回城。 | 房間描述需清楚列出出口、支援 `recall` 例外。 |
| 狀態 | `help position`, `score` | 查生命、體力、經驗。 | NPC 應回應 `score` 未達標的情境（例如醫館）。 |
| 團隊 | `help groups` | `group <name>`, `gtalk`. | 戰役場景提供 `group formation` 教學。 |
| 戰鬥 | `help war`, `kill`, `flee`. | `flee` 扣經驗，`kill` 需配裝。 | Boss 房說明 `flee` 代價。 |
| 技能 | `help allskill`, `learn`, `enable`. | 學習/致能流程。 | NPC 需具備 `learn !list` scripts。 |
| 貿易 | `help trade`, `sell`, `buy`. | 物價/稅率/店舖營運。 | 商店 reset 需呼應 `trade` 指南。 |
| 物件 | `help object`, `inventory`. | 裝備欄位 `wear` / `remove`. | 物品描述加上 wearable slots。 |

## 玩家心得 / 其它說明（`newhand/players`, `newhand/other`）

- 內容多為對攻略、心情、或特定任務提示的純文字；建議逐步把精華搬到對應地圖或任務 NPC 中，保留歷史原文於附錄。
- 可在 docs/links.md 中，將玩家心得引用到外部論壇或 `phorum.html`，以保留討論脈絡。

## 行動清單

1. 編寫新教學區域前，先勾選以上規則/指令是否都有 NPC、看板或巨集提示。
2. 若調整 PK、robot、multi 政策，需更新 `newhand/rule/index.html` 摘要並在 `system.md` 公告。
3. `docs/data/commands.json` 僅包含指令索引（因原站整合在一頁）；若拆成多頁，記得重新執行 `scripts/build_docs.py`。

> 原文：newhand/rule/index.html、newhand/newbies/index.html、newhand/commands/index.html
