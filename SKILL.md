---
name: 苹果式产品/UI/文案原则手册
description: >-
  用这个 when：需要按苹果风格审查或设计产品方案、App/网页界面、官网或发布会式文案（中英文）；含原则清单、自查检查表、正反例改写、审查流程，以及设计思想源头（Rams/Jobs/Ive/Insanely Simple/Creative Selection）、WWDC 与 Apple Style Guide 规范要点、SF 字体与中文排版、苹果文案句式拆解和 5 组实战改写。
---
# 苹果式 产品 / UI / 文案 原则手册（Apple-style Design Principles Handbook）

> 用途：按苹果式的思路审查或设计产品方案、界面、官网或发布会式文案。
> 说明：本手册只提炼方法与原则，示例全是原创的虚构产品（笔记 App「Leaf」、耳机「Hush」、手表「Pulse」等），不引用、不复制苹果的文案和素材。
> 数值类规范（44pt、对比度、字号）出自 Apple Human Interface Guidelines（HIG）与 WCAG，用前请对照最新版 HIG 核实。

**目录**
- 用起来：A 核心原则清单 → B 自查检查表 → C 正反例改写 → D 使用流程（审查时按 D 走，用 A 的编号引用原则）
- 为什么这样做：E 设计思想源头（Rams、Jobs 与 Ive、《Insanely Simple》、《Creative Selection》）
- 规范细节：F 设计规范层（WWDC 演讲、Apple Style Guide、SF 字体与中文排版，末尾附补充检查项）
- 写文案：G 文案拆解（10 个样本、页面骨架、标题公式、卖点模板、中英本地化差异）
- 练手：H 实战练习（5 组改前改后）
- 参考来源

---

## A. 核心原则清单

格式：**原则**：一句话。｜为什么｜怎么做

### A1. 产品（Product）

1. **聚焦（Focus）**：做成一件事，胜过做完十件。
   - 为什么：资源和用户注意力都有限，平均分配就是平庸。
   - 怎么做：写下产品「唯一要解决的问题」，砍掉不直接服务于它的功能；每个版本只讲 1 个主故事。
2. **对一千件事说不（Saying no）**：功能清单的价值在于删掉了什么。
   - 为什么：每加一个功能，都会给所有用户增加理解成本。
   - 怎么做：维护一份「不做清单」，写明理由；新需求先回答「不做会怎样」。
3. **简单是复杂的终点（Simplicity ≠ simplistic）**：简单不是少做，而是把复杂留在内部。
   - 为什么：用户看到的是结果，不该承担系统的复杂度。
   - 怎么做：用智能默认值代替设置项；能自动判断的不让用户选。
4. **从体验倒推技术（Start with the experience）**：先定义用户的感受，再选技术。
   - 为什么：技术驱动容易做出「能做但没人要」的东西。
   - 怎么做：方案以「用户在某个场景下的某个时刻」开头，而不是「我们有某项能力」。
5. **整体体验（Whole experience）**：开箱、上手、使用、售后都是产品。
   - 为什么：用户的评价来自最弱的那一环。
   - 怎么做：画出端到端旅程，每个触点指定负责人和质量标准。
6. **软硬与服务一体（Integration）**：自己掌控关键环节，体验才能连贯。
   - 为什么：割裂的系统会把衔接成本转嫁给用户。
   - 怎么做：跨设备 / 跨模块保持同一套交互模型、同一套命名，状态能无缝接续。
7. **看不见的地方也要做好（Care for the unseen）**：背面的做工决定正面的气质。
   - 为什么：细节是信任的累积，粗糙会在某个时刻暴露。
   - 怎么做：检查空状态、错误态、加载态、边界数据、极端字号。
8. **好设计是尽可能少的设计（Less, but better，受 Dieter Rams 影响）**：每个元素都要有存在的理由。
   - 为什么：装饰会抢走内容的注意力。
   - 怎么做：逐个元素问「删掉会损失什么」，答不上来就删。
9. **有主张的默认值（Opinionated defaults）**：替用户做好大多数决定，同时保留出口。
   - 为什么：大多数人从不改设置，默认值就是产品本身。
   - 怎么做：默认值覆盖 80% 场景；高级选项后置（渐进披露）。

### A2. UI（界面，依据 HIG）

10. **清晰（Clarity）**：任何尺寸下，文字都可读，图标一看就懂，功能不含糊。
    - 为什么：看不清就用不了。
    - 怎么做：正文 iOS 默认 17pt、最小 11pt；避免 Ultralight / Thin / Light 小字；图标配文字或用通用符号。
11. **内容优先，界面退后（Deference / content first）**：UI 是舞台，不是主角。
    - 为什么：用户为内容而来。
    - 怎么做：控件少、轻、靠边；全屏背景延伸到导航栏下方；用留白代替边框和底色。
12. **层级（Hierarchy）**：一屏只有一个第一眼。
    - 为什么：所有东西都重要，等于没有重要的。
    - 怎么做：按「最重要→次要」从上到下、从起始侧到末尾侧排列；用字号、字重、颜色三者中的 1–2 个拉开层级；用分组和布局表达层级，而不是靠装饰。
13. **深度与分层（Depth / layers）**：用层次关系说明「我在哪、从哪来、回哪去」。
    - 为什么：空间感帮助理解导航。
    - 怎么做：模态从触发源展开、收回到原位；导航层与内容层分开。
14. **Liquid Glass 只用于功能层**：玻璃材质给导航和控件，内容层保持实体。
    - 为什么：玻璃叠玻璃会让层级混乱、可读性下降。
    - 怎么做：不在内容区（列表、卡片）用玻璃；不玻璃叠玻璃；着色（tint）只给主操作；形状与容器同心（concentric），多用胶囊形；测试「降低透明度」「增强对比度」。
15. **一致性与熟悉感（Consistency）**：用系统组件和平台惯例，让人不用学。
    - 为什么：熟悉的交互零学习成本。
    - 怎么做：优先系统控件、SF Symbols、标准手势；同一操作在各平台位置一致；同一个颜色只表达一种含义。
16. **字体有节制（Typography）**：一种字族、少量字重、清楚的字号阶梯。
    - 为什么：字体太多会模糊层级、显得不专业。
    - 怎么做：西文 SF Pro（衬线需求用 New York），中文苹方（PingFang SC）；字重以 Regular / Medium / Semibold / Bold 为主；支持动态字体（Dynamic Type），放大至少 200% 时层级仍然成立。
17. **颜色是语义，不是装饰（Semantic color）**：颜色用来表达状态与可交互性。
    - 为什么：滥用颜色会让真正的信号失效。
    - 怎么做：用系统色 / 语义色（label、secondaryLabel、systemBackground…）；一个强调色（tint）代表可点击；每个自定义色都给浅色、深色、高对比三个版本；不只靠颜色传递信息。
18. **留白是结构（Whitespace as structure）**：间距本身就在分组。
    - 为什么：靠近即相关，疏远即无关。
    - 怎么做：统一间距刻度（如 4/8 的倍数）；组内间距 < 组间间距；对齐优先，缩进表示从属。
19. **动效有目的（Purposeful motion）**：动画解释变化，而不是表演。
    - 为什么：无意义的动画分散注意力，甚至让人不适。
    - 怎么做：动效跟随手势、符合物理直觉（弹簧、惯性），短而准；高频操作少加动画；动画可被打断；支持「减弱动态效果」（Reduce Motion），用淡入淡出替代位移和缩放。
20. **无障碍是底线（Accessibility for everyone）**：可感知、可理解、可适配。
    - 为什么：无障碍让产品覆盖更多人，也让所有人在弱光、单手、嘈杂时更好用。
    - 怎么做：触控目标 ≥ 44×44pt（visionOS 60×60pt）；文字对比度 ≥ 4.5:1（18pt 及以上或粗体 ≥ 3:1）；每个控件有 VoiceOver 标签；支持动态字体、增强对比度、降低透明度；信息不只靠颜色或声音。
21. **渐进披露（Progressive disclosure）**：先给最常用的，再给更多。
    - 为什么：选项太多会让人无从下手。
    - 怎么做：主界面只留核心操作；高级功能放进菜单、二级页或「更多」。

### A3. 文案（Copywriting，官网 / 发布会式）

22. **一句话只说一件事（One idea per line）**：短句、有节奏。
    - 为什么：屏幕上的人是扫读，不是细读。
    - 怎么做：标题 ≤ 8 个英文词 / ≤ 12 个汉字；一段只讲一个利益点；长句拆短。
23. **讲利益，不堆参数（Benefit over spec）**：先说「你能做什么」，再用参数证明。
    - 为什么：参数是证据，不是理由。
    - 怎么做：结构「利益 → 场景 → 数字佐证」；参数放到小字或规格页。
24. **动词驱动、以「你」为中心（Verb-led, you-focused）**：主语是用户，动作是重点。
    - 为什么：动词带来画面感和行动感。
    - 怎么做：少用「我们的产品拥有…」，多用「你可以…」「随手…」；按钮以动词开头（「添加到购物袋」）。
