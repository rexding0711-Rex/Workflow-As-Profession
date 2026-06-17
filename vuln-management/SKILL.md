---
name: vuln-management
description: >
  【漏洞管理】建立系统化的漏洞管理流程。从漏洞识别（扫描/众测/自主报告）、
  评估（CVSS 评分+业务上下文）、优先级排序、修复跟踪到验证闭环。
  对齐 CVSS v4.0、CVE/NVD、EPSS 等标准。
  当用户提及 vulnerability management、漏洞管理、漏洞扫描、CVE、
  CVSS、漏洞修复优先级、patch management 等关键词时触发。
  NOT for: 威胁建模（threat-modeling）、事件响应（incident-response）。
license: MIT
metadata: {version: 1.0.0, author: Workflow-As-Profession, category: cybersecurity, updated: 2026-06-17}
argument-hint: "<资产范围 + 当前漏洞管理痛点>"
---

# Vulnerability Management — 漏洞管理

每个公司都说"我们重视安全"，但问"你们现在有几个已知漏洞？SLA 是多少天修？"
大部分公司答不上来。漏洞管理不是跑个扫描出个报告，是从发现到修复到验证的闭环。

## 何时触发

用户提及：vulnerability management、漏洞管理、漏洞扫描、CVE、CVSS、
漏洞修复优先级、patch management、渗透测试 等关键词时触发。

## 漏洞管理生命周期

```
识别 → 评估 → 优先级 → 修复 → 验证 → 闭环
```

## 优先级公式

```
优先级 = CVSS 分数 × 业务影响 × 可利用性
```

### 修复 SLA

| 优先级 | CVSS | 修复 SLA | 示例 |
|--------|------|---------|------|
| P0-Critical | ≥9.0 + 有 PoC | 24h | Log4Shell、暴露在公网的 RCE |
| P1-High | 7.0-8.9 或 Critical 但有补偿控制 | 7 天 | 认证绕过、SQLi |
| P2-Medium | 4.0-6.9 | 30 天 | XSS（非特权上下文） |
| P3-Low | <4.0 | 90 天或下个 Release | 信息泄露（非敏感） |

### 例外处理
- 漏洞无法修复（遗留系统无补丁）→ 补偿控制（WAF 规则、网络隔离）
- 漏洞修复成本 > 风险 → 正式记录 Risk Acceptance，管理层签字

## 输出模板

```markdown
# 漏洞管理报告 — [日期]

## 当前状态
| | Critical | High | Medium | Low |
|---|---------|------|--------|-----|
| 未修复 | [N] | [N] | [N] | [N] |
| SLA 超期 | [N] | [N] | [N] | [N] |

## Top 5 需立即关注
| CVE | CVSS | 资产 | SLA | Owner | 状态 |
|-----|------|------|-----|-------|------|
| [CVE-XXXX] | [X] | [主机] | [日期] | [人] | [进度] |

## 趋势（本月）
- 新发现：[N] → 已修复：[N] → 存量：[N]（↑/↓/→）
```

## 质量原则
1. Critical 24h、High 7d ——做不到就别定这样的 SLA
2. 每周一次漏洞评审会（Security + Engineering + Product）
3. 漏洞不是"修完就完了"——要验证修复有效、没有引入新问题
