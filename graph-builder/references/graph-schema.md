# 图谱数据模型

## 图结构定义

```yaml
graph:
  name: "陶瓷散热产业链图谱"
  version: "2024-06-15"
  description: "陶瓷基板散热领域的产业链图谱"
  
  nodes:
    - entity_id: "ENT-001"
      type: "公司"
      label: "富乐华"
      
  edges:
    - relation_id: "REL-001"
      type: "提供"
      from: "ENT-001"
      to: "ENT-015"
      
  metadata:
    created: "2024-01-01"
    updated: "2024-06-15"
    source_count: 15
    entity_count: 120
    relation_count: 350
```

## 节点（Node）模型

```yaml
node:
  id: "ENT-001"              # 唯一标识
  type: "公司"                # 实体类型
  label: "富乐华"             # 显示名称
  
  properties:                # 属性
    name: "江苏富乐华半导体科技有限公司"
    short_name: "富乐华"
    industry: "陶瓷基板"
    region: "中国·江苏"
    scale: "员工500+"
    founded: "2015"
    stage: "B轮"
    tags: ["AMB", "国产替代"]
    
  computed:                   # 计算属性
    centrality: 0.85         # 中心度
    degree: 15               # 度数（连接数）
    betweenness: 0.12        # 中介中心度
    closeness: 0.45         # 接近中心度
    eigenvector: 0.78        # 特征向量中心度
    pagerank: 0.23          # PageRank值
    community: "陶瓷基板集群"  # 所属社群
    community_id: 1          # 社群ID
    
  sources:                    # 来源
    - "EXP-2024-001"
    - "EXP-2024-005"
    
  confidence: "高"             # 置信度
  created: "2024-01-15"     # 创建时间
  updated: "2024-06-15"     # 更新时间
  version: 3                # 版本号
```

## 边（Edge）模型

```yaml
edge:
  id: "REL-001"             # 唯一标识
  type: "提供"               # 关系类型
  label: "提供AMB基板"        # 显示标签
  
  from: "ENT-001"           # 起点（公司）
  to: "ENT-015"             # 终点（客户）
  
  properties:               # 属性
    product: "AMB陶瓷基板"
    price_range: "100-200元/片"
    volume: "10万片/月"
    start_date: "2023-01"
    status: "合作中"
    satisfaction: "高"
    
  strength: "强"             # 关系强度
  direction: "单向"          # 方向
  verification: "已验证"      # 验证状态
  
  time:                     # 时间属性
    start: "2023-01"
    end: null               # 未终止
    duration: "18个月"
    
  sources:                  # 来源
    - "EXP-2024-005"
    
  confidence: "高"
  created: "2024-03-10"
  updated: "2024-06-15"
```

## 社群（Community）模型

```yaml
community:
  id: 1
  name: "陶瓷基板集群"
  description: "陶瓷基板领域的公司、技术、供应商"
  
  members:                  # 成员
    - "ENT-001"  # 富乐华
    - "ENT-002"  # 日本京瓷
    - "ENT-003"  # 罗杰斯
    - "ENT-010"  # 氮化铝粉供应商
    - "ENT-015"  # 光模块厂商
    
  internal_edges: 45        # 内部连接数
  external_edges: 12        # 外部连接数
  density: 0.35             # 密度
  cohesion: 0.78            # 凝聚度
  
  key_entities:             # 关键实体（中心度最高的）
    - "ENT-001"  # 富乐华（中心度0.85）
    - "ENT-002"  # 日本京瓷（中心度0.82）
    
  bridges:                  # 桥梁节点（连接其他社群的）
    - "ENT-015"  # 光模块厂商（连接光通信社群）
```

## 路径（Path）模型

```yaml
path:
  id: "PATH-001"
  name: "氮化铝粉 → 数据中心"
  description: "从原材料到终端应用的完整产业链路径"
  
  nodes:                    # 路径节点
    - "ENT-100"  # 氮化铝粉供应商
    - "ENT-001"  # 富乐华
    - "ENT-015"  # 光模块厂商
    - "ENT-020"  # 数据中心
    
  edges:                    # 路径边
    - "REL-100"  # 供应氮化铝粉
    - "REL-001"  # 提供AMB基板
    - "REL-015"  # 提供光模块
    
  length: 3                 # 路径长度（跳数）
  total_distance: 3.5       # 加权距离
  
  bottleneck:               # 瓶颈
    node: "ENT-100"         # 氮化铝粉供应商（唯一来源）
    risk: "高"              # 供应中断风险高
    
  value_distribution:       # 价值分布
    - node: "ENT-100"       # 原材料（价值占比10%）
      value_share: 0.10
    - node: "ENT-001"       # 加工（价值占比40%）
      value_share: 0.40
    - node: "ENT-015"       # 组件（价值占比30%）
      value_share: 0.30
    - node: "ENT-020"       # 集成（价值占比20%）
      value_share: 0.20
```