25. **具体胜于宏大（Concrete over abstract）**：用一个可想象的场景代替形容词。
    - 为什么：「强大」「极致」「革命性」人人都说，等于没说。
    - 怎么做：把形容词换成画面或对比（「从早上通勤听到晚上回家」）。
26. **数字要有参照（Numbers with meaning）**：数字少而准，并说明它意味着什么。
    - 为什么：孤立的数字没有感知。
    - 怎么做：一屏只突出 1 个大数字；附上对比对象或换算（「最长 30 小时，约等于…」）；注明测试条件。
27. **标题有巧思，正文要直白（Clever headline, plain body）**：标题可以双关、押韵、反转，正文必须一读就懂。
    - 为什么：标题负责被记住，正文负责被理解。
    - 怎么做：标题用双关 / 对仗 / 极短的反差；巧思不能牺牲清楚，看不懂就改直白。
28. **节奏与留白（Rhythm）**：文案也有「留白」。
    - 为什么：短-短-长的节奏更容易记住。
    - 怎么做：用三段式、并列、句号断句；少用感叹号；一个页面只有一个主口号。
29. **克制自信（Confident restraint）**：不喊叫、不夸张、不贬低对手。
    - 为什么：自信来自事实，夸张会削弱可信度。
    - 怎么做：去掉「最」「第一」「颠覆」等无法证明的词（中文还涉及广告法）；用事实说话。
30. **本地化是重写，不是翻译（Transcreation）**：中文要有中文的节奏和韵味。
    - 为什么：英文双关直译成中文往往失效。
    - 怎么做：保留意图，重造修辞（英文双关 → 中文对仗 / 四字格 / 谐音）；中文标题追求音节平衡；中英文之间加空格；数字用阿拉伯数字；术语保持一致。
31. **界面文案要友好、简明（UI writing）**：说清发生了什么、接下来做什么。
    - 为什么：报错和提示是用户最焦虑的时刻。
    - 怎么做：不怪用户、不用技术代码；给出可执行的下一步；同一个概念全程用同一个词。

---

## B. 自查检查表（可勾选）

### B1. 产品
- [ ] 能用一句话说清这个方案解决什么问题、为谁解决
- [ ] 有明确的「不做清单」，砍掉的功能有理由
- [ ] 默认值覆盖大多数人，用户不改设置也好用
- [ ] 端到端旅程（发现→上手→日常→出错→离开）每一环都设计过
- [ ] 跨端 / 跨模块的交互和命名一致
- [ ] 空状态、错误态、加载态、离线、极端数据都考虑过

### B2. 视觉层级
- [ ] 每屏只有一个视觉焦点 / 主操作
- [ ] 眯眼看（模糊测试），层级顺序与重要程度一致
- [ ] 层级靠布局和分组表达，而不是边框、阴影、色块堆叠
- [ ] 控件与内容分离：导航 / 控件在功能层，内容在内容层
- [ ] 使用 Liquid Glass 时：只在导航 / 控件上用，无玻璃叠玻璃，内容区不用玻璃，tint 只给主操作

### B3. 字体
- [ ] 字族 ≤ 2 种（推荐系统字体：SF Pro / 苹方）
- [ ] 字号阶梯清楚，层级级数 ≤ 4
- [ ] 正文不小于平台默认（iOS 17pt），最小不低于 11pt
- [ ] 小字不用细字重（Ultralight / Thin / Light）
- [ ] 支持动态字体，放大到 200% 不截断、层级仍成立
- [ ] 中文行高适当放宽（约 1.5–1.7 倍），中英文混排加空格

### B4. 色彩
- [ ] 一个强调色（tint），只用于可交互元素
- [ ] 同一种颜色只代表一种含义
- [ ] 使用语义色，浅色 / 深色 / 高对比三种外观都检查过
- [ ] 文字对比度 ≥ 4.5:1（大字或粗体 ≥ 3:1）
- [ ] 信息不只靠颜色区分（配合图标、文字、形状）
- [ ] 在强光、弱光、不同屏幕上看过

### B5. 留白与布局
- [ ] 使用统一的间距刻度
- [ ] 组内间距 < 组间间距，分组一眼可辨
- [ ] 元素对齐到同一网格，缩进表示从属
- [ ] 尊重安全区域（Safe Area），全屏背景延伸到导航栏下
- [ ] 小屏、大屏、横竖屏、分屏都能自适应
- [ ] 形状圆角与容器同心（concentric）

### B6. 动效
- [ ] 每个动画都能回答「它在解释什么变化」
- [ ] 动效方向与手势一致，进入与退出路径对称
- [ ] 时长短（反馈类通常在零点几秒量级），不阻塞操作，可被打断
- [ ] 高频操作没有多余动画
- [ ] 开启「减弱动态效果」时有替代方案（淡入淡出代替位移、缩放、视差）
- [ ] 重要信息不只靠动画传达（有文字 / 触感反馈）

### B7. 无障碍
- [ ] 所有触控目标 ≥ 44×44pt
- [ ] 所有控件和图片有 VoiceOver 标签，朗读顺序合理
- [ ] 支持动态字体、增强对比度、降低透明度、减弱动态效果
- [ ] 不只靠颜色 / 声音 / 动画传递信息
- [ ] 手势操作有按钮替代
- [ ] 用 Accessibility Inspector 或同类工具审计过

### B8. 文案
- [ ] 标题足够短（英文 ≤ 8 词 / 中文 ≤ 12 字），一句只说一件事
- [ ] 先讲利益，再给参数佐证
- [ ] 主语是「你」，用动词驱动
- [ ] 没有空洞形容词（强大、极致、革命性、颠覆、赋能）
- [ ] 每个数字都有参照或换算，并注明条件
- [ ] 标题有记忆点，但不牺牲清楚
- [ ] 中文是重写而非直译，节奏顺口，中英文 / 数字加空格
- [ ] 按钮以动词开头；报错说清原因和下一步
- [ ] 术语全篇统一，没有无法证明的极限词

---

## C. 正反例改写（全部为原创虚构示例）

### C1. UI 改写

**UI-1 笔记 App「Leaf」首页**
- 改前：顶部导航栏放了搜索、筛选、排序、同步、分享、设置 6 个图标；每张笔记卡片有彩色边框和阴影；右下角浮动按钮配色是渐变彩虹色；标签用 5 种颜色。
- 改后：导航栏只留「搜索」和「新建」；排序、筛选收进「…」菜单；卡片去掉边框和阴影，用留白分组、标题 Semibold、摘要用 secondaryLabel；全局只有一个强调色，只用于「新建」和链接；标签改成同色的文字加小圆点。
- 改了什么：做减法（6→2 个入口，渐进披露）；层级靠字重和灰度而不是装饰；颜色回归语义，只表示可交互。

**UI-2 耳机配套 App「Hush」降噪设置页**
- 改前：一个 0–100 的滑杆加 3 个开关（风噪抑制、自适应、透传增强），每项下面都有一大段技术说明，字号 12pt Light 灰色。
- 改后：用一个三段式分段控件（降噪 / 自适应 / 通透），默认「自适应」；技术说明收进每项旁边的「i」；说明文字用系统 footnote 样式和 secondaryLabel 颜色，Regular 字重，支持动态字体；分段控件高度 ≥ 44pt。
- 改了什么：用有主张的默认值替代参数调节；细字重小字改成可读的系统样式；触控目标达标；复杂度藏在内部。

**UI-3 手表 App「Pulse」运动完成页**
- 改前：全屏烟花粒子动画持续 3 秒，期间无法点击；结果数据用红绿两色区分「达标 / 未达标」；完成按钮是右上角 28pt 的小「×」。
- 改后：一个短促的圆环闭合动画加一次触感反馈，可点击跳过；开启「减弱动态效果」时改为淡入；达标状态用「对勾图标 + 文字」再配颜色；底部放一个全宽的「完成」按钮。
- 改了什么：动效有目的、可打断、可减弱；不只靠颜色（照顾色盲）；按钮尺寸和位置符合无障碍与单手操作。

**UI-4（加分）设置页玻璃材质**
- 改前：列表每一行都用半透明毛玻璃，底部工具栏也是玻璃，弹出菜单又叠一层玻璃。
- 改后：列表回到实体背景（内容层）；只有工具栏和浮动控件用玻璃材质；菜单在玻璃上用填充和 vibrancy，不再叠玻璃。
- 改了什么：材质只用于功能层，避免玻璃叠玻璃，恢复清晰层级。

### C2. 文案改写（中英文）

**文案-1 耳机「Hush」主标题（中文）**
- 改前：Hush 采用新一代自研 H2 芯片和 6 麦克风阵列，降噪深度高达 48dB，带来极致静谧的革命性听觉体验。
- 改后：**世界很吵。你可以不听。**（副标：自适应降噪，地铁里也能听清每个字。）
- 改了什么：去掉参数和空洞形容词；短句加反转制造节奏；主语变成「你」；参数挪到下方作为佐证。

