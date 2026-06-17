---
name: flow
description: >
  【流程编排引擎】根据用户职业自动加载对应的 SOP YAML，将元能力（analyze/create/review/decide 等）
  按职业 SOP 组装为工作流。当用户说"我是XX职业"、"帮我按XX流程做"、"XX岗位的日常工作怎么搞"
  或提及任何职业/岗位名称时触发。也支持英文关键词：flow, workflow, SOP, profession, role, orchestrate。
  覆盖 16 个行业分类、254 个职业的完整工作流定义。
---

# Flow — 元能力编排引擎

## 架构

三层设计，自上而下：

```
Flow 层（本 Skill）    →  根据职业匹配 YAML，组装 SOP
元能力层（元 Skills）   →  /analyze  /create  /review  /decide  /execute  /monitor  ...
YAML 定义层             →  references/workflows/{行业}/{职业}.yaml（223 个职业 SOP）
```

**核心逻辑：每个职业 = 一组元能力的特定排列组合。**  
Flow 不创造新能力，只编排已有元能力。YAML 是职业的骨架，元能力是肌肉。

---

## 触发条件

以下任一情况，进入 Flow 编排逻辑：

- 用户自报职业："我是管理顾问/财务分析师/BD/产品经理/..."
- 用户描述岗位任务："帮我做组织诊断"、"做一轮尽调"、"出个估值模型"
- 用户想建立工作流："帮我把XX岗位的日常工作流程化"
- 用户不知道用什么 Skill："我有一个XX问题，该用什么流程"
- 关键词：`flow` `工作流` `SOP` `流程` `职业` `岗位` `日常工作`

---

## 工作流

### Step 1：识别职业 → 匹配 YAML

从用户输入中提取职业/岗位名称，在 `references/workflows/` 下匹配最相关的 YAML。

18 个行业分类目录：

| 目录 | 行业 | 职业数 |
|------|------|--------|
| `admin` | 行政管理 | 18 |
| `consulting` | 咨询 | 15 |
| `creative` | 创意/设计 | 16 |
| `data` | 数据 | 16 |
| `digital` | 数字化 | 16 |
| `education` | 教育 | 18 |
| `finance` | 金融 | 13 |
| `healthcare` | 医疗健康 | 18 |
| `it` | 信息技术 | 21 |
| `legal` | 法律 | 20 |
| `management` | 管理 | 17 |
| `marketing` | 市场营销 | 10 |
| `operations` | 运营/供应链 | 21 |
| `product` | 产品 | 10 |
| `sales` | 销售 | 10 |
| `supply` | 供应链 | 15 |

如果用户职业不在已有 YAML 中：
- 告知用户暂无该职业的预定义 SOP
- 询问是否用 `/professional`（通用专业分析）代替
- 或帮用户基于相近职业 YAML 现场定制

### Step 2：加载 YAML → 展示 SOP 骨架

读取匹配到的 YAML，向用户展示该职业的 SOP 结构：

```
📋 {职业名称} 工作流

🔄 日常（Daily）：
  /monitor → 跟踪监控（15min）
  /new-info → 情报扫描（10min）
  /mark → 标记重点（5min）

📦 项目（Projects）：
  1. 财务建模（3-4天）
     /modeling → /analyze → /professional → /visual
  2. 估值分析（2-3天）
     /modeling → /analyze → /decide
  ...
```

### Step 3：按 SOP 执行

根据用户需求，分两种模式执行：

**日常模式** — 用户说"帮我做今天的日常"：
- 按 YAML `daily` 字段，依次调用每个元技能
- 每个 skill 结束后汇报结果，再进入下一个
- 总时长控制在 YAML 定义的时间范围内

**项目模式** — 用户说"帮我做XX项目"：
- 匹配 YAML `projects` 中的项目名
- 按 `flow` 字段定义的步骤链式执行
- 每一步的输出是下一步的输入
- 标注每步预估耗时，执行前确认

### Step 4：交付物归档

按 YAML `output` 字段整理交付物清单，生成结构化摘要。

---

