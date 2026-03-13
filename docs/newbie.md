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

### 玩家心得（`players/newplayer/*` 重要摘錄）

> 完整索引見 `docs/data/players.json`（`category = "newplayer"`）。以下整理能直接推敲遊戲系統與教學流程的文章：

| 文章 | 重點資訊 | 來源 |
| --- | --- | --- |
| whitelee 的《新手入門教學》 | 逐步說明創角流程（性別選擇會影響武官技能、守護神頻率建議選 1、出生地推薦洛陽），以及初期生存指引：`select`/`query` 選技能，`buy bacon`/`eat bacon` 與大夫免費饅頭維持飢餓度，`repair cloth 100` 修裝備，`deposit coins`/`withdraw coins` 管理資金，`donate !with` 領救濟金。也整理 1–50 級升級節奏與三大職系轉職位置。 | `newhand/players/newplayer/0104101.html` |
| whitelee 的《新手升級教學》 | 針對 11–100 級提供地區、目標 Mob 與注意事項：<11→陳留/秦皇陵外、20 級弘農楓橋大道、30+ 晉陽與長安商人、50+ 建議留在長安，60 後推秦皇陵、天君府、羅漢宮、武當山、北平→秦皇島→天庭，最後以武當七俠/黃龍洞衝 hero。 | `newhand/players/newplayer/0104121.html` |
| Godkaii《關於國家—for 新手》 | 解釋 `realm` 介面如何判斷國力、人數、裝備；加入條件（先用 chat 取得同意、注意入國費與救濟金冷卻），以及 `realm !who`, `realm !object`, `realm !make`, `/r`, `realm !leave`、`realm !read` 等常用權限。提醒國法需用 `realm !help <英文國名>` 查閱。 | `newhand/players/newplayer/0104231.html` |
| 《新手上路》 | 把新手區動線、`bore hole` 任務機制、`learn girl flee`、`enable`/`cast`/`group`用法寫成逐步流程，並附洛陽主要服務座標（武器店 `/2sw`、車站 `/6s`、鏢局 `/3e2se` 等）與地鐵 `bus`/`ship` 操作、`area help <編號>` 說明。 | `newhand/players/newplayer/9903151.html` |
| 《我的道士練法》 | 詳列道士屬性加點順序（先 CON→DEX→STR，轉職後補 INT/WIS）與高階訓練 NPC（襄陽魏延、襄平玉霖大師），並將火/雷/毒/酸系技能學習來源、領悟條件及 1–52 級練功地點整理成表。 | `newhand/players/newplayer/9904101.html` |
| 《alias 真的很方便》 | 示範 alias 的多指令寫法：`alias rr remove %1:repair %1 %2:wear %1` 讓「脫裝→修復→穿回」一次完成，延伸 `rr2` 修第二件裝備，提醒 alias 可與 `history (!)`、編號語法（`3.xxx`）混用，並建議戰鬥情境大量使用。 | `newhand/players/newplayer/9905191.html` |
| 《新手教戰守則》 | 深入講解屬性限制（各職業 STR/DEX/CON/WIS/INT 上限）、`train !list`、`enable`/`learn`/`config` 常見問題、`recall set 1-10` 快速移動、`area`/`find`/`where`/`auction` 指令的實戰用途與注意事項（例如救濟金時間無法入國、`sac corpse` 前要 `get all corpse`）。 | `newhand/players/newplayer/9907151.htm` |

**對 merc-area-builder 的啟示**

1. 教學區文本應引導玩家使用 `select/query`, `donate !with`, `repair <item> <gold>` 等關鍵指令，確保歷史攻略提到的 NPC/座標在現行區域仍存在。
2. 國家區域需提供 `/r`（realm recall）後的導覽文字、信件板與 `realm !object` 專用工坊，以符合攻略描述。
3. 練功區域與交通（bus/ship/recall set）是這些文章的核心，更新區域資料時應同步調整 `docs/maps.md`、`docs/download.md` 中的座標與建議等級，並在新區域 index 裡提及可行的 leveling loop。

### 職業心得（`players/bard`, `players/bravo`, `players/general`, `players/mage`）

> `docs/data/players.json` 可用 `jq '.[] | select(.category==\"bravo\")'` 等指令篩選所有文章。以下整理對職業平衡與區域掉落最有價值的重點。