**文案-2 耳机「Hush」主标题（英文）**
- 改前：Hush features an industry-leading 6-mic array and advanced ANC technology for an unparalleled audio experience.
- 改后：**Hear less. Listen more.**（Sub: Adaptive noise cancellation that tunes itself to the room you're in.）
- 改了什么：动词驱动、对仗、4 个词；利益（专注地听）先于技术；「unparalleled」这类无法证明的词删掉。

**文案-3 笔记 App「Leaf」功能介绍（中文）**
- 改前：Leaf 支持 OCR 文字识别功能，能够对图片中的文字内容进行识别并转换为可编辑文本格式。
- 改后：**拍下白板，带走文字。** 照片里的字，直接可以搜、可以改。
- 改了什么：用具体场景（白板）代替术语（OCR）；动词「拍」「带走」「搜」「改」驱动；从 34 字压到 24 字。

**文案-4 笔记 App「Leaf」同步（英文）**
- 改前：Leaf utilizes a robust cloud-based synchronization infrastructure to ensure data consistency across multiple devices.
- 改后：**Start on your phone. Finish on your laptop.** Your notes are already there.
- 改了什么：把「同步」翻译成用户的一天；三段短句形成节奏；去掉 utilize、robust、infrastructure 这类空话。

**文案-5 手表「Pulse」续航（数字的用法，中文）**
- 改前：电池容量 410mAh，续航时间 36 小时，快充 30 分钟可充至 80%。
- 改后：**一天戴到底，睡觉也不摘。** 最长 36 小时续航¹；充电 30 分钟，够你用上一整天²。（¹² 脚注写明测试条件）
- 改了什么：只突出一个最有感知的数字；数字换算成生活场景；mAh 这类无感参数移到规格页；用脚注保证可信。

**文案-6 手表「Pulse」续航（英文本地化对照）**
- 改前（中文直译成英文）：Wear it the whole day, sleep without taking it off.
- 改后：**All day. All night. No charger in sight.**（Up to 36 hours of battery life.¹）
- 改了什么：不直译，重写成英文的三拍节奏加押韵；中文版用对仗，英文版用押韵，各自用母语的修辞。

**文案-7 界面报错（中英文）**
- 改前：错误代码 0x3F：同步失败，请检查。 / Error 0x3F: Sync failed.
- 改后：**还没同步上。** 连上网络后会自动继续，你的笔记已安全保存在本机。 / **Not synced yet.** Syncing resumes automatically once you're online. Your notes are saved on this device.
- 改了什么：去掉技术代码；先安抚（数据安全），再说下一步；语气平和、不怪用户。

**文案-8 标题双关（英文→中文的取舍）**
- 改前（英文原稿）：**Note-worthy.**（Note 与 noteworthy 双关）直译中文：「值得注意。」（双关丢失，味道没了）
- 改后中文：**记下的，都值得。**
- 改了什么：放弃无法移植的英文双关，用中文的短句和余韵重新表达「每条笔记都有价值」。

---

## D. 使用流程（审查一个页面 / 方案 / 文案）

1. **定目标（1 句话）**：写出这份材料要让谁、在什么场景、完成什么、感受到什么。写不出来，先停下来澄清。
2. **做减法**：列出所有元素 / 功能 / 卖点，逐个问「删掉会损失什么」，标出可删、可后置（渐进披露）、必须保留三类。
3. **查层级**：模糊测试或 3 秒测试，看第一眼落在哪里；确认只有一个主焦点、一个主操作、一个主口号。
4. **按检查表逐项过**：产品 → 视觉层级 → 字体 → 色彩 → 留白布局 → 动效 → 无障碍 → 文案（第 B 部分），记录不通过项。
5. **分级**：
   - P0 阻断：无障碍不达标（对比度、44pt、VoiceOver）、信息错误、核心任务走不通
   - P1 重要：层级混乱、功能过载、文案只堆参数、颜色语义冲突
   - P2 打磨：间距不统一、动效节奏、措辞润色
6. **给改写，不只给批评**：每个问题按「问题 → 依据的原则编号 → 具体改法 / 改后示例」输出；文案至少给 2 个备选（直白版、有巧思版），中英文分别本地化。
7. **复核整体**：改完后再看一遍整体，确认风格一致、没有因为局部改动打破全局；在深色模式、大字号、减弱动态效果下各看一遍。

**输出模板**
```
## 一句话结论
（整体评价 + 最关键的 1–3 个改动）

## 问题与建议
| 级别 | 位置 | 问题 | 原则 | 建议 / 改后示例 |
|---|---|---|---|---|

## 做减法清单
- 删除：…
- 后置：…

## 文案改写
- 改前 → 改后（直白版 / 巧思版）→ 改了什么
```

---

## E. 设计思想源头

> 本章只用自己的话转述观点。每条后面标了来源，引语最多一个短语。书籍部分只依据作者公开的书摘、访谈和公开书评，没有读到原书全文的地方不展开。

### E1. Dieter Rams 好设计十原则

格式：**原则**：用一句话转述。→ 落到产品 / UI 上是什么意思
来源：Vitsœ 官方页面 https://www.vitsoe.com/us/about/good-design

1. **创新（innovative）**：创新跟着技术一起往前走，但创新本身不是目的。→ 新技术要能换来新体验才值得用。「用了 AI」不算卖点，「少走了三步」才算。
2. **有用（useful）**：产品是拿来用的，凡是妨碍使用的东西都要去掉。→ 每个功能、每个元素都要说得出它帮用户完成了什么。
3. **美（aesthetic）**：天天用的东西会影响人的状态，美是有用的一部分，前提是做工到位。→ 视觉打磨不是锦上添花，粗糙的界面会让人觉得工具也不可靠。
4. **易懂（understandable）**：让产品的结构一看就明白，最好不用解释。→ 界面本身就是说明书，需要引导浮层来解释的地方，往往说明设计还没做完。
5. **克制（unobtrusive）**：工具应该中性、低调，把表达的空间留给用户。→ 对应原则 #11，界面退后，让用户的内容做主角。
6. **诚实（honest）**：不把产品夸得比实际更新、更强、更值钱，不许做不到的承诺。→ 文案里的承诺必须和真实能力、真实开放情况对得上（对应原则 #29）。
7. **耐久（long-lasting）**：不追潮流，所以不会过时。→ 少用流行一阵就过时的视觉手法（夸张渐变、拟物纹理），把功夫花在结构和排版上。
8. **细节到底（thorough down to the last detail）**：任何地方都不能随意、不能碰运气，细致本身就是对用户的尊重。→ 空状态、报错、加载、边界数据和主流程一样要设计（对应原则 #7）。
9. **环保（environmentally friendly）**：在整个生命周期里节省资源，减少物理和视觉上的污染。→ 数字产品也有「视觉污染」，比如弹窗、红点、无意义的通知。少打扰也是一种环保。
10. **尽可能少的设计（as little design as possible）**：Rams 的原话是一个短语 "Less, but better"，意思是只做要紧的部分，不让产品背上多余的负担。→ 每加一个元素都要问「删掉会损失什么」（对应原则 #8）。

**对我们做产品的启示**
- 十条里有四条直接说的是「少」和「真」：有用、克制、诚实、少设计。苹果式的减法就是从这里来的。
- 可以把十条当成评审时的提问清单：「这个功能有用吗？」「这句文案诚实吗？」「这个视觉效果三年后还好看吗？」
- 第 6 条（诚实）最容易被忽略，也最伤信任：落地页的承诺和产品实际体验一旦对不上，后面的设计再好也很难补回来。

### E2. Steve Jobs 与 Jony Ive：关于产品、简化和做减法

| 观点（转述） | 场合与来源 |
|---|---|
| 聚焦的意思是对其他上百个好主意说不，要非常谨慎地挑选。 | Jobs，1997 WWDC 闭幕演讲：https://www.youtube.com/watch?v=H8eP99neOVs |
| 要从用户体验出发，倒推到技术，而不是拿着技术去找卖点。 | Jobs，1997 WWDC 问答环节：https://www.youtube.com/watch?v=EZll3dJ2AjY |
| 简单比复杂更难：得先把思路理干净才能做简单，但做到了回报极大。他把这叫作自己的口头禅 "focus and simplicity"。 | Jobs，1998 年 BusinessWeek 采访 "There's Sanity Returning"，转引自 BBC：https://www.bbc.com/news/world-us-canada-15195448 |
| 靠焦点小组很难设计产品，很多时候用户要等你拿给他看，才知道自己想要什么。 | 同上采访，转引自 https://allaboutstevejobs.com/verbatim/quotes |
| 设计不只是外观和手感，设计是「它怎么工作」（"design is how it works"）。 | Jobs，《纽约时报杂志》2003 年 "The Guts of a New Machine"：https://www.nytimes.com/2003/11/30/magazine/the-guts-of-a-new-machine.html |
| 简单不是「没有杂乱」，没有杂乱只是简单带来的结果。简单是把一个东西的目的和位置说清楚。 | Ive，2012 年 The Telegraph 采访：https://www.telegraph.co.uk/technology/apple/9283706/Jonathan-Ive-interview-simplicity-isnt-simple.html |
| 好产品应该让人觉得理所当然，好像只能这样做；要把复杂问题的难度藏起来，让用户感觉不到。 | Ive，同上采访，另见 CNET 报道：https://www.cnet.com/tech/mobile/apples-jony-ive-knighted-discusses-quest-for-simplicity/ |
| 简单是提炼出一个东西的本质，让人一看就知道它是什么、能做什么；找到最简单的解法需要很大的力气。 | Ive，2013 年 Charlie Rose 访谈：https://www.macrumors.com/2013/11/22/jony-ive-and-designer-marc-newson-interviewed-on-charlie-rose-show/ |
| 看不见的地方也要用心，比如抽屉背面；产品本身就在传达做它的人在乎什么。 | Ive，同一场访谈，见 https://www.idownloadblog.com/2013/11/22/jony-ive-on-charlier-rose-on-the-value-of-simplicity/ |