## YAML 字段说明

每个职业 YAML 包含以下字段：

```yaml
name: 职业标识符
description: 一句话描述该工作流

daily:                    # 日常例行（每天或高频）
  - skill: /xxx           # 元技能名称
    trigger: "触发条件"    # 什么时候执行
    output: "产出物"       # 产出什么
    time: "耗时"           # 预估时间

projects:                 # 项目级工作流
  - name: "项目名"
    flow:
      - skill: /xxx       # 链式步骤
        step: "第N步描述"
        output: "产出物"
        time: "耗时"
    total: "项目总耗时"

skills:                   # 该职业使用的全部元技能清单
  - /xxx

output:                   # 该职业的全部产出物清单
  - "产出物名"
```

---

## 已注册元技能对照表

YAML 中引用的元技能与 daimon skills 目录中的实际 Skill 对应：

| YAML 引用 | 元 Skill | 能力类型 |
|-----------|----------|---------|
| `/analyze` | analyze-all | 数据分析/诊断 |
| `/create` | create-all | 内容/文档生成 |
| `/review` | review-all | 复盘/沉淀 |
| `/decide` | decide-all | 决策支持 |
| `/execute` | execute-all | 执行推进 |
| `/monitor` | monitor-all | 信息监测 |
| `/mark` | mark | 知识标记 |
| `/quick` | quick-check | 快速筛选 |
| `/professional` | professional | 专业分析 |
| `/new-info` | new-info | 实时情报 |
| `/dd` | due-diligence | 深度尽调 |
| `/pitch` | pitch | 汇报生成 |
| `/modeling` | modeling | 财务建模 |
| `/plan` | plan-on-the-spot | 快速计划 |
| `/process` | process | 流程设计 |
| `/policy` | policy | 政策分析 |
| `/pricing` | pricing | 定价策略 |
| `/sales` | sales | B2B销售 |
| `/deal` | deal-analyzer | 交易条款审查 |
| `/design` | design | UI/UX设计 |
| `/visual` | visual | 报告可视化 |
| `/market-search` | market-search | 市场搜索 |
| `/user-research` | user-research | 用户研究 |
| `/graph` | graph-builder | 产业链图谱 |
| `/network` | network | 人脉网络 |
| `/crm` | crm | 客户关系 |
| `/learn` | learn | 快速学习 |
| `/experiment` | experiment | 增长实验 |
| `/format` | data-formatter | 数据格式化 |
| `/tech-compare` | tech-compare | 技术对比 |
| `/tech-article` | tech-article | 技术文章 |
| `/summary` | doc-summary | 长文档摘要 |
| `/interview` | interview-simulator | 访谈模拟 |
| `/workshop` | workshop | 工作坊引导 |
| `/meeting` | meeting-to-action | 会议转行动 |
| `/geo` | content-engine | GEO内容引擎 |
| `/social-media` | social-media | 社媒运营 |
| `/sourcing` | sourcing | 寻源采购 |
| `/negotiate` | negotiate | 谈判 |
| `/patent` | patent | 专利分析 |
| `/event-manager` | event-manager | 活动管理 |

---

## 核心规则

1. **Flow 不创造新能力** — 只编排已有元技能，不做元技能做不到的事
2. **YAML 是单一真相源** — 职业 SOP 以 YAML 为准，不凭空编造步骤
3. **链式执行** — 项目模式下，前一步的输出是后一步的输入，不能跳步
4. **时间感知** — 执行前告知预估耗时，执行中用 `/mark` 记录关键节点
5. **兜底** — 如果职业无匹配 YAML，用 `/professional` 通用分析替代，不要拒绝用户

---

## 与单个元技能的关系

当用户直接说"帮我分析一下这个数据" → 走 `/analyze`（analyze-all），不走 Flow。  
当用户说"我是数据分析师，帮我搭日常工作流" → 走 Flow，加载 `data/data-analyst.yaml`，组装 `/analyze + /visual + /monitor + ...`。

**一句话：Flow 管「怎么组合」，元技能管「具体做什么」。**
