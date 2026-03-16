---
layout: default
title: 技能資料庫
---

# 技能資料庫與職業設定

> 與區域開發的關聯：技能決定 NPC 能力、掉落秘笈、任務獎勵與訓練場內容。此頁依 `docs/data/skills.json` 與 `skill/index.html` 生成，方便在 GitHub Pages 直接查看分類與詳細欄位。

## 類別統計

| 類別 | 檔案數 | 說明 |
| --- | --- | --- |
| 武器技能 | 11 | 劍、刀、弓、槍、棍、斧、鞭、扇、短兵、拳法、氣功。 |
| 法術技能 | 10 | 火、風、光、聖、雷、水、土、暗、邪、毒系。 |
| 職業技能 | 7 | 格鬥、暗殺、法師、鑄造、吟唱、醫療、盜賊。 |
| 其他技能 | 3 | 步法、技能總覽、技能熟練度。 |

- `scripts/build_docs.py` 會根據 `skill/index.html` 重建 `docs/data/skills.json` 與本頁；若新增類別或技能頁，請更新來源 HTML 後重跑腳本。
- `skill/learnlv.html` 屬於「技能熟練度」參照頁；它應計入 `skill/index.html` 的分類統計，但不應和一般技能明細頁等量看待。

## 展開詳細資料

以下內容可直接在 GitHub Pages 展開查看，不必回到原始 HTML 逐頁翻找。

## 武器技能

<details><summary><strong>神盤鬼斧六絕式</strong>(`ghost axe`)</summary>

- 原文頁面：[`skill/axe.html`]({{ '/skill/axe.html' | relative_url }})
- 類別：武器技能
- 英文名稱：ghost axe
- 中文名稱：神盤鬼斧六絕式
- 攻擊武器：斧
- 互相教導：可以
- 技能功能：攻擊類
- 技能分類：技能
- 浪費數值：體力
- 領悟技能：霸虎戰訣(tiger axe)
- 領悟機率：極低
- 預備功夫：從缺

</details>
<details><summary><strong>猛龍刀法</strong>(`her blade`)</summary>

- 原文頁面：[`skill/blade.html`]({{ '/skill/blade.html' | relative_url }})
- 類別：武器技能
- 英文名稱：her blade
- 中文名稱：猛龍刀法
- 攻擊武器：大刀
- 互相教導：不可以
- 技能功能：攻擊類
- 技能分類：技能
- 浪費數值：體力
- 領悟技能：魔刀(dragon blade)
- 領悟機率：很低
- 預備功夫：從缺

</details>
<details><summary><strong>射日箭法</strong>(`shoot sun`)</summary>

- 原文頁面：[`skill/bow.html`]({{ '/skill/bow.html' | relative_url }})
- 類別：武器技能
- 英文名稱：shoot sun
- 中文名稱：射日箭法
- 攻擊武器：弓
- 互相教導：不可以
- 技能功能：攻擊類
- 技能分類：技能
- 浪費數值：體力
- 領悟技能：水雲箭法(water cloud blast)
- 領悟機率：很低
- 預備功夫：從缺

</details>
<details><summary><strong>碧血十二針</strong>(`be needle`)</summary>

- 原文頁面：[`skill/dagger.html`]({{ '/skill/dagger.html' | relative_url }})
- 類別：武器技能
- 英文名稱：be needle
- 中文名稱：碧血十二針
- 攻擊武器：短兵
- 互相教導：不可以
- 技能功能：攻擊類
- 技能分類：技能
- 浪費數值：體力
- 領悟技能：七奇炙針訣(seven dagger)
- 領悟機率：極低
- 預備功夫：從缺

</details>
<details><summary><strong>先天乾坤功</strong>(`universe`)</summary>

- 原文頁面：[`skill/energy.html`]({{ '/skill/energy.html' | relative_url }})
- 類別：武器技能
- 英文名稱：universe
- 中文名稱：先天乾坤功
- 攻擊武器：空手
- 互相教導：不可以
- 技能功能：攻擊類
- 技能分類：技能
- 浪費數值：體力
- 領悟技能：極火六陽(six fire)
- 領悟機率：極低
- 預備功夫：從缺

