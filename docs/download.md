---
layout: default
title: 下載與區域撰寫手冊
---

# 下載與區域撰寫手冊

> 與區域開發的關聯：此處收錄官方釋出檔案（`merc-fju*.tar.gz`）與 00~07 系列撰寫介紹。`merc-area-builder` 在操作 VNUM、mob/obj/roo/res/shp 時，可直接引用這些格式說明。

## 官方釋出檔案

| 檔案 | 大小 (bytes) | 說明 |
| --- | --- | --- |
| `download/merc-fju.tar.gz` | 1,144,260 | 原始釋出檔，對應 2001 年版本。 |
| `download/merc-fju-2.0.tar.gz` | 1,280,407 | 第二版，支援 FreeBSD；`merc-area-builder` 目前使用的 UTF-8 改版即源自此檔。 |
| `download/fjumud.tar.gz` | 1,190,578 | FreeBSD 打包版本。 |

> 請將解壓後的 `area/`、`doc/` 內容與現行 repo 比對，僅挑選必要的參考檔；避免將舊資料直接覆蓋正式伺服器。

## 撰寫介紹（`download/00~07.html`）

| 編號 | 主題 | 整理後重點 |
| --- | --- | --- |
| 00 | 參考手冊 | 硬體需求（Linux kernel 2.0.30+、32MB RAM）、必要工具（tar/zip/gcc/crypt），適合放入 README。 |
| 01 | 怪物寫法 | `mob/*.mob` 結構，`Vnum`、`Act`、`Effect`、`#Learn` 格式。 |
| 02 | 房間寫法 | `roo/*.roo` 內容，`SectorType`、`RoomFlag`、`#Exit`。 |
| 03 | 物品寫法 | `obj/*.obj` 欄位、`ItemType`、`WearLoc`、`Value0-5`。 |
| 04 | 重置寫法 | `res/*.res` 指令（M/O/P/G/E/D），並提醒 `#` 標記為註解。 |
| 05 | 區域標題 | `index` 檔欄位（Echo、Editor、Name、Serial、Capital）與 `~` 收尾規則。 |
| 06 | 商店寫作 | `shp/*.shp` (`Type`, `Keeper`, `Object1..5`) 與坐騎設定。 |
| 07 | 怪物程式 | `#Learn`、`#Give` 等 MobProg 格式，包含可教學技能範例。 |

> 建議在 Merc-FJU 專案 `references/` 中引用此表，或為每個主題建立現代化示範檔案（UTF-8 + 目前 VNUM 區段）。

## 行動建議

1. **自動化對照**：若 `merc-area-builder` 新增 VNUM，請將對應的範例（mob/obj/roo/res/shp）以 Markdown 範本連結回上述編號。
2. **教學任務**：在長安/北平等主城設置書架/書卷 (`book index`) 物件，讓玩家閱讀 00~07 內容，作為遊戲內的區域創建教學。
3. **版本棧**：當未來釋出 `merc-fju-3.0` 等檔案時，請更新本頁表格與 README，並重新記錄檔案大小以利校驗。

> 原文：download/index.html 及 download/00~07.html
