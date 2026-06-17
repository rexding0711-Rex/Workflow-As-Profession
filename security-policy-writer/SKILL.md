---
name: security-policy-writer
description: >
  【安全策略撰写】撰写信息安全策略、标准和流程文档。
  从信息安全管理体系（ISMS）框架到具体的安全 SOP，
  覆盖 ISO 27001/SOC 2 对齐、可接受使用策略、访问控制策略、
  数据分类策略、供应商安全评估。当用户提及 security policy、安全策略、
  信息安全管理制度、ISO 27001、SOC 2、合规文档 等关键词时触发。
  NOT for: 威胁建模（threat-modeling）、事件响应（incident-response）。
license: MIT
metadata: {version: 1.0.0, author: Workflow-As-Profession, category: cybersecurity, updated: 2026-06-17}
argument-hint: "<策略类型 + 适用组织规模 + 合规要求>"
---

# Security Policy Writer — 安全策略撰写

安全策略不是"有了就行"的文档。好的策略让员工知道"该做什么、不该做什么、
为什么"，差的策略只是塞在 Confluence 里吃灰的 PDF。

## 何时触发

用户提及：security policy、安全策略、信息安全管理制度、ISO 27001、SOC 2、
可接受使用策略、访问控制、数据分类、供应商安全评估等关键词时触发。

## 策略体系金字塔

```
Policy（方针） — 管理层承诺。"我们保护客户数据的承诺"
  └─ Standard（标准） — 必须遵守的规则。"所有生产系统必须启用 MFA"
     └─ Procedure（流程） — 怎么做到。"启用 MFA 的操作步骤"
        └─ Guideline（指南） — 最佳实践建议。"推荐使用硬件密钥而非 SMS"
```

## 核心策略模板

### 访问控制策略
- 最小权限原则（Least Privilege）
- 权限申请-审批-评审循环（Quarterly Access Review）
- 离职/转岗权限回收时限（≤24h）
- 特权账号管理（Privileged Access Management）

### 数据分类策略
| 等级 | 定义 | 加密 | 共享 | 保留 | 销毁 |
|------|------|------|------|------|------|
| 公开 | 可对外 | 否 | 任意 | — | — |
| 内部 | 员工可见 | 传输加密 | 公司域内 | 按需 | 删除 |
| 机密 | 限部门 | 存储+传输 | 审批 | 法规要求 | 安全擦除 |
| 绝密 | 限指定人 | 存储+传输+应用层 | 禁止共享 | 法规要求 | 证书销毁 |

## 质量原则
1. Policy 是管理层意志，必须有批准签名和生效日期
2. 每年至少 review 一次（SOC 2/ISO 27001 要求）
3. 写给人看不是写给审计看——用简单英语/中文，别堆砌术语
4. 每个规则附一句"为什么"——员工理解原因才能遵守
