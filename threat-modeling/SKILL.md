---
name: threat-modeling
description: >
  【威胁建模】用 STRIDE、攻击树、Kill Chain 等方法系统化识别系统威胁。
  回答四个问题：我们在构建什么？什么会出错？我们该怎么做？我们做对了吗？
  覆盖 STRIDE-per-element、攻击面分析、风险矩阵（Likelihood×Impact）。
  当用户提及 threat modeling、威胁建模、STRIDE、攻击树、attack surface、
  安全设计、security design review 等关键词时触发。
  NOT for: 事件响应（用 incident-response）、漏洞管理（用 vuln-management）。
license: MIT
metadata: {version: 1.0.0, author: Workflow-As-Profession, category: cybersecurity, updated: 2026-06-17}
argument-hint: "<要建模的系统/功能 + 数据流图>"
---

# Threat Modeling — 威胁建模

不要等到被黑了才开始想"我们哪里不安全"。威胁建模是在设计和开发阶段系统化地找"什么会出错"，
在攻击者找到漏洞之前先找到。

## 四问框架

1. **我们在构建什么？** — 画 Data Flow Diagram
2. **什么会出错？** — 用 STRIDE 找威胁
3. **我们该怎么做？** — 评估风险 + 缓解方案
4. **我们做对了吗？** — 验证缓解措施有效

## STRIDE-per-element

| DFD 元素 | 威胁（STRIDE） |
|---------|--------------|
| External Entity | Spoofing（假冒身份） |
| Process | Tampering（篡改）、Repudiation（抵赖）、Elevation of Privilege（提权） |
| Data Flow | Information Disclosure（信息泄露）、Denial of Service（拒绝服务） |
| Data Store | Tampering、Information Disclosure、DoS |

## 风险矩阵

```
影响 →     低      中      高
可能性 ↓
高        中风险   高风险  🔴严重
中        低风险   中风险  高风险
低        🟢可接受  低风险  中风险
```

## 输出模板

```markdown
# [系统/功能] — 威胁模型

## DFD（数据流图描述）
[外部实体→进程→数据存储→数据流]

## 威胁清单

| ID | 威胁 | STRIDE 类型 | 可能性 | 影响 | 风险 | 缓解 |
|----|------|-----------|--------|------|------|------|
| T1 | [描述] | [S/T/R/I/D/E] | H/M/L | H/M/L | 🔴/🟡/🟢 | [方案] |

## 未缓解的严重风险
[列出 🔴 且无缓解方案的威胁 → 必须修复]
```

## 质量原则
1. 每个 DFD 元素至少有一个对应的 STRIDE 检查
2. 高风险 + 无缓解 = Launch Blocker
3. 威胁模型是活文档，系统改了模型要更新