**对我们做产品的启示**
- 简单是**想清楚**的结果，不是**删干净**的结果。先回答「这个产品到底是干什么的」，再谈删哪些元素。只删不想，得到的是「空」，不是「简单」。
- 评审方案时，先问它从哪种体验倒推出来，而不是用了什么技术。
- 不要指望用户调研替你做决定。调研能告诉你问题在哪，答案要靠团队拿出能看能摸的东西（见 E4 的 demo 文化）。
- 「看不见的地方」包括报错、空状态、权限说明、导出文件的命名，这些细节在替产品表态。

### E3. Ken Segall《Insanely Simple》（《疯狂的简洁》）

> 作者曾任苹果广告代理商 Chiat\Day 的创意总监，iMac 这个名字是他提的。下面的内容来自作者官网公开的序章 PDF、作者本人的访谈和公开书评，没有读过的章节细节不展开。

**简单之杖（Simple Stick）**：这是苹果内部的说法。一份方案被乔布斯「敲了简单之杖」，不是因为做得不好，而是因为它没把想法提炼到本质，该走直线的地方拐了弯。序章里的例子是：团队给同一个产品的两个版本各设计了一套包装，乔布斯直接说合成一个，一个产品，一个盒子。作者也强调，更简单的路往往不是更省事的路，可能要花更多时间、钱和力气。来源：https://kensegall.com/wp-content/uploads/2017/09/Insanely-Simple_intro.pdf

**十个 Think（各章标题，用自己的话转述）**，主要来源：Marketing Week 对作者的访谈 https://www.marketingweek.com/qa-ken-segall/ 、Financial Post 书评 https://financialpost.com/entrepreneur/take-steve-jobss-lead-and-think-simple

| 章节 | 核心意思 | 落到我们的工作里 |
|---|---|---|
| Think Brutal | 直说。含糊和留余地只会制造复杂。 | 评审意见直接指向问题，不绕弯；对事不对人。 |
| Think Small | 小团队、少开会，人越多复杂度越高。 | 关键决策会只叫真正要拍板和干活的人。 |
| Think Minimal | 选项越多越复杂，一条广告只讲一件事。作者讲过一个故事：扔一个纸团，对方能接住；一次扔五个，一个也接不住。 | 一个页面一个主信息，一个版本一个主故事（对应原则 #1、#22）。 |
| Think Motion | 别被大公司的慢流程拖住，项目要一直动起来。 | 少走审批，多做能演示的版本。 |
| Think Iconic | 一张有标志性的图，可能比一堆信息更有力量。 | 每个功能找一个「一眼就懂」的画面或图标，而不是一张功能表。 |
| Think Phrasal | 命名和措辞要短、要好记，少起编号式的名字。 | 产品名和功能名用人能念出口的词，避免一串型号。 |
| Think Casual | 非正式的氛围让人敢说真话，决策也更快。 | 内部评审少走形式，多看实物。 |
| Think Human | 用人的方式说话，打动情感，而不是堆技术。 | 文案以「你」为主语、讲场景（对应原则 #24、#25）。 |
| Think Skeptic | 对唱衰的声音保持怀疑，不让反对意见稀释好想法。 | 有数据或 demo 支撑的方向，不因为一两个反对意见就改得面目全非。 |
| Think War | 真正关键的事要全力去打，必要时制造一个清晰的对手。 | 定位时明确「我们不是什么」，对照对象要清楚。 |

**对我们做产品的启示**
- 「简单」首先是**组织问题**：人少、话直、决策快，才做得出简单的东西。流程复杂的团队很难做出简单的产品。
- 评审时可以直接问一句「这里能不能敲一下简单之杖？」，也就是能不能合并、能不能只留一个。
- 对外沟通坚持「一个纸团」：首屏只讲一件事，其他的往后放。

### E4. Ken Kocienda《Creative Selection》（《创意选择》）

> 作者是前苹果软件工程师，参与过 Safari 和初代 iPhone，负责 iPhone 键盘与自动纠错。下面的内容来自公开书摘、书评和作者访谈。作者本人也提醒过，这本书不是一份「照着做就能变成苹果」的清单，他写的是工作中自然形成的做法。来源：Commoncog 书摘 https://commoncog.com/creative-selection/

**核心观点**
1. **demo 驱动，不是规格书驱动**：讨论的最小单位是一个能实际操作的 demo，而不是文档或口头描述。作者打过一个比方：两个人各自想象一只可爱的小狗，谁也说服不了谁；摆出两张照片，讨论马上就能进行。具体的样例让讨论变得可能。（Commoncog）
2. **迭代挑选（creative selection）**：做 demo → 拿到反馈 → 改进 → 再做 demo，每一轮留下最好的部分，逐步收敛到更好的版本，像自然选择一样。（brettworks 读书笔记 https://brettworks.com/2019/01/25/notes-on-ken-kociendas-creative-selection-2018/ 、MacRumors https://www.macrumors.com/2018/09/04/creative-selection-kocienda-book/）
3. **每次评审都有一个拍板人**：拍板的人有唯一的批准权，并决定下一步做什么；层层 demo 评审一直往上，到乔布斯那里做最终判断。（Commoncog）
4. **少给不必要的选择**：作者给乔布斯演示 iPad 键盘时准备了两种布局，乔布斯看了一两分钟就问：我们只需要其中一个，对吧？作者事后把这件事总结为果断、品味和同理心的结合：替用户选好最好的默认值。（iMore 作者访谈 https://www.imore.com/creative-selection-best-book-ever-written-about-apple）
5. **启发式（heuristics）和算法同样重要**：动画多长、滑动多远才算手势、双指最多放大几倍，这些数字没有工程上的「最优解」，只能靠反复试用和判断去找合适的默认值。（Commoncog）
6. **小团队**：作者认为这种文化只在小团队里成立，领导要能直接接触做事的人和 demo。（Commoncog）

**七个要素**（来源：Matt Tillotson 书评 https://matttillotson.com/books/creative-selection-ken-kocienda 、Commoncog）

| 要素 | 意思（转述） | 落到我们的工作里 |
|---|---|---|
| 灵感 Inspiration | 敢想大的，想象可能性 | 每个版本先写「理想的那个时刻」，再谈范围 |
| 协作 Collaboration | 和人合作，把各自长处拼在一起 | 设计、工程、文案一起看同一个 demo |
| 手艺 Craft | 用技能做出高质量，并且一直想做得更好 | 设定可测的质量门槛（性能、对比度、错误率） |
| 勤勉 Diligence | 把脏活累活做完，不走捷径 | 边界状态、多语言、大字号逐个检查 |
| 果断 Decisiveness | 敢做难的决定，不拖延 | 每次评审指定拍板人，当场定，记录理由 |
| 品味 Taste | 培养精细的判断力，让整体达到协调 | 用对比样例训练判断：同一个页面做两版放在一起看 |
| 同理心 Empathy | 从别人的视角看世界，让作品适应他们的生活 | 拿真实用户场景测（单手、弱网、大字号、读屏） |

**对我们做产品的启示**
- 争论设计时，先停下来做两个能点的版本，再讨论。别在文档里吵。
- 评审会要有拍板人，讨论结束时要有结论。没有结论的评审只会制造复杂度。
- 动画时长、默认值、阈值这类「手感参数」要专门留时间反复试用，不能拍脑袋定完就算了。
- 遇到「要不要给用户一个选项」时，默认先回答「我们能不能替他选好」。

---

## F. 设计规范层

### F1. WWDC 设计类演讲要点

**写 UI 文案**

1. **Writing for interfaces（WWDC22）**：https://developer.apple.com/videos/play/wwdc2022/10037/
   - 框架是 **PACE**：Purpose（这一屏的目的）、Anticipation（预判下一步）、Context（使用情境）、Empathy（同理心）。
   - 每屏只有一个目的：按信息层级排序，标题和按钮要能单独看懂，因为人不会按顺序读；想清楚哪些话可以删掉或挪走。
   - 声音（voice）保持一致，语气（tone）随情境调整：报警时冷静清楚，庆祝时可以热情，但感叹号要少用。
   - 弹窗：标题直接提出问题，按钮写具体动作（不用「是 / 否」）；「取消」容易产生歧义，要慎用；有破坏性的操作要标出来。
   - 报错和空状态：不用 oops 这类感叹词，也不用敷衍的道歉；告诉用户怎么修，空状态要说明内容会怎样出现在这里。最后一条建议：把文字读出声。
