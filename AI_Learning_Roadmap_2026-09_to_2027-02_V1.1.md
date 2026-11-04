# AI 学习半年路线 V1.1｜2026.09–2027.02

> 版本：V1.1  
> 校准日期：2026-09-15  
> 核心目标：从“AI 帮我把东西做出来，但我自己不懂”成长为“AI 可以高效参与开发，但我能理解、修改、Debug、测试、部署、维护并讲清楚一个中小型 AI Application / Automation / Integration 系统”。

---

## 0. V1.1 的推进方式

V1 的主要问题不是大方向错了，而是月份切分过硬：简单知识和高认知成本能力被放在同一个月份里，容易出现“前面很快、后面很虚”。

V1.1 改为：

> **月份只做阶段参考，真正推进由能力 Gate 决定。**

核心能力通过：

1. 空白复现；
2. 能讲清数据流与原因；
3. 能定位一个故意注入的 Bug。

通过后可以提前进入下一学习包，不等待自然周 / 自然月；没有通过则补深度，不为了“赶路线”硬上。

---

## 1. 当前状态｜W37 已完成

W37 已经超出原 V1 中“9 月只学会看懂”的预期，但大部分新能力仍处于“初步会用”，不能按掌握计算。

当前已接触并实际使用：

- PowerShell / 命令行基础；
- JSON；
- HTTP / API / GET；
- Python 变量、list、dict、if、for、函数、参数、return；
- `requests`；
- `try / except` 基础；
- JSON 文件读写；
- Todo CRUD + CLI + JSON 持久化；
- Git 最小流程。

当前重点薄弱：

- 数据层级；
- 函数输入 / 输出边界；
- `return` / 循环 / 缩进；
- `try / except` 范围；
- 从空白组织中等长度程序；
- Git 还没有形成持续开发习惯。

因此 W38 不继续盲目堆新名词，而是先把地基补实。

---

# 第一阶段｜W38：巩固 + 代码组织

## 目标

把“跟着写出一个程序”推进到“能重新组织一个小 Python 项目”。

## 主要能力

- Todo 核心逻辑空白复现；
- 模块 / `import`；
- 文件与路径基础；
- `venv` / `pip` / `requirements.txt`；
- `.env` / `.gitignore` / API Key 安全意识；
- Git branch / merge 最小使用；
- `try / except` 边界进一步巩固。

## Gate

能在较少提示下完成：

> 单文件 Todo → 拆成 2–3 个模块 → 虚拟环境 → 依赖文件 → 配置 / 密钥不进 Git → 有意义的 Git 提交

并能解释主要数据流。

## 本阶段不主动上

- SQLite；
- FastAPI；
- logging；
- LLM API；
- Docker。

如果提前通过 Gate，立即进入 W39，不等周末。

---

# 第二阶段｜W39：数据库 + HTTP 深化 + 第一次 LLM API

## 目标

第一次把“普通 Python 程序”与“数据库 + AI Model API”连接起来。

## 主要能力

### SQLite

- 表 / 行 / 列的最小理解；
- `CREATE` / `INSERT` / `SELECT` / `UPDATE` / `DELETE`；
- 参数化查询；
- JSON 文件与 SQLite 的基本取舍。

### HTTP 深化

- GET / POST；
- params；
- headers；
- JSON request body；
- API Key；
- 401 / 404 / 429 / 500 的基本含义。

### LLM API

- 成功调用一次真实模型 API；
- 从多层 JSON response 中取出真正的模型输出；
- 初步理解 Token / 调用成本；
- 把 Key 放环境变量而不是代码里。

## Gate

能完成：

> Python → POST LLM API → 解析嵌套 JSON → 把结果存入 SQLite

并能说清 request / response / Python data / database 四层之间的区别。

---

# 第三阶段｜W40：结构化输出 + 工程化 Mini Project

## 目标

从“会调用 AI”进到“AI 输出可以被程序可靠消费”。

## 主要能力