</details>
<details><summary><strong>筆之心</strong>(`know pen`)</summary>

- 原文頁面：[`skill/fan.html`]({{ '/skill/fan.html' | relative_url }})
- 類別：武器技能
- 英文名稱：know pen
- 中文名稱：筆之心
- 攻擊武器：筆扇
- 互相教導：可以
- 技能功能：攻擊類
- 技能分類：技能
- 浪費數值：體力
- 領悟技能：臨書點穴(write pen)
- 領悟機率：很低
- 預備功夫：從缺

</details>
<details><summary><strong>泰山長拳</strong>(`long fist`)</summary>

- 原文頁面：[`skill/fist.html`]({{ '/skill/fist.html' | relative_url }})
- 類別：武器技能
- 英文名稱：long fist
- 中文名稱：泰山長拳
- 攻擊武器：空手
- 互相教導：可以
- 技能功能：攻擊類
- 技能分類：技能
- 浪費數值：體力
- 領悟技能：瀧山拳法(lung shan)
- 領悟機率：很低
- 預備功夫：從缺

</details>
<details><summary><strong>楊家槍法</strong>(`young gun`)</summary>

- 原文頁面：[`skill/lance.html`]({{ '/skill/lance.html' | relative_url }})
- 類別：武器技能
- 英文名稱：young gun
- 中文名稱：楊家槍法
- 攻擊武器：槍矛
- 互相教導：不可以
- 技能功能：攻擊類
- 技能分類：技能
- 浪費數值：體力
- 領悟技能：密傳˙八極槍(eight gun)
- 領悟機率：極低
- 預備功夫：從缺

</details>
<details><summary><strong>猴棍</strong>(`monkey stick`)</summary>

- 原文頁面：[`skill/stick.html`]({{ '/skill/stick.html' | relative_url }})
- 類別：武器技能
- 英文名稱：monkey stick
- 中文名稱：猴棍
- 攻擊武器：棍棒
- 互相教導：不可以
- 技能功能：攻擊類
- 技能分類：技能
- 浪費數值：體力
- 領悟技能：日晃棍法(day stick)
- 領悟機率：極低
- 預備功夫：從缺

</details>
<details><summary><strong>華山劍法</strong>(`hua sword`)</summary>

- 原文頁面：[`skill/sword.html`]({{ '/skill/sword.html' | relative_url }})
- 類別：武器技能
- 英文名稱：hua sword
- 中文名稱：華山劍法
- 攻擊武器：長劍
- 互相教導：可以
- 技能功能：攻擊類
- 技能分類：技能
- 浪費數值：體力
- 領悟技能：封山劍法(fonxan sword)
- 領悟機率：很低
- 預備功夫：從缺

</details>
<details><summary><strong>紫龍鞭法</strong>(`gwhip`)</summary>

- 原文頁面：[`skill/whip.html`]({{ '/skill/whip.html' | relative_url }})
- 類別：武器技能
- 英文名稱：gwhip
- 中文名稱：紫龍鞭法
- 攻擊武器：鞭
- 互相教導：不可以
- 技能功能：攻擊類
- 技能分類：技能
- 浪費數值：體力
- 領悟技能：冥蛇鞭法(ming snake)
- 領悟機率：很低
- 預備功夫：從缺

</details>

## 法術技能

<details><summary><strong>輕度傷害</strong>(`cause light`)</summary>

- 原文頁面：[`skill/dark.html`]({{ '/skill/dark.html' | relative_url }})
- 類別：法術技能
- 英文名稱：cause light
- 中文名稱：輕度傷害
- 攻擊武器：空手
- 互相教導：不可以
- 技能功能：攻擊類
- 技能分類：暗系
- 浪費數值：法力
- 領悟技能：中度傷害(cause serious)
- 領悟機率：極高
- 預備功夫：從缺

</details>
<details><summary><strong>製造食物</strong>(`create food`)</summary>