2. **Add personality to your app through UX writing（WWDC24）**：https://developer.apple.com/videos/play/wwdc2024/10140/
   - 声音是品牌价值在文字上的表达，基本不变；语气是声音在不同情境下的调节。
   - 苹果写作者用四个词校准自己的声音：清楚、简单、友好、有帮助。不同场景把其中某几项「调大」或「调小」，但不会关掉任何一项。
   - 找到自己产品声音的练习：把 App 想成一个人，用便利贴写出形容词，再归类，最后选出 2–3 个关键属性。
   - 同一句「帮你存钱」，在面向年轻投资者的 App 里和面向孩子的 App 里会写成完全不同的话，区别就在声音。
   - 不为了显得有个性而牺牲有用；避免行话；写作要包容。
3. **Make a big impact with small writing changes（WWDC25）**：https://developer.apple.com/videos/play/wwdc2025/404/
   - **删填充词**：simply、quickly 这类副词和形容词常常是在替用户的处境做假设；感叹词、客套话（sorry、please）也大多可以删掉。只保留能补充信息的修饰（比如「自动」）。
   - **去重复**：标题和正文不要换个说法重复同一件事，合并成一句。
   - **先说为什么（lead with the why）**：把好处放到句首，比如先说「想收到预约提醒」，再说「输入手机号」。
   - **建词表**：三列，分别写要用的词、不用的同义词、定义。同一个概念全程用一个词，按钮名也写进词表。
4. **HIG：Writing**（规范页）：https://developer.apple.com/design/human-interface-guidelines/writing
   - 按钮和链接几乎都用动词，不要为了俏皮牺牲清楚；链接不写「点击这里」。
   - 设置项标签要实用，说明只写「打开后会怎样」，用户能推出关闭时的情况；需要跳到系统设置时，直接给按钮或链接。
   - 报错放在离问题最近的地方，不怪用户，说清楚怎么修；比起「密码太短」，直接告诉用户密码至少要几个字符更有用。
   - 少用「我的 / 你的」这类物主代词；**避免用「我们」**，因为用户不清楚「我们」是谁，报错里尤其如此。
   - 多步流程用一致的按钮措辞（开始、继续 / 下一步、完成）。


**排版**

5. **The details of UI typography（WWDC20）**：https://developer.apple.com/videos/play/wwdc2020/10175/
   - **光学尺寸**：同一套字形在小字号时要更宽松、笔画更稳，大字号时更紧凑。SF 以前分 Text 和 Display 两套，现在用可变字体，在大约 17–28pt 之间连续过渡。
   - **字距（tracking）和字偶距（kerning）不是一回事**：kerning 由字体设计师针对字母对做好，一般不要动；tracking 必须随字号变化，自定义字距也要分字号设置。文字放不下时，优先让系统自动收紧，太紧就宁可截断。
   - **行高**：长段落用宽松行距（loose leading），高度受限的列表可以收紧，但 HIG 建议三行以上的文字不要用紧行距。
   - **text styles 本身就是层级系统**：字号、字重、行高的组合是预设好的，需要强调时用 emphasized 变体（同字号加粗）。
   - 网页可以用 `system-ui`、`ui-rounded`、`ui-serif`、`ui-monospace` 调用苹果平台上的系统字体。尽量用系统能力，系统每年改进，产品会跟着一起变好。

**动效**

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

**无障碍**

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

### F2. Apple Style Guide：对写作最有用的规则

来源：Apple Style Guide（2026 年 6 月版）https://support.apple.com/guide/applestyleguide/welcome/web ，PDF 版 https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf 。下表是英文规则的转述，「中文对应」一栏是我们自己的建议，不是苹果的规定。

| 类别 | 规则（转述） | 中文对应建议 |
|---|---|---|
| 语气 | 苹果用非正式的口吻，英文鼓励用 aren't、can't 这类缩约形式，但要考虑本地化。 | 用口语化的短句，不用公文腔（「进行」「予以」「相关」）。 |
| 人称 | 不用 we、us、I，改写成以读者或产品为主语（HIG 也建议避免「我们」）。 | 少说「我们将为您…」，改成「你可以…」或直接写结果。 |
| 客套 | 说明性文字里避免 please。 | 少用「请」开头堆砌，直接用动词开头：「输入密码」。 |
| 感叹号 | 宣传文案偶尔可以用，文档里避免。 | 界面文案基本不用感叹号，庆祝场景例外。 |
| 大小写 | 分句首大写（sentence-style）和每词首字母大写（title-style）两种；写到界面元素名时，照屏幕上的大小写原样写。 | 中文界面里引用按钮或菜单名，和屏幕上的字一字不差，用引号或加粗标出。 |
| 数字 | 一到九一般拼写成单词，但表示数值、计量单位和百分比时一律用阿拉伯数字；句子不要以数字开头。 | 中文界面统一用阿拉伯数字，数字和单位、数字和汉字之间按 F3 处理间距。 |
| 操作动词 | tap 后面不加 on，不说 click on，不说 click and drag；菜单命令用 choose，对象用 select；输入内容用 enter（type 专指敲键）。 | 触屏用「轻点」，桌面用「点按」或「点击」，全产品统一；「拖到」就不必再说「点击并拖动」。 |
| 开关 | 想说「打开」时不要用 enable；面向用户的文字不用 toggle；开关（switch）通常不必提，直接描述动作。 | 用「打开 / 关闭」，不用「启用 / 禁用」「切换开关」。 |
| 弹窗 | 用 dialog，不用 dialog box；面向用户的文字避免 "error message"，用 alert。 | 中文写「提示」「警告」，避免对用户说「错误信息」「异常」。 |
| 缩写和符号 | 不用 e.g.，改用 for example；via 尽量少用；and/or 要改写。 | 不用「等等…」「如：」堆砌，不用「/」表示「或」。 |
| 国际化 | 句式简单，不用习语和俚语，能写全称就不用缩写和符号，方便人工和机器翻译。 | 正文避免网络梗和谐音梗；梗只留在标题里，而且要有直白的备选版本（对应原则 #27）。 |
| 包容 | 写作要包容，谈到残障时关注个人本身。 | 示例和插图避免默认性别；用「用户」「大家」，不用「小哥哥 / 小姐姐」。 |

### F3. SF 字体家族与中文排版

**SF 字体家族**（来源：HIG Typography https://developer.apple.com/design/human-interface-guidelines/typography 、WWDC20 10175）
- **SF Pro**：iOS、iPadOS、macOS、tvOS、visionOS 的系统字体，无衬线。
- **SF Compact**：watchOS 的系统字体，字形更窄，适合小屏；表盘复杂功能用 SF Compact Rounded。
- **SF Mono**：等宽字体，用于代码和需要对齐的数字。
- **Rounded 圆体**：SF Pro 和 SF Compact 等都有圆体版本，适合圆润的界面元素或想换一种语气的场景。
- **New York（NY）**：衬线字体，可以单独用，也能和 SF 搭配，适合阅读类和编辑感的标题。
- 还有 SF Arabic、SF Hebrew 等多语言变体。系统字体都是可变字体，支持动态光学尺寸，字重从 Ultralight 到 Black，SF 还有 Condensed、Expanded 等宽度。SF Symbols 的字重和文字一一对应。
- **默认 / 最小字号**（HIG）：iOS、iPadOS 17 / 11pt；macOS 13 / 10pt；tvOS 29 / 23pt；visionOS 17 / 12pt；watchOS 16 / 12pt。
- **字距**：应用里的系统字体会按字号自动调整字距；做设计稿时，按 Apple Design Resources 提供的字距表手动设置。规律是字号越大字距越紧。
- **苹方（PingFang SC / TC / HK）**：2015 年随 iOS 9 和 OS X El Capitan 推出的中文系统字体，属于黑体类，替代了之前基于黑体（Heiti）的中文系统字体。来源：https://zh.wikipedia.org/zh-cn/苹方 、https://gist.github.com/bitinn/42c95ed95aa3dcf155e2