- Structured Output / JSON 输出；
- 基本输出校验；
- 失败后的重试 / 兜底思路；
- Prompt 最小工程化；
- Token 成本基础；
- `logging`：INFO / WARNING / ERROR；
- README 最小写法。

## 实际任务

完成一个 Mini Project：

> CLI / 输入 → LLM API → 结构化结果 → SQLite → logging → 错误处理

这个 Mini Project 不是最终 Portfolio，但需要自己真正理解。

## Gate

- 能画出数据流；
- 能讲 3 分钟；
- 能处理一次模型返回格式不符合预期；
- 能定位一个故意制造的错误。

## 里程碑

W40 结束前后，开始确定主 Portfolio 的主题，并建立仓库 / README 草案。

---

# 第四阶段｜W41–W42：FastAPI + 从脚本进入服务

## 目标

把本地脚本升级成可以被别的软件调用的 Web Service。

## 主要能力

- FastAPI 最小结构；
- GET / POST Endpoint；
- Request / Response Schema；
- Python 业务逻辑与 API 层的边界；
- SQLite / 数据层与 API 层的连接；
- 基础错误响应；
- 最小测试意识。

## 实际任务

把 W40 Mini Project 服务化：

> Client → FastAPI → 业务逻辑 → LLM API / SQLite → Response

同时正式启动主 Portfolio 的最小 V0.x。

---

# 2026 年 11 月｜真实集成 + 第一次上线

## 本月目标

从“本地能跑”变成“外部系统可以调用、公网可以访问”。

## 主要能力

- Webhook；
- 幂等 / 去重基础；
- 重试；
- 基础测试；
- 配置管理；
- PaaS 部署（优先先上线，不以 Docker 为前置）；
- 日志查看；
- 健康检查；
- Git 分支持续使用。

### AI 能力

- Function / Tool Calling 基础；
- 让 LLM 选择一个工具并传入参数；
- Tool 执行结果回传给模型；
- Workflow 的基本概念。

## Portfolio 生长

Portfolio 至少加入：

- 一个外部系统 / API；
- 一个数据库；
- 一个 AI 能力；
- 一个真实触发方式（Webhook / 定时任务之一）；
- 最小部署版本。

## 月底希望达到

> “我有一个真正在线的小系统，别人 / 另一个程序能够调用它；我知道请求怎么进、数据怎么存、错误去哪里看。”

---

# 2026 年 12 月｜Tool Calling / Agent 基础 + Docker + 可靠性

## 本月目标

让系统开始像“AI Automation / Integration”而不是普通 CRUD 服务。

## 主要能力

- 手写最小 Agent Loop：
  - LLM 判断下一步；
  - 选择工具；
  - 执行；
  - 把结果回传；
  - 结束或继续；
- Function / Tool Calling 深化；
- 失败 / 超时 / 重试；
- Docker 基础；
- Dockerfile；
- 需要时再进入 Docker Compose；
- 结构化日志与故障记录；
- 基本部署可复现。

## RAG

RAG 不作为“为了简历必须做”的项目。

如果 Portfolio 真实需要查询自有文档 / 知识库，则进入：

- 文档切分；
- Embedding；
- 检索；
- 召回质量；
- 将检索结果用于 LLM。

如果项目不需要，则不为了堆技术强行添加。

## Agent Framework

暂不优先。先理解手写 Agent / Tool Calling，再决定是否需要 LangGraph 等框架。

---

# 2027 年 1 月｜Production-like：把 Portfolio 做“活”

## 本月目标

主项目从“功能完整”进入“稳定、可解释、可维护”。

## 主要能力

- VPS / PaaS 持续部署；
- 域名 / HTTPS（项目需要时）；
- 日志 / 健康检查；
- 错误告警；
- 重试 / 限流基本思路；
- 数据备份 / 恢复基本意识；
- 测试补齐；
- 配置 / 密钥管理；
- 故障复盘；
- README / Architecture / Runbook。

## 可选深入

只有 Portfolio 真实需要时才深入：

- RAG 优化；
- LangGraph 等 Agent Framework；
- OAuth；
- n8n / Make；
- 更复杂数据库 / 缓存。

