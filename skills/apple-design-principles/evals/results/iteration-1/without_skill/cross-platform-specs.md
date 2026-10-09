iOS 和 Web 的常用标准：

| 项目 | iOS | Web |
|---|---|---|
| 按钮最小尺寸 | 44×44pt（Apple HIG） | 44×44px（WCAG 推荐） |
| 正文字号 | 17pt（系统 Body） | 16px |
| 对比度 | 4.5:1（大字 3:1） | 4.5:1（大字 3:1），WCAG AA |
| 减弱动效 | 支持「减弱动态效果」 | 用 CSS `prefers-reduced-motion` |
| 焦点样式 | 系统自带，键盘/外接键盘时可见 | 不要去掉 outline，用 `:focus-visible` 设计清晰的焦点环 |

依据：Apple Human Interface Guidelines、WCAG 2.1/2.2。建议两端共用一套设计 token，再按平台换算单位。