- 原文頁面：[`skill/earth.html`]({{ '/skill/earth.html' | relative_url }})
- 類別：法術技能
- 英文名稱：create food
- 中文名稱：製造食物
- 攻擊武器：空手
- 互相教導：不可以
- 技能功能：未知
- 技能分類：土系
- 浪費數值：法力
- 領悟技能：偵測藏匿(detect hidden)
- 領悟機率：極高
- 預備功夫：從缺

</details>
<details><summary><strong>詛咒術</strong>(`curse`)</summary>

- 原文頁面：[`skill/evil.html`]({{ '/skill/evil.html' | relative_url }})
- 類別：法術技能
- 英文名稱：curse
- 中文名稱：詛咒術
- 攻擊武器：空手
- 互相教導：不可以
- 技能功能：攻擊類
- 技能分類：邪系
- 浪費數值：法力
- 領悟技能：魔界之門(gate)
- 領悟機率：極高
- 預備功夫：從缺

</details>
<details><summary><strong>火焰之掌</strong>(`burning hands`)</summary>

- 原文頁面：[`skill/fire.html`]({{ '/skill/fire.html' | relative_url }})
- 類別：法術技能
- 英文名稱：burning hands
- 中文名稱：火焰之掌
- 攻擊武器：空手
- 互相教導：不可以
- 技能功能：攻擊類
- 技能分類：火系
- 浪費數值：法力
- 領悟技能：烈焰術(flamestrike)
- 領悟機率：極高
- 預備功夫：從缺

</details>
<details><summary><strong>群仙祝福</strong>(`bless`)</summary>

- 原文頁面：[`skill/holy.html`]({{ '/skill/holy.html' | relative_url }})
- 類別：法術技能
- 英文名稱：bless
- 中文名稱：群仙祝福
- 攻擊武器：空手
- 互相教導：不可以
- 技能功能：防禦類
- 技能分類：聖系
- 浪費數值：法力
- 領悟技能：巨人之力(giant strength)
- 領悟機率：極高
- 預備功夫：從缺

</details>
<details><summary><strong>千丈光芒</strong>(`make light`)</summary>

- 原文頁面：[`skill/light.html`]({{ '/skill/light.html' | relative_url }})
- 類別：法術技能
- 英文名稱：make light
- 中文名稱：千丈光芒
- 攻擊武器：空手
- 互相教導：不可以
- 技能功能：未知
- 技能分類：光系
- 浪費數值：法力
- 領悟技能：夜視術(infravision)
- 領悟機率：極高
- 預備功夫：從缺

</details>
<details><summary><strong>酸液術</strong>(`acid blast`)</summary>

- 原文頁面：[`skill/poison.html`]({{ '/skill/poison.html' | relative_url }})
- 類別：法術技能
- 英文名稱：acid blast
- 中文名稱：酸液術
- 攻擊武器：空手
- 互相教導：不可以
- 技能功能：攻擊類
- 技能分類：毒系
- 浪費數值：法力
- 領悟技能：眼盲術(blindness)
- 領悟機率：極高
- 預備功夫：從缺

</details>
<details><summary><strong>輕度電擊術</strong>(`shocking grasp`)</summary>

- 原文頁面：[`skill/thunder.html`]({{ '/skill/thunder.html' | relative_url }})
- 類別：法術技能
- 英文名稱：shocking grasp
- 中文名稱：輕度電擊術
- 攻擊武器：空手
- 互相教導：不可以
- 技能功能：攻擊類
- 技能分類：雷電系
- 浪費數值：法力
- 領悟技能：小雷球(lightning bolt)
- 領悟機率：極高
- 預備功夫：從缺

</details>
<details><summary><strong>輕度治療</strong>(`cure light`)</summary>

- 原文頁面：[`skill/water.html`]({{ '/skill/water.html' | relative_url }})
- 類別：法術技能
- 英文名稱：cure light
- 中文名稱：輕度治療
- 攻擊武器：空手
- 互相教導：不可以
- 技能功能：防禦類
- 技能分類：水系
- 浪費數值：法力
- 領悟技能：療毒術(cure poison)
- 領悟機率：極高
- 預備功夫：從缺

