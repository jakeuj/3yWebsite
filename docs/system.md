---
layout: default
title: 系統公告與世界觀
---

# 系統公告與世界觀

> 與區域開發的關聯：本章整理官方公告、歷史故事、Immortal 名冊與版權規定。撰寫 Merc-FJU 區域時，可依這些資料安排 Serial/Capital、限制技能來源、或回推 NPC/管理者設定。

## 故事情節與版本要點（來自 `config/index.html`）

- 背景設定：玩家因時光裂縫進入三國時代，透過冒險挑戰獲得上天挑選。這提供「傳送至戰場／考驗」的劇情理由，適合 `Room School` 至主城的引導文本。
- 製作群：`config/index.html` 列出區域、技能、顧問與技術指導。規劃新區域時，可對照原作者習慣（如 Ast 專長化學系、Cutty 擅長法術等）決定 NPC 或任務彩蛋。
- Serial / Capital：原站以 Serial（區域序號）、Capital（首都房號）為核心欄位；撰寫 index/roo 時，務必遵循 merc-area-builder 建議的「一區一千位段」策略。
- 版權宣告：
  - 由 Merc 2.2 修改，Diku/Merc 仍持有部分版權。
  - 使用者不得刪除配件內版權宣告，且若開放公開遊戲需保留 `help fju` / `credit`。
  - 違反條款製作群可禁止開放並保留法律追訴權。
- 角色稱謂：Immortal / 顧問／區域作者多以 `[代號]` 表示，可直接映射到 NPC 或劇情用語。

## 公告時間線（節錄，完整內容見 `docs/data/news.json`）

| 日期 | 事件 | 影響 | 來源 |
| --- | --- | --- | --- |
| 2002/02/01 | 隱藏術(hide)技能開放、背刺(backstab)技能更改 | 技能更新 / 國家系統 | `news/200202011.html` |
| 2002/01/31 | [公告] 重開後新增功能 | 技能更新 / 國家系統 | `news/200201311.html` |
| 2002/01/29 | [公告] 更新部分 | 系統維護 | `news/200201291.html` |
| 2002/01/26 | [公告] 停機公告 | 系統維護 | `news/200201261.html` |
| 2002/01/25 | 新增百幻身法謎題、開放百幻身法 | 系統維護 | `news/200201251.html` |
| 2002/01/22 | 新技能開放「舞蝶扇、銷魂劍法」等 | 技能更新 / 國家系統 | `news/200201222.html` |
| 2002/01/22 | [公告] 新增 HELP ROBOT 和 HELP MULTI | 系統維護 | `news/200201221.html` |
| 2002/01/21 | [公告] 有關robot和multi的認定 | 系統維護 | `news/200201212.html` |
| 2002/01/21 | [警告] 工作站 sun.cc.ntut.edu.tw | 系統維護 | `news/200201211.html` |
| 2002/01/20 | [警告] 工作站 fths16.fths.tyc.edu.tw | 系統維護 | `news/200201201.html` |

> 建議：將表格匯入專案 issue/roadmap，將與技能有關的公告標註在 `skills.md` 內對應條目，確保區域新增時知道最新平衡補丁。

## Immortal / 神族名單（節錄，更多見 `docs/data/immortals.json`）

| 代號/頁面 | 職責／摘要 | 聯絡 |
| --- | --- | --- |
| `imm/ast.html` | 管理員名稱﹕Ast 等級﹕120，自介為化學系 Ast，常負責區域維護。 | ast@mud.ch.fju.edu.tw |
| `imm/cutty.html` | 管理員 Cutty，專精法術技能，等級 120。 | lc@muds.net |
| `imm/denny.html` | Denny（蘇家興），程式開發主力。 | paul@mud.ch.fju.edu.tw |
| `imm/dye.html` | Dye，化學系背景，擅長區域資料。 | dye@mud.ch.fju.edu.tw |
| `imm/ene.html` | Ene，化研所，法術與區域設計。 | ene@mud.ch.fju.edu.tw |
| `imm/falcon.html` | Falcon，等級 117，Email：chan-chang-wei@kimo.com.tw。 | chan-chang-wei@kimo.com.tw |
| `imm/gamma.html` | 顧問 Gamma，負責顧問/技術指導。 | gamma@mud.ch.fju.edu.tw |
| `imm/gooder.html` | 顧問 Gooder，電子科背景，擔任技術顧問。 | d8442406@ice.oit.edu.tw |
| `imm/hank.html` | Hank，等級 119，參與伺服器維護。 | hank@mud.ch.fju.edu.tw |
| `imm/hubert.html` | Hubert，生物系背景，專長區域故事。 | hubert@mud.ch.fju.edu.tw |

### 使用建議

1. **NPC/任務映射**：當需要官方授權 NPC 時，可直接參考此名單創建「元老級」角色，並於描述加註 Email 作為彩蛋。
2. **技能/公告對照**：若某公告由特定 Immortal 署名，可將區域內對應 NPC 指向該角色，維持世界觀一致。

## 版權與配件規範（`announce/index.html`）

- **配件範圍**：`src/`, `area/`, `angel/`, `data/`, `greeting/`, `social/`, `document/`, `etc/`, `help/`, `edit/`。
- **禁止事項**：刪除版權宣告、接受捐贈、公開遊戲未標示「三國歪傳之降龍伏虎」。
- **應遵循事項**：
  - 釋出遊戲必須保留 Diku/Merc 與製作群字樣。
  - 公開遊戲需主動通知製作群，並維持 `help fju` 與 `credit` 指令。
  - 若僅使用部分配件亦需附版權宣告。

> 在 Merc-FJU 專案進行正式替換時，請於 PR 描述中引用對應條文，確保法務／授權可追溯。

## 系統欄位對區域開發的影響

| 欄位 | 說明 | merc-area-builder 行動 |
| --- | --- | --- |
| Serial | 區域識別號，建議 3 位數流水號並於 `directory.lst` 留註解。 | 在新增區域前確認無 VNUM 衝突，並更新 `area/directory.lst`。 |
| Capital | 首都／回城房號。 | 指向主城/首都 `roo`，並同步 `Room School`、交通設定。 |
| Echo / Fog | index 內可設定 echo/fog 效果。 | 使用 `Fog` 做天氣敘述，對應 `maps.md` 的氣候描述。 |

## 參考原文

> 原文：config/index.html

> 原文：announce/index.html

> 原文：news/index.html + 各子頁

> 原文：imm/*.html
