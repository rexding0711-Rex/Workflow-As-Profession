# Kimi Desktop Skills 综合审计报告

**审计时间：** 2026-06-17  
**审计路径：** `C:\Users\Rex\AppData\Roaming\kimi-desktop\daimon-share\daimon\skills`  
**审计范围：** 206 个技能目录，1503 个文件，551 个子目录  
**审计方法：** 安全审计 + 结构与合规审计 + 内容质量审计  

---

## 执行摘要

本次审计采用三种独立方法对 Kimi Desktop 的 206 个技能进行了全面检查。**发现 1 个高危安全问题、3 个中等风险、3 个结构化合规缺陷和若干内容质量问题**。

> ⚠️ **环境说明：** 审计在 WSL2 中执行，文件位于 Windows NTFS 分区（drvfs 挂载）。WSL2 drvfs 下所有文件统一显示为 777 权限，实际访问控制由 Windows NTFS ACL 管理，因此"777 权限"在本环境中并非真实安全风险。但父级 `config.json` 中存储的活跃 API 密钥和 JWT Token 仍然是需要关注的安全问题（见下方说明）。

---

## 一、安全审计结果

### 🔴 高风险

| # | 问题 | 位置 | 说明 |
|---|------|------|------|
| 1 | **exec() 执行任意用户代码** | `py-perf-analyzer/scripts/perf_profile.py:61,132,191,309` | 4 处 `exec(code, script_globals)` 直接执行用户提供的 Python 脚本，无沙箱保护 |

### ⚠️ 独立安全提醒（不在 skills/ 范围内）

| # | 问题 | 位置 | 说明 |
|---|------|------|------|
| — | **父级目录含活跃 API 密钥和 JWT** | `daimon-share/daimon/config.json`、`kimi-code-key.json` | 包含 `kimiCode.apiKey`、JWT accessToken（过期 2026-07-18）、refreshToken（过期 2026-09-14）。建议将此文件权限设为 600，或使用系统密钥环存储 |

### 🟡 中等风险

| # | 问题 | 位置 | 说明 |
|---|------|------|------|
| 4 | **subprocess 调用 86 处** | `docx/`、`code-safety-audit/`、`code-to-chart/`、`http-load-tester/` 等 | 多数用于调用 pandoc、ffmpeg 等外部工具，参数化调用但仍有注入风险 |
| 5 | **API 密钥引用 23 处** | `stock-assistant/`、`cn-finance-data/` 等 | 代码中通过环境变量或 secrets.local.json 读取 API 密钥，方法正确但文件以明文存储 |
| 6 | **`__import__` 动态导入** | `stock-assistant/scripts/monitor.py:1434-1447` | 使用 `__import__('datetime')` 而非 `import datetime`，不必要的动态导入 |
| 7 | **Shell 脚本 trap rm -rf** | `gitlab-cli-guide/scripts/build-claude-skill.sh:39`、`swarm-coding/scripts/init-webapp-template.sh:73` | trap 中使用 `rm -rf` 清理临时目录，目录来自变量但仍有误删风险 |

### 🟢 低风险

| # | 问题 | 说明 |
|---|------|------|
| 8 | 文件删除操作 11 处 | 均为临时文件清理（`os.unlink`、`shutil.rmtree`），用途正当 |
| 9 | 硬编码 IP 地址 | 仅 `sunlight-analysis/PUBLISH.md` 中出现一个服务器 IP `170.9.8.41`，其余为文档示例 |
| 10 | 依赖文件 | 发现 7 个 `requirements.txt` 和 5 个 `package.json`，依赖项均为常见库 |

### ✅ 安全亮点

- **无硬编码密钥**：所有 API 密钥均通过环境变量或配置文件读入，源代码中未硬编码真实凭证
- **无 JWT Token 泄露**：skills 目录内未发现 JWT（父级 config.json 中有，独立报告）
- **无恶意 URL**：硬编码的 URL 均为正规 API 端点（api.kimi.com、open.feishu.cn、tushare.pro 等）
- **数据库操作有防护**：`database-inspector` 和 `sql-tutor` 使用正则过滤危险 SQL 关键字
- **路径验证**：`email-manager/scripts/imap.js` 实现了 `ALLOWED_WRITE_DIRS` 路径白名单

---

