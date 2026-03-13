---
layout: default
title: 外部連結／論壇
---

# 外部連結與 Telnet 服務

> 與區域開發的關聯：這些連結提供歷史 BBS、Telnet 端點與聯絡方式，便於追溯原始公告、玩家社群與鏡像來源，並可在遊戲中設置 NPC／佈告欄呼應。

## Telnet / BBS 範例（`docs/data/links.json`）

| 類別 | 位址 | 備註 |
| --- | --- | --- |
| Telnet 主站 | `telnet://140.112.2.33:3000` | drake.ntu.edu.tw 測試點。 |
| BBS (NTU) | `telnet://bbs.ntu.edu.tw` | 與 `phorum.html` 相同來源，可嵌入官方公告。 |
| BBS (casamia) | `telnet://140.112.66.169:8888` | 傳統 BBS 節點，原站常用於分享任務攻略。 |
| BBS (casamia 備援) | `telnet://140.112.66.169` / `telnet://140.113.91.2` | 備援連線。 |
| 其他端口 | `telnet://140.113.5.151:7777` | 另一路線上世界，可作跨服劇情。 |

## 聯絡信箱

- `xeen@mud.ch.fju.edu.tw`：原站負責人之一，適合作為 NPC 彩蛋。
- `mailto:` 連結多集中於 Immortal/公告頁面，詳見 `system.md` 的名單。

## Phorum / 討論版

- `phorum.html` 目前為 frame 框架，需搭配 `phorum-m.html` 與伺服器端 CGI 才能完整顯示。建議在 docs 站台採「歷史紀錄」方式描述，而非嵌入失效連結。
- 若需引用討論串，可在 `docs/links.md` 內新增章節，將討論摘錄轉寫為 Markdown，並在最末標註 `> 原文：phorum/*.html`。

## 遊戲內應用

1. **公告板**：在主城設立「四大 BBS 情報台」NPC，包含 Telnet 位址與 `help phorum` 指令。
2. **傳送任務**：利用不同 Telnet 端點的地名擴充世界觀，例如 `casamia` → 海上貿易線，`drake` → 學院任務。
3. **玩家支線**：可設計 `note` 任務要求玩家寄信給特定 Email，以觸發 Reward（僅作 RP 用途）。

> 原文：link/index.html、links.html（frameset）、phorum.html