**中文排版要点**（来源：W3C《中文排版需求》clreq https://www.w3.org/TR/clreq/ ）
- **中西混排间距**：汉字和西文、阿拉伯数字之间留出不超过 1/4 个汉字宽的空隙；如果西文在行首或行尾，就不用加。（clreq 西文使用比例字体时的混排处理）网页上通常用一个半角空格或排版引擎来实现。
- **标点**：中文用全角标点，简体中文引号用 “ ” 和 ‘ ’。不要用全角的英文字母和数字，clreq 明确建议交给排版引擎去处理比例字体。
- **行首行尾禁则**：句号、逗号、顿号等点号和右括号、右引号不能出现在行首；左括号、左引号不能出现在行尾。（clreq 6.1.1）
- **行高**：clreq 指出行距（行与行之间的空白）通常是字号的 50%–100%，也就是 line-height 大约 1.5–2.0，超过字号并不会更好读。界面正文取 1.5–1.7 比较稳妥（和 B3 一致）。
- **行长**：clreq 把「每行多少字」列为版心设计的基本要素，但没有给出统一数值。所以本手册不硬定一个数字，按设备和字号实测，避免一行长到读完找不到下一行。
- **字体搭配**：黑体（苹方属于这一类）适合标题、界面和对话人名；正文里要强调时，用更粗的字重（clreq 3.1.1.3）。
- **字重**：中文笔画多，小字号要避免 Light 及以下的细字重（和 HIG 的建议一致）。

**F 部分补充检查项（并入 B 表使用）**
- [ ] 文案用 PACE 过一遍：这一屏的目的、下一步、使用情境、写给谁
- [ ] 删掉了填充词（轻松、快速、只需、哎呀、抱歉、请）
- [ ] 好处放在句首（先说为什么）
- [ ] 有词表：同一个概念、同一个按钮全程用同一个词
- [ ] 界面文案里没有「我们」；按钮不用「是 / 否」，写具体动作
- [ ] 动效用弹簧、可打断、尊重手势动量，默认不回弹
- [ ] 大字号下布局能从横排变成竖排，不截断
- [ ] 中西文之间有间距，标点遵守行首行尾禁则，行高 1.5–1.7

---

## G. 文案拆解：苹果式句式

> 观察日期：2026-10-09，对象是 apple.com 和 apple.com.cn 的当前产品页，以及历史发布会的公开报道。这里只归纳句式结构，不整句引用；需要提到原文时，只点出关键字或修辞手法。

### G1. 10 个样本

格式：**页面 / 场合** → 句式公式 → 为什么有效

1. **iPhone 18 Pro 产品页，可变光圈板块**（https://www.apple.com/iphone-18-pro/ ，中文 https://www.apple.com.cn/iphone-18-pro/ ）
   → 公式：**功能名 + 圈内梗双关**。英文把产品名里的 Pro 当成动词，和一句常见的「懂的都懂」式口头禅拼在一起；中文改成「圈」字同字复现，光圈的「圈」和行内人的「圈」是一个字。
   → 为什么有效：功能名负责说清楚，双关负责让人记住，还顺便点出目标用户是「懂行的人」。中英文各用自己的语言找双关，没有硬译。
2. **AirPods Pro 3 产品页，降噪板块**（https://www.apple.com/airpods-pro/ ）
   → 公式：**反转悖论**，拿「最好的东西」和「你听不到」放在一起。卖的是安静，却说成「最好的声音是没听到的那个」。中文版改用文言味的否定句式（「非…不…」），把一句英文俏皮话换成中文的韵律。
   → 为什么有效：降噪本来是看不见、听不到的功能，悖论把这种「没有」变成了一个可以感知的好处。
3. **MacBook Pro 产品页，芯片板块**（https://www.apple.com/macbook-pro/ ）
   → 公式：**数字 + 名词。比较短语。** 两个短句：先报数量，再给定性。中文版合成一句，下半句借用含数字的成语，「三」和「一」前后呼应。
   → 为什么有效：先给一个具体事实，再给一个态度，短句之间的停顿形成节奏。中文用成语做数字游戏，比直译「无人能及」更顺口。
4. **MacBook Air / Pro 产品页，AI 板块**（https://www.apple.com/macbook-air/ ）
   → 公式：**主题词。改写熟语。** 先给板块主题，再改动一个大家熟悉的短语（歌名、谚语、经文里的句式）中的一个词，让它刚好指向产品。中文版不翻熟语，换成「大显神威」这类本土口语。
   → 为什么有效：熟语自带节奏和记忆点，改一个词会制造「咦」的一下。本地化时这种梗几乎没法翻译，所以中文直接重写（对应原则 #30）。
5. **隐私页主标题**（https://www.apple.com/privacy/ ，中文 https://www.apple.com.cn/privacy/ ）
   → 公式：**价值词。+ 品牌断言。** 一个价值词，后面跟一句「这就是 [品牌]」。中文版把品牌名当形容词用（「这很 Apple」）。
   → 为什么有效：把一个抽象价值直接绑到品牌身上，等于宣称这是品牌的性格。只有当品牌真的长期这样做时，这句话才立得住（诚实，见 E1-6）。
6. **iPad Air 产品页首屏**（https://www.apple.com/ipad-air/ ，中文 https://www.apple.com.cn/ipad-air/ ）
   → 公式：**一个拟声词就是标题。** 英文用一个模拟「嗖」一声的词，暗示轻和快。中文没有翻拟声词，换成一个网络口语形容词（「超拉风」）。
   → 为什么有效：一个词，零解释，靠声音和画面配合。中文选的是同样感觉的本土词，而不是去找一个对应的拟声字。
7. **Apple Watch Series 12 健康板块**（https://www.apple.com/apple-watch-series-12/ ）
   → 公式：**三拍口令改最后一拍。** 借「预备、开始」这种三拍口令，只把最后一拍换成和健康数据有关的词。中文版写成对仗句（「该…该…，都…」），讲的是休息和冲刺都有数据可依。
   → 为什么有效：三拍天生好记，最后一拍的意外就是笑点和卖点。中文改用对仗，保留了「两种状态都照顾到」的意思。
8. **iPod 发布（2001）**（Apple 新闻稿 https://www.apple.com/newsroom/2001/10/23Apple-Presents-iPod/ ）
   → 公式：**数字 + 能装下它的地方**，也就是把存储容量换算成「多少首歌放进口袋」。
   → 为什么有效：5 GB 是参数，「一口袋的歌」是画面。数字有了参照物（对应原则 #26）。
9. **iPhone 发布会（2007）**（文字稿与修辞分析 https://www.european-rhetoric.com/analyses/ikeynote-analysis-iphone/transcript-2007/ ）
   → 公式：**三件套 + 反转揭晓。** 先说今天要发布三样东西，重复几遍让观众记住，再揭晓这不是三台设备，而是一台。
   → 为什么有效：三的节奏让人记得住，反转制造惊喜，并把一个复杂产品压缩成一个概念。
10. **MacBook Air 发布（2008）**（Apple 新闻稿 https://www.apple.com/newsroom/2008/01/15Apple-Introduces-MacBook-Air-The-Worlds-Thinnest-Notebook/ ，现场报道 https://www.infoworld.com/article/2317220/jobs-unveils-skinny-notebook-itunes-movie-rentals.html ）
    → 公式：**一个最高级的主张 + 一个道具当场证明。** 宣称「最薄」，然后从一个普通的办公文件袋里把电脑拿出来。
    → 为什么有效：演示本身就是文案，观众自己得出结论，比任何形容词都可信。另外，发布会上常见的「还有一件事」（One more thing）是**假结尾 + 再揭晓**，同样是在制造节奏上的惊喜（https://en.wikipedia.org/wiki/Stevenote ）。

### G2. 产品页的整体骨架（从多个页面归纳）

```
首屏      产品名（小字）+ 一句巧思标题 + 一句直白副标 + 主视觉 + 1 个主按钮
先看重点  5–8 张卡片，每张写 1 个卖点：短标题 + 1 句话 / 1 个数字
细看      分章节（设计 / 性能 / 拍摄 / 健康 …）
          每章：小标签（eyebrow，说明这一章讲什么）
                → 巧思标题（被记住）
                → 直白正文（被理解）
                → 1 个大数字或 1 张大图（证据）
                → 脚注（测试条件）
对比 / 为什么在这里买 / 全部规格（最后才出现参数表）
```
英文页的「先看重点」「细看」这类导航文字，在中文页上也是重写过的，用的是更口语、更贴近中文互联网习惯的说法。

### G3. 标题公式清单（示例都是原创虚构产品）

| # | 公式 | 原创示例 |
|---|---|---|
| T1 | **现状。反转。**（A 很麻烦。你可以不。） | 会议纪要 App：「会开完了。纪要也写完了。」 |
| T2 | **改写熟语（只换一个词）** | 图表工具：「一图省千言。」 |
| T3 | **数字 + 装得下它的地方** | 移动硬盘：「一整季的剧，装进外套口袋。」 |
| T4 | **三拍动词** | 植物识别 App：「拍一下。认出来。记得住。」 |
| T5 | **功能名 + 圈内梗 / 同字双关** | 降噪耳机的通透模式：「通透模式，人情世故也听得透。」 |
| T6 | **价值词 + 品牌断言** | 笔记 App「Leaf」：「不催你，这很 Leaf。」 |
| T7 | **一个拟声词 / 一个字就是标题** | 相机 App 快门板块：「咔嚓。」 |
| T8 | **悖论：卖「没有」** | 静音键盘：「最好听的键盘声，是没有声音。」 |
| T9 | **名词。定性短语。**（事实 + 态度） | 双摄行车记录仪：「两颗镜头。一个不落。」 |
| T10 | **对仗（中文专用）** | 跑步手表：「该慢就慢，该冲就冲。」 |