## 实际任务

至少经历一次：

> 故障现象 → 假设 → 日志 / 测试验证 → 根因 → 修复 → 预防

并把它沉淀为求职可讲的真实 Debug 案例。

---

# 2027 年 2 月（截至 2 月 20 日）｜停止扩技术，开始证明能力

## 本月目标

把过去几个月的能力变成：

> 别人能看懂、能验证、愿意给面试机会的证据。

## 主要任务

- 主 Portfolio 最终整理；
- README；
- 架构图 / 数据流；
- Demo；
- Case Study；
- 中文简历；
- 英文 Resume；
- GitHub 整理；
- 项目 5～10 分钟讲解；
- 模拟技术追问；
- 整理一个完整真实故障案例；
- 目标岗位清单与投递材料。

### 市场校准

在 12 月～2 月之间，可以做少量低成本市场校准：

- Remote；
- 线上兼职 / Paid Trial；
- 不影响当前生活安排的面试；
- 用真实反馈判断 Portfolio 和能力缺口。

2027-02-20 起再全面开放异地线下求职。

## 本月不做

- 不因为焦虑新增技术栈；
- 不突然学前端全家桶；
- 不刷算法；
- 不追新 Agent 框架；
- 不重写 Portfolio 主架构，只做必要修复与打磨。

## 2 月 20 日希望达到

> “我能拿出一个连续演进数月、自己真正理解、部署、维护、Debug 过的 AI 应用 / 自动化系统，讲清需求、数据流、技术取舍和故障，并具备正式投递初级 AI Application / Automation / Integration / Implementation 岗位的资格。”

---

# Portfolio：从 10 月开始纵向生长

Portfolio 不再等到 12 月或 1 月才启动。

建议节奏：

```text
10 月：确定真实问题 + 建仓库 + 最小 CLI / 数据流
11 月：API + DB + LLM + FastAPI + 第一次部署
12 月：Webhook / Tool Calling / Docker / 可靠性
1 月：测试 / 监控 / 故障 / 按需 RAG / 文档
2 月：重构、Demo、Case Study、面试讲解
```

项目选择优先满足：

- 解决真实问题；
- 有真实使用者（哪怕先是自己）；
- 至少两个系统 / API 之间有连接；
- 有真实数据流；
- 有数据库；
- 有 AI 能力；
- 有错误处理；
- 有测试；
- 可以部署；
- 能解释业务价值和技术取舍。

---

# 市场信号对路线的校准

当前岗位观察反复出现的底层能力是：

> Python + API + 数据库 + Debug / 测试 + 部署 + LLM API + 系统集成

上层能力常见：

> Agent / Workflow / Tool Calling / RAG

因此学习顺序坚持：

> **工程底座优先，AI 能力尽早接入，框架最后。**

不把职位标题当路线，而把反复出现的交付能力当路线。

---

# 这半年暂时不需要主动扩展的技术

除非 Portfolio / 真实岗位明确需要，否则不要主动加入：

- React / Vue 等前端框架；
- Java / C / C++；
- 算法刷题；
- Kubernetes；
- 微服务；
- 分布式系统；
- 系统学习机器学习 / 深度学习；
- Fine-tuning；
- 为了简历做复杂 RAG；
- Agent Framework 大对比；
- MCP 深挖；
- 云计算证书；
- 系统化 DevOps 全家桶。

需要的时候再学，不因为“听说很重要”提前塞进路线。

---

# V1.1 整条路线只需要记住十步

1. 把 Python 基础写实；
2. 学会组织代码和开发环境；
3. 把数据存进数据库；
4. 会和普通 API / LLM API 说话；
5. 让 AI 输出变成程序可可靠使用的数据；
6. 把脚本做成 FastAPI 服务；
7. 用 Webhook / Tool Calling 把系统真正连起来；
8. 部署、看日志、测试、Debug；
9. 让一个 Portfolio 连续生长几个月；
10. 用这个系统证明自己能交付，而不是证明自己看过多少教程。