</details>
<details><summary><strong>體力恢復術</strong>(`refresh`)</summary>

- 原文頁面：[`skill/wind.html`]({{ '/skill/wind.html' | relative_url }})
- 類別：法術技能
- 英文名稱：refresh
- 中文名稱：體力恢復術
- 攻擊武器：空手
- 互相教導：不可以
- 技能功能：防禦類
- 技能分類：風系
- 浪費數值：法力
- 領悟技能：微風喚醒術(wakeup)
- 領悟機率：極高
- 預備功夫：從缺

</details>

## 職業技能

<details><summary><strong>打聽技能</strong>(`pry`)</summary>

- 原文頁面：[`skill/bard.html`]({{ '/skill/bard.html' | relative_url }})
- 類別：職業技能
- 英文名稱：pry
- 中文名稱：打聽技能
- 攻擊武器：空手
- 互相教導：不可以
- 技能分類：吟唱系
- 浪費數值：法力
- 領悟技能：從缺
- 預備功夫：從缺

</details>
<details><summary><strong>劍君十二恨</strong>(`hate sword`)</summary>

- 原文頁面：[`skill/bravo.html`]({{ '/skill/bravo.html' | relative_url }})
- 類別：職業技能
- 英文名稱：hate sword
- 中文名稱：劍君十二恨
- 攻擊武器：長劍
- 互相教導：不可以
- 技能功能：攻擊類
- 技能分類：暗殺系
- 浪費數值：體力
- 領悟技能：從缺
- 預備功夫：從缺

</details>
<details><summary><strong>經脈逆行</strong>(`anti physique`)</summary>

- 原文頁面：[`skill/doctor.html`]({{ '/skill/doctor.html' | relative_url }})
- 類別：職業技能
- 英文名稱：anti physique
- 中文名稱：經脈逆行
- 攻擊武器：空手
- 互相教導：不可以
- 技能功能：冥想類
- 技能分類：醫療系
- 浪費數值：法力
- 領悟技能：從缺
- 預備功夫：從缺

</details>
<details><summary><strong>斬龍破鳳刀</strong>(`dragon phoenix`)</summary>

- 原文頁面：[`skill/general.html`]({{ '/skill/general.html' | relative_url }})
- 類別：職業技能
- 英文名稱：dragon phoenix
- 中文名稱：斬龍破鳳刀
- 攻擊武器：大刀
- 互相教導：不可以
- 技能功能：攻擊類
- 技能分類：格鬥系
- 浪費數值：體力
- 領悟技能：從缺
- 預備功夫：從缺

</details>
<details><summary><strong>死黑核爆裂地獄</strong>(`dark hell`)</summary>

- 原文頁面：[`skill/mage.html`]({{ '/skill/mage.html' | relative_url }})
- 類別：職業技能
- 英文名稱：dark hell
- 中文名稱：死黑核爆裂地獄
- 攻擊武器：空手
- 互相教導：不可以
- 技能功能：攻擊類
- 技能分類：法師系
- 浪費數值：法力
- 領悟技能：七鑰守護神(seven key numen)
- 領悟機率：極低
- 預備功夫：從缺

</details>
<details><summary><strong>加強武器威力</strong>(`enchant weapon`)</summary>

- 原文頁面：[`skill/smith.html`]({{ '/skill/smith.html' | relative_url }})
- 類別：職業技能
- 英文名稱：enchant weapon
- 中文名稱：加強武器威力
- 攻擊武器：空手
- 互相教導：不可以
- 技能功能：物品類
- 技能分類：鑄造系
- 浪費數值：法力
- 領悟技能：鑑定術(identify)
- 領悟機率：一般
- 預備功夫：從缺

</details>
<details><summary><strong>抹毒</strong>(`venom`)</summary>

