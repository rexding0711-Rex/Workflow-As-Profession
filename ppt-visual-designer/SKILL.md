---
name: ppt-visual-designer
description: 为PPT演示文稿生成高质量视觉资产（图片）的AI设计助手。基于presentation-first设计哲学，提供从封面、章节分隔、概念可视化、对比图到结尾海报的全套图片生成规范。包含4K/16:9标准、配色系统、字体层级、安全区规划、以及针对不同幻灯片角色的专用提示词模板。当用户需要为PPT生成配图、封面图、章节分隔图、概念图、数据背景图、对比图或结尾图时触发。关键词：PPT配图、幻灯片图片、封面图、演讲配图、presentation image、slide asset、keynote visual。
---

# PPT 视觉资产设计器

## 这个 Skill 做什么

为PPT演示文稿生成**高质量的视觉资产图片**——不是完整的PPT文件，也不是网页，而是可以直接插入到PowerPoint/Keynote/Google Slides中的16:9图片。

每一张图片都是**视觉论点**：帮助幻灯片更快、更有力地传达核心观点，同时为文字层留出可编辑的安全空间。

### 支持的幻灯片图片类型

| 类型 | 用途 | 视觉特征 |
|------|------|---------|
| **封面/Opening Hero** | 第1页，抓住注意力 | 最强对比、最清晰身份、一个主导hero主体 |
| **章节分隔/Section Divider** | 章节之间，重置节奏 | 比封面更简化、更多留白、更干净的几何 |
| **概念可视化/Concept Visualization** | 解释抽象概念 | 一个隐喻+一个结构支撑层，不做信息图 |
| **对比板/Comparison Plate** | 展示张力、前后对比 | 分割构图、镜像对象、非对称对抗 |
| **数据背景/Data Backdrop** | 支撑数据/图表页 | 克制结构、干净标题区、冷静边缘 |
| **系统/流程板/System Plate** | 可视化流程、层级、架构 | 大块面、 deliberate 连接线、少量节点类型 |
| **结尾海报/Closing Poster** | 最后一页，压缩判断 | 简洁、有力、情绪已解决、大量留白 |

**设计哲学**：`presentation-first`，不是`web-first`。
- 图片是**视觉论点**，不是装饰填充物
- 每张图片必须在1秒内传达情感或概念方向
- 系列一致性比单图巧思更重要

---

## 何时使用

**合适的场景**：
- 为演讲PPT生成封面、章节分隔图、概念图
- 为商业汇报生成对比图、数据背景图
- 为产品发布生成系统架构图、流程图
- 为任何演示文稿生成统一视觉风格的图片资产

**不合适的场景**：
- 需要生成完整PPT文件（用 `guizang-ppt-skill` 或 `pptx`）
- 需要生成网页/产品UI（用其他设计Skill）
- 需要生成信息图表/复杂数据图表（用专门的数据可视化工具）
- 需要大量文字内容（PPT图片应保持文字最小化）

---

## 核心设计规范

### 1. 色彩系统

使用克制的演示调色板。大部分Deck应只使用1种基础模式+1种强调色族，不要六种无关颜色。

#### 核心中性色

| 颜色名 | Hex | 用途 |
|--------|-----|------|
| **纸白 Paper White** | `#F6F1E8` | 浅色背景Deck、图表、纸质区域、编辑感平静 |
| **墨黑 Ink Black** | `#111317` | 深色Deck、排版对比区、电影感负空间 |
| **石墨 Graphite** | `#2A2F36` | 中性支撑色，用于表面、图表、阴影、低噪结构 |
| **石灰 Stone Gray** | `#A8A29A` | 分隔线、微妙纹理、薄注释区、低强调支撑 |

#### 信号强调色

| 颜色名 | Hex | 用途 |
|--------|-----|------|
| **钢蓝 Steel Blue** | `#345D7E` | 理性、技术强调色，用于数据、系统、解释性幻灯片 |
| **信号橙 Signal Orange** | `#D96A31` | 能量强调色，用于变革、运动、变化、紧迫感 |
| **信号红 Signal Red** | `#B6422E` | 保留用于警告、冲突、断裂、损失或战略张力 |
| **哑金 Muted Gold** | `#B08A46` | 高级强调色，用于总结海报、里程碑、高价值强调 |

#### 色彩规则

- **每份Deck只使用1个强调色作为主导能量源**
- 第二个强调色仅在需要对比或比较时允许
- 背景必须比主焦点物体更平静
- 文字安全区应比hero区更低的对比噪点
- 如果Deck已有品牌色，将品牌色映射到强调色角色，不引入额外饱和度