使用规则：标题选一个公式就够，不要叠加；每个巧思标题都要配一句直白副标（原则 #27）；报错、设置、权限等界面文案不用这些公式。

### G4. 卖点结构模板

**单个卖点（一屏或一张卡片）**
```
小标签：功能类别（2–4 字）
标题：  好处或画面（套用 G3 中的一个公式，≤ 12 字）
正文：  1–2 句，先说为什么，再说怎么做到（场景 → 能力）
证据：  1 个数字 + 参照物，或 1 个演示画面
脚注：  测试条件
```
**整页**：一个主张（首屏）→ 3–5 个支撑卖点（按用户在意的顺序，不按技术架构排）→ 证据（数字、对比、口碑）→ 行动（一个主按钮）→ 参数（放到最后）。
**发布会**：一句话立起冲突 → 三件套 → 反转揭晓 → 每个卖点配「一张图 + 一句话 + 一次演示」→ 一个大数字 → 回到开头那句话 → 还有一件事 → 价格和上市时间。

### G5. 中英本地化差异规律

1. **修辞各找各的**：英文常用双关、改写熟语、头韵；中文换成成语、四字格、对仗、同字复现、叠字（像「冲冲冲」）和网络口语。很少逐字翻译。
2. **断句不同**：英文喜欢用句号切成两三个极短句；中文更常用逗号连成上下两句，再用句号收尾，靠对仗制造节奏。
3. **中文更口语、更接地气**：同一个板块，中文版常常比英文版更活泼，比如用「美翻天」（MacBook Air 中文页）、「溜到飞起」（iPad Air 中文页）这类口语；英文版则偏冷幽默。
4. **最高级的处理**：英文页可以直接说「世界最好」；中文页同一位置更倾向于用可以量化的相对提升（比如「提升到 X 倍」）。这也和《广告法》第九条禁止「国家级、最高级、最佳」等用语一致（https://www.samr.gov.cn/zt/ndzt/2019n/bjspjsqjxcjwljxyjsckpxc/zcfg/art/2023/art_f383fbf8c106420b8951ba8d9508d32d.html ）。
5. **专有名词保留英文**：芯片、功能、材质的名称（如 M5、Liquid Glass、Center Stage）在中文页保留英文，并且中英文之间留空格（见 F3）。
6. **导航和界面文字也要重写**：「Get the highlights」这类导航文字在中文里会换成符合本地习惯的动词（如「刷」）。本地化覆盖到每一个按钮。
7. **品牌名可以变成形容词**：中文用「这很 X」把品牌当形容词用，英文则用「这就是 X」的断言句。

---

## H. 实战练习：普通文案 / 页面 → 苹果式改写

> 5 组都是原创虚构的案例。原则编号对应 A 部分（#1–#31），E、F、G 指本手册的相应章节。

### H1. SaaS 工具首页：团队任务看板「Tally」

**改前（页面结构）**
- 顶部导航：9 个链接，外加「免费试用」「预约演示」两个同样醒目的按钮。
- 首屏标题：「新一代 AI 驱动的智能协同项目管理平台，全面赋能企业数字化转型」。
- 首屏下方：12 个功能图标组成的宫格，每个配 4 个字（智能排期、多维视图、权限管控……）。
- 再往下：客户 logo 墙、三档价格表，页面底部又把功能列了一遍。

**改后**
- 导航：只留「产品、价格、客户、登录」四项，加一个主按钮「免费试用」。
- 首屏：
  - 标题：**谁在做什么，一眼就清楚。**
  - 副标：Tally 把任务、负责人和截止日放在同一块看板上。现有的表格，5 分钟导进来。
  - 主按钮「免费试用 14 天」；次要链接「看 2 分钟演示 ›」。
  - 主视觉：一张真实的看板截图，不用抽象插画。
- 三段式场景，每段只有一个标题、一句话和一张截图：
  - **分配**：「拖一下，就交出去了。」
  - **跟进**：「快到期的，自己会冒出来。」
  - **复盘**：「这周做了什么，周五自动写好。」
- 证据：一句话加一个数字，比如「1,200 个团队每周用它开站会¹」，脚注写明统计口径。
- 价格放到独立页面，首页只留一个入口。

**改在哪 / 为什么**
- 去掉「新一代、AI 驱动、赋能、数字化转型」这类空话，换成用户能看见的结果：原则 #25、#29，以及 F1 的「删填充词」。
- 12 个功能收成 3 个场景，按用户的一周来排，而不是按功能模块排：原则 #1、#2、#21，以及 E3 的 Think Minimal（一个纸团）。
- 两个同样醒目的按钮改成一主一次：原则 #12。
- 副标先说好处，再说怎么做到：F1 的 lead with the why，以及原则 #23。
- 标题用的是 G3-T1（结果画面式），场景标题用短句形成节奏：原则 #28。

### H2. 硬件产品页：便携投影仪「Beam」

**改前**
- 首屏标题：「Beam 投影仪：1080P 原生分辨率，500 ANSI 流明，支持 4K 解码，内置智能系统，双 5W 扬声器，自动对焦，梯形校正」。
- 配图：白底产品图，四周贴满参数角标。
- 下面直接是规格表。
- 英文版是直译：「Beam Projector: 1080P native resolution, 500 ANSI lumens…」

**改后**
- 首屏：小字「Beam」；标题 **「白墙，就是银幕。」**；副标「开机自动对焦，摆歪了也会自己校正。」；主视觉是卧室墙上正在放电影的画面。
- 英文首屏不翻译，重写：**"Any wall. Movie night."**（副标：Auto-focus and auto-keystone. Set it down and press play.）
- 先看重点：6 张卡片（画面、声音、便携、自动对焦、续航、系统），每张一个数字加一句换算，比如「一部 2 小时的电影，一次充电看完¹」。
- 细看：设计、画面、声音、续航分章节，每章都按「小标签 → 巧思标题 → 直白正文 → 1 个大数字 → 脚注」排。
- 页尾放「全部规格」，ANSI 流明、解码格式这类参数都在这里。

**改在哪 / 为什么**
- 参数从标题里拿走，挪到证据层和规格页：原则 #23、#26。
- 用画面代替参数堆叠（「白墙就是银幕」）：原则 #25，标题公式 G3-T3 的变体。
- 页面骨架套用 G2，卖点结构套用 G4。
- 英文版重写成三拍短句，不直译：原则 #30，以及 G5-1、G5-2。
- 续航写成「看完一部电影」并加脚注：原则 #26、#29，以及 E1-6 的诚实。

### H3. App 设置页：相机 App「Lumo」

**改前**
- 一屏平铺 24 个开关，没有分组。
- 标签中英混杂，比如「启用 HDR 增强算法（实验性）」「Enable AI Scene Recognition」。
- 每个开关下面都有 11pt Light 的灰色说明，很多写的是「关闭后将不会…」。
- 底部有一个「保存设置」按钮，不点保存就离开，改动会丢失。
- 要用定位时，写着「请前往 系统设置 > 隐私 > 定位服务 开启权限」。

**改后**
- 分成四组：拍摄、画质、存储、隐私。常用的 6 项放在最前面，其余收进「高级」二级页。
- 标签改成简短的名词：「HDR」「场景识别」「网格线」。说明只写打开后会怎样，比如「拍摄高反差场景时，自动合成多张照片」。
- 用「打开 / 关闭」，不用「启用 / 禁用」，中英文不混用。
- 改动立即生效，去掉保存按钮。
- 定位权限改成一行说明加一个「前往设置」按钮，直接跳过去。
- 说明文字用 footnote 样式、secondaryLabel 颜色、Regular 字重，支持动态字体；字号变大时，开关移到文字下面。

**改在哪 / 为什么**
- 分组加二级页：原则 #21、#12、#18。
- 即时生效、替用户省掉一步：原则 #9、#3。
- 设置标签和说明的写法：F1 的 HIG Writing（说明只写打开后的效果，直接给跳转按钮）、F2 的「enable → 打开」。
- 去掉细字重小字：原则 #10、#16，以及 F3 的最小字号。
- 大字号下改变布局：F1 第 9 场（Dynamic Type），原则 #20。

### H4. 空状态与报错：云盘「Drift」

**改前**
- 空状态：一张大插画，配文「哎呀，这里空空如也~」，没有任何按钮。
- 上传失败弹窗：标题「Oops! 出错了」，正文「错误码 E1032：上传失败，请稍后重试。」，按钮「确定」「取消」。

**改后**
- 空状态：
  - 标题：**还没有文件**
  - 正文：把文件拖到这里，或者从手机上传。传好的文件会出现在这里。
  - 按钮：「上传文件」
- 报错：
  - 标题：**“合同.pdf”没有上传**
  - 正文：文件超过 2 GB 的上限。压缩后再试，或者改用桌面版上传。
  - 按钮：「压缩并重试」（主）、「以后再说」
  - 错误码收进「详细信息」，方便客服排查。
