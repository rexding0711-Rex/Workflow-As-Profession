# Workflow-As-Profession

> **Workflow is profession.** 206 atomic AI skills · 14 industries · composable career workflows
>
> **工作流即职业。** 206 个原子化 AI 技能 · 14 个行业领域 · 可组合职业工作流

*[中文版本 ↓](#中文版本)*

---

## English

Traditional AI tools offer "general capability," but real work is "role-specific." An investment analyst and a sales director need completely different AI capabilities.

This project treats **the profession itself** as the orchestration unit: each workflow = one real career's complete AI operating manual, composed from atomic skills like Lego blocks.

### Three-Layer Architecture

```
┌──────────────────────────────────────────────┐
│  Products · Industry Solutions                 │
│  Finance suite · Marketing toolkit · etc.      │
│  (Packaging multiple workflows — planned)      │
├──────────────────────────────────────────────┤
│  Workflows · Career Workflows                  │
│  financial-analyst · sales-director · ...      │
│  Each workflow = 1 career's full AI playbook   │
│  (Design pattern — YAML: daily→projects→output)│
├──────────────────────────────────────────────┤
│  Skills · Atomic Skills — 206 ✅               │
│  /analyze · /modeling · /market-search · ...   │
│  Each skill = SKILL.md + references + scripts  │
└──────────────────────────────────────────────┘
```

### Atomic Skills (Current Core)

206 standalone skills. Each contains:
- **SKILL.md** — system prompt with trigger rules, execution flow, I/O spec
- **references/** — supplementary docs (optional)
- **scripts/** — Python/JS/Shell helpers (optional)

### Career Workflow (Design Pattern)

Each YAML workflow defines a profession's complete AI playbook:

```yaml
# Example: financial-analyst workflow
daily:                          # 3 tasks/day, ~30 min total
  - skill: /monitor             → Track financial data, budget, anomalies
  - skill: /new-info            → Scan industry reports, policy changes
  - skill: /mark                → Flag key assumptions, risk signals

projects:                       # Typical project patterns
  - name: "Financial Modeling"
    flow:
      - skill: /modeling        → 3-statement model
      - skill: /analyze         → Historical analysis
      - skill: /professional    → DuPont / ratio analysis
      - skill: /visual          → Visualization

skills: [/modeling, /analyze, /professional, /visual, /decide, ...]
output: [Financial model, Valuation, Investment memo, Presentation, ...]
```

### Industries Covered

| Industry | Example Roles | Key Skills |
|----------|-------------|------------|
| 💰 Finance | Financial Analyst, Portfolio Manager, Equity Researcher | `core-finance`, `equity-researcher`, `deal-analyzer` |
| 🔒 Cybersecurity | Security Analyst, CISO, Security Engineer | `incident-response`, `threat-modeling`, `security-policy-writer`, `vuln-management` |
| 📊 Consulting | Strategy Consultant, Management Consultant | `mba-decision`, `hypothesis-driven`, `issue-tree` |
| 📱 Product | Product Manager, Growth PM, Technical PM | `prd-writer`, `user-story-mapping`, `stakeholder-alignment`, `product-strategy` |
| 🔍 UX Research | UX Researcher, Design Strategist, UX Designer | `user-interview-guide`, `usability-testing`, `persona-builder`, `design-critique` |
| 📈 Marketing | Brand Manager, Growth Lead, Digital Marketing | `core-marketing`, `campaign-plan`, `seo-copywriting-guide` |
| 🏢 Management | Project Director, Team Lead, Dept Head | `core-strategy`, `change-management`, `org-design` |
| 💻 IT | Software Engineer, DevOps, Frontend | `code-safety-audit`, `k8s-cluster-ops`, `gitlab-cli-guide` |
| 📊 Data | Data Scientist, Data Engineer, BI Analyst | `data-driven`, `corr-insight`, `data-viz-gen` |
| ✍️ Creative | Content Creator, Copywriter, Video Producer | `content-engine`, `ad-creative`, `short-video-script` |
| ⚙️ Operations | Ops Manager, Supply Chain, Project Manager | `core-operations`, `operations-lean`, `process` |
| 🎓 Education | Teacher, Professor, Corporate Trainer | `case-methodology`, `learn`, `programming-tutor` |
| 🏥 Healthcare | Doctor, Pharmacist, Medical Researcher | `scientific-problem-selection`, `paper-writing` |
| ⚖️ Legal | Lawyer, Paralegal, Compliance Officer | `legal-contract-gen`, `compliance-review-planner` |
| 🏗️ Admin | Knowledge Manager, Project Assistant | `meeting-to-action`, `doc-summary`, `daily-report` |
| 👥 HR | HRBP, Recruiter, People Ops Manager | `jd-writer`, `structured-interview`, `performance-review`, `employee-relations`, `onboarding-design`, `people-analytics` |
| 🤝 Customer Success | CSM, Onboarding Manager, Renewal Manager | `customer-health-score`, `qbr-narrative`, `escalation-playbook`, `renewal-strategy` |
| 🏭 Industrial Sales | Tier 2 Materials Sales, Sales Engineer, BD Manager | `industrial-sales-cycle`, `rfq-response`, `technical-spec-sell`, `supply-chain-value-prop` |
| 🛒 Sales | Sales Director, Account Manager | `sales`, `crm`, `negotiate` |
| 🚚 Supply Chain | Supply Chain Manager, Procurement, Logistics | `supply-chain-risk`, `inventory-optimization`, `supplier-scorecard`, `logistics-planning` |
| 🔧 Meta | Skill Creator, Batch Orchestrator, Reviewer | `skill-creator`, `create-all`, `review-all` |

### Design Principles

1. **Profession as Workflow** — Give AI a *career identity*, not a generic tool. Each workflow defines what a profession does, how, and what it outputs.
2. **Skills Compose** — Atomic skills are Lego blocks. A career uses 10–15 skills, but skills are reusable across careers.
3. **Explicit Mismatch** — AI must *flag mismatches* in output. Better to say "this doesn't fit" than to force a wrong answer.
4. **Data Assets > AI Interactions** — The most valuable layer is structured knowledge, industry templates, and analytical frameworks — not the conversation.

### Audit Status

✅ **Three-method audit passed** (2026-06-17)  
✅ Security: zero hardcoded keys, dangerous functions documented  
✅ Compliance: 100% MIT LICENSE coverage, 100% YAML front matter  
✅ Content quality: broken references fixed, format standardized  

Full report: [AUDIT_REPORT.md](AUDIT_REPORT.md)

### Quick Start

**Use a single skill:**
1. Find the skill under `skills/`
2. Load `SKILL.md` as system prompt into your AI agent
3. Provide `references/` as context when needed
4. Review and run `scripts/` locally if applicable

**Orchestrate a career workflow:**
1. Define workflow structure using the YAML pattern above
2. Pick 10–15 skills from the 206 available
3. Organize as daily → projects → output
4. AI executes daily tasks and projects per the workflow definition

### Directory Structure

```
.
├── README.md
├── LICENSE                    # MIT
├── AUDIT_REPORT.md            # Three-method audit report
├── .gitignore
│
└── skills/                    # 206 atomic skills
    ├── skill-name/
    │   ├── SKILL.md           # Core prompt (required)
    │   ├── LICENSE            # MIT
    │   ├── scripts/           # Python/JS/Shell (optional)
    │   ├── references/        # Reference docs (optional)
    │   └── assets/            # Assets (optional)
    └── ...
```

### Contributing

**Adding a new skill:**
1. Create `skills/{skill-name}/` directory
2. Write `SKILL.md` with YAML front matter (`name`, `description`)
3. Include MIT `LICENSE` file
4. Optionally add `references/`, `scripts/`, `assets/`

**Skill standards:**
- SKILL.md starts with `---` YAML front matter
- Description clearly states trigger conditions and use cases
- Scripts must include docstrings / comments
- All file references must resolve

### License

MIT — Free to use, modify, distribute, and use commercially. See [LICENSE](LICENSE)

---

## 中文版本

传统 AI 工具提供「通用能力」，但真实工作场景是「职业特定」。投资分析师和销售总监需要的 AI 能力完全不同。

本项目把 **职业本身** 作为编排单元：每个工作流 = 一个真实职业的完整 AI 操作手册，由原子技能像乐高积木一样组合而成。

### 三层架构

```
┌──────────────────────────────────────────────┐
│  Products · 行业产品                           │
│  金融分析套件 · 营销增长工具包 · 合规审查系统     │
│  （将多个工作流打包为行业解决方案 — 规划中）       │
├──────────────────────────────────────────────┤
│  Workflows · 职业工作流                        │
│  financial-analyst · sales-director · ...     │
│  每个工作流 = 1 个职业的完整 AI 操作手册         │
│  （设计模式 — YAML 定义 daily→projects→output）  │
├──────────────────────────────────────────────┤
│  Skills · 原子技能 — 206 个 ✅                 │
│  /analyze · /modeling · /market-search · ...  │
│  每个 skill = 1 个 SKILL.md + references + scripts │
└──────────────────────────────────────────────┘
```

### 原子技能层（当前核心）

206 个独立技能，每个包含：
- **SKILL.md** — 系统提示词，含触发规则、执行流程、输入/输出规范
- **references/** — 参考文档（可选）
- **scripts/** — 配套脚本，Python/JS/Shell（可选）

### 职业工作流层（设计模式）

每个 YAML 工作流定义一个职业的完整 AI 操作手册：

```yaml
# 示例：financial-analyst 工作流
daily:                          # 每日 3 任务，共约 30 分钟
  - skill: /monitor             → 跟踪财务数据、预算执行、异常指标
  - skill: /new-info            → 扫描行业财报、政策变化
  - skill: /mark                → 标记关键假设、数据变化、风险信号

projects:                       # 典型项目模式
  - name: "财务建模"
    flow:
      - skill: /modeling        → 三表模型（利润/资产负债/现金流）
      - skill: /analyze         → 历史财务分析（同比/环比/结构）
      - skill: /professional    → 杜邦分析/财务指标分析
      - skill: /visual          → 财务可视化

skills: [/modeling, /analyze, /professional, /visual, /decide, ...]
output: [财务模型, 估值模型, 投资建议, 汇报材料, ...]
```

### 覆盖行业

| 行业 | 示例职业 | 相关技能 |
|------|---------|---------|
| 💰 金融 | 财务分析师、投资经理、股票研究员 | `core-finance`, `equity-researcher`, `deal-analyzer` |
| 🔒 网络安全 | 安全分析师、CISO、安全工程师 | `incident-response`, `threat-modeling`, `security-policy-writer`, `vuln-management` |
| 📊 咨询 | 战略顾问、管理顾问、IT 顾问 | `mba-decision`, `hypothesis-driven`, `issue-tree` |
| 📱 产品 | 产品经理、增长 PM、技术 PM | `prd-writer`, `user-story-mapping`, `stakeholder-alignment`, `product-strategy` |
| 🔍 用户体验 | UX 研究员、设计策略师、UX 设计师 | `user-interview-guide`, `usability-testing`, `persona-builder`, `design-critique` |
| 📈 营销 | 品牌经理、数字营销、增长负责人 | `core-marketing`, `campaign-plan`, `seo-copywriting-guide` |
| 🏢 管理 | 项目总监、团队负责人、部门主管 | `core-strategy`, `change-management`, `org-design` |
| 💻 IT | 软件工程师、DevOps、前端开发 | `code-safety-audit`, `k8s-cluster-ops`, `gitlab-cli-guide` |
| 📊 数据 | 数据科学家、数据工程师、商业分析师 | `data-driven`, `corr-insight`, `data-viz-gen` |
| ✍️ 创意 | 内容创作者、文案、视频制作 | `content-engine`, `ad-creative`, `short-video-script` |
| ⚙️ 运营 | 运营经理、供应链、项目经理 | `core-operations`, `operations-lean`, `process` |
| 🎓 教育 | 教师、教授、企业培训师 | `case-methodology`, `learn`, `programming-tutor` |
| 🏥 医疗 | 医生、药剂师、医学研究员 | `scientific-problem-selection`, `paper-writing` |
| ⚖️ 法律 | 律师、法务、合规官 | `legal-contract-gen`, `compliance-review-planner` |
| 🏗️ 行政 | 知识管理、项目助理 | `meeting-to-action`, `doc-summary`, `daily-report` |
| 👥 人力资源 | HRBP、招聘经理、People Operations | `jd-writer`, `structured-interview`, `performance-review`, `employee-relations`, `onboarding-design`, `people-analytics` |
| 🤝 客户成功 | CSM、Onboarding Manager、续约经理 | `customer-health-score`, `qbr-narrative`, `escalation-playbook`, `renewal-strategy` |
| 🏭 工业品销售 | Tier 2 材料销售、销售工程师、业务拓展 | `industrial-sales-cycle`, `rfq-response`, `technical-spec-sell`, `supply-chain-value-prop` |
| 🛒 销售 | 销售总监、客户经理 | `sales`, `crm`, `negotiate` |
| 🚚 供应链 | 供应链经理、采购、物流 | `supply-chain-risk`, `inventory-optimization`, `supplier-scorecard`, `logistics-planning` |
| 🔧 元技能 | 技能创建、批量编排、审查 | `skill-creator`, `create-all`, `review-all` |

### 设计理念

1. **职业即工作流** — 不是给 AI 一个通用工具，而是给 AI 一个**职业身份**。每个工作流定义了一个职业应该做什么、怎么做、输出什么。
2. **技能可组合** — 原子技能像乐高积木，可以组合成任意工作流。一个职业需要 10–15 个技能，但这些技能可以跨职业复用。
3. **显式不匹配** — AI 输出时**显式标注不匹配参数**，确保用户知道哪里对不上。宁可不做，不要瞎做。
4. **数据资产 > AI 交互** — 最值钱的不是 AI 对话层，而是底层的结构化知识、行业模板和分析框架。

### 审计状态

✅ **三方法全面审计通过**（2026-06-17）  
✅ 安全审计：零硬编码密钥，危险函数已标注  
✅ 结构合规：100% MIT LICENSE 覆盖，100% YAML front matter  
✅ 内容质量：断裂引用已修复，格式规范统一  

完整报告：[AUDIT_REPORT.md](AUDIT_REPORT.md)

### 快速开始

**使用单个技能：**
1. 在 `skills/` 中找到需要的技能目录
2. 将 `SKILL.md` 的内容作为系统提示词加载到 AI Agent
3. 如有 `references/`，按需提供为上下文
4. 如有 `scripts/`，审查后在本地执行

**编排职业工作流：**
1. 参考上方 YAML 示例定义工作流结构
2. 从 206 个原子技能中选取 10–15 个
3. 按 daily → projects → output 组织
4. AI 按工作流定义自动执行日常任务和项目

### 目录结构

```
.
├── README.md
├── LICENSE                    # MIT 许可证
├── AUDIT_REPORT.md            # 三方法审计报告
├── .gitignore
│
└── skills/                    # 206 原子技能
    ├── skill-name/
    │   ├── SKILL.md           # 核心提示词（必需）
    │   ├── LICENSE            # MIT 许可证
    │   ├── scripts/           # 可选脚本（Python/JS/Shell）
    │   ├── references/        # 可选参考文档
    │   └── assets/            # 可选资源文件
    └── ...
```

### 贡献指南

**添加新技能：**
1. 创建 `skills/{skill-name}/` 目录
2. 编写 `SKILL.md`（必须含 YAML front matter：`name`、`description`）
3. 添加 MIT `LICENSE` 文件
4. 可选：`references/`、`scripts/`、`assets/`

**技能规范：**
- SKILL.md 首行为 `---`，含 YAML front matter
- 描述清晰说明触发条件和使用场景
- 脚本必须有文档注释
- 引用文件确保路径存在

### 许可证

MIT — 自由使用、修改、分发、商用。详见 [LICENSE](LICENSE)
