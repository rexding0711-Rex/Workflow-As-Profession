# 元能力图谱（Meta-Skill Landscape）

> 最后更新：2026-06-16  
> 用途：定义 Flow 编排系统中所有原子能力的分类、边界和相互关系  
> 读者：开发这个系统的你 + 将来任何想理解这个架构的人

---

## 架构总览

```
                         ┌──────────────────┐
                         │   Flow 编排引擎    │
                         │  223 职业 × 18 行业 │
                         └────────┬─────────┘
                                  │ 组装调用
          ┌───────────────────────┼───────────────────────┐
          │                       │                       │
    ┌─────▼─────┐          ┌─────▼─────┐          ┌─────▼─────┐
    │  感知层    │    →     │  分析层    │    →     │  设计层    │
    │  6 个能力  │          │  9 个能力  │          │  5 个能力  │
    └───────────┘          └───────────┘          └───────────┘
          │                       │                       │
    ┌─────▼─────┐          ┌─────▼─────┐          ┌─────▼─────┐
    │  创作层    │    →     │  执行层    │    →     │  反思层    │
    │  8 个能力  │          │  10 个能力 │          │  4 个能力  │
    └───────────┘          └───────────┘          └───────────┘
                                  │
                          ┌───────▼───────┐
                          │   协作层       │
                          │   4 个能力     │
                          └───────────────┘
```

**7 层、46 个元能力**。每一层的能力可以独立调用，也可以按职业 SOP 链式组装。

---

## Layer 1：感知层（Sensing）

> 收集信息、感知环境、扫描信号。输入驱动。

| # | 元技能 | Skill 目录 | 核心问题 | 典型产出 |
|---|--------|-----------|---------|---------|
| 1 | `/monitor` | monitor-all | "发生了什么变化？" | 监测摘要、异常提醒 |
| 2 | `/new-info` | new-info | "有什么新情报？" | 情报简报 |
| 3 | `/market-search` | market-search | "市场是什么样的？" | 细分市场画像、TAM/SAM/SOM |
| 4 | `/user-research` | user-research | "用户需要什么？" | 用户画像、旅程地图 |
| 5 | `/quick` | quick-check | "这个值不值得深挖？" | 快速判断、下一步建议 |
| 6 | `/learn` | learn | "我怎么快速搞懂？" | 认知框架、学习路径 |

---

## Layer 2：分析层（Analysis）

> 理解本质、拆解问题、诊断根因。信号 → 洞察。

| # | 元技能 | Skill 目录 | 核心问题 | 典型产出 |
|---|--------|-----------|---------|---------|
| 7 | `/analyze` | analyze-all | "数据/事实说明了什么？" | 分析报告、洞察 |
| 8 | `/professional` | professional | "多维度综合怎么看？" | 专业分析报告 |
| 9 | `/dd` | due-diligence | "有没有隐藏问题？" | 尽调报告、风险清单 |
| 10 | `/tech-compare` | tech-compare | "技术路线怎么选？" | 参数对比矩阵 |
| 11 | `/benchmarking` | benchmarking | "和最好的差在哪？" | 对标分析 |
| 12 | `/industry-analysis` | industry-analysis | "行业怎么玩？" | 行业速写 |
| 13 | `/hypothesis-driven` | hypothesis-driven | "先猜一个方向？" | 假设验证报告 |
| 14 | `/issue-tree` | issue-tree | "怎么拆成小问题？" | 问题树 |
| 15 | `/mece-framework` | mece-framework | "逻辑有没有遗漏？" | MECE 检查 |

---

## Layer 3：设计层（Design）

> 构思方案、建模预测、制定策略。洞察 → 方案。

| # | 元技能 | Skill 目录 | 核心问题 | 典型产出 |
|---|--------|-----------|---------|---------|
| 16 | `/design` | design | "怎么设计？" | 设计规范、原型 |
| 17 | `/modeling` | modeling | "数字怎么算？" | 财务模型、敏感性分析 |
| 18 | `/process` | process | "流程怎么走？" | SOP、流程图 |
| 19 | `/policy` | policy | "政策有什么影响？" | 影响矩阵、应对建议 |
| 20 | `/pricing` | pricing | "定什么价？" | 定价方案、价格带 |

