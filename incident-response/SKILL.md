---
name: incident-response
description: >
  【安全事件响应】构建和管理安全事件响应流程。从事件分级（Severity 1-4）、
  IR Playbook 设计、War Room 运行到事后复盘（Postmortem），
  覆盖检测→遏制→根除→恢复→复盘全过程。含 NIST SP 800-61 对齐框架。
  当用户提及 incident response、安全事件、安全应急、breach、数据泄露、
  IR playbook、war room、postmortem 等关键词时触发。
  NOT for: 威胁建模（用 threat-modeling）、漏洞管理（用 vuln-management）。
license: MIT
metadata: {version: 1.0.0, author: Workflow-As-Profession, category: cybersecurity, updated: 2026-06-17}
argument-hint: "<事件描述 + 受影响系统>"
---

# Incident Response — 安全事件响应

安全事件不是"会不会发生"，是"什么时候发生"。好的 IR 不是出了事手忙脚乱，
是每个人都知道自己的角色、知道第一件事做什么、知道谁该联系、知道复盘不是为了甩锅。

## 何时触发

用户提及：incident response、安全事件、安全应急、breach、数据泄露、IR playbook、
cyber incident、安全攻击、勒索软件、DDoS 等关键词时触发。

**排除：** 威胁建模→threat-modeling；漏洞管理→vuln-management。

## IR 生命周期（NIST 对齐）

```
准备 → 检测&分析 → 遏制&根除&恢复 → 事后复盘
```

### Severity 分级

| 等级 | 定义 | 响应时间 | 升级到 |
|------|------|---------|--------|
| S1-Critical | 生产数据泄露、客户数据外泄 | 15 min | CISO+CEO |
| S2-High | 内部系统被入侵、恶意软件爆发 | 30 min | CISO |
| S3-Medium | 单台机器异常、可疑登录 | 2 h | Security Team Lead |
| S4-Low | 钓鱼邮件未遂、常规告警 | 24 h | 值班工程师 |

### War Room 运行规则
- 指定 Incident Commander（不是官最大的，是最了解系统的）
- Scribe 全程记录时间线
- 每 30 min 对外沟通一次更新
- 禁止在 War Room 里甩锅

## 输出模板

```markdown
# IR Postmortem — [事件名] | [日期]

## 时间线
| 时间 | 事件 |
|------|------|
| [时间] | 首次检测 |
| [时间] | 确认为 S[X] 并升级 |
| [时间] | 遏制完成 |
| [时间] | 根除 |
| [时间] | 恢复 |

## 根因（5 Whys）
[至少问 5 次为什么]

## 改进措施
| # | 措施 | 负责人 | 截止 |
|---|------|--------|------|
| 1 | [系统修复] | [人] | [日期] |
| 2 | [流程改进] | [人] | [日期] |
```

## 质量原则
1. 检测到→15min 内确认→分级→通知
2. 复盘找系统问题不找替罪羊
3. 每个改进措施有 owner 和 deadline
4. S1/S2 必须 72h 内完成复盘
