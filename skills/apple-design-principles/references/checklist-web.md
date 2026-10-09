# Web 检查表（WCAG 2.2 口径，单位 CSS px）

> 审网页、落地页、Web App、桌面 Web 工具时读。苹果式原则（聚焦、层级、颜色语义、动效有目的）不变，**数值和机制换成 Web 的**：用 CSS px、WCAG 2.2 和浏览器能力，不用 iOS 的 pt。
> WCAG 数值于 2026-10-09 抓取 W3C 原文核对（WCAG 2.2，W3C Recommendation 2024-12-12）：https://www.w3.org/TR/WCAG22/ 。下表「准则」列链接到该准则原文。
> 工具类 / SaaS 还要再过 [checklist-tool-ui.md](checklist-tool-ui.md)；iOS 对照见 [platform-mapping.md](platform-mapping.md)。

## 目录
W1 无障碍硬指标（WCAG 2.2）｜W2 层级与布局｜W3 字体与排版｜W4 颜色与主题｜W5 动效｜W6 表单与反馈｜W7 营销页（Persuade）专项｜W8 性能与感知速度

## W1. 无障碍硬指标（WCAG 2.2，AA 为底线）

| 检查项 | 要求（W3C 原文转述） | 准则 / 级别 |
|---|---|---|
| 文字对比度 | 普通文字 ≥ 4.5:1；大字 ≥ 3:1。大字 = 至少 18 pt，或 14 pt 粗体，或中日韩字体的等效字号 | [1.4.3](https://www.w3.org/TR/WCAG22/#contrast-minimum) AA |
| 更高对比度 | 文字 7:1，大字 4.5:1 | [1.4.6](https://www.w3.org/TR/WCAG22/#contrast-enhanced) AAA |
| 非文本对比度 | 识别控件和状态所需的视觉信息（输入框边框、开关状态、焦点环、图表关键部分）对相邻颜色 ≥ 3:1 | [1.4.11](https://www.w3.org/TR/WCAG22/#non-text-contrast) AA |
| 目标尺寸（最小） | 指针目标至少 **24×24 CSS px**；例外：间距足够（以每个小目标为中心画直径 24 CSS px 的圆，彼此不相交）、页面上有达标的等效控件、句中行内链接、浏览器默认控件、必要呈现 | [2.5.8](https://www.w3.org/TR/WCAG22/#target-size-minimum) AA（2.2 新增） |
| 目标尺寸（增强） | 至少 **44×44 CSS px**（同样有等效、行内等例外） | [2.5.5](https://www.w3.org/TR/WCAG22/#target-size-enhanced) AAA |
| 焦点可见 | 任何可用键盘操作的界面，都要有焦点指示可见的模式；不要 `outline: none` 而不给替代 | [2.4.7](https://www.w3.org/TR/WCAG22/#focus-visible) AA |
| 焦点不被遮挡 | 获得焦点的组件不能被作者创建的内容（吸顶栏、Cookie 横幅、悬浮聊天）完全挡住 | [2.4.11](https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum) AA（2.2 新增） |
| 焦点外观 | 焦点指示面积至少相当于组件 2 CSS px 粗的轮廓，且聚焦前后同一批像素对比 ≥ 3:1 | [2.4.13](https://www.w3.org/TR/WCAG22/#focus-appearance) AAA（2.2 新增） |
| 键盘 | 所有功能都能用键盘完成 | [2.1.1](https://www.w3.org/TR/WCAG22/#keyboard) A |
| 拖拽替代 | 拖拽能完成的操作，也能用单指针不拖拽完成（例如排序给「上移 / 下移」） | [2.5.7](https://www.w3.org/TR/WCAG22/#dragging-movements) AA（2.2 新增） |
| 名称、角色、值 | 自定义控件能被读屏识别；纯图标按钮有可访问名称（`aria-label`） | [4.1.2](https://www.w3.org/TR/WCAG22/#name-role-value) A |
| 可见标签在名称里 | 按钮上看到的字要包含在可访问名称里（看到「搜索」，名称不能是「查找」） | [2.5.3](https://www.w3.org/TR/WCAG22/#label-in-name) A |
| 不只靠颜色 | 颜色不能是传达信息、提示操作的唯一手段 | [1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color) A |
| 结构可读 | 视觉上的标题、列表、表格关系在代码里也成立（语义标签） | [1.3.1](https://www.w3.org/TR/WCAG22/#info-and-relationships) A |
| 状态消息 | 「已保存」「3 条结果」这类状态不抢焦点也能被读屏读到（`role="status"` / `aria-live`） | [4.1.3](https://www.w3.org/TR/WCAG22/#status-messages) AA |
| 文字缩放 | 不借助辅助技术放大到 200% 不丢内容和功能 | [1.4.4](https://www.w3.org/TR/WCAG22/#resize-text) AA |
| 重排 | 宽 320 CSS px（≈1280 px 宽放大 400%）时不出现横竖双向滚动；数据表、地图等除外 | [1.4.10](https://www.w3.org/TR/WCAG22/#reflow) AA |
| 文字间距 | 用户把行高调到 1.5 倍、段后 2 倍、字距 0.12 倍、词距 0.16 倍时不丢内容 | [1.4.12](https://www.w3.org/TR/WCAG22/#text-spacing) AA |
| 自动动画 | 自动开始、超过 5 秒、和其他内容并列的移动 / 轮播 / 自动更新，要能暂停、停止或隐藏 | [2.2.2](https://www.w3.org/TR/WCAG22/#pause-stop-hide) A |
| 闪烁 | 任意 1 秒内闪烁不超过 3 次 | [2.3.1](https://www.w3.org/TR/WCAG22/#three-flashes-or-below-threshold) A |
| 交互动效可关 | 由交互触发的运动动画可以关闭（非必要时） | [2.3.3](https://www.w3.org/TR/WCAG22/#animation-from-interactions) AAA |
| 输入纠错 | 能检测到错误且知道怎么改时，给出修改建议 | [3.3.3](https://www.w3.org/TR/WCAG22/#error-suggestion) AA |
| 防错（法律 / 金融 / 数据） | 产生付款、法律承诺、删改用户数据的提交：可撤销，或提交前检查，或可确认修改 | [3.3.4](https://www.w3.org/TR/WCAG22/#error-prevention-legal-financial-data) AA |
| 不重复填写 | 同一流程里填过的信息自动带出或可选择 | [3.3.7](https://www.w3.org/TR/WCAG22/#redundant-entry) A（2.2 新增） |
| 无障碍登录 | 登录不强制认知测试（记密码、解谜）——允许粘贴密码、密码管理器、其他登录方式 | [3.3.8](https://www.w3.org/TR/WCAG22/#accessible-authentication-minimum) AA（2.2 新增） |
| 帮助位置一致 | 多页重复出现的帮助入口（客服、帮助中心）保持相同相对顺序 | [3.2.6](https://www.w3.org/TR/WCAG22/#consistent-help) A（2.2 新增） |
| 标题和标签 | 标题和表单标签说清主题或用途 | [2.4.6](https://www.w3.org/TR/WCAG22/#headings-and-labels) AA |

> 做法提示（非 WCAG 原文）：苹果式产品建议主要按钮做到 44×44 CSS px，AA 的 24 px 只当底线；对比度用工具实测，不靠肉眼。

## W2. 层级与布局
- [ ] 首屏 3 秒测试：第一眼落在唯一的主信息或主操作上（#12）
- [ ] 每屏一个主按钮，其余降为次按钮或文字链接
- [ ] 导航只有一套；同一组入口不在顶栏、侧栏、卡片里重复出现
- [ ] 统一间距刻度（4 / 8 的倍数）；组内间距 < 组间间距（#18）
- [ ] 正文行长控制在约 60–80 个西文字符；中文按实测，不让一行长到找不到下一行
- [ ] 响应式：320 CSS px 宽仍可用（1.4.10），触屏布局下目标不缩小到 24 px 以下

## W3. 字体与排版
- [ ] 正文基准 16px 起（行业惯例，非 WCAG 要求）；字号级数 ≤ 4
- [ ] 用 `rem` 而不是写死 `px` 高度的容器，放大 200% 不截断（1.4.4）
- [ ] 系统字体栈优先（`system-ui` 等，见 [typography-zh.md](typography-zh.md)）；最多两种字族
- [ ] 中文行高 1.5–1.7；中西文、数字之间有间距
- [ ] 小字不用细字重

## W4. 颜色与主题
- [ ] 一个强调色只表示「可点」；警告、删除、成功各有语义色（#17）
- [ ] 支持 `prefers-color-scheme` 深色模式时，深浅两套都实测对比度
- [ ] 尊重 `prefers-contrast` / Windows 高对比（`forced-colors`）时控件仍可辨认
- [ ] 不用纯颜色区分状态（1.4.1）：加图标、文字或形状

## W5. 动效
- [ ] 每个动画都能说出它在解释什么变化（#19）
- [ ] 尊重 `prefers-reduced-motion: reduce`：位移、缩放、视差换成淡入或直接切换（对应 2.3.3）
- [ ] 轮播、自动播放视频有暂停按钮，或干脆不自动播放（2.2.2）
- [ ] 不给每个区块都加滚动淡入；一个页面最多一个编排过的动效时刻
- [ ] 悬停效果不是唯一的提示方式（触屏没有悬停）

## W6. 表单与反馈
- [ ] 每个输入框有可见标签，不只靠 placeholder
- [ ] 报错写在出错字段旁边，说清怎么改（3.3.3），并能被读屏读到
- [ ] 提交后有明确结果反馈；状态消息用 `role="status"`（4.1.3）
- [ ] 允许粘贴密码、支持密码管理器（3.3.8）
- [ ] 已填信息不让用户重填（3.3.7）

## W7. 营销页（Persuade）专项
- [ ] 首屏：产品名 + 巧思标题 + 直白副标 + 一个主按钮 + 真实产品画面（见 [marketing-copy.md](marketing-copy.md)）
- [ ] 主按钮文字写清点了会发生什么（「免费试用 14 天」而不是「了解更多」）
- [ ] 官网的承诺（免费、开放注册、支持的平台）与产品实际状态一致
- [ ] 数字有脚注写明条件；没有无法证明的最高级

## W8. 性能与感知速度
- [ ] 首屏主视觉尽快出现，图片预留尺寸，避免加载时布局跳动
- [ ] 超过约 1 秒的操作有即时反馈（按钮状态、骨架屏、进度）
- [ ] 长任务见 [checklist-tool-ui.md](checklist-tool-ui.md) T4