---

## Layer 4：创作层（Creation）

> 产出内容、生成文档、可视化呈现。方案 → 交付物。

| # | 元技能 | Skill 目录 | 核心问题 | 典型产出 |
|---|--------|-----------|---------|---------|
| 21 | `/create` | create-all | "怎么写出来？" | 文档、报告、文案 |
| 22 | `/pitch` | pitch | "怎么汇报？" | PPT大纲、演讲稿 |
| 23 | `/tech-article` | tech-article | "技术文章怎么写？" | 技术解析文章 |
| 24 | `/visual` | visual | "数据怎么好看？" | 图表、可视化方案 |
| 25 | `/format` | data-formatter | "数据怎么整？" | 结构化数据表 |
| 26 | `/summary` | doc-summary | "长文怎么浓缩？" | 1页核心摘要 |
| 27 | `/geo` | content-engine | "GEO内容怎么排？" | 内容矩阵、发布日历 |
| 28 | `/plan` | plan-on-the-spot | "计划怎么出？" | 快速计划书 |

---

## Layer 5：执行层（Execution）

> 推动落地、管理关系、完成交易。方案 → 结果。

| # | 元技能 | Skill 目录 | 核心问题 | 典型产出 |
|---|--------|-----------|---------|---------|
| 29 | `/execute` | execute-all | "怎么推下去？" | 执行计划、进度追踪 |
| 30 | `/sales` | sales | "怎么卖？" | 销售提案、谈判策略 |
| 31 | `/deal` | deal-analyzer | "条款怎么审？" | 红旗条款、谈判建议 |
| 32 | `/negotiate` | negotiate | "怎么谈？" | 谈判策略、话术 |
| 33 | `/crm` | crm | "客户怎么管？" | 客户管理视图 |
| 34 | `/network` | network | "人脉怎么维护？" | 关系维护计划 |
| 35 | `/sourcing` | sourcing | "供应商哪里找？" | 供应商短名单、RFQ |
| 36 | `/event-manager` | event-manager | "活动怎么搞？" | 活动方案、执行清单 |
| 37 | `/social-media` | social-media | "社媒怎么发？" | 内容日历、分发计划 |
| 38 | `/mark` | mark | "重点怎么记？" | 结构化标签 |

---

## Layer 6：协作层（Collaboration）

> 引导群体、促进共识、传递知识。个体 → 群体。

| # | 元技能 | Skill 目录 | 核心问题 | 典型产出 |
|---|--------|-----------|---------|---------|
| 39 | `/workshop` | workshop | "怎么引导一群人？" | 工作坊方案、产出记录 |
| 40 | `/meeting` | meeting-to-action | "会议怎么变行动？" | 会议纪要、行动清单 |
| 41 | `/interview` | interview-simulator | "怎么问出东西？" | 访谈记录、洞察 |
| 42 | `/patent` | patent | "专利怎么布局？" | 专利地图、FTO报告 |

---

## Layer 7：反思层（Reflection）

> 复盘沉淀、决策判断、持续改进。结果 → 学习。

| # | 元技能 | Skill 目录 | 核心问题 | 典型产出 |
|---|--------|-----------|---------|---------|
| 43 | `/review` | review-all | "学到了什么？" | 复盘报告、改进措施 |
| 44 | `/decide` | decide-all | "该怎么选？" | 决策建议、风险分析 |
| 45 | `/experiment` | experiment | "怎么试？" | 实验方案、结果分析 |
| 46 | `/storyline-pyramid` | storyline-pyramid | "故事怎么讲？" | 金字塔结构汇报 |

---

## 能力关系图

