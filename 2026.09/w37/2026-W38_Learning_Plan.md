# 2026-W38 AI 学习计划

> 周期：2026-09-14 ～ 2026-09-20  
> 当前状态：W37 已完成；9 月 14 日已完成 Todo CLI CRUD + JSON 持久化 + 菜单交互练习  
> 本周定位：V1.1 路线的第一个“能力门控周”  
> 核心原则：本周不是继续堆新技术，而是把上周“会跟着做”变成“能重新组织、能解释、能修”。

---

## 1. 本周唯一核心目标

把当前 Python 基础从：

> **跟着提示能完成一个小程序**

推进到：

> **能在较少提示下重新写出核心逻辑，并把单文件程序整理成一个最小 Python 项目。**

本周如果提前通过所有 Gate，可以直接进入 W39，不等待周末。

---

## 2. 本周五个核心能力

### 能力 1：Todo 核心逻辑空白复现 + 数据流讲解

重点不是再抄昨天代码，而是隔一段时间重新写。

至少能重新完成 / 解释：

- `show_todos()`；
- `add_todo()`；
- `complete_todo()`；
- `delete_todo()`；
- `load_todos()`；
- `save_todos()`；
- `while True` 菜单；
- `input()` 为什么要 `int()`；
- 用户编号从 1 开始、list index 从 0 开始为什么要转换。

#### Gate

不看昨天完整代码，在空白文件中写出一个能运行的最小 Todo 版本；允许查单个函数名 / 语法，但不能照着旧文件逐行复制。

然后用自己的话讲清：

```text
程序启动
→ load
→ Python list/dict
→ 用户选择
→ CRUD 修改内存数据
→ save
→ JSON 文件
```

---

### 能力 2：模块 / import｜从一个文件拆成一个小项目

学习最小模块化：

```text
todo_app/
├── main.py
├── todo.py
├── storage.py
└── todos.json
```

目标理解：

- 为什么不把所有函数都堆在 `main.py`；
- `import` 的作用；
- `main.py` 负责什么；
- `todo.py` 负责什么；
- `storage.py` 负责什么；
- 一个函数从另一个文件被调用时，数据怎么传过去。

#### Gate

能把现有 Todo 拆成 2～3 个 `.py` 文件并正常运行，并能解释为什么这么拆。

---

### 能力 3：venv / pip / requirements.txt｜让项目有自己的依赖环境

学习：

- `venv` 是什么；
- 为什么每个项目最好有独立环境；
- 创建 / 激活虚拟环境；
- `pip install`；
- `pip freeze` 或等价方式生成 `requirements.txt`；
- 如何根据依赖文件恢复环境。

#### Gate

能够自己完成：

```text
新建项目目录
→ 创建 venv
→ 激活
→ 安装一个包
→ 生成 requirements.txt
```

并用白话解释为什么这样做。

---

### 能力 4：.env / .gitignore｜密钥和本地文件不能乱进 Git

本周只用假 Key 演示，不需要真正调用 LLM API。

学习：

- 什么信息应该放环境变量；
- `.env` 文件解决什么问题；
- `.gitignore` 解决什么问题；
- 为什么 API Key 不应该直接写在 Python 源代码或提交到 Git；
- `.venv/`、`.env` 等常见忽略项。

#### Gate

建立一个包含假 Key 的 `.env`，确保 `.gitignore` 能阻止它被 Git 跟踪，并能解释原因。

---

### 能力 5：Git 从“做过一次”变成开发工作流 + try/except 边界巩固

Git 本周重点：

- `git status`；
- 有意义地 `add` / `commit`；
- 新建一个 branch；
- 在 branch 做一个小改动；
- merge 回主分支；
- 看懂当前工作树发生了什么。

不是为了每天凑 commit，而是每完成一个有意义的小改动就保存历史。

同时继续复习 `try / except`：

- 哪一行真的可能失败？
- 为什么不应该把整个 `main` 都包进一个超大的 `try`？
- `FileNotFoundError`、`JSONDecodeError`、`ValueError` 分别对应什么风险？

#### Gate

完成一次真实 branch → 修改 → commit → merge，并能解释每一步；同时完成一次故障注入练习，判断 `try` 应该放在哪里。

---

## 3. 本周正式任务顺序

建议按下面顺序推进，不按自然日硬切：

### Task A｜先做 72 小时复现

9 月 14 日的 Todo 不立刻反复抄。

到约 72 小时后做一次空白复现，重点检查：

- 函数；
- 参数；
- `return`；
- list / dict；
- input 类型；
- JSON load / dump；
- CRUD 数据流。

### Task B｜模块化 Todo

把单文件版本拆成：

```text
main.py

todo.py

storage.py
```

先少拆，不追求“标准架构”。

### Task C｜建立独立 Python 环境

对模块化后的 Todo 建：

```text
.venv/
requirements.txt
.gitignore
```

### Task D｜配置安全练习

加入：

```text
.env
```

放一个假的：

```text
OPENAI_API_KEY=test-key
```

重点是理解“配置和代码分离”，本周不急着真的调用模型。

### Task E｜Git 分支 + 故障注入

做一次小功能修改，例如：

- 增加“未完成任务数量”；或
- 输入不存在编号时给出提示。

在 branch 完成，测试后 merge。

然后由 ChatGPT 给 2～3 个坏代码片段，让用户定位问题。

---

## 4. 本周周测 / Gate Check

从 W38 开始，不再以选择 / 判断题为核心。

### 50%｜空白复现

例如：

- 写一个读取 JSON → 处理 → 保存的最小程序；
- 写 2 个相互 import 的模块；
- 写一个小函数处理 list of dict。

### 30%｜故障定位

例如：

- `return` 放错位置；
- `input()` 类型错误；
- `.env` / Git 安全问题；
- 文件路径 / import 错误；
- `try / except` 范围过大或过小。

### 20%｜白话讲解

至少能讲清：

- 模块化为什么有用；
- venv 为什么存在；
- `.env` / `.gitignore` 分别做什么；
- 程序数据从 `main.py` 到函数 / 文件之间怎么流动。

---

## 5. 本周明确不主动学习

在 W38 Gate 通过前，不主动展开：

- SQLite；
- FastAPI；
- logging；
- LLM API；
- Tool Calling；
- Agent；
- RAG；
- Docker。

这些不是不重要，而是为了避免“上层内容跑得比基础理解快”。

---

## 6. 提前通过后的滚动入口

如果 W38 五个核心能力提前全部通过，不等待 9 月 20 日，直接进入 W39。

W39 的第一学习包：

```text
SQLite 最小 CRUD
→ 参数化查询
→ JSON vs SQLite
```

之后进入：

```text
POST / headers / auth
→ 第一次 LLM API
```

---

## 7. 本周 Learning Log 规则

不增加新台账文件。

每天结束只追加少量内容：

- 今天通过了什么；
- 哪个能力仍是 🟡 / 🔴；
- 一个最值得记住的错误 / Bug；
- 下一次需要复现什么。

如出现“代码能跑但自己讲不清”的关键点，直接写：

```text
解释债：xxx
```

不用单独创建 `debt.md`。

---

## 8. W38 成功标准

W38 成功不是“学了更多名词”，而是：

1. 能从空白重新写出 Todo 核心逻辑；
2. 能把一个单文件程序拆成最小多模块项目；
3. 能独立创建 venv、管理依赖；
4. 能正确处理 `.env` / `.gitignore`，知道密钥为什么不能进 Git；
5. 能完成一次 branch → commit → merge，并在故障注入中定位基础问题。

如果这五条过了，W38 立即结束，进入 W39。
