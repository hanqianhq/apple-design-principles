# 规范快照：会随版本变化的数值与规范

> 需要具体数值、或用户问「最新规范」时读。**这里是全 skill 数值的唯一权威来源**；其他文件里出现的数值如与本文件冲突，以本文件为准。
> 规范会更新：引用前先看「核对日期」。距今超过一年，或遇到新的 WWDC / 新系统版本，先去原链接复核再用。

## 目录
1. 核对记录
2. Apple HIG 数值（字号、控件尺寸、对比度）
3. WCAG 2.2 数值（Web）
4. 当前 Apple 平台材质：Liquid Glass
5. WWDC 设计讲座要点（排版、动效、无障碍）
6. 其他带版本的资料

## 1. 核对记录

| 项目 | 来源 | 核对日期 | 方式 |
|---|---|---|---|
| HIG 控件尺寸、字号、对比度表 | developer.apple.com HIG（Buttons / Typography / Accessibility） | 2026-10-09 | 抓取页面数据原文核对 |
| WCAG 2.2 各成功准则数值 | https://www.w3.org/TR/WCAG22/ （W3C Recommendation，2024-12-12 版） | 2026-10-09 | 抓取 W3C 原文核对 |
| Liquid Glass、WWDC 讲座要点 | Apple 开发者文档与 WWDC 视频页（链接见下） | 2026-10-09 | v1 研究时整理，本次未重新逐条核对 |
| Apple Style Guide | support.apple.com（v1 研究时为 2026 年 6 月版） | 2026-10-09 | v1 研究时整理，本次未重新核对 |

## 2. Apple HIG 数值

**控件（点按区域）尺寸**（HIG Accessibility；Buttons 页也写明一般规则「至少 44x44 pt，visionOS 60x60 pt」）

| 平台 | 默认控件尺寸 | 最小控件尺寸 |
|---|---|---|
| iOS、iPadOS | 44×44 pt | 28×28 pt |
| macOS | 28×28 pt | 20×20 pt |
| tvOS | 66×66 pt | 56×56 pt |
| visionOS | 60×60 pt | 28×28 pt |
| watchOS | 44×44 pt | 28×28 pt |

**字号**（HIG Typography / Accessibility）

| 平台 | 默认字号 | 最小字号 |
|---|---|---|
| iOS、iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

**对比度**（HIG Accessibility，以 WCAG AA 为参照）：17 pt 及以下文字 4.5:1；18 pt 及以上 3:1；**粗体任意字号 3:1**。注意这与 WCAG 的「大字」定义（18 pt，或 14 pt 粗体）不完全相同；Web 以 WCAG 为准。默认达不到时，至少在「增强对比度」下提供更高对比的配色。

链接：https://developer.apple.com/design/human-interface-guidelines/buttons ｜ https://developer.apple.com/design/human-interface-guidelines/typography ｜ https://developer.apple.com/design/human-interface-guidelines/accessibility

## 3. WCAG 2.2 数值（Web）

完整的 Web 检查项和每条准则的链接见 [checklist-web.md](checklist-web.md)。核心数值：

| 准则 | 级别 | 数值 |
|---|---|---|
| 1.4.3 Contrast (Minimum) | AA | 文字 4.5:1；大字 3:1（大字 = 至少 18 pt，或 14 pt 粗体，或中日韩字体的等效字号） |
| 1.4.6 Contrast (Enhanced) | AAA | 文字 7:1；大字 4.5:1 |
| 1.4.11 Non-text Contrast | AA | 控件边界、状态、必要图形 3:1 |
| 2.5.8 Target Size (Minimum) | AA（2.2 新增） | 24×24 CSS px，有间距、等效控件、行内等例外 |
| 2.5.5 Target Size (Enhanced) | AAA | 44×44 CSS px |
| 2.4.13 Focus Appearance | AAA（2.2 新增） | 焦点指示至少相当于 2 CSS px 粗的轮廓面积，前后对比 3:1 |
| 1.4.10 Reflow | AA | 320 CSS px 宽（约等于 1280 px 宽下放大 400%）不出现双向滚动 |
| 1.4.4 Resize Text | AA | 不借助辅助技术放大到 200% 不丢内容和功能 |
| 1.4.12 Text Spacing | AA | 行高 1.5 倍、段后 2 倍、字距 0.12 倍、词距 0.16 倍时不丢内容 |
| 2.2.2 Pause, Stop, Hide | A | 自动开始、持续超过 5 秒、与其他内容并列的动画要能暂停 / 停止 / 隐藏 |
| 2.3.1 Three Flashes | A | 任意 1 秒内闪烁不超过 3 次 |

## 4. 当前 Apple 平台材质：Liquid Glass

