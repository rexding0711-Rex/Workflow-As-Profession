# 异常处理预案

## 信息收集异常（Layer 1: monitor）

### 采集失败

```yaml
error: 采集失败
retry: 3次
  retry_1: 更换User-Agent重试
  retry_2: 使用备用代理重试
  retry_3: 降低采集频率重试
fallback:
  option_1: 跳过该源，标记"数据源缺失"
  option_2: 使用缓存数据（如有）
  option_3: 通知用户，提供手动输入入口
escalation: 连续3次失败 → 通知用户 + 记录日志
```

### 数据清洗失败

```yaml
error: 数据清洗失败
retry: 2次
  retry_1: 放宽清洗规则
  retry_2: 手动确认规则
fallback:
  option_1: 返回原始数据，标记"未清洗"
  option_2: 部分清洗，保留可清洗部分
  option_3: 用户手动清洗
```

## 分析处理异常（Layer 2: analyze）

### 数据不足

```yaml
error: 数据不足，无法分析
retry: 2次
  retry_1: 扩大数据采集范围
  retry_2: 调整分析粒度（从详细到概览）
fallback:
  option_1: 输出基于有限数据的初步分析，标注置信度
  option_2: 暂停等待用户补充数据
  option_3: 切换分析维度（如无法分析技术，转分析商业）
```

### 分析结果异常

```yaml
error: 分析结果矛盾或不可信
retry: 2次
  retry_1: 交叉验证，使用不同方法
  retry_2: 检查数据质量
fallback:
  option_1: 标注不确定性，呈现多版本分析
  option_2: 降低分析深度，仅呈现事实
  option_3: 请求人工复核
```

## 决策支持异常（Layer 3: decide）

### 决策信息不足

```yaml
error: 决策信息不足
retry: 2次
  retry_1: 回退到分析层，要求补充分析
  retry_2: 扩大信息收集范围
fallback:
  option_1: 输出有条件决策（"如果A成立，则选择X"）
  option_2: 呈现所有选项，不给出推荐
  option_3: 暂停等待用户补充信息
```

### 评分数据缺失

```yaml
error: 评分数据缺失
retry: 2次
  retry_1: 使用行业基准数据
  retry_2: 使用历史数据推算
fallback:
  option_1: 标注缺失项，调整权重
  option_2: 仅使用可用数据评分
  option_3: 请求用户手动评分
```

## 内容生成异常（Layer 4: create）

### 模板不匹配

```yaml
error: 模板不匹配
retry: 2次
  retry_1: 选择最接近的模板
  retry_2: 混合多个模板
fallback:
  option_1: 使用通用模板
  option_2: 用户提供自定义模板
  option_3: 输出无格式内容，用户自行排版
```

### 内容质量不达标

```yaml
error: 内容质量不达标
retry: 3次
  retry_1: 调整生成参数
  retry_2: 更换生成策略
  retry_3: 增加示例输入
fallback:
  option_1: 输出初稿，标注"需人工润色"
  option_2: 降低标准，输出简化版本
  option_3: 请求用户反馈，迭代生成
```

## 执行推进异常（Layer 5: execute）

### 任务分配失败

```yaml
error: 任务分配失败
retry: 2次
  retry_1: 检查负责人可用性
  retry_2: 调整任务拆分粒度
fallback:
  option_1: 重新分配负责人
  option_2: 任务合并，减少依赖
  option_3: 标记为"待分配"，通知项目经理
```

### 进度跟踪异常

```yaml
error: 进度跟踪异常
retry: 2次
  retry_1: 检查数据源可用性
  retry_2: 使用替代跟踪方式
fallback:
  option_1: 手动更新进度
  option_2: 延长检查周期
  option_3: 使用里程碑跟踪替代详细跟踪
```

## 复盘沉淀异常（Layer 6: review）

### 数据不全无法复盘

```yaml
error: 数据不全无法复盘
retry: 2次
  retry_1: 扩大数据收集范围
  retry_2: 降低复盘粒度
fallback:
  option_1: 基于可用数据部分复盘
  option_2: 延期复盘，等待数据
  option_3: 定性复盘替代定量复盘
```

## 跨职能异常

### 合同审查中断

```yaml
error: 合同审查中断
retry: 2次
  retry_1: 重新加载文档
  retry_2: 分章节审查
fallback:
  option_1: 输出已审查部分
  option_2: 标记未审查部分，通知法务
  option_3: 使用简化审查清单
```

### 供应商评估中断

```yaml
error: 供应商评估中断
retry: 2次
  retry_1: 重新获取供应商数据
  retry_2: 使用备用数据源
fallback:
  option_1: 基于可用数据部分评估
  option_2: 标记信息缺失项
  option_3: 请求供应商补充材料
```

## 通用降级策略

```yaml
degrade_levels:
  level_1: 自动重试（3次）
  level_2: 使用备选方案
  level_3: 降低输出精度/深度
  level_4: 标记异常，输出半成品
  level_5: 暂停等待人工干预
  level_6: 终止流程，通知用户

escalation_rules:
  - 连续2个步骤异常 → 通知用户
  - 关键步骤异常（决策/执行）→ 立即通知
  - 超时超过预期200% → 自动终止
  - 数据丢失风险 → 立即终止 + 备份
```