#### 渐变规则

- 最多2-3个色标的克制渐变
- 渐变应引导深度或情绪，不成为主体本身
- 避免默认的紫蓝"AI渐变"处理，除非主题明确要求

### 2. 排版规则

**PPT图片中的文字是可选的，非必需的。**

在大多数情况下，最佳幻灯片图片应：
- 无文字
- 或一个短标签
- 或一个超大数字
- 或一个短章节标记

**不要把完整幻灯片标题、长中文段落、项目列表或解释性正文烤入图片中。这些文字属于可编辑的幻灯片图层。**

#### 文字层级（如需在图片中放文字）

| 角色 | 建议字体 | 长度 | 用途 |
|------|---------|------|------|
| Hero Word | 压缩怪诞体/粗体编辑无衬线 | 1-4词 | 封面和章节图片 |
| Section Marker | 大写字母标签/宽字间距 | 1-2词 | 分隔页 |
| Data Numeral | 等宽或怪诞体数字 | 1个数字 | 数据驱动幻灯片 |
| Diagram Label | 干净无衬线/高对比 | 1-3词 | 概念板和系统图 |
| Micro Label | 仅在必要时 | 极短 | 投影中可读的注释 |

#### 排版规则

- 如果必须使用文字，必须能在投影和截图压缩中存活
- 优先大标签而非多个小标签
- 英文全大写和大数字比密集混合语言小字更安全
- 中文文字仅在短、大、必需时允许
- 不要以完美字体准确性为首要设计目标；优先层级、可读性和色调

### 3. 图片标准规格

| 属性 | 标准 | 说明 |
|------|------|------|
| 宽高比 | 16:9 水平 | 默认，除非Deck明确要求纵向或社交变体 |
| 主分辨率 | 3840×2160 (4K) | 首选 |
| 可接受降级 | 1920×1080 | 备用 |
| 主导焦点 | 1个 | 必须有且只有一个主导焦点 |
| 文字安全空间 | 25%-35% | 干净留白区域用于文字叠加 |
| 图片内文字 | 最小化或无 | 除非明确请求，否则不烤入文字 |

#### 裁切安全

- 关键视觉意义必须能在4:3的温和裁切中存活
- 避免将关键人脸、符号或标签放在最外8%边缘
- 如果图片包含标签，必须在安全区裁切中存活

#### 导出行为

- 避免在PDF导出中消失的微细细节
- 避免在投影仪上压入黑色的超暗阴影区域
- 避免在压缩截图中消失的细低对比线
- 如果幻灯片需要大量叠加文案，请提供一个更平静、更多负空间的第二版本

---

## 幻灯片组件样式

### 封面/Opening Hero

- **目的**：停止注意力并建立Deck的核心情感前提
- **构图**：一个主导hero主体，一个支撑层，一个清晰的标题安全区域
- **视觉行为**：全Deck中最强对比和最清晰身份
- **避免**：均匀分布的拼贴、到处都是小细节、海报文字填满画面

### 章节分隔/Section Divider

- **目的**：在章节之间重置节奏
- **构图**：比封面更简化的主体，更多负空间，更清晰的几何
- **视觉行为**：像一个呼吸，不是第二个封面
- **避免**：叙事过载和重细节密度

### 概念可视化/Concept Visualization

- **目的**：通过一个视觉隐喻解释一个抽象概念
- **构图**：一个隐喻+一个结构支撑层
- **视觉行为**：比段落更快，比信息图更干净
- **避免**：在一个画面中解释五个想法

### 对比板/Comparison Plate

- **目的**：可视化张力、权衡、前后或两个竞争系统
- **构图**：分割画面、镜像对象或非对称对抗
- **视觉行为**：没有标题也能读懂对比
- **避免**：两边同样杂乱或"左边坏/右边好"的俗套

### 数据背景/Data Backdrop

- **目的**：支撑数据或图表重的幻灯片而不压倒数据层
- **构图**：克制的结构、干净的标题区域、平静的边缘
- **视觉行为**：比说明更建筑感
- **避免**：与图表争夺焦点的强烈主体

### 系统/流程板/System Plate

- **目的**：可视化流程、层级、路由、序列或架构
- **构图**：大块面、深思熟虑的连接器、少量节点类型
- **视觉行为**：应该感觉有设计感，不像图表工具的截图
- **避免**：微标签、拥挤的箭头、字面化的软件窗口装饰

### 结尾海报/Closing Poster