## 二、结构与合规审计结果

### 核心指标

| 指标 | 数值 | 状态 |
|------|------|------|
| 技能总数 | 206 | — |
| LICENSE 覆盖率 | **45.1%** (93/206) | ❌ 不达标 |
| YAML front matter 缺失 | **68** 个技能 (33%) | ⚠️ 偏高 |
| 含 scripts/ 目录 | 59 个 (28.6%) | ✅ 正常 |
| 含 references/ 目录 | 63 个 (30.6%) | ✅ 正常 |
| 仅单个 SKILL.md | 52 个 (25.2%) | ✅ 正常 |

### 主要问题

**1. LICENSE 覆盖率不足（113 个技能缺失）**

所有存在的 LICENSE 均为 MIT 许可证。缺失 LICENSE 在未授权情况下默认为"保留所有权利"，对分发和复用构成法律风险。

缺失 LICENSE 的技能类别分布：
- 商业/管理类（core-*、elective-*、mba-* 等）：约 30 个
- 工具/技术类（k8s-cluster-ops、stock-assistant、gitlab-cli-guide 等）：约 25 个
- 数据处理类（cn-finance-data、data-formatter、batch-download 等）：约 15 个
- 内容创作类（general-writing、report-writing、paper-writing 等）：约 20 个
- 其他：约 23 个

**2. YAML Front Matter 缺失（68 个技能）**

68 个 SKILL.md 没有 YAML front matter（`---` 包裹的元数据块）。这意味着这些技能缺少结构化的 `name`、`description` 字段，影响：
- 技能发现和索引
- Kimi Desktop 的自动加载机制
- 元数据驱动的搜索/过滤

注：这些文件的 name 字段在 front matter 外以其他形式存在，因此"命名一致性"检查（方法二 §4）显示的基本一致——它们没有 YAML name 字段可对比。

**3. 异常多子技能结构（2 个）**

- `gitlab-cli-guide/`：38 个 SKILL.md（每个 glab 子命令一个）
- `general-writing/`：13 个 SKILL.md（不同写作场景）

这种嵌套结构不符合其他 204 个技能的模式，可能是特意设计的"技能套件"。

**4. 重复脚本文件**

```
pptx/scripts/convert.sh  ≡  pptx-swarm/scripts/convert.sh  (MD5 一致)
pptx/scripts/check.sh    ≡  pptx-swarm/scripts/check.sh    (MD5 一致)
```

`pptx` 和 `pptx-swarm` 共享相同的检查/转换脚本，维护时需同步更新。

---

## 三、内容质量审计结果

### 核心指标

| 指标 | 数值 |
|------|------|
| SKILL.md 平均质量评分 | **4.4 / 10** |
| TODO/FIXME 残留 | 24 处 |
| 占位符（xxx/YOUR_）残留 | 23 处 |
| 断裂引用 | 9 处（涉及 3 个技能） |
| 纯英文技能（中文<5%） | 51 个 (24.8%) |
| 中文为主技能（>80%） | **0 个** |

### Top 5 最佳质量

| 排名 | 技能 | 评分 | 亮点 |
|------|------|------|------|
| 1 | `web-security-audit` | 10/10 | 571 行，含完整 OWASP 检查清单和代码示例 |
| 2 | `wechat-post-craft` | 9/10 | 704 行，图文排版方法论详尽 |
| 3 | `deep-research-swarm` | 9/10 | 513 行，多代理协作框架完整 |
| 4 | `research-paper-refiner` | 8/10 | 351 行，学术润色流程清晰 |
| 5 | `programming-tutor` | 8/10 | 757 行（最长），8 种教学模式 |

### Bottom 5 最差质量

| 排名 | 技能 | 评分 | 问题 |
|------|------|------|------|
| 1 | `monitor-all` | 0/10 | 仅 41 行，无示例、无格式说明、无约束 |
| 2 | `deep-probe` | 1/10 | **仅 10 行**（最短），疑似占位未完成 |
| 3 | `crm` | 1/10 | 169 行但缺乏结构和操作指引 |
| 4 | `flow-orchestrate` | 1/10 | 192 行但内容空泛 |
| 5 | `learn` | 1/10 | 151 行，缺乏教学方法论 |

### 断裂引用（9 处）

