# 触发测试（2026-10-09）

两种方法，都不是真实的 agent 加载日志，仅作参考。

## A. 模拟判断（作者本人逐条判断「只看 name + description 时，agent 会不会加载这个 skill」）

v1 description：中文一句「用这个 when：需要按苹果风格审查或设计产品方案、App/网页界面、官网或发布会式文案…」，name 为中文（不符合 agentskills.io 的 name 规则，claude.ai 上传会被拒）。
v2 description：见 SKILL.md。

| id | 应触发 | v1 | v2 | 说明 |
|---|---|---|---|---|
| t01 设置页截图不够苹果风 | 是 | ✅ | ✅ | |
| t02 pricing page 层级、删什么（英文，未提 Apple） | 是 | ❌ | ✅ | v1 只写「按苹果风格」，未提 Apple 时不明确 |
| t03 改成发布会文案 | 是 | ✅ | ✅ | |
| t04 改写报错信息（英文） | 是 | ❌ | ✅ | v1 未覆盖界面文案 / 报错 |
| t05 后台页做减法 | 是 | ❓ | ✅ | v1 未提后台 / 工具 |
| t06 空状态 + 引导（中英） | 是 | ❌ | ✅ | |
| t07 landing page hero 标题 | 是 | ❓ | ✅ | v1 有「官网」，可能触发 |
| t08 Web 对比度、图标按钮尺寸 | 是 | ❌ | ✅ | v1 未提无障碍 / WCAG |
| t09 tagline 本地化（不是翻译） | 是 | ❓ | ✅ | v1 只有「中英文」 |
| t10 删除确认弹窗文案 | 是 | ❌ | ✅ | |
| n01 写 React 组件 | 否 | ✅ 不触发 | ✅ 不触发 | v2 明确排除写代码 |
| n02 Apple 财报 | 否 | ✅ | ✅ | v2 明确排除 Apple company news |
| n03 iPhone 耗电 | 否 | ✅ | ✅ | v2 明确排除设备故障 |
| n04 数据库表设计 | 否 | ✅ | ✅ | |
| n05 技术博客翻译 | 否 | ✅ | ✅ | v2 明确排除 plain translation |
| n06 App Store 提交被拒 | 否 | ✅ | ✅ | v2 明确排除 |
| n07 赛博朋克海报 | 否 | ✅ | ✅ | |
| n08 SwiftUI view model | 否 | ✅ | ✅ | |
| n09 投资人邮件 | 否 | ✅ | ✅ | |
| n10 CSS 构建报错 | 否 | ✅ | ✅ | |

结果：应触发 v1 **2/10 确定 + 3 不确定**，v2 **10/10**；不应触发两版都 **10/10** 不触发。

## B. 词汇重叠代理（可复现：`python3 trigger_proxy.py <v1 SKILL.md> <v2 SKILL.md>`，输出见 trigger-proxy.json）

用 query 与 description 的词 / 中文二字词重叠打分，计算「应触发」与「不应触发」的分离度（AUC，0.5 = 随机，1 = 完全分开）。

| 版本 | description 字符数 | AUC | 零重叠的应触发 query |
|---|---|---|---|
| v1 | 191 | 0.575 | t02 t04 t07 t09 t10 |
| v2 初稿 | 833 | 0.875 | 无 |
| v2 调整后 | 858 | 0.925 | 无 |

调整内容：英文把 landing-page / product-page 拆成空格写法并加 headline；中文触发词加「截图、设置页、落地页、标题、对比度」。

## 局限
- A 是作者本人判断，作者知道每条 query 的标签，不是盲测。
- B 只看词汇重叠，不理解否定（例如 n06 因 description 里「Not for … App Store submission」反而得分较高）；真实 agent 是语义判断。
- 调整 description 用的是同一批 20 条 query，存在过拟合风险；没有独立的验证集。
- 没有在 Claude Code / Cursor / Codex 里实际运行触发测试（box 上没有可用的 agent CLI）。