## 图谱统计

```yaml
graph_stats:
  # 基础统计
  node_count: 120
  edge_count: 350
  node_types:
    公司: 50
    技术: 15
    产品: 20
    客户: 15
    供应商: 10
    专家: 5
    投资机构: 3
    项目: 2
  
  edge_types:
    提供: 80
    使用: 60
    投资: 20
    竞争: 30
    合作: 25
    供应: 40
    采购: 30
    影响: 15
    参与: 20
    推出: 10
  
  # 网络指标
  density: 0.048            # 密度（稀疏）
  average_degree: 5.83      # 平均度数
  diameter: 6               # 直径（最长最短路径）
  average_path_length: 2.8  # 平均路径长度
  clustering_coefficient: 0.35  # 聚类系数
  
  # 连通性
  connected_components: 1   # 连通分量数
  largest_component: 120    # 最大连通分量
  isolated_nodes: 0           # 孤立节点
  
  # 中心性
  top_centrality_nodes:      # 中心度最高的节点
    - "ENT-001": 0.85       # 富乐华
    - "ENT-002": 0.82       # 日本京瓷
    - "ENT-010": 0.75       # 氮化铝粉供应商
    
  # 社群
  communities: 3             # 社群数量
  community_sizes:
    - "陶瓷基板集群": 45
    - "光通信集群": 35
    - "半导体集群": 40
```

## 数据存储格式

### 节点文件（nodes.csv）
```csv
id,type,label,name,short_name,industry,region,scale,founded,stage,tags,centrality,degree,confidence,created,updated
ENT-001,公司,富乐华,江苏富乐华半导体科技有限公司,富乐华,陶瓷基板,中国·江苏,员工500+,2015,B轮,"AMB,国产替代",0.85,15,高,2024-01-15,2024-06-15
ENT-002,公司,日本京瓷,京瓷株式会社,京瓷,陶瓷基板,日本,员工10000+,1959,上市,"DBC,陶瓷基板",0.82,20,高,2024-01-15,2024-06-15
```

### 边文件（edges.csv）
```csv
id,type,label,from,to,product,price_range,volume,start_date,status,strength,verification,confidence,created,updated
REL-001,提供,提供AMB基板,ENT-001,ENT-015,AMB陶瓷基板,100-200元/片,10万片/月,2023-01,合作中,强,已验证,高,2024-03-10,2024-06-15
REL-002,竞争,竞争,ENT-001,ENT-002,陶瓷基板市场,,,,,强,已验证,高,2024-01-15,2024-06-15
```

### JSON格式（完整图谱）
```json
{
  "graph": {
    "name": "陶瓷散热产业链图谱",
    "version": "2024-06-15",
    "nodes": [
      {
        "id": "ENT-001",
        "type": "公司",
        "label": "富乐华",
        "properties": {
          "name": "江苏富乐华半导体科技有限公司",
          "industry": "陶瓷基板",
          "region": "中国·江苏"
        },
        "computed": {
          "centrality": 0.85,
          "degree": 15
        }
      }
    ],
    "edges": [
      {
        "id": "REL-001",
        "type": "提供",
        "from": "ENT-001",
        "to": "ENT-015",
        "properties": {
          "product": "AMB陶瓷基板",
          "volume": "10万片/月"
        }
      }
    ]
  }
}
```

## 图谱更新规则

### 新增规则
- 新实体：如果ID不存在，新增节点
- 新关系：如果(from, to, type)不存在，新增边
- 自动计算：新增后重新计算中心度、社群

### 更新规则
- 属性更新：如果属性值变化，更新并记录历史
- 关系更新：如果关系属性变化，更新并记录历史
- 冲突处理：如果来源冲突，标注冲突并标记待人工确认

### 删除规则
- 实体删除：如果实体不再相关，标记为"已归档"
- 关系删除：如果关系终止，标记为"已终止"，不物理删除
- 软删除：保留历史，仅标记状态

### 合并规则
- 实体合并：如果两个实体实为同一实体，合并属性、关系
- 关系合并：如果多条关系实为同一关系，合并属性
- 合并记录：保留合并历史，可追溯

## 图谱版本控制

```yaml
version_control:
  current_version: "2024-06-15-v3"
  
  history:
    - version: "2024-06-15-v3"
      changes:
        - "更新富乐华产能：100万→200万片/月"
        - "新增投资机构：某产业基金"
      added_nodes: 5
      updated_nodes: 10
      added_edges: 15
      updated_edges: 8
      
    - version: "2024-05-15-v2"
      changes:
        - "新增客户：某光模块厂商"
        - "新增供应商：某氮化铝粉厂商"
      added_nodes: 8
      updated_nodes: 5
      added_edges: 20
      updated_edges: 5
      
    - version: "2024-04-15-v1"
      changes:
        - "初始创建"
      added_nodes: 100
      updated_nodes: 0
      added_edges: 300
      updated_edges: 0
```
