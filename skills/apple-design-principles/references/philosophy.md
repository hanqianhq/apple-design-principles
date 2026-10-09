# 设计思想源头 → 可执行检查点

> 讲「为什么这样做」时读。上半部分是可直接用于评审的提问清单，下半部分是带来源的观点转述（只用自己的话转述，引语不超过一个短语；书籍部分只依据公开序章、访谈和书评）。

## 目录
- 0. 评审提问清单（从下面各节提炼）
- E1. Dieter Rams 好设计十原则
- E2. Steve Jobs 与 Jony Ive：产品、简化和做减法
- E3. Ken Segall《Insanely Simple》
- E4. Ken Kocienda《Creative Selection》

## 0. 评审提问清单

| 提问 | 出处 | 对应原则 |
|---|---|---|
| 这个产品 / 页面唯一要解决的问题是什么？哪些好主意要说不？ | Jobs 1997（E2） | #1 #2 |
| 方案是从哪种用户体验倒推出来的，而不是从哪项技术出发？ | Jobs 1997（E2） | #4 |
| 删掉这个元素会损失什么？答不上来就删。 | Rams 第 10 条（E1） | #8 |
| 文案的每个承诺，产品今天都做得到吗？ | Rams 第 6 条「诚实」（E1） | #29 |
| 能不能合并成一个？（「简单之杖」） | Segall（E3） | #1 |
| 一屏是不是只扔一个「纸团」？ | Segall Think Minimal（E3） | #22 |
| 有没有一个能点的 demo，而不是在文档里争论？ | Kocienda（E4） | — |
| 能不能替用户选好，而不是多给一个选项？ | Kocienda iPad 键盘故事（E4） | #9 |
| 看不见的地方（报错、空状态、导出文件名）做好了吗？ | Ive 2013（E2） | #7 |
| 这次评审谁拍板？结论是什么？ | Kocienda（E4） | — |

## E1. Dieter Rams 好设计十原则

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

## E2. Steve Jobs 与 Jony Ive：关于产品、简化和做减法

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

## E3. Ken Segall《Insanely Simple》（《疯狂的简洁》）

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

## E4. Ken Kocienda《Creative Selection》（《创意选择》）

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