- **目的**：将Deck的最终判断压缩成一张难忘的图片
- **构图**：大胆、简洁、情绪已解决
- **视觉行为**：总结能量，不是新信息
- **避免**：在结尾重新引入复杂度

---

## 布局原则

### 构图

- 默认宽高比 16:9
- 将最重要的主题放在中心80%宽度和80%高度内
- 根据幻灯片布局在左侧、右侧或顶部预留干净的标题安全区
- 让安全区明显比hero区更平静

### 层级

- 一个主导焦点
- 一个次要支撑层
- 一个背景氛围层

如果图片有四个同等响亮焦点，通常在幻灯片上会失败。

### 密度

- 封面幻灯片可以承载中等视觉密度
- 正文幻灯片应该更干净
- 数据支撑图片应该是最平静的
- 分隔页应该比正文页更简单

### 空间规则

- 边缘应容忍温和裁切
- 避免将关键人脸、符号或标签放在最外8%边缘
- 当非对称创造更干净的文字位置时，优先非对称
- 仅当概念本身是对抗或仪式时，对称才可接受

---

## 深度与材质

深度应来自平面、光线、氛围和材质对比，而非花哨的3D效果。

### 首选深度信号

- 前景/中景/背景分离
- 方向性光线
- 控制的阴影边缘
- 大气雾或微妙渐变衰减
- 哑光与反光表面之间的纹理对比
- 克制的胶片颗粒或纸张颗粒

### 材质指导

- 哑光纸、拉丝金属、烟熏玻璃、墨水、织物、混凝土和柔光都有效
- 仅当主题明确需要数字未来感时使用光泽玻璃形态
- 在严肃Deck中避免塑料、玩具般的、过度渲染的3D图标表面

### 层级逻辑

- 前景承载情感
- 中景承载结构
- 背景承载色调

不要让背景纹理比信息更响亮。

---

## 提示词模板

### 核心提示词骨架

```
Create a [slide role] image for a presentation.
Topic: [topic].
Slide thesis: [one-sentence judgment].
Visual direction: editorial, presentation-first, high signal, not stock.
Composition: one dominant focal point, one supporting layer, clean [left/right/top] title-safe zone.
Aspect ratio: 16:9 horizontal, 4K.
Palette: [base colors] with [accent color].
Texture and depth: [grain/material/light direction].
Text in image: minimal or none. If needed, only [short label / big numeral / chapter marker].
Series consistency: match the deck's existing palette, lighting, geometry, and contrast behavior.
Avoid: stock office scenes, generic SaaS illustration, tiny labels, neon purple AI wallpaper, clutter, watermark.
```

### 封面提示词模板

```
Create a presentation cover image.
The slide thesis is: [thesis].
The image should stop attention in one second and explain the deck's main conflict at a glance.
Use one dominant hero subject, cinematic but controlled composition, and a clean top-left title-safe zone.
Make it feel like an editorial poster rather than a movie poster or startup ad.
16:9 horizontal, 4K, minimal text, strong thumbnail readability.
```

### 章节分隔提示词模板

```
Create a section divider image for a presentation chapter.
The chapter theme is: [theme].
Use a simplified visual language, stronger negative space, and a cleaner composition than the cover.
The image should feel like a reset in rhythm, not another busy hero scene.
Leave a large [left/right/top] safe zone for the chapter title.
16:9 horizontal, 4K.
```

### 概念可视化提示词模板

```
Create a concept visualization for a presentation slide.
Slide thesis: [thesis].
Translate the abstract idea into one clear visual metaphor.
Do not create an infographic, dashboard, or icon soup.
Use one metaphorical scene plus one structural support layer.
Leave room for slide text overlay.
16:9 horizontal, 4K.
```

### 对比提示词模板

```
Create a comparison image for a presentation slide.
Compare: [A] versus [B].
The difference should be obvious even without captions.
Use a split composition or asymmetric confrontation with a clean title-safe zone.
Avoid cliche before/after stock imagery.
16:9 horizontal, 4K.
```

### 结尾海报提示词模板

```
Create a closing poster image for the final slide of a presentation.
Final judgment: [judgment].
The image should feel resolved, memorable, and compress the whole deck into one emotional frame.
Use bold simplicity, controlled contrast, and generous negative space for a short final statement.
Do not introduce new complexity.
16:9 horizontal, 4K.
```

---

## 工作流

### Step 1 · 需求澄清（动手前必做）

**如果用户已经给了完整的幻灯片结构**，可以跳过直接进入 Step 2。

