---
name: apple-design-principles
description: >-
  Apple-style design and copy guidance for reviewing or writing product plans, app and web UI, UX copy (buttons, empty states, errors, confirmation dialogs, notifications) and landing page, product page, headline or keynote copy in English and Chinese. Covers focus and subtraction, hierarchy, typography, color, motion, accessibility (Apple HIG and WCAG 2.2), web and SaaS/tool interfaces, and Chinese-English transcreation. Use whenever the user wants to critique, audit, simplify or polish a screen, screenshot, page or flow, rewrite product or interface copy, or make something feel more like Apple, even if Apple is not mentioned. 中文触发：苹果风、苹果式、审查界面、截图、设置页、落地页、做减法、层级、改文案、标题、发布会文案、官网文案、空状态、报错文案、确认弹窗、无障碍、对比度、本地化。Not for writing or debugging code, backend or data work, Apple company news, device troubleshooting, App Store submission, or plain translation.
license: CC-BY-4.0
metadata:
  author: hanqianhq
  version: "2.0.0"
  repository: https://github.com/hanqianhq/apple-design-principles
---

# Apple-style Design Review｜苹果式设计审查

用苹果式的方法审查和改写产品方案、界面与文案：**先聚焦，再层级，再细节；每条批评都给出改法。**
示例一律用原创虚构产品，不复制苹果的文案和素材。本 skill 与 Apple Inc. 无关。

## 1. 先分流（每次开始前做）

先判断三件事，再决定读哪份 reference。分错类型是最常见的失误：给网页套 iOS 的 pt，给后台工具套营销页的「巧思」。

| 判断 | 选项 | 读什么 |
|---|---|---|
| **界面类型** | **Persuade**：落地页、产品页、发布会、广告——目标是让人记住并行动 | [marketing-copy.md](references/marketing-copy.md) |
| | **Operate**：App 功能页、设置、后台、SaaS / 工具——目标是把任务做完 | [checklist-tool-ui.md](references/checklist-tool-ui.md) |
| | **Read**：帮助文档、说明、更新日志——目标是看懂 | [ux-writing.md](references/ux-writing.md) |
| **平台** | iOS / iPadOS / watchOS / visionOS | [checklist-ios.md](references/checklist-ios.md) |
| | Web（含桌面浏览器、移动网页、Electron） | [checklist-web.md](references/checklist-web.md) |
| | 两端同一套设计 | [platform-mapping.md](references/platform-mapping.md) |
| **任务** | 审查（给问题和改法） | 第 2 节流程 + 对应 checklist |
| | 写 / 改文案 | [ux-writing.md](references/ux-writing.md)（界面）或 [marketing-copy.md](references/marketing-copy.md)（营销） |
| | 中英本地化 | [marketing-copy.md](references/marketing-copy.md) 第 5 节 + [typography-zh.md](references/typography-zh.md) |

分流规则：
- **单位跟平台走**：iOS 用 pt 和 HIG；Web 用 CSS px 和 WCAG 2.2（例如目标尺寸 AA 是 24×24 CSS px，44×44 是 AAA 或推荐值）。两者都要时并列给出。
- **Operate 先真后美**：数据真实、任务走得通、危险操作有保护，排在任何视觉打磨之前。
- **Persuade 才用巧思**：报错、设置、权限、确认弹窗只写直白版，不套标题公式。
- 用户给的是截图或描述而不是代码：按看到的写，看不到的状态（加载、出错、空）列为「待确认」，不要编。

## 2. 审查流程（复制这份清单，逐项打勾）

```
- [ ] 1 定目标：一句话写出「谁、在什么场景、要完成什么」。写不出来就先问。
- [ ] 2 分流：界面类型 × 平台 × 任务（第 1 节），读对应 reference。
- [ ] 3 做减法：列出全部元素 / 功能 / 卖点，标「删 / 后置 / 保留」。
- [ ] 4 查层级：3 秒测试——第一眼落在哪？是否只有一个主焦点、一个主操作、一个主信息？
- [ ] 5 过检查表：按对应 checklist 逐项过，记录不通过项和证据（位置、数值、原文）。
- [ ] 6 分级：按第 3 节定 P0 / P1 / P2。
- [ ] 7 给改法：每条都写「问题 → 依据 → 改法或改后文案」；文案给直白版，营销文案再加巧思版，中英文分别写。
- [ ] 8 复核：改完整体再看一遍——风格一致吗？深色模式、大字号、减弱动效、键盘操作下还成立吗？
```

