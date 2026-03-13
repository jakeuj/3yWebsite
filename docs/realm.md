---
layout: default
title: 國家系統
---

# 國家系統（realm）

> 與區域開發的關聯：`realm` 指令涵蓋政體、官位、權限、銀行需求與新聞/信件。設計主城、國家領地或 Capital 房間時，需確保這些指令有實際 NPC/場景支援。

## 指令摘要（`docs/data/realm_commands.json`）

| 指令 | 摘要 | 來源 |
| --- | --- | --- |
| `realm` | 列出所有國家與基本資訊（國庫、成員數）。 | `realm/doc/01.html` |
| `realm !create [英文國名] [中文國名]` | 建國需英雄等級、非管理者、無國籍、銀行資金 1,000 萬。建國者成為預設君主。 | `realm/doc/01.html` |
| `realm !countersign [英文國名]` | 需五位英雄連署且每人終身一次、銀行 10 萬。 | `realm/doc/01.html` |
| `realm !join [英文國名]` | 依國家規費入國，加入後成為追隨者並等待認證。 | `realm/doc/01.html` |
| `realm !attribution` | 顯示官位、薪水與國家權限。 | `realm/doc/01.html` |
| `realm !who [英文國名]` | 查詢國家人事與人口狀況。 | `realm/doc/01.html` |
| `realm !help [英文國名]` | 查詢國家簡介、領地、人員、寶物。 | `realm/doc/01.html` |
| `realm !quit [英文國名]` | 叛國：降低技能 10%，立即移出領地；君主不可使用，需 `realm !fordo`。 | `realm/doc/01.html` |
| `realm !leave` | 離開國家領地（須位於領地且允許離境狀態）。 | `realm/doc/01.html` |
| `realm !news` / `!notelist` / `!read` | 於首都檢視國家大事與信件，需對應權限。 | `realm/doc/03.html` |

> 其餘檔案 04~09 針對官職調整、國庫徵稅、軍隊管理、懸賞等進階功能，請直接查閱 `docs/data/realm_commands.json`。

## 國家列表（2002/01/25，`realm/list/index.html`）

| 序號 | 英文名 | 中文名 | 國王 | 狀態 |
| --- | --- | --- | --- | --- |
| 34 | gay | 『玻璃』王國 | Kikit | 已成立 |
| 33 | yanzi | 『燕姿』親衛隊 | Marcoyan | 已成立 |
| 32 | reverie | 發呆集散地 | Forms | 已成立 |
| 31 | Gun | 『槍』 | Ponny | 已成立 |
| 30 | DVM | 弒神一族 | Mickey | 已成立 |
| 29 | nike | 夢幻 | Nike | 已成立 |
| 28 | dragon | （原頁面顯示龍系國家） | 暫缺 | 已成立 |

- 可將此列表視為歷史資料，並在新區域「國家事務所」展示，或作為 `realm !help` 的範例資料。
- 若 merc-area-builder 專案新增/合併國家，請更新此表並標注日期。

## 國家廣告（`realm/ads/index.html`）

| 日期 | 內容 | 用途 |
| --- | --- | --- |
| 2001/04/07 | 血剎盟國 (DCSG) 招募 | 可作為 NPC 佈告欄文案。 |
| 2001/04/07 | 史萊姆王國 (slime sky) 招募 | 範例：如何描述國家特色。 |

> 可將 `ads/` 內各 HTML 直接放到 `capital` 房間的公告板，並在 `res` 中重置可閱讀的 `paper` 或 `board`。

## 區域開發建議

1. **銀行與稅務**：建國/連署需銀行金額，請確保主城中有與 `merc-area-builder` 流程一致的銀行 NPC/房號。
2. **權限與職務**：`realm !attribution` 顯示權限標籤（例如 `[觀看國家新聞]`），區域 NPC 需在授權流程中檢查這些 flag。
3. **新聞/信件**：`realm !news` 與 `!notelist` 限於首都，請將首都房間 (`Capital`) 設為具備 `board` 或 `note` 物件的安全區，搭配 `maps.md` 交通節點。
4. **叛國與懸賞**：`realm !quit` 降技能 10%，`merc-area-builder` 在設定懸賞或罪惡島 VNUM 時要描述這個懲罰，並確定 `RoomRecall` 不會把叛國者送回國土。

> 原文：realm/doc/*.html、realm/list/index.html、realm/ads/index.html
