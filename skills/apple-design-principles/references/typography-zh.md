# 字体与中文排版

> 字体选择、中文排版、中英混排时读。各平台默认 / 最小字号等会随版本变化的数值见 [spec-snapshot.md](spec-snapshot.md)；Web 字号与缩放要求见 [checklist-web.md](checklist-web.md)。

**SF 字体家族**（来源：HIG Typography https://developer.apple.com/design/human-interface-guidelines/typography 、WWDC20 10175）
- **SF Pro**：iOS、iPadOS、macOS、tvOS、visionOS 的系统字体，无衬线。
- **SF Compact**：watchOS 的系统字体，字形更窄，适合小屏；表盘复杂功能用 SF Compact Rounded。
- **SF Mono**：等宽字体，用于代码和需要对齐的数字。
- **Rounded 圆体**：SF Pro 和 SF Compact 等都有圆体版本，适合圆润的界面元素或想换一种语气的场景。
- **New York（NY）**：衬线字体，可以单独用，也能和 SF 搭配，适合阅读类和编辑感的标题。
- 还有 SF Arabic、SF Hebrew 等多语言变体。系统字体都是可变字体，支持动态光学尺寸，字重从 Ultralight 到 Black，SF 还有 Condensed、Expanded 等宽度。SF Symbols 的字重和文字一一对应。
- **默认 / 最小字号**：见 [spec-snapshot.md](spec-snapshot.md) 的「HIG 字号」表。
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

**Web 上的中文字体栈（建议，非苹果规定）**
- `font-family: system-ui, -apple-system, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif;`
- 中文正文 `line-height` 取 1.5–1.7；混排间距可用 CSS `text-autospace`（浏览器支持不一，不支持时手动加半角空格）。
- WCAG 2.2 的 1.4.12 要求用户把行高调到 1.5 倍、段距 2 倍、字距 0.12 倍、词距 0.16 倍时内容不丢失，所以不要用固定高度容器装中文正文（见 [checklist-web.md](checklist-web.md)）。