- 英文对照：
  - 空状态：**No Files Yet** / Drag files here or upload from your phone. They'll appear here.（按钮：Upload Files）
  - 报错：**"Contract.pdf" Wasn't Uploaded** / The file is larger than 2 GB. Compress it and try again, or use the desktop app.（按钮：Compress and Retry / Not Now）

**改在哪 / 为什么**
- 去掉「哎呀」「Oops」，正文也不再堆「请稍后」这种客套：F1 的 WWDC22 和 WWDC25 两场（删感叹词和客套），F2 的 please 规则。
- 标题点名是哪个文件出了什么事，正文说原因加下一步：原则 #31，以及 HIG Writing 的报错写法。
- 「确定 / 取消」改成写清动作的按钮：F1 的 WWDC22（按钮写具体动作）。
- 空状态告诉用户内容会怎样出现，并给一个入口：HIG Writing 关于空白页的建议，原则 #7。
- 全程没有出现「我们」：F2 人称规则，HIG Writing。
- 英文版用标题式大小写写弹窗标题，并且全产品统一：F2 大小写规则。

### H5. 发布会开场：电子书阅读器「Folio」

**改前（开场 15 分钟的流程）**
1. 公司历程、融资情况、团队介绍
2. 市场规模数据，每页 PPT 8 条要点
3. 一口气列出 20 项新功能
4. 最后公布价格

**改后（开场骨架，正文 5 分钟以内）**
1. **一句话立起冲突**（约 30 秒）：「我们每天读得越来越多，读完的却越来越少。」
2. **三件套**：今天发布三样东西，一块看久了眼睛也不累的屏，一个记得你读到哪一页的书架，一支能把划线变成笔记的笔。三样东西各重复一遍。
3. **反转揭晓**：这不是三件产品，是一台 Folio。
4. **每个卖点 = 一张图 + 一句话 + 一次演示**：在台上的阳光灯下直接读；把 Folio 塞进西装内袋；随手划一句，笔记自动出现在手机上。
5. **一个大数字**：「一次充电，读完 30 本书¹」，脚注写明测试条件。
6. **回到开头**：再说一遍开场那句话，这一次给出答案。
7. **还有一件事**：家庭共享书架，一个小而真实的惊喜。
8. **价格和上市时间**：一页说清楚。
公司历程和融资情况放进新闻稿，不在台上讲。

**改在哪 / 为什么**
- 20 项功能砍到 3 个，用三件套串起来：原则 #1、#22，以及 G1-9 的三件套加反转。
- 用演示代替形容词：G1-10 的道具证明，以及 E4 的 demo 驱动。
- 一场只给一个大数字：原则 #26。
- 首尾呼应加「还有一件事」制造节奏：原则 #28，以及 G4 的发布会结构。
- 公司自己的事挪出主舞台，主语始终是观众：原则 #24，以及 E3 的 Think Human。

---

## 参考来源（只学方法与观点，未大段摘录原文；单条引语不超过一个短语）

**苹果官方规范**
- Apple HIG 总览：https://developer.apple.com/design/human-interface-guidelines
- HIG Layout：https://developer.apple.com/design/human-interface-guidelines/layout
- HIG Typography：https://developer.apple.com/design/human-interface-guidelines/typography
- HIG Color：https://developer.apple.com/design/human-interface-guidelines/color
- HIG Motion：https://developer.apple.com/design/human-interface-guidelines/motion
- HIG Accessibility：https://developer.apple.com/design/human-interface-guidelines/accessibility
- HIG Buttons（44×44pt）：https://developer.apple.com/design/human-interface-guidelines/buttons
- HIG Writing：https://developer.apple.com/design/human-interface-guidelines/writing
- Adopting Liquid Glass：https://developer.apple.com/documentation/TechnologyOverviews/adopting-liquid-glass
- Apple Style Guide：https://support.apple.com/guide/applestyleguide/welcome/web （PDF：https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf ）

**WWDC 演讲**
- WWDC25 Meet Liquid Glass：https://developer.apple.com/videos/play/wwdc2025/219/
- WWDC25 Get to know the new design system：https://developer.apple.com/videos/play/wwdc2025/356/
- WWDC25 Make a big impact with small writing changes：https://developer.apple.com/videos/play/wwdc2025/404/
- WWDC24 Add personality to your app through UX writing：https://developer.apple.com/videos/play/wwdc2024/10140/
- WWDC24 Get started with Dynamic Type：https://developer.apple.com/videos/play/wwdc2024/10074/
- WWDC23 Animate with springs：https://developer.apple.com/videos/play/wwdc2023/10158/
- WWDC22 Writing for interfaces：https://developer.apple.com/videos/play/wwdc2022/10037/
- WWDC20 The details of UI typography：https://developer.apple.com/videos/play/wwdc2020/10175/
- WWDC20 Make your app visually accessible：https://developer.apple.com/videos/play/wwdc2020/10020/
- WWDC18 Designing Fluid Interfaces：https://developer.apple.com/videos/play/wwdc2018/803/

**设计思想**
- Dieter Rams 好设计十原则（Vitsœ）：https://www.vitsoe.com/us/about/good-design
- Jobs 1997 WWDC「聚焦就是说不」：https://www.youtube.com/watch?v=H8eP99neOVs
- Jobs 1997 WWDC 问答「从用户体验倒推技术」：https://www.youtube.com/watch?v=EZll3dJ2AjY
- Jobs 1998 BusinessWeek 采访（BBC 转引）：https://www.bbc.com/news/world-us-canada-15195448 ；另见 https://allaboutstevejobs.com/verbatim/quotes
- Jobs 2003 NYT "The Guts of a New Machine"：https://www.nytimes.com/2003/11/30/magazine/the-guts-of-a-new-machine.html
- Ive 2012 Telegraph 采访：https://www.telegraph.co.uk/technology/apple/9283706/Jonathan-Ive-interview-simplicity-isnt-simple.html ；CNET 报道：https://www.cnet.com/tech/mobile/apples-jony-ive-knighted-discusses-quest-for-simplicity/
- Ive 2013 Charlie Rose 访谈：https://www.macrumors.com/2013/11/22/jony-ive-and-designer-marc-newson-interviewed-on-charlie-rose-show/ ；https://www.idownloadblog.com/2013/11/22/jony-ive-on-charlier-rose-on-the-value-of-simplicity/
- Ken Segall《Insanely Simple》序章（作者官网）：https://kensegall.com/wp-content/uploads/2017/09/Insanely-Simple_intro.pdf ；作者访谈：https://www.marketingweek.com/qa-ken-segall/ ；书评：https://financialpost.com/entrepreneur/take-steve-jobss-lead-and-think-simple
- Ken Kocienda《Creative Selection》书摘：https://commoncog.com/creative-selection/ ；作者访谈：https://www.imore.com/creative-selection-best-book-ever-written-about-apple ；书评：https://matttillotson.com/books/creative-selection-ken-kocienda 、https://brettworks.com/2019/01/25/notes-on-ken-kociendas-creative-selection-2018/ 、https://www.macrumors.com/2018/09/04/creative-selection-kocienda-book/

**排版与本地化**
- W3C《中文排版需求》clreq：https://www.w3.org/TR/clreq/
- 苹方（维基百科）：https://zh.wikipedia.org/zh-cn/苹方 ；El Capitan 苹方使用笔记：https://gist.github.com/bitinn/42c95ed95aa3dcf155e2
- 《中华人民共和国广告法》（第九条，极限词）：https://www.samr.gov.cn/zt/ndzt/2019n/bjspjsqjxcjwljxyjsckpxc/zcfg/art/2023/art_f383fbf8c106420b8951ba8d9508d32d.html

**文案与发布会观察（只归纳句式）**
- apple.com / apple.com.cn 产品页（2026-10-09 观察）：iPhone 18 Pro、AirPods Pro 3、MacBook Pro、MacBook Air、iPad Air、Apple Watch Series 12、Privacy
- iPod 新闻稿（2001）：https://www.apple.com/newsroom/2001/10/23Apple-Presents-iPod/
- iPhone 发布会文字稿与修辞分析（2007）：https://www.european-rhetoric.com/analyses/ikeynote-analysis-iphone/transcript-2007/
- MacBook Air 新闻稿（2008）：https://www.apple.com/newsroom/2008/01/15Apple-Introduces-MacBook-Air-The-Worlds-Thinnest-Notebook/ ；现场报道：https://www.infoworld.com/article/2317220/jobs-unveils-skinny-notebook-itunes-movie-rentals.html
- 「One more thing」传统：https://en.wikipedia.org/wiki/Stevenote

**本手册未收录（没找到可靠的公开来源）**
- 两本书逐章的细节和原文案例：只用了序章、作者访谈和公开书评能确认的部分。
- 中文正文每行字数的统一推荐值：clreq 没有给出，所以不写死数字。
- 苹果官方的中文写作规范：Apple Style Guide 公开的只有英文版，F2 里的中文对应都是我们自己的建议。