（WWDC25 推出；随系统更新可能调整。原则层面的要求见 [principles.md](principles.md) #14。）
- 玻璃材质只给功能层（导航栏、工具栏、浮动控件），内容层（列表、卡片）保持实体。
- 不玻璃叠玻璃；菜单在玻璃上用填充和 vibrancy。
- 着色（tint）只给主操作；形状与容器同心（concentric），多用胶囊形。
- 在「降低透明度」「增强对比度」下测试可读性。
- 来源：Adopting Liquid Glass https://developer.apple.com/documentation/TechnologyOverviews/adopting-liquid-glass ；WWDC25 Meet Liquid Glass https://developer.apple.com/videos/play/wwdc2025/219/ ；WWDC25 Get to know the new design system https://developer.apple.com/videos/play/wwdc2025/356/

## 5. WWDC 设计讲座要点（排版、动效、无障碍）

写作类讲座（WWDC22 / 24 / 25 与 HIG Writing）的要点在 [ux-writing.md](ux-writing.md)。

### 排版

5. **The details of UI typography（WWDC20）**：https://developer.apple.com/videos/play/wwdc2020/10175/
   - **光学尺寸**：同一套字形在小字号时要更宽松、笔画更稳，大字号时更紧凑。SF 以前分 Text 和 Display 两套，现在用可变字体，在大约 17–28pt 之间连续过渡。
   - **字距（tracking）和字偶距（kerning）不是一回事**：kerning 由字体设计师针对字母对做好，一般不要动；tracking 必须随字号变化，自定义字距也要分字号设置。文字放不下时，优先让系统自动收紧，太紧就宁可截断。
   - **行高**：长段落用宽松行距（loose leading），高度受限的列表可以收紧，但 HIG 建议三行以上的文字不要用紧行距。
   - **text styles 本身就是层级系统**：字号、字重、行高的组合是预设好的，需要强调时用 emphasized 变体（同字号加粗）。
   - 网页可以用 `system-ui`、`ui-rounded`、`ui-serif`、`ui-monospace` 调用苹果平台上的系统字体。尽量用系统能力，系统每年改进，产品会跟着一起变好。

### 动效

6. **Designing Fluid Interfaces（WWDC18）**：https://developer.apple.com/videos/play/wwdc2018/803/
   - 立刻响应，内容跟着手指一比一移动，一旦跟不上，用户马上就能察觉。
   - 随时可以打断、可以改主意：动画进行中也能接受新手势。
   - 空间一致：元素从哪里来就回哪里去，进出路径对称。
   - 保留手势的动量：根据松手时的速度推算终点（projection）；有动量的手势可以给一点回弹，点按这类没有动量的操作不要回弹。
7. **Animate with springs（WWDC23）**：https://developer.apple.com/videos/play/wwdc2023/10158/
   - 弹簧动画能让位置和速度都连续，所以能接住手势的速度，被打断时也能平滑地转向。
   - 只调两个参数：时长（duration）和弹性（bounce）。先调时长定节奏，再调弹性定性格。
   - 拿不准就用 bounce = 0。想活泼一点或者在手势结束时，再加一点弹性：大约 15% 显得轻快，30% 就能明显看到回弹。
   - 弹簧需要有回弹才好看是误解，不回弹的弹簧动画同样很好。

### 无障碍

8. **Make your app visually accessible（WWDC20）**：https://developer.apple.com/videos/play/wwdc2020/10020/
   - 不只靠颜色：配合形状和符号，并响应「区分时不仅依赖颜色」这个设置。
   - 4.5:1 是大多数情况下可接受的最低对比度；打开「增强对比度」时要提供更高对比的版本。一般规律是浅色模式下颜色更深，深色模式下颜色更浅。
   - 响应「粗体文本」：用系统文字样式就会自动支持。
   - 「减弱动态效果」打开时，用交叉淡入淡出替代位移；「降低透明度」打开时，模糊背景变成实色，以保证文字可读。
9. **Get started with Dynamic Type（WWDC24）**：https://developer.apple.com/videos/play/wwdc2024/10074/
   - 用内置文字样式，自动获得动态字体支持。
   - 尽量不截断：标签行数不设上限，大字号时让文字多占几行。
   - 字号变大时调整布局：横排改竖排，多列改少列。
   - 有意义的图标要跟着字号放大（SF Symbols 会自动跟随）；纯装饰的图可以不放大，但文字要能绕排。
   - 无法放大的固定栏（比如标签栏）要支持「大内容查看器」（Large Content Viewer）。

## 6. 其他带版本的资料

- Apple Style Guide：v1 研究时为 2026 年 6 月版。https://support.apple.com/guide/applestyleguide/welcome/web （PDF：https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf ）
- 《中华人民共和国广告法》第九条（禁止「国家级、最高级、最佳」等用语）：https://www.samr.gov.cn/zt/ndzt/2019n/bjspjsqjxcjwljxyjsckpxc/zcfg/art/2023/art_f383fbf8c106420b8951ba8d9508d32d.html
- 产品页句式观察（marketing-copy.md 第 1 节）：2026-10-09 观察 apple.com / apple.com.cn，页面改版后样本可能失效，句式规律仍可用。