| 職業 | 重點資訊 | 來源 |
| --- | --- | --- |
| 刺客（bravo） | `0104241` 描述 1→HERO 的技能流程（華山/翦雲 → 風雲袖步 → 封山 → 龍袖 → 俠客 → HERO 後補無量/天道、神龍、劍君十二恨），並提醒法器與連擊。`0104242`–`0104244` 逐項列出劍法、步法、拳法的學習對象、屬性限制與攻傷。 | `newhand/players/bravo/*.html` |
| 將軍（general） | `0104231` 提供將軍技能全貌與推進順序，`0104232` 之後的系列針對刀、弓、防禦/輔助詳列 NPC 來源與領悟條件，並強調法器、連擊切換。 | `newhand/players/general/*.html` |
| 伶人（bard） | `0106121` 的「水、風、聖系伶人練法」給出屬性建議（HERO 時 STR/CON ≥20、INT/WIS ≥25）、優先技能（群仙祝福→巨人之力→靈神訣→聖光、破風彩雲步、筆扇/玄陰掌）與 50 級後建議先練聖光術。`9905181` 補充 50 級前後的升級節奏與法器選擇。 | `newhand/players/bard/*.html` |
| 天師（mage） | `0106101`、`0106102` 強調天師法術與陣營聯動：善良才能穩定使用七鑰守護神，中立適合以死黑核爆/極度傷害輪替，邪惡則需依賴抽換與帶跑。文章列出大量技能熟練度、攻傷與 MP 消耗測試，對設計天師專屬任務與補給十分關鍵。 | `newhand/players/mage/*.html` |

**對 merc-area-builder 的啟示**

1. 這些職業攻略需對應具名 NPC（如弘農卉沁、陳留程昱、襄平主廚、秦皇陵老人），設計新城或改版時務必先確認 NPC 仍存在或提供替代。
2. 解迷或法器（劍君十二恨、斬龍破鳳刀等）常見於攻略流程，若移除或移位要同步更新 docs+技能資料，並在遊戲內提供新的線索。
3. 探索路徑與屬性門檻應反映在任務描述與掉落；例如伶人需善良陣營、天師需善/中立轉換，區域敘述要提供可改陣營或補給的指引。

> 原文：newhand/players/bravo/*.html、newhand/players/general/*.html、newhand/players/bard/*.html、newhand/players/mage/*.html

### NPC / 掉落對照

| 類別 | 文章 | 推薦 NPC / 掉落 | 欄位用途 |
| --- | --- | --- | --- |
| 伶人 | `bard/index.html`（尤以 `0106121`） | 程昱 (`chen yu`, 筆之心)、蒯越 (`kuai yue`, 玄陰掌)、倫直 (`lun zhi`, refresh)、弘農卉沁 (`whae shin`, 天神守護/群仙祝福)、襄平主廚 (`chef`, 花語刀法) | 確保這些 NPC 仍在原城市或提供替代教學，否則伶人法術鏈會斷。 |
| 刺客 | `bravo/index.html` 系列 | 洛陽武器店老闆（泰山長拳）、陳留浪人（風雲袖步）、襄陽魏延（相思系列）、襄平主廚/chef（海流刀）、秦皇陵/武當等解迷場景（劍君十二恨、逍遙遊） | 調整技能掉落時須更新 `docs/skills.md` 與此表，並在區域 index 標註必要 VNUM。 |
| 將軍 | `general/index.html` 系列 | 洛陽地下水區老人（猛龍刀法）、弘農黃甫嵩（猛龍高價版）、襄平主廚（相思刀）、襄陽魏延（相思→花語）、秦皇陵/天庭高階場景（斬龍破鳳刀、鳳舞箭） | 嚴格依賴特定 NPC；若地圖改版要先確認 `area/directory.lst` 中仍載入這些房間。 |
| 天師 | `mage/index.html` 連載 | 善/中立陣營轉換 NPC（女鬼、宗教祭壇）、八卦主神/邪龍/黑虎等 boss 掉落的法器、提供補給的洛陽藥房/泉水點。 | 陣營鎖定影響技能，建議在主城補給線或任務中提供明確提示。 |

> 若需更多細節，可開啟各職業 `index.html` 查看原表格，或直接查 `docs/data/players.json` 中對應分類的 `summary` 欄位。

## 行動清單

1. 編寫新教學區域前，先勾選以上規則/指令是否都有 NPC、看板或巨集提示。
2. 若調整 PK、robot、multi 政策，需更新 `newhand/rule/index.html` 摘要並在 `system.md` 公告。
3. `docs/data/commands.json` 僅包含指令索引（因原站整合在一頁）；若拆成多頁，記得重新執行 `scripts/build_docs.py`。

> 原文：newhand/rule/index.html、newhand/newbies/index.html、newhand/commands/index.html