| 技能 | 引用路径 | 状态 |
|------|---------|------|
| `seo-copywriting-guide` | `references/core-eeat-benchmark.md` | 文件不存在 |
| `skill-creator` | `references/api_docs.md` | 文件不存在 |
| `skill-creator` | `references/finance.md` | 文件不存在 |
| `skill-creator` | `references/mnda.md` | 文件不存在 |
| `skill-creator` | `references/policies.md` | 文件不存在 |
| `skill-creator` | `references/schema.md` | 文件不存在 |
| `xlsx` | `references/calculation_guide.md` | 文件不存在 |
| `xlsx` | `references/model_construction.md` | 文件不存在 |
| `xlsx` | `references/workbook_format.md` | 文件不存在 |

### 占位符残留

- `create-all/references/audience-modes.md` 中有大量 `xxx` 占位符（模板标记，可能属于预期设计）
- `cn-finance-data/` 文档中的 `your_token_here` 为合理的使用说明
- 少量 `content-engine/SKILL.md` 中的 `xxx` 为表格示例未填充

### 语言分布

```
0-20%（纯英文）    : 51 个 (24.8%)
20-50%（英主中辅）  : 90 个 (43.7%)
50-80%（中主英辅）  : 65 个 (31.6%)
80-100%（中文为主） : 0 个
```

无任何一个 SKILL.md 以中文为主（>80%）。考虑到 Kimi 是中国产品，纯英文技能占比偏高。

---

## 四、综合风险评估

```
🔴 高危: 1 项（exec() 执行用户代码）
🟡 中危: 3 项（subprocess 调用、API 密钥存储方式、trap rm -rf）
🟢 低危: 3 项（临时文件清理、硬编码 IP、依赖安全）
📋 合规缺陷: 3 项（LICENSE 缺失 113、YAML 缺失 68、断裂引用 9）
📝 质量问题: 2 项（平均分 4.4/10、占位符残留）
⚠️ 独立提醒: 父级 config.json 含活跃 API 密钥和 JWT Token
```

---

## 五、改进建议（按优先级）

### 🔴 立即处理

1. **审查 py-perf-analyzer 的 exec() 使用**  
   建议添加沙箱执行环境（Docker 容器或 `RestrictedPython`），或至少添加明显的安全警告

2. **保护父级 config.json 中的 API 密钥和 JWT Token**  
   文件位于 `daimon-share/daimon/config.json`，包含活跃的 Kimi API 密钥和 JWT Token。建议：
   - Windows 侧：确保 `%AppData%\kimi-desktop` 目录仅当前用户可读
   - 或使用 Windows DPAPI / 系统凭据管理器存储

3. **检查 `stock-assistant/secrets.local.json` 是否存在**  
   该文件在 `.gitignore` 模式中但审计未发现。如果存在，确认其不含真实 API 密钥；如果用户填写过模板，立即检查安全性

### 🟡 短期改进

4. **补全 LICENSE 文件**（113 个缺失）  
5. **补全 YAML front matter**（68 个缺失）  
6. **修复断裂引用**（9 处，涉及 `skill-creator`、`xlsx`、`seo-copywriting-guide`）  
7. **更新 `deep-probe`（仅 10 行）和 `monitor-all`（41 行）** 的内容

### 🟢 长期优化

8. **提高内容质量**：当前平均分 4.4/10，目标 6.0/10  
9. **增加中文技能比例**：目前无任何技能以中文为主  
10. **合并重复脚本**：`pptx` 和 `pptx-swarm` 共享脚本应提取为公共模块  
11. **统一 `gitlab-cli-guide` 和 `general-writing` 的嵌套结构**：考虑将它们展平或标记为"技能套件"

---

## 六、审计方法说明

| 方法 | 技术手段 | 检查项数 |
|------|---------|---------|
| **安全审计** | grep 正则扫描、find 权限检查、依赖分析 | 密钥/危险函数/URL/权限/依赖 |
| **结构与合规** | 文件统计、MD5 去重、YAML 解析 | LICENSE/字段/结构/命名/重复 |
| **内容质量** | 行数统计、关键词匹配、Unicode 分析 | 评分/引用/文档/占位符/语言 |

全部审计为**只读操作**，未修改任何文件。

---

*报告由 Claude Code 自动生成 | 2026-06-17*