```
感知层 ──→ 分析层 ──→ 设计层 ──→ 创作层 ──→ 执行层
  │           │           │           │           │
  │   /monitor → /analyze → /modeling → /pitch  → /execute
  │   /new-info→ /dd      → /process → /create  → /sales
  │   /market  → /issue   → /pricing → /visual  → /deal
  │   /user    → /bench   → /policy  → /format  → /negotiate
  │   /quick   → /industry→ /design  → /summary → /crm
  │   /learn   → /hypo    │           → /geo     → /network
  │             → /mece   │           → /plan    → /sourcing
  │             → /prof   │           → /tech    → /event
  │                       │                      → /social
  │                       │                      → /mark
  │                       │
  └─────────────── 协作层 ───────────────────────┘
                  /workshop  /meeting  /interview  /patent
                              │
                         反思层 ←────────────────┘
                  /review  /decide  /experiment  /storyline
```

**典型链式调用示例**：
```
/monitor → /analyze → /professional → /pitch → /execute → /review
 感知      分析         综合           汇报       执行       复盘

/market-search → /issue-tree → /hypothesis-driven → /decide → /create
 市场扫描         问题拆解        假设验证             决策       产出
```

---

## 覆盖热度（223 个 YAML 中的引用频次）

### 🔥 高频（>100 次引用）—— 核心中的核心

| 元技能 | 近似引用数 | 说明 |
|--------|-----------|------|
| `/analyze` | ~180 | 几乎每个职业都需要 |
| `/create` | ~160 | 产出文档/方案 |
| `/execute` | ~150 | 执行推进 |
| `/review` | ~120 | 复盘改进 |

### ⭐ 中频（40-100 次）

| 元技能 | 说明 |
|--------|------|
| `/monitor` / `/mark` / `/new-info` | 日常三件套 |
| `/pitch` / `/professional` | 汇报与分析 |
| `/process` / `/plan` / `/decide` | 流程、计划、决策 |
| `/workshop` (51) | 工作坊引导 |

### 📌 低频但关键（<40 次）

某些行业特化能力强引用少但不可或缺：
- `/patent` (2 个职业引用，但 CTO/R&D 没有它就断了)
- `/dd` (尽调，M&A/投资/合规必需)
- `/tech-compare` (技术密集型行业必需)
- `/negotiate` (11 个职业引用，集中在法律/销售)
- `/sourcing` (采购/运营必需)

---

## 已知缺口（待建设）

### 能力空白

| 缺口 | 影响职业数 | 建议 |
|------|-----------|------|
| 编程/开发 | IT 类 21 个职业 | 可能需要 `/code` 元技能（但 code-arch-optimizer 等已存在，需评估是否抽象为元技能） |
| 医疗临床 | healthcare 18 个职业 | 专业壁垒高，目前由 `/analyze + /professional` 拼凑，可能不够 |
| 金融合规 | finance + legal | `/compliance` 可以独立为一个元技能（合规审查是高频需求） |
| 供应链物流 | operations | `/logistics` 在 YAML 中作为项目出现但未抽象为独立元技能 |

### 目录空白

| 目录 | 状态 |
|------|------|
| `digital/` | 🚧 空目录，需要补充数字营销/数字化转型类职业 |
| `supply/` | 🚧 空目录，需要补充供应链专业类职业（与 operations 有重叠，需明确边界） |

---

## 设计原则

1. **原子性**：每个元技能做一件事且只做一件事。`/analyze` 不管怎么写报告，`/create` 不管怎么分析
2. **可组合**：元技能之间通过「输入→输出」链接，前一个的输出是后一个的输入
3. **最小完备**：不在元技能数量上追求多，在"覆盖所有职业 SOP 的最小集合"上追求全
4. **Flow 层不创造能力**：如果 YAML 需要的元技能不存在，优先创建元技能，而不是在 Flow 层特殊处理
5. **名字即约定**：YAML 中的 `/xxx` 引用 = daimon 目录下的 `xxx/` 或映射表中的别名

---

## 版本历史

| 日期 | 变更 |
|------|------|
| 2026-06-16 | 初始版本：7 层 46 个元能力，补全 6 个幽灵技能（workshop/negotiate/event-manager/patent/social-media/sourcing），修复 /graph → graph-builder 引用 |
