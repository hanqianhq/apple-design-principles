分流：两端同一套设计 → platform-mapping；数值核对日期 2026-10-09（spec-snapshot）。

| 问题 | iOS（HIG） | Web（WCAG 2.2 / 惯例） | 推荐 |
|---|---|---|---|
| 按钮最小尺寸 | 默认 44×44 pt，最小 28×28 pt | AA：24×24 CSS px（SC 2.5.8，有间距例外）；AAA：44×44 CSS px（SC 2.5.5） | 两端主要按钮都做 44；Web 24 是底线 |
| 正文字号 | 默认 17 pt（最小 11 pt），用 Dynamic Type 文字样式 | WCAG 不规定字号；16px 是惯例；要求是放大 200% 不丢内容（1.4.4）、320 CSS px 重排（1.4.10） | iOS 17 pt / Web 16px，`rem` 单位 |
| 对比度 | ≤17 pt：4.5:1；≥18 pt 或粗体：3:1 | 文字 4.5:1，大字 3:1（1.4.3 AA）；控件、焦点环等非文本 3:1（1.4.11） | 设计令牌里统一用 4.5:1 校验 |
| 减弱动效 | 系统「减弱动态效果」开启时替换位移和缩放 | `@media (prefers-reduced-motion: reduce)`；自动播放 >5 秒需可暂停（2.2.2） | 要做，两端都做 |
| 焦点样式 | 外接键盘时用系统焦点环 | 焦点可见（2.4.7 AA）；不被吸顶栏遮挡（2.4.11 AA）；2.4.13（AAA）建议 2 CSS px 轮廓、3:1 | React 中用 `:focus-visible`，2px 实线 + offset，不写 `outline: none` |

依据：
- HIG Buttons：https://developer.apple.com/design/human-interface-guidelines/buttons
- HIG Typography：https://developer.apple.com/design/human-interface-guidelines/typography
- WCAG 2.2：https://www.w3.org/TR/WCAG22/#target-size-minimum 、#contrast-minimum 、#non-text-contrast 、#focus-visible 、#focus-not-obscured-minimum
