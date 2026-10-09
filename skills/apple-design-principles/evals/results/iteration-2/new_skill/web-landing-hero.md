## 一句话结论
Hero 想说的太多、按钮抢焦点、还有几处 WCAG 硬伤。先修无障碍（P0），再收成一句话 + 一个主按钮。

## 分流
界面类型：Persuade（营销首屏）｜平台：Web（CSS px，WCAG 2.2）｜依据：checklist-web W1/W5/W7、marketing-copy

## 问题与改法
| 级别 | 位置 | 问题（证据） | 依据 | 改法 |
|---|---|---|---|---|
| P0 | 正文 | #A0A0A0 on white ≈ 2.6:1，低于 4.5:1；13px 偏小 | WCAG 1.4.3（AA 4.5:1） | 正文用 #595959 以深（≥ 7:1 更稳），字号 16px 起（惯例，非 WCAG 要求） |
| P0 | 轮播 | 5 张自动播放、永不停止 | WCAG 2.2.2 Pause, Stop, Hide | 改成静态主视觉；若保留 carousel：提供暂停按钮、尊重 `prefers-reduced-motion`、不自动轮播 |
| P0 | 社交图标链接 | 18×18 px，纯图标无名称 | WCAG 2.5.8（24×24 CSS px，AA）、4.1.2 | 点按区域 ≥ 24×24 CSS px（推荐 44），加 `aria-label="Lingo on LinkedIn"`，给读屏可访问名称 |
| P1 | 按钮 | 「Start Free Trial」「Book a Demo」同样醒目 | #12 层级 | 一个 primary button：Start Free Trial；Book a Demo 改成文字链接 |
| P1 | 标题 | 堆叠 Next-Generation、AI-Powered、Omnichannel、Empowering | #25、#29；marketing-copy §3 | 见下，写用户看到的结果 |

## 文案改写（标题两版）
- 直白版（Plain）：**Every meeting, in every language.** Sub: Lingo translates live as people speak, so everyone follows along in their own language.
- 巧思版（Clever）：**Talk freely. Be understood.** Sub: Real-time translation for meetings across 40 languages.¹（¹ 脚注写清语言列表口径）
- CTA：[Start Free Trial] · Watch a 2-minute demo ›
- 中文版：**说你的语言，大家都听得懂。**

## 待确认
- 支持的语言数、准确率等数字的来源；移动端 hero 的排版