整个任务期间都按这份清单走，后续追问也一样；不要只做第一轮。

## 3. 优先级总表

| 级别 | 类别 | 必须有 | 常见反模式 |
|---|---|---|---|
| **P0 阻断** | 真实与信任 | 界面上只有真实数据；计数、分页、余额前后一致；营销承诺 = 实际能力 | 写死的示例动态；「共 128 个」配空表格；官网「免费注册」、注册页「仅限邀请」 |
| | 任务走得通 | 核心流程能走到结果；失败时说清发生了什么、数据还在不在、下一步 | 只有转圈没有结果；「操作失败」 |
| | 危险与不可逆 | 删除 / 覆盖 / 扣费前说明影响范围；能撤销或有回收站；和常用操作分开 | 红色「全部删除」紧挨「导出」，点了就删 |
| | 无障碍硬指标 | 文字对比度 ≥ 4.5:1（大字 3:1）；目标尺寸达标（iOS 44pt / Web ≥ 24 CSS px）；可读屏、可键盘操作、焦点可见 | 浅灰小字；18px 纯图标链接无名称；`outline: none` |
| **P1 重要** | 聚焦与层级 | 一屏一个主操作、一个主信息；入口不重复 | 两个同样响亮的按钮；同一组入口出现多次 |
| | 一致性 | 一张术语表，一个概念一个词；同一动作全程同名 | 素材 / 资产 / 文件混用；按钮叫「发布」，提示说「提交成功」 |
| | 状态完整 | 空、加载、长任务进度、部分失败、无权限都设计过 | 无权限的按钮点了才报错；长任务刷新后消失 |
| | 文案 | 先说好处或结果，动词开头，不堆参数和空话 | 「新一代 AI 驱动的全场景赋能平台」 |
| | 颜色语义 | 一个强调色表示「可点」；警告 / 删除各有颜色；不只靠颜色 | 品牌色同时当按钮、警告和装饰 |
| **P2 打磨** | 视觉细节 | 统一间距刻度、字号 ≤ 4 级、去装饰性阴影渐变 | 每张卡片不同圆角和阴影 |
| | 动效与语气 | 动效解释变化、短、可打断、可减弱；语气平和 | 每个区块淡入上滑；满屏感叹号 |

同一个问题按最高的那一级算。不确定的写「待确认」并说明需要什么证据。

## 4. 输出模板（默认格式，可按任务增减）

完整版见 [assets/review-report-template.md](assets/review-report-template.md)。

```markdown
## 一句话结论
（整体判断 + 最关键的 1–3 个改动）

## 分流
界面类型：… ｜ 平台：… ｜ 依据：…（HIG / WCAG 2.2 / 本 skill 的 checklist）

## 问题与改法
| 级别 | 位置 | 问题（证据） | 依据 | 改法 / 改后示例 |
|---|---|---|---|---|

## 做减法清单
- 删除：…  - 后置：…  - 合并：…

## 文案改写
- 改前 → 改后（直白版｜营销场景加巧思版｜EN）→ 为什么

## 待确认
- 截图里看不到、需要用户确认的状态或数据
```

只写文案时，可只输出「文案改写」一节；只问标准时，按 [platform-mapping.md](references/platform-mapping.md) 第 4 节回答：分平台给值，标明 AA / AAA / 惯例，附来源链接。

## 5. 范例（输入 → 输出 → 为什么）

**输入**：「Web 版云笔记的删除弹窗：标题『确定吗？』，按钮『是』『否』；删除后无法恢复；按钮是 20×20px 的纯图标。」

**输出（节选）**

