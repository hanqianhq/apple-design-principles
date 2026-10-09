# 苹果式产品 / UI / 文案原则（Apple-style Design Principles）

[English](README.md)

一个 [Agent Skill](https://agentskills.io)：用苹果式的方法审查和改写产品方案、App 与网页界面、界面文案、官网和发布会文案。原则是**先聚焦，再层级，再细节；每条批评都给出改法**。支持中英文。

包含：
- **分流**：先判断界面是用来说服（营销页）、操作（App、SaaS、后台工具）还是阅读（文档），再看平台；然后套用对应的检查表和单位（iOS 用 pt + HIG，Web 用 CSS px + WCAG 2.2）。
- **检查表**：
  - iOS
  - Web：WCAG 2.2，已对照 W3C 原文核对
  - 工具 / SaaS 界面：数据真实、计数与分页一致、危险操作、长任务、计费透明、权限、术语表、资产引用关系、承诺与能力一致
- **界面文案**：按钮、状态、空状态、报错、确认弹窗、通知、设置项。
- **营销文案**：产品页骨架、标题公式、发布会结构、中英本地化（重写而不是翻译）。
- **规范快照**：会随版本变化的数值（HIG 尺寸、WCAG 数值、Liquid Glass），每条都标了核对日期。

## 安装

### Claude Code（插件市场）
```text
/plugin marketplace add hanqianhq/apple-design-principles
/plugin install apple-design-principles@apple-design-principles
```
在终端里也可以用：`claude plugin marketplace add hanqianhq/apple-design-principles`。

### 通用：`skills` 命令行（[vercel-labs/skills](https://github.com/vercel-labs/skills)）
```bash
npx skills add hanqianhq/apple-design-principles                 # 交互式选择
npx skills add hanqianhq/apple-design-principles -a claude-code -g # 装到 Claude Code 用户目录
npx skills add hanqianhq/apple-design-principles -a cursor -a codex
```

### 手动复制
把 `skills/apple-design-principles/` 整个文件夹（不只是 `SKILL.md`）复制到下面任一位置：

| 工具 | 项目内 | 用户级 |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Cursor | `.agents/skills/` 或 `.cursor/skills/` | `~/.cursor/skills/` |
| Codex | `.agents/skills/` | `~/.agents/skills/` |

```bash
git clone https://github.com/hanqianhq/apple-design-principles
cp -r apple-design-principles/skills/apple-design-principles ~/.claude/skills/
```

### Claude.ai / Claude 客户端
把 `skills/apple-design-principles/` 文件夹打成 zip，在设置里作为自定义 skill 上传。frontmatter 只用了标准字段，可以正常上传。

## 试试这样问
- 「按苹果设计师的标准审一下这个设置页，按 P0 / P1 / P2 给问题和改法。」
- 「这个后台工具页帮我按苹果式标准审一遍。」
- 「把这段产品介绍改成发布会风格，中英文各一版。」
- 「删除确认弹窗的标题和按钮应该怎么写？」
- 「iOS 和网页的按钮最小多大？请注明依据。」
- "Rewrite these error messages: 'Error 500', 'Operation failed'."

## 目录结构
```text
.claude-plugin/          plugin.json、marketplace.json（Claude Code 插件）
skills/apple-design-principles/
  SKILL.md               分流、流程清单、优先级表、输出模板、范例、索引
  references/            按需读取（原则、检查表、文案、规范快照、来源……）
  assets/                审查报告模板
  evals/                 测试题、触发测试、评分脚本、结果
```

## 测评
`skills/apple-design-principles/evals/` 里有 7 道测试题和 20 条触发测试。在随附的一轮测试里，正则检查项的得分是：

| 版本 | 得分 |
|---|---|
| v2.0.0 | 53/53 |
| v1 | 42/53 |
| 不用 skill | 35/53 |

**这些数字来自作者自己做、自己评的单轮测试，不是盲测**。方法和局限见 [evals/README.md](skills/apple-design-principles/evals/README.md)。

## 来源与准确性
Apple HIG 和 WCAG 2.2 的数值已在 2026-10-09 对照原文核对，链接放在 `references/spec-snapshot.md` 和 `references/sources.md`。规范会更新，用到具体数值前，请以最新版 Apple Human Interface Guidelines 和 [WCAG](https://www.w3.org/TR/WCAG22/) 为准。

## 许可
[CC BY 4.0](LICENSE)：可以分享和改编（包括商用），需要署名。

## 声明
本项目与 Apple Inc. 无关联，未获 Apple 认可或赞助。Apple、iPhone、iPad、Mac、Apple Watch、SF Pro、Liquid Glass 等是 Apple Inc. 在美国及其他国家和地区注册的商标。所有示例都是原创虚构产品，没有复制苹果的文案和素材；本项目只提炼方法与原则，并注明出处。