- 原文頁面：[`skill/thief.html`]({{ '/skill/thief.html' | relative_url }})
- 類別：職業技能
- 英文名稱：venom
- 中文名稱：抹毒
- 攻擊武器：空手
- 互相教導：不可以
- 技能功能：物品類
- 技能分類：盜賊系
- 浪費數值：法力
- 領悟技能：開鎖(pick)
- 領悟機率：低
- 預備功夫：從缺
- 職業限制：伶 人則等級最低要 一級才能學習﹐熟練度最高可以到 出神入化﹗ 刺 客則等級最低要 一級才能學習﹐熟練度最高可以到 出神入化﹗ 郎 中則等級最低要 一級才能學習﹐熟練度最高可以到 出神入化﹗ 武 官則等級最低要 一級才能學習﹐熟練度最高可以到 出神入化﹗ 將 軍則等級最低要 一級才能學習﹐熟練度最高可以到 出神入化﹗ 天 師則等級最低要 一級才能學習﹐熟練度最高可以到 出神入化﹗ 文 官則等級最低要 一級才能學習﹐熟練度最高可以到 出神入化﹗ 道 士則等級最低要 一級才能學習﹐熟練度最高可以到 出神入化﹗ 鑄劍師則等級最低要 一級才能學習﹐熟練度最高可以到 出神入化﹗ 盜 賊則等級最低要 一級才能學習﹐熟練度最高可以到 一代宗師﹗ 平 民不能學習此技能﹗
- 限 制：一、本技能限制學識不能低於五。
- 教 導：一、襄平的藥材行老闆(druggest)有教導抹毒﹐他可能會教導你﹐費用 1500 兩。

</details>

## 其他技能

<details><summary><strong>技能的熟練度共分十二個等級</strong> - 特殊參照頁</summary>

- 原文頁面：[`skill/learnlv.html`]({{ '/skill/learnlv.html' | relative_url }})
- 類別：其他技能
- 說明：這頁是技能熟練度參照，不是一般技能明細頁，因此不一定會有 `英文名稱 / 中文名稱 / 領悟技能` 等欄位。

</details>
<details><summary><strong>騎術</strong>(`mount`)</summary>

- 原文頁面：[`skill/skill.html`]({{ '/skill/skill.html' | relative_url }})
- 類別：其他技能
- 英文名稱：mount
- 中文名稱：騎術
- 攻擊武器：空手
- 互相教導：不可以
- 技能功能：騎術
- 技能分類：技能
- 浪費數值：體力
- 領悟技能：從缺
- 預備功夫：從缺

</details>
<details><summary><strong>翦雲步</strong>(`cloud steps`)</summary>

- 原文頁面：[`skill/step.html`]({{ '/skill/step.html' | relative_url }})
- 類別：其他技能
- 英文名稱：cloud steps
- 中文名稱：翦雲步
- 攻擊武器：空手
- 互相教導：可以
- 技能功能：閃躲類
- 技能分類：技能
- 浪費數值：體力
- 領悟技能：青玄身法(gdragon steps)
- 領悟機率：很低
- 預備功夫：從缺

</details>

## 區域設計建議

1. **掉落／習得來源**：於 `res` 檔內安排 NPC 擁有特定技能，並在 `mob` 描述中註記「可教導」或「僅領悟」。
2. **熟練度上限**：技能頁面常以「馬馬虎虎」、「神乎其技」描述各職業上限，請在 NPC 對話或任務條件中引用這些詞彙，避免與英文 Rank 混用。
3. **資源消耗**：資料欄位中的「浪費數值」可直接映射成戰鬥節奏；例如步法技能多耗體力，在山地或長途區域可安排更多休息節點。
4. **秘笈／study**：任何 `study` 互動都需在區域 `obj` 檔設計對應書籍，並在 `help` 或 `notes` 中補足說明。

## 與公告／國家系統的連動

- 請對照 `system.md` 的公告時間線；例如某步法在特定日期後才開放時，區域掉落或 NPC 教學也應標註版本時點。
- 國家系統指令如 `realm !join` 會查技能欄位（權限），因此 `realm.md` 的資料應與此頁交叉檢查。

> 原文：skill/index.html 及所有 `skill/*.html`