| 级别 | 位置 | 问题（证据） | 依据 | 改法 / 改后示例 |
|---|---|---|---|---|
| P0 | 删除 | 不可逆且没说影响范围 | checklist-tool-ui「危险操作」；WCAG 3.3.4 | 删除先进「最近删除」保留 30 天；弹窗写清对象和后果 |
| P0 | 图标按钮 | 20×20px，且无可访问名称 | WCAG 2.5.8（24×24 CSS px）、4.1.2 | 点按区域 ≥ 24×24 CSS px（推荐 44），加 `aria-label="删除笔记"` |
| P1 | 弹窗文案 | 「确定吗？是 / 否」看不出在删什么 | ux-writing「确认弹窗」 | 见下 |

- 改前：确定吗？［是］［否］
- 改后：**删除「周会记录」？** 笔记会移到「最近删除」，30 天内可以恢复。［删除］（破坏性样式）［取消］
- EN：**Delete "Weekly Sync"?** The note moves to Recently Deleted for 30 days. [Delete] [Cancel]

**为什么**：标题直接问具体问题，按钮写动作而不是「是 / 否」；先降低风险（可恢复）再写文案；Web 用 CSS px 和 WCAG，不套 iOS 的 pt。

## 6. 核心原则速记

完整的 31 条原则（带「为什么 / 怎么做」和编号 #1–#31）在 [principles.md](references/principles.md)。审查时引用编号。

1. 聚焦：做好一件事；留一份「不做清单」（#1 #2）。
2. 简单是把复杂藏在里面；默认值替用户做决定（#3 #9）。
3. 一屏一个第一眼；层级靠布局和分组，不靠装饰（#12 #18）。
4. 界面退后，内容在前；材质和装饰只给功能层（#11 #14）。
5. 颜色是语义；不只靠颜色传达信息（#17）。
6. 动效解释变化：短、可打断、可减弱（#19）。
7. 无障碍是底线，数值见 checklist（#20）。
8. 文案先讲好处，再给证据；动词开头，主语是用户，不说「我们」（#23 #24 #31）。
9. 标题可以巧，正文必须直白（#27）。
10. 本地化是重写，不是翻译（#30）。

## 7. References 索引（按需读取，用到哪份读哪份）

| 文件 | 内容 | 什么时候读 |
|---|---|---|
| [principles.md](references/principles.md) | 31 条原则：产品 / UI / 文案，含为什么和怎么做 | 需要引用依据、解释理由时 |
| [checklist-ios.md](references/checklist-ios.md) | iOS / Apple 平台检查表（HIG 口径） | 审 App 界面 |
| [checklist-web.md](references/checklist-web.md) | Web 检查表（WCAG 2.2 原文核对，CSS px） | 审网页、Web App |
| [checklist-tool-ui.md](references/checklist-tool-ui.md) | 工具 / SaaS / 后台检查表：数据真实、计数分页、危险操作、长任务、计费、权限、术语表、资产引用 | Operate 类界面 |
| [platform-mapping.md](references/platform-mapping.md) | iOS ↔ Web 数值和机制对照 | 两端共用设计、或用户问「标准是多少」 |
| [ux-writing.md](references/ux-writing.md) | 按钮、状态、空状态、报错、确认弹窗、通知、术语表模板 | 写任何界面文字 |
| [marketing-copy.md](references/marketing-copy.md) | 产品页骨架、标题公式、卖点模板、发布会结构、中英本地化 | 落地页、产品页、发布会、广告 |
| [typography-zh.md](references/typography-zh.md) | SF 字体家族、中文排版、中西混排 | 字体、排版、中英混排问题 |
| [apple-style-guide.md](references/apple-style-guide.md) | Apple Style Guide 写作规则转述 + 中文对应建议 | 英文措辞、用词规范 |
| [spec-snapshot.md](references/spec-snapshot.md) | 会随版本变化的数值和规范（HIG 字号、Liquid Glass、WWDC 要点、WCAG 版本），带核对日期 | 需要具体数值或最新规范时；用前看核对日期 |
| [philosophy.md](references/philosophy.md) | Rams、Jobs / Ive、《Insanely Simple》、《Creative Selection》→ 可执行检查点 | 方案评审、需要讲「为什么这样做」时 |
| [examples.md](references/examples.md) | 13 组「输入 → 输出 → 为什么」改写范例 | 需要参照改写风格时 |
| [sources.md](references/sources.md) | 全部来源链接 | 需要给出处时 |