**如果用户只给了主题或模糊想法**，用以下问题逐项对齐：

| # | 问题 | 为什么问 |
|---|------|---------|
| 1 | **Deck的主题是什么？** | 决定视觉方向 |
| 2 | **目标受众是谁？演示场景？** | 决定风格严谨度 |
| 3 | **需要哪些类型的图片？**（封面/章节/概念/对比/数据/系统/结尾） | 决定需要哪些提示词模板 |
| 4 | **整体视觉基调？** | 从配色系统推荐基础色+强调色 |
| 5 | **是否有品牌色？** | 将品牌色映射到强调色角色 |
| 6 | **需要多少张图片？** | 规划工作量和系列一致性 |

### Step 2 · 选择设计规范

根据用户回答，从以下方面确定设计参数：

1. **基础色模式**：浅色（Paper White背景）或深色（Ink Black背景）
2. **强调色**：Steel Blue / Signal Orange / Signal Red / Muted Gold
3. **文字安全区位置**：左侧、右侧或顶部（取决于幻灯片文字布局）

### Step 3 · 生成图片

对于每张图片，按以下清单生成：

1. **这张幻灯片的角色是什么？**（封面/章节/概念/对比/数据/系统/结尾）
2. **单句论点是什么？**
3. **安全区在哪里？**
4. **观众在1秒内应该感受到什么？**
5. **必须避免什么？**

如果以上任何一项缺失，在生成前推断出来。

使用对应的提示词模板，填充具体参数，生成图片。

### Step 4 · 系列一致性检查

所有图片必须感觉属于同一视觉系统：

- [ ] 调色板一致（基础色+强调色）
- [ ] 光线方向一致
- [ ] 纹理一致（胶片颗粒/纸张颗粒/金属/玻璃等）
- [ ] 几何语言一致
- [ ] 构图框架一致
- [ ] 对比行为一致

### Step 5 · 交付与使用建议

生成图片后，告知用户：
- 图片保存路径
- 建议直接拖拽到PowerPoint/Keynote/Google Slides中
- 幻灯片中文字放在图片上方（不要烤入图片）
- 如需更多图片，可继续使用相同设计参数生成

---

## 检查清单

### 生成前检查

- [ ] 幻灯片角色已明确（封面/章节/概念/对比/数据/系统/结尾）
- [ ] 单句论点已提炼
- [ ] 文字安全区位置已确定
- [ ] 配色方案已选定（基础色+强调色）
- [ ] 系列一致性参数已确认

### 生成后检查

- [ ] 图片有且只有一个主导焦点
- [ ] 25%-35%区域是干净的文字安全空间
- [ ] 图片在1秒内传达了情感或概念方向
- [ ] 没有烤入完整句子或段落
- [ ] 没有使用俗套的办公室/握手/笔记本场景
- [ ] 没有霓虹紫蓝"AI渐变"壁纸
- [ ] 没有充满微小符号对象
- [ ] 没有密集的数据图表或UI截图
- [ ] 没有水印
- [ ] 能在三个距离工作：全屏演示、PDF导出、缩略图视图

---

## 核心设计原则（哲学）

1. **一图一论点** — 每张图片只传达一个幻灯片层级的论点
2. **1秒可读性** — 如果观众在1秒内无法理解情感或概念方向，图片对演示来说太模糊
3. **系列一致性 > 单图巧思** — 跨Deck的重复选择（调色板、光线、纹理、几何、构图、对比行为）比单张图片的创意更重要
4. **高级但不 flashy** — 足够鲜明以锚定幻灯片，足够克制以支撑叠加内容
5. **为叠加设计** — 必须考虑标题叠加、副标题叠加和裁切安全
6. **更少的强元素 > 许多平均元素** — 优先少而强的元素，而非许多平均元素

---

## 对比：与现有PPT Skill的关系

| Skill | 输出 | 场景 |
|-------|------|------|
| **ppt-visual-designer**（本Skill） | 单张图片资产（PNG/JPG） | 为已有PPT生成配图、封面、概念图 |
| **guizang-ppt-skill** | 单文件HTML横向翻页PPT | 生成完整网页版演示文稿 |
| **pptx** / **pptx-swarm** | .pptx文件 | 生成标准PowerPoint文件 |

**典型配合使用**：
1. 用 `ppt-visual-designer` 生成高质量的封面图、章节图、概念图
2. 用 `pptx` 或 `guizang-ppt-skill` 生成完整的PPT结构
3. 将生成的图片插入到PPT中作为视觉资产
