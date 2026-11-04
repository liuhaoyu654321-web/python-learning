# 2026-W37 Learning Log

> 周次：2026-W37  
> 官方周期：2026-09-07 ～ 2026-09-13  
> 实际提前开始：2026-09-05  
> 当前记录截至：2026-09-06  
> 本周核心：命令行 → JSON → HTTP / API

---

## 2026-09-05｜命令行基础

### 今天实际做了什么
- 在 Windows PowerShell 中学习并实际使用基础命令。
- 从 `C:\Users\spiderman` 出发，练习查看当前位置、查看目录内容、进入文件夹、返回上一级。
- 独立进入 `Documents\AI-Learning-Practice`。
- 创建练习目录 `AI-Learning-Practice`。
- 创建 Python 文件 `hello.py`。
- 向 `hello.py` 写入：

```python
print("hello")
```

- 在 PowerShell 中查看文件内容并运行：

```powershell
python hello.py
```

- 成功得到输出：

```text
hello
```

### 接触并使用过的命令

```text
pwd
 dir
 cd
 cd ..
 mkdir
 New-Item
 Set-Content
 type
 python hello.py
```

> 注：`New-Item`、`Set-Content` 目前属于“第一次接触并成功使用”，暂不判定为熟练。

### 当前已能解释的核心概念
- PowerShell：用于通过文字命令控制电脑的命令行环境。
- `pwd`：查看“我现在在哪个目录”。
- `dir`：查看当前目录里有什么。
- `cd`：切换 / 进入目录。
- `cd ..`：返回上一级目录。
- `python hello.py`：调用 Python 去执行 `hello.py` 文件。
- PowerShell ≠ Python：PowerShell 是命令环境，Python 是被调用来运行 `.py` 文件的工具。

### 独立验收结果
已独立完成：

```text
C:\Users\spiderman
→ Documents
→ AI-Learning-Practice
→ dir
→ python hello.py
→ hello
```

**判断：命令行基础第一阶段通过。**

### 仍需后续巩固
- `New-Item`、`Set-Content`、`type` 需要在后续练习中再次使用。
- 目前掌握的是最基础目录导航与运行 Python 文件，还没有学习更复杂的命令参数、管道、重定向等内容。

---

## 2026-09-06｜JSON + HTTP / API 入门

### 一、JSON 基础

#### 今天理解了什么
- JSON 是一种常见的数据组织格式，方便程序之间传递和读取数据。
- 能识别并解释 `Key : Value`。
- 能区分以下基础 Value 类型：
  - String：文字，如 `"Eric"`
  - Number：数字，如 `84.5`
  - Boolean：`true / false`
  - `null`：目前没有具体值
- 理解：
  - `{ }` = Object（对象），用于描述“一个东西有哪些信息 / 属性”。
  - `[ ]` = Array（数组），用于表示“一列 / 多个东西”。
- 理解简单嵌套结构，例如：

```json
{
  "name": "Eric",
  "skills": ["AI", "Python"],
  "workout": {
    "type": "back",
    "duration": 120
  }
}
```

#### 已能自主判断的例子
- `skills` 用 `[ ]`，因为它表示“有哪几个技能”。
- `workout` 用 `{ }`，因为 `type`、`duration` 等都是在描述同一次训练的信息。
- `address` 用 `{ }`，因为 `city`、`country` 都是在描述同一个 address。
- `completed: false` 表示“未完成”。

#### 本日暴露出的一个小问题
- 看到 `duration: 120` 时，一度直接理解成“120 秒”。
- 后来明确：**JSON 只保存数值本身，单位和具体语义要看字段定义或上下文。**

**判断：JSON 基础第一阶段通过；能读懂简单 JSON，但还不等于能熟练手写复杂 JSON。**

---

### 二、API / HTTP 入门

#### 今天理解了什么
- API：一个程序对另一个程序开放功能或数据的接口 / 规则。
- API 的价值包括：
  - 控制权限与安全
  - 让访问方式统一
  - 隐藏服务器 / 数据库内部实现
- Request：客户端发出去的请求。
- Response：服务器返回的整个回答。
- URL：请求要发往的网络地址。
- GET：可以先理解为“读取 / 获取数据”的请求方式。
- JSON 与 API 不是同一个东西：
  - API 是程序之间沟通的接口 / 规则。
  - JSON 是 Response 中常见的数据格式之一。

### 三、第一次真实 API 请求

在 PowerShell 中执行：

```powershell
curl https://jsonplaceholder.typicode.com/todos/1
```

实际返回中包括：

```text
StatusCode        : 200
StatusDescription : OK
Content           : {
                      "userId": 1,
                      "id": 1,
                      "title": "delectus aut autem",
                      "completed": false
                    }
```

#### 对这次请求的理解
当前已能用自己的话解释：

```text
PowerShell
→ 使用 curl
→ 向一个 URL 发出 Request
→ 服务器接收并处理请求
→ 返回 Response
→ Response 中包含状态信息和 Content
→ Content 中包含 JSON 数据
```

#### 今天新增理解
- `200 OK`：服务器成功处理了这次请求。
- Response 不只是 `Content`；`Content` 是 Response 中最关心的数据内容之一。
- JSONPlaceholder 是用于学习 / 测试 API 的假数据服务，本次 `/todos/1` 返回的是一条模拟 Todo 数据。

### 当前掌握度判断
**已理解：**
- API、Request、Response、URL、GET 的基本关系。
- JSON 在 API 返回数据中的位置。
- `200 OK` 表示请求成功。
- 能跟随流程使用 `curl` 发出一次真实请求并读懂主要结果。

**还不能判定熟练：**
- 还没有独立写出多个不同 API 请求。
- 还没有系统理解 HTTP Headers。
- 还没有学习 404、500 等其他状态码。
- 还没有学习 POST / PUT / DELETE。
- 还没有学习 Query Parameters、Request Body、Authentication 等内容。

---

## 截至 2026-09-06 的本周能力链

目前已经第一次真正串通：

```text
命令行
  ↓
PowerShell
  ↓
curl
  ↓
URL
  ↓
GET Request
  ↓
API / Server
  ↓
Response
  ↓
200 OK + Content
  ↓
JSON
```

这是本周目前最重要的进展。

---

## 需要进入 W37 周测的内容

### 必测
- `pwd`、`dir`、`cd`、`cd ..` 的作用。
- 从某个目录进入目标文件夹并运行 `.py` 文件。
- PowerShell 与 Python 的区别。
- Key / Value。
- String / Number / Boolean / `null`。
- `{ }` 与 `[ ]` 的区别。
- Object / Array 简单嵌套。
- API / Request / Response / URL / GET 的关系。
- Response 与 Content 的区别。
- `200 OK` 的含义。
- 用自己的话解释一次 `curl` API 请求的全过程。

### 后续需要再次出现才能判定稳固
- `New-Item`
- `Set-Content`
- `type`
- 独立使用 `curl` 请求另一个 API

---

## 下一学习起点

下次继续时，不需要重学命令行和 JSON 定义。

优先从以下位置继续：
1. 再做 1–2 个真实 GET 请求，确认不是只会跟着复制一次。
2. 让用户自己从 URL、Request、Response、JSON 中定位信息。
3. 之后再逐步引入新的 HTTP 概念；不要一次堆太多状态码或方法。

## 2026-09-08 今日学习总结

### 今日学习目标

今天主要完成两部分：

1. 复习并确认 JSON / HTTP / API / curl 基础理解
2. 进入 Python 基础代码阅读与修改

今天核心任务已完成，并额外提前学习了一部分函数与 Debug 基础。

### 一、今天实际学了什么

#### 1. Python 变量与赋值

理解：

```python
name = "Eric"
age = 24
```

* `name`、`age` 是变量名
* `"Eric"`、`24` 是值
* `=` 是赋值 Assignment，不是数学上的等号
* 变量可以重新赋值：

```python
name = "Eric"
name = "Tom"
```

最后 `name` 的当前值是 `"Tom"`。

#### 2. list 与 dict

Python List：

```python
foods = ["eggs", "chicken", "broccoli"]
```

理解为：

> 一列多个值。

Python Dict：

```python
person = {
    "name": "Eric",
    "age": 24
}
```

理解为：

> 用 Key : Value 保存一组有明确含义的信息。

当前记忆方式：

```text
[] → list → 有哪些东西
{} → dict → 每个东西对应什么信息
```

#### 3. Index 与 Key 取值

List 使用索引：

```python
skills = ["AI", "Python", "n8n"]

skills[0]  # AI
skills[1]  # Python
skills[2]  # n8n
```

Python List 从 `0` 开始编号。

Dict 使用 Key：

```python
person["name"]
person["age"]
```

#### 4. list + dict 嵌套

能读懂：

```python
users = [
    {"name": "Eric", "age": 24},
    {"name": "Tom", "age": 28}
]
```

并理解：

```python
users[1]["name"]
```

表示：

> 先取第 2 个用户，再取这个用户的 `name`。

还能读懂更深一层：

```python
users[0]["skills"][1]
```

理解为：

> 第 1 个用户 → skills → skills 中索引 1 的值。

#### 5. if / elif / else

理解：

```python
age = 24

if age >= 18:
    print("Adult")
```

条件为 `True` 才执行缩进里的代码。

理解：

```python
if ...
elif ...
else ...
```

Python 从上往下判断，命中第一个成立条件后，不再继续执行后面的分支。

#### 6. Python 缩进 Indentation

理解：

```python
if age >= 18:
    print("Adult")

print("Finished")
```

* 有缩进的 `print("Adult")` 属于 `if`
* 没有缩进的 `print("Finished")` 不属于 `if`
* Python 用缩进表示代码属于哪个结构

#### 7. for 循环

理解：

```python
foods = ["eggs", "chicken", "broccoli"]

for food in foods:
    print(food)
```

核心理解：

```text
foods = 全部
food = 当前这一项
```

`for` 可以先理解为：

> 把一组数据一个一个拿出来处理。

#### 8. for + if

能读懂：

```python
scores = [59, 80, 95]

for score in scores:
    if score >= 60:
        print("Pass")
    else:
        print("Fail")
```

并能判断最终输出：

```text
Fail
Pass
Pass
```

#### 9. 累计与计数

求和：

```python
total = 0

for number in numbers:
    total = total + number
```

理解：

> 每一轮把当前数字加进 total。

计数：

```python
count = 0

if condition:
    count = count + 1
```

理解：

> 每发现一个符合条件的数据，就让 count 加 1。

已经能区分：

```text
total = total + number → 求总和
count = count + 1      → 数有几个
```

#### 10. 函数 Function

理解最基础函数：

```python
def greet():
    print("Hello")

greet()
```

* `def`：定义函数
* `greet()`：调用函数

理解参数：

```python
def greet(name):
    print("Hello", name)

greet("Eric")
```

调用时 `"Eric"` 被传给 `name`。

#### 11. return 与 print

今天非常重要的一点。

```python
print(...)
```

理解为：

> 显示给人看。

```python
return ...
```

理解为：

> 把结果返回给程序继续使用。

例如：

```python
def add(a, b):
    return a + b

result = add(10, 20)
```

最终：

```text
result = 30
```

还实际理解了：

> `return` 执行后会直接结束当前函数。

今天通过实际代码发现，如果函数只有：

```python
print(name)
```

但没有 `return`，那么：

```python
result = function()
```

得到的会是：

```text
None
```

#### 12. dict.get()

理解安全读取：

```python
user.get("height")
```

如果没有 `"height"`，默认返回：

```text
None
```

也可以设置默认值：

```python
user.get("height", 180)
```

如果 Key 不存在，就返回 `180`。

已独立写出：

```python
city = person.get("city", "Unknown")
```

#### 13. 基础报错与 Debug

今天初步认识三个常见 Python 错误：

```text
KeyError
→ dict 中没有这个 Key

NameError
→ 使用了没有定义的变量名

TypeError
→ 当前数据类型不支持这个操作
```

当前 Debug 初步流程：

```text
先看报错最后一行
→ 看错误类型
→ 看报错提到哪个变量 / Key / 数据
→ 回到对应代码位置
```

理解：

> 返回 `0` 不代表程序出错。
> “没有数据满足条件”可以是正常结果。

### 二、今日实际动手

今天不只是口头判断，还在 VS Code 的 `Practice.py` 中自己进行了代码修改和运行。

完成了：

```python
city = person.get("city", "Unknown")
```

随后完成了一个小型综合练习：

```python
def count_old_enough(users, min_age):
    for user in users:
        if user["age"] >= min_age:
            name = user.get("name")
            print(name)
```

数据：

```python
users = [
    {"name": "Eric", "age": 24},
    {"name": "Tom", "age": 16},
    {"name": "Alice", "age": 30}
]
```

调用：

```python
count_old_enough(users, 18)
```

最终成功运行：

```text
Eric
Alice
```

过程中真实遇到并理解了几个问题：

* 函数定义参数位置不能直接写 `18`
* `def count_old_enough(users, min_age)` 与调用 `count_old_enough(users, 18)` 的区别
* `return name` 会在找到 Eric 后直接结束函数，导致 Alice 不再被检查
* 函数内部只 `print()`、没有 `return` 时，外部变量接收到的是 `None`
* 最终改为直接调用函数，成功去掉多余的 `None`

### 三、今日掌握度判断

**基本掌握 / 可以继续使用：**

* 变量与赋值
* list / dict 基础
* 索引与 Key
* list + dict 嵌套读取
* `if / elif / else`
* Python 缩进基本逻辑
* `for` 循环基本逻辑
* `for + if`
* 累计与计数的基本区别

**已经理解，但需要继续通过代码巩固：**

* 函数参数
* `return`
* `print` 与 `return` 的区别
* 函数调用结果
* `.get()`
* `None`

**刚开始接触：**

* Debug
* KeyError / NameError / TypeError

### 四、今天最有价值的错误

今天最有价值的不是某一道题答错，而是实际写代码时出现了：

```python
return name
```

导致函数找到第一个符合条件的人后直接结束。

以及：

```python
result = count_old_enough(users, 18)
print(result)
```

导致屏幕出现：

```text
Eric
Alice
None
```

通过真实运行，开始理解：

```text
print → 显示
return → 返回并结束函数
没有 return → 默认返回 None
```

这部分建议后面重点复习。

### 五、今日学习进度

今日核心任务：**100% 完成**

并额外提前学习：

* 函数
* 参数
* `return`
* `.get()`
* `None`
* Python 基础报错与 Debug

今天已经不需要再增加新知识。

### 六、下次优先复习

下次开始学习时，优先主动回忆：

1. `list` 和 `dict` 分别适合什么情况？
2. `for user in users` 中，`user` 和 `users` 分别是什么？
3. `print` 和 `return` 有什么区别？
4. 为什么没有 `return` 的函数可能得到 `None`？
5. `KeyError`、`NameError`、`TypeError` 分别代表什么？
6. `def function(users, min_age)` 和 `function(users, 18)` 有什么区别？

然后再继续下一阶段 Python 阅读与修改练习。
## 2026-09-09 今日学习总结

### 1. 函数参数进一步巩固

理解了：

```python
def count_old_enough(users, min_age):
```

这里：

* `users`：整个用户列表
* `user`：`for` 循环当前正在处理的一个用户
* `min_age`：参数，具体值由调用函数时传入

例如：

```python
count_old_enough(users, 25)
```

运行这一次函数时：

```text
min_age = 25
```

进一步区分：

```python
def function(min_age):
```

是**定义参数**。

```python
function(25)
```

是**传入具体参数值**。

---

### 2. `print`、`return`、`None`

今天重点复习并基本理解了这三个概念。

#### `print`

```python
print(10)
```

作用：

> 把内容显示给人看。

#### `return`

```python
return 10
```

作用：

> 把结果返回给调用这个函数的地方，让程序继续使用。

例如：

```python
def add(a, b):
    return a + b

x = add(10, 20)
```

执行过程：

```text
add(10, 20)
→ return 30
→ x 接住
→ x = 30
```

#### `None`

函数如果没有写 `return`：

```python
def test():
    print(10)
```

那么它默认返回：

```text
None
```

例如：

```python
a = test()
print(a)
```

输出：

```text
10
None
```

今天的重要记忆：

```text
print → 给人看
return → 给程序
没有 return → 默认返回 None
```

---

### 3. `return` 会结束函数

例如：

```python
def find_adult(users):
    for user in users:
        if user["age"] >= 18:
            return user["name"]
```

如果 Eric 是第一个满足条件的人：

```text
Eric → 满足条件
→ return "Eric"
→ 函数直接结束
```

所以后面的 Alice 即使也满足条件，也不会再检查。

如果改成：

```python
print(user["name"])
```

循环不会结束，就可以继续处理后面的用户。

---

# 4. 第一次用 Python 调用真实 API

以前使用：

```powershell
curl.exe https://jsonplaceholder.typicode.com/todos/1
```

今天第一次改成 Python：

```python
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos/1"
)
```

理解了整个过程：

```text
Python
↓
requests.get()
↓
发送 HTTP GET Request
↓
API / Server
↓
返回 HTTP Response
↓
response 接住结果
```

`requests` 可以暂时理解成：

> Python 中别人已经做好的 HTTP 请求工具箱。

---

### 5. HTTP Status Code

使用：

```python
print(response.status_code)
```

得到：

```text
200
```

理解：

> `200 OK` 表示服务器成功接收并处理了这次 HTTP Request，并返回 Response。

不能理解成：

> 所有业务操作一定成功。

---

# 6. `response.json()`

API Response 中的数据可以通过：

```python
data = response.json()
```

转成 Python 可以直接处理的数据结构。

例如 API 返回一个 Todo：

```python
{
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
}
```

在 Python 中：

```text
data → dict
```

因为结构是：

```text
{
Key: Value
}
```

---

# 7. 从 API 数据中读取字段

如果：

```python
data = {
    "title": "delectus aut autem",
    "completed": False
}
```

可以：

```python
data["title"]
```

得到：

```text
delectus aut autem
```

也可以：

```python
data["completed"]
```

得到：

```text
False
```

这里本质上仍然只是昨天学过的：

> Python `dict` 通过 Key 读取 Value。

---

# 8. API 返回多个数据：list + dict

把 URL 从：

```text
/todos/1
```

改成：

```text
/todos
```

后，API 返回很多 Todo。

结构变成：

```python
[
    {"id": 1, "title": "..."},
    {"id": 2, "title": "..."},
    {"id": 3, "title": "..."}
]
```

理解：

```text
最外层 [] → list
每一个 {} → dict
```

所以：

```python
data[0]
```

表示：

> 第一个 Todo。

而：

```python
data[0]["title"]
```

表示：

> 第一个 Todo → 取它的 title。

今天已经自己成功写出并运行：

```python
print(data[0]["title"])
```

---

# 9. 用 `for` 处理 API 返回的一批数据

今天第一次把之前学的 `for` 真正应用到 API 数据：

```python
for todo in data:
    print(todo["title"])
```

理解：

```text
data → 整个 Todo list
todo → 当前这一轮正在处理的一个 Todo dict
```

和之前：

```python
for user in users:
```

是完全相同的逻辑。

---

# 10. `for + if + API`

成功自己写出：

```python
for todo in data:
    if todo["completed"] == True:
        print(todo["title"])
```

实现：

> 遍历所有 Todo，只输出已经完成的 Todo。

也了解到更常见的写法：

```python
if todo["completed"]:
```

因为 `todo["completed"]` 本身已经是 `True / False`。

目前使用：

```python
== True
```

也完全没问题，而且更容易理解。

---

# 11. 对真实 API 数据进行计数

今天又把昨天学过的：

```python
count = 0
count = count + 1
```

应用到了真实数据。

例如：

```python
count = 0

for todo in data:
    if todo["completed"] == True:
        count = count + 1

print(count)
```

实际统计得到：

```text
completed=True → 90
```

修改条件：

```python
if todo["completed"] == False:
```

得到：

```text
completed=False → 110
```

总数：

```text
90 + 110 = 200
```

这也第一次使用了一个简单的 **交叉验证思路**：

> 两类数据加起来等于总数，可以辅助检查代码逻辑是否合理。

---

# 12. 今天接触到的真实 Debug

### `ModuleNotFoundError`

看到：

```text
ModuleNotFoundError: No module named 'requests'
```

第一反应：

> Python 当前环境找不到这个模块 / 第三方库。

而不是 API 地址错误。

---

### SSL / 网络错误

今天还真实遇到了类似：

```text
SSLError
UNEXPECTED_EOF_WHILE_READING
```

重新运行后又正常成功。

初步认识：

```text
SSLError
ConnectionError
Timeout
```

通常优先怀疑：

> 网络、HTTPS、代理、远程服务连接等问题。

不一定意味着自己的 Python 逻辑写错。

---

### 代码逻辑错误

如果：

```text
True = 90
False = 108
总数应该 = 200
```

却对不上：

```text
90 + 108 ≠ 200
```

第一反应应该优先检查代码逻辑，例如：

* `if` 条件
* 缩进
* `count`
* 有没有漏处理数据
* 有没有提前 `return`

而不是第一时间认为网络有问题。

---

# 13. 今天真正串起来的一条完整链路

这是今天最重要的成果：

```text
Python
↓
requests.get()
↓
HTTP Request
↓
API
↓
Response
↓
response.status_code
↓
response.json()
↓
list / dict
↓
索引 / Key
↓
for
↓
if
↓
count
↓
得到最终结果
```

以前这些是分开的知识，今天第一次真正组成了一个完整的小程序流程。

---

## 当前掌握度

**今天明显变稳定：**

* 函数参数
* `return`
* `print`
* `None`
* `list + dict`
* `for`
* `if`
* 基础计数
* HTTP/API/JSON 之间的关系

**今天新建立：**

* Python `requests`
* Python 调真实 API
* `response.status_code`
* `response.json()`
* 用 Python 处理 API 返回的数据
* 基础网络错误判断

**还需要继续练：**

* 自己从空白开始写完整 API 程序
* `requests` 的更多用法
* 函数和 API 结合
* 异常处理
* 更系统的 Debug
* 不依赖 AI 补全完成代码

### 今日核心学习进度

**核心任务：100% 完成。**

今天最重要的变化可以概括成一句话：

> 从“能看懂一点 Python 语法”，第一次进入了“能用 Python 获取真实 API 数据，并进行读取、筛选和统计”的阶段。

## 2026-09-10 今日学习总结

### 一、今日核心目标

今天的重点不是继续堆新语法，而是验证昨天学过的东西能不能真正自己重新搭起来。

今天完成的主线：

```text
从空白写 API 请求
→ 解析 JSON
→ 读取 dict
→ Debug
→ Function + API
→ for + if + count
→ return 统计结果
```

**今日核心任务：100% 完成。**

---

### 二、重新理解 `response` 和 `data`

今天进一步明确：

```python
response = requests.get(url)
data = response.json()
```

两者不是一回事。

`response` 是整个 HTTP Response，里面可能包括：

```text
状态码
Headers
Body / Content
```

而：

```python
data = response.json()
```

表示：

> 把 Response Body 中的 JSON 数据解析成 Python 可以直接操作的数据。

解析以后，`data` 通常已经不是“JSON 格式本身”，而是 Python：

```text
dict
或
list
```

判断方法：

```text
最外层 {} → dict
最外层 [] → list
```

---

### 三、第一次真正从空白重新写 API 请求

今天一开始没有完全记住昨天的代码，第一次参考了 `practice2.py`。

随后关闭参考，在提示：

```text
导入 requests
→ 发 GET 请求
→ 打印状态码
```

的情况下重新写出了：

```python
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos/1"
)

print(response.status_code)
```

这说明目前：

> API 程序的基本骨架已经开始形成，但还需要继续重复练习，才能达到真正熟练。

---

### 四、第一次真正理解 Python 环境问题

运行程序时遇到：

```text
ModuleNotFoundError: No module named 'requests'
```

今天没有简单重新安装，而是第一次真正排查了 **Python Environment**。

执行：

```powershell
python --version
```

发现终端默认：

```text
Python 3.12.10
```

但 VS Code 当时使用的是：

```text
CPython 3.15.0rc1
```

随后通过：

```powershell
where.exe python
```

发现电脑中存在多个 Python：

```text
Python 3.12
Python 3.13
Python 3.15
```

今天建立了一个非常重要的概念：

> **同一台电脑可以存在多个 Python 环境，每一个环境拥有自己的第三方库。**

所以：

```text
“电脑装了 requests”
≠
“所有 Python 都能 import requests”
```

最后明确给 Python 3.12 安装：

```powershell
C:\Users\spiderman\AppData\Local\Programs\Python\Python312\python.exe -m pip install requests
```

再次运行成功得到：

```text
200
```

---

### 五、今天完整经历了一次 Debug 流程

这次 `ModuleNotFoundError` 的实际排查过程：

```text
看到错误
↓
判断不是 API 本身
↓
怀疑 Python 环境
↓
检查实际解释器
↓
发现多个 Python
↓
切换到 Python 3.12
↓
仍然报错
↓
验证 3.12 也没有 requests
↓
给指定环境安装 requests
↓
重新运行
↓
成功
```

今天进一步理解：

> Debug 不是看到错误就乱改，而是先提出假设，再通过运行结果验证。

还学到了一个重要原则：

> **一次尽量只改变一个变量，方便判断到底是哪一步解决了问题。**

---

### 六、`dict` 读取与 `AttributeError`

解析 API：

```python
data = response.json()
```

以后，尝试写了：

```python
print(data.title())
```

得到：

```text
AttributeError: 'dict' object has no attribute 'title'
```

重新认识到：

如果 `data` 是：

```python
{
    "title": "delectus aut autem"
}
```

应该：

```python
data["title"]
```

而不是：

```python
data.title()
```

区别：

```text
data["title"]
→ 从 dict 中通过 Key 取值

data.title()
→ 调用 data 身上的 title 方法
```

修复以后成功输出：

```text
200
delectus aut autem
```

---

### 七、第一次真正把 Function + API 接起来

今天开始不再让函数只处理人为写的小数据，而是让它处理真实 API 返回的数据。

写出：

```python
def get_title(todo):
    return todo["title"]
```

关键理解：

`todo` 接收的是完整的一条 Todo：

```python
{
    "id": 1,
    "title": "...",
    "completed": False
}
```

而不是直接接收：

```text
"title"
```

随后调用：

```python
title = get_title(data)
print(title)
```

完整过程：

```text
data
↓
传给 get_title(data)
↓
函数里的 todo = data
↓
todo["title"]
↓
return title
↓
变量 title 接住返回结果
```

---

### 八、进一步巩固 `print` 和 `return`

今天一开始曾写：

```python
def get_title(todo):
    print(todo["title"])
```

随后自己改为：

```python
def get_title(todo):
    return todo["title"]
```

继续巩固昨天的核心区别：

```text
print → 给人看
return → 把结果交给程序继续使用
```

例如：

```python
title = get_title(data)
```

这里：

```text
get_title()
→ return 结果
→ title 接住
```

---

### 九、第一次让函数处理一整批 API 数据

把 API：

```text
/todos/1
```

改成：

```text
/todos
```

以后：

```python
data = response.json()
```

得到的是：

```text
所有 Todo 组成的 list
```

然后自己完成了：

```python
def count_completed(todos):
    count = 0

    for todo in todos:
        if todo["completed"] == True:
            count += 1

    return count
```

再调用：

```python
result = count_completed(data)
print(result)
```

成功得到：

```text
90
```

这里第一次真正把这些知识全部组合起来：

```text
API
+
list
+
dict
+
function
+
parameter
+
for
+
if
+
count
+
return
```

---

### 十、今天出现的一个小 `KeyError` 风险

写函数时曾把：

```python
todo["completed"]
```

拼成：

```python
todo["comleted"]
```

这种情况运行时会导致类似：

```text
KeyError: 'comleted'
```

因为 dict 里没有这个 Key。

进一步建立：

```text
KeyError
→ 优先检查字典 Key 名
→ 拼写
→ 数据里到底有没有这个字段
```

---

### 十一、完成了简单的数据交叉验证

已知：

```text
Todo 总数 = 200
completed=True = 90
```

能够自己推理：

```text
completed=False
= 200 - 90
= 110
```

说明今天已经不只是“跑出一个数字”，而开始知道：

> 可以通过不同结果之间的关系检查程序输出是否合理。

---

### 十二、今天建立起来的完整 Python + API 链路

目前已经亲手运行：

```text
Python Environment
↓
import requests
↓
requests.get()
↓
HTTP Request
↓
HTTP Response
↓
status_code
↓
response.json()
↓
list / dict
↓
function
↓
for
↓
if
↓
count
↓
return
↓
最终结果
↓
Debug
```

这是目前几天学习中第一次把这么多基础知识真正串进一个完整的小程序。

---

### 十三、今天的岗位市场反馈

今天还第一次用自己搭建的 Job Market Scanner 的真实 JD 数据反过来检查学习路线。

这批岗位明显反复出现：

```text
Python
API
数据库 / SQL
Debug
Agent / Workflow
RAG
后端框架
部署
Git
Docker / Linux
真实项目落地
需求理解与沟通
```

因此目前的学习路线没有必要因为看到大量 Agent 岗位就提前跳到 LangChain、RAG 或复杂 Agent。

当前仍应该继续：

```text
Python
→ Debug / 文件 / 异常处理
→ Git
→ SQL / 数据库
→ FastAPI / API
→ Docker / Linux
→ Agent / Tool Calling
→ RAG
→ 部署
```

今天真实 JD 也验证了：AI 编程工具可以大量使用，但招聘真正要求的是能理解、修改、调试和交付，而不是完全脱离 AI 手写所有代码。

---

### 十四、当前掌握度更新

**比昨天明显更稳：**

```text
list / dict
dict Key 读取
for
if
count
函数参数
return
Python 调 API
```

**今天新建立：**

```text
Python 多环境概念
第三方库属于具体 Python 环境
指定解释器安装 pip package
AttributeError 基础判断
Function + API
函数处理一整批 API 数据
Debug 假设 → 验证思路
```

**仍需继续练习：**

```text
完全脱离参考从空白写 API 小程序
function 独立设计
异常处理
文件读写
模块 / import
Git
SQL / 数据库
更系统的 Debug
```

### 今日最终判断

今天最重要的进步可以概括成：

> **昨天是“能够用 Python 处理 API 数据”，今天开始变成“能够把 API 数据交给函数处理，并且开始理解程序运行环境和真实 Debug”。**

这一步已经开始从单独学语法，进入到**小型程序组合能力**。
可以。下面这段直接**追加到你现在的 `2026-W37_Learning_Log.md`** 就行。今天正式学习的总结你前面已经记录过，所以这次我只记录晚上的「复习 + 练习」，避免重复。内容依据你当前 Learning Log 和刚才实际复习表现整理。

````markdown
## 2026-09-10｜晚间复习与练习

### 今日复习目标

晚上进行约 30 分钟闭卷复习，重点检查此前学习中仍不稳定的知识，而不是继续追求新内容。

重点复习：

- `response / response.json() / data`
- List / Dict 数据层级
- 函数参数应该接收哪一层数据
- `print / return / None`
- `return` 对函数执行流程的影响
- 常见错误的初步分类与 Debug

---

### 1. API 数据层级复习

重新复习了：

```python
response = requests.get(url)
data = response.json()
````

当前理解：

* `requests.get(url)`：向 URL 发起 HTTP GET 请求
* `response`：完整的 HTTP Response，不只是 JSON 数据
* `response.json()`：读取并解析 Response 中的 JSON Body
* `data`：解析后得到的 Python 数据，通常是 `dict` 或 `list`

本次复习中仍出现了把 JSON、`response.json()` 和解析后的 Python `data` 混在一起的情况。

状态：🟡 需要继续复习

---

### 2. List / Dict 与循环变量

练习数据：

```python
data = [
    {"name": "Eric", "age": 24},
    {"name": "Tom", "age": 16}
]
```

能够正确判断：

```python
data
```

是整个 List。

```python
data[0]
```

是第一个 Dict。

```python
data[0]["name"]
```

得到 `"Eric"`。

进一步复习：

```python
for user in data:
```

这里的 `user` 不是 JSON / Dict 中原本存在的 Key，而是程序员自己定义的循环变量，代表“当前正在处理的这一项”。

状态：🟢 基本理解

---

### 3. 函数参数与数据层级

这是本次复习最重要的薄弱点。

例如：

```python
def get_age(user):
    return user["age"]
```

函数内部使用：

```python
user["age"]
```

说明参数应该接收一个用户 Dict：

```python
get_age(users[0])
```

而不是整个 List，也不是已经取出的数字。

另一个例子：

```python
def count_adults(users):
    for user in users:
        ...
```

因为函数内部需要：

```python
for user in users
```

所以参数需要接收整个用户 List。

本次形成的重要判断规则：

> 不要根据参数名字猜它需要什么数据，要看函数内部是怎么使用这个参数的。

如果看到：

```python
user["age"]
```

通常说明需要一个 Dict。

如果看到：

```python
for user in users:
```

通常说明需要一个可以遍历的集合，例如 List。

状态：🟡 从容易混淆进步到能够正确判断，但仍需继续练习

---

### 4. print / return / None

练习：

```python
def get_age(user):
    print(user["age"])

result = get_age(person)
print(result)
```

一开始能够意识到“没有 `return` 会得到 `None`”，但漏掉了函数内部 `print()` 产生的输出。

正确输出：

```text
24
None
```

原因：

```text
print(user["age"])
→ 在屏幕显示 24

函数没有 return
→ 默认返回 None

result 接住 None

print(result)
→ 显示 None
```

之后反向练习：

```python
def get_age(user):
    return user["age"]

result = get_age(person)
print(result)
```

能够正确判断：

```text
24
```

因为 `return` 把 `24` 返回给 `result`，最终由外部 `print(result)` 打印。

核心区别：

* `print()`：显示内容，不等于返回值
* `return`：把值返回给函数调用处
* 没有 `return`：函数默认返回 `None`

状态：🟡 理解明显增强，但仍出现一次遗漏 `None` 的情况，需要继续主动回忆

---

### 5. return 会立即结束函数

练习：

```python
def find_adult(users):
    for user in users:
        if user["age"] >= 18:
            return user["name"]
```

数据：

```python
Eric 24
Tom 16
Alice 30
```

能够正确判断最终只返回：

```text
Eric
```

原因：

Eric 第一个满足条件，执行：

```python
return "Eric"
```

之后整个函数立即结束，所以不会继续检查 Tom 和 Alice。

当前理解：

> 程序第一次真正执行到 `return` 时，当前函数立即结束。

状态：🟢 基本掌握

---

### 6. Debug 分类复习

能够正确判断：

```text
ModuleNotFoundError: No module named 'requests'
```

优先检查：

* Python 环境
* 第三方库是否安装
* 当前 Interpreter 是否正确

能够正确判断：

```text
KeyError: 'completed'
```

优先检查：

* Dict 是否存在该 Key
* Key 拼写
* 实际数据结构

能够正确判断：

```text
SSLError / ConnectionError
```

优先检查：

* 网络
* HTTPS
* 代理
* 连接状态

对于：

```text
NameError: name 'count' is not defined
```

最初回答“名字错了”，进一步修正为：

* 变量可能没有定义
* 定义位置可能不正确
* 变量名可能拼错

状态：🟢 基础错误分类已经比较稳定

---

### 7. 综合练习表现

完成了多道闭卷预测题。

能够正确判断：

```python
get_age(users[1])
```

传入的是 Tom 的 Dict，最终：

```text
16
```

能够正确理解：

```python
def count_adults(users):
```

需要接收整个 List，因为函数内部需要：

```python
for user in users:
```

并正确判断三个用户中：

```text
Eric 24
Tom 16
Alice 30
```

成年人数量为：

```text
2
```

---

### 本次复习后的掌握度更新

🟢 相对稳定：

* List / Dict 基础访问
* `for` 循环中的“当前项”
* `return` 会结束函数
* 基础计数逻辑
* ModuleNotFoundError / KeyError / 网络错误基础分类
* 简单嵌套数据访问

🟡 继续重点巩固：

1. `response`、`response.json()`、`data` 的区别
2. 函数参数到底应该传 List、Dict 还是单个值
3. `print / return / None`
4. 不根据变量名字猜数据类型，而根据代码如何使用变量来判断
5. 从空白独立写出完整 API Python 程序

### 今日复习结论

本次约 30 分钟复习没有继续追求新知识，而是通过闭卷回答和代码预测暴露真实薄弱点。

当前最值得继续训练的核心不是 `if / for` 基础语法，而是：

> 看懂数据现在处在哪一层，以及函数到底需要哪一层数据。

相比此前，对 `return`、`None`、List / Dict 和基础 Debug 的理解已经更加稳定，但函数参数的数据层级仍需要通过后续代码练习继续强化。

```
```
下面这段直接追加到你的 `2026-W37_Learning_Log.md` 即可。

````markdown
## 2026-09-11｜Python 异常处理、文件读写与 Git 入门

### 今日学习目标

今天继续沿着 Python → API → 数据处理 → Debug 的路线推进。

完成内容：

- 从空白重新写最小 API 请求
- `try / except` 异常处理
- 指定 `requests` 请求异常
- 理解对象属性、对象方法、Dict 取值的区别
- JSON 文件写入与读取
- `json.dump()` / `json.load()`
- 文件模式 `"w"` / `"r"`
- 一次真实 `TypeError` Debug
- Git 最小基础
- 重新理解“项目驱动学习”和就业能力之间的关系

---

### 1. 从空白重新写 API 请求

重新从空白完成：

```python
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos/1"
)

data = response.json()

print(data["title"])
````

成功输出：

```text
delectus aut autem
```

目前能够较稳定回忆：

```text
import requests
→ requests.get(...)
→ response
→ response.json()
→ data
→ data["title"]
```

状态：🟢 基础链路开始稳定

---

### 2. try / except 基础

第一次正式学习异常处理。

基础结构：

```python
try:
    # 尝试执行可能出错的代码
except:
    # 出错后执行
```

核心理解：

```text
try 没出错
→ 正常继续执行
→ 跳过 except

try 中途出错
→ try 后面的代码停止
→ 跳到 except
```

例如：

```python
try:
    print("A")
    number = 10 / 0
    print("B")
except:
    print("C")

print("D")
```

正确输出：

```text
A
C
D
```

一开始曾误以为 `except` 只有在 try 什么都没有执行成功时才会进入，之后修正为：

> try 里面任何一步真正抛出异常，就会跳到 except。

状态：🟡 新知识，基本理解

---

### 3. API + try / except

将异常处理接入真实 API：

```python
try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data["title"])
    else:
        print("请求失败")

except:
    print("网络异常")
```

进一步理解了两类不同的问题：

```text
404 / 500 等 HTTP 状态
→ 程序可能仍正常收到 Response
→ 可以用 status_code + if 判断

ConnectionError / SSLError 等
→ Python 真正抛出异常
→ 可以通过 except 捕获
```

重要理解：

> API 返回失败状态 ≠ 一定进入 except。

---

### 4. 不使用过宽的 except

一开始使用：

```python
except:
    print("网络异常")
```

发现问题：

如果代码本身出现 `KeyError`、`TypeError` 等错误，也可能被误认为“网络异常”，不利于 Debug。

改为：

```python
except requests.exceptions.RequestException:
    print("网络异常")
```

当前理解：

```text
except:
→ 太宽，很多异常都会抓

except requests.exceptions.RequestException:
→ 主要处理 requests 请求相关异常
```

状态：🟡 能理解用途，长名字暂时不要求背熟

---

### 5. `.`、属性、方法与 Dict 取值

今天重点解决了：

```python
response.status_code
```

为什么使用 `.` 而不是：

```python
response["status_code"]
```

当前理解：

#### Dict 按 Key 取值

```python
data["title"]
```

意思：

> 去 Dict 中找到 `"title"` 这个 Key 对应的 Value。

#### 对象属性

```python
response.status_code
```

意思：

> 获取 `response` 对象自身携带的 `status_code` 属性。

#### 对象方法

```python
response.json()
```

意思：

> 调用 `response` 对象自带的 `json()` 功能。

形成当前判断：

```text
data["title"]
→ Dict 按 Key 取值

response.status_code
→ 对象属性

response.json()
→ 对象方法
```

也意识到此前：

```python
requests.get(...)
```

本身也已经使用过 `.`。

状态：🟡 初步理解对象属性 / 方法，不深入类和对象原理

---

### 6. JSON 文件写入

学习 Python 自带模块：

```python
import json
```

写文件：

```python
with open("user.json", "w", encoding="utf-8") as file:
    json.dump(
        data,
        file,
        ensure_ascii=False,
        indent=2
    )
```

当前理解：

```text
"w"
→ write
→ 写入模式

file
→ 给当前打开的文件对象起的临时变量名
→ 不是文件夹

json.dump(data, file)
→ 把 Python 数据写入 JSON 文件
```

进一步知道：

```text
ensure_ascii=False
→ 中文更容易正常保存

indent=2
→ JSON 排版更易读
```

另外：

> `"w"` 模式下，文件不存在时会创建；已存在时会覆盖原内容。

状态：🟢 基础写入已完成实际操作

---

### 7. JSON 文件读取

学习：

```python
with open("user.json", "r", encoding="utf-8") as file:
    saved_data = json.load(file)

print(saved_data["title"])
```

当前理解：

```text
"r"
→ read
→ 读取模式
```

并区分：

```text
json.dump()
→ Python 数据写入 JSON 文件

json.load()
→ JSON 文件重新读取成 Python 数据
```

数据来源区别：

```text
data
← response.json()
← 网络服务器 Response

saved_data
← json.load(file)
← 本地 JSON 文件
```

状态：🟢 基础读写链路已跑通

---

### 8. 文件读写综合练习

独立完成：

```python
data = {
    "name": "Eric",
    "age": 24
}
```

要求：

```text
data
→ 保存到 person.json
→ 再读取
→ 保存到 saved_data
→ 打印 saved_data["name"]
```

最终成功输出：

```text
Eric
```

说明已经实际跑通：

```text
Python Dict
→ json.dump()
→ JSON 文件
→ json.load()
→ Python Dict
→ 按 Key 读取
```

---

### 9. 今日真实 Debug：TypeError

第一次运行综合练习时出现：

```text
TypeError:
got an unexpected keyword argument 'ensure_asci11'
```

原因：

把：

```python
ensure_ascii
```

错误写成：

```python
ensure_asci11
```

修正后程序成功运行。

今天新增 Debug 经验：

```text
TypeError
+
unexpected keyword argument
→ 优先检查函数参数名字是否拼错
```

状态：🟢 完成一次真实 Debug

---

### 10. Git 最小基础

第一次正式接触 Git。

当前理解：

> Git 是记录代码变化、保存不同版本的版本管理工具。

今天只学习三个核心动作：

```text
git status
→ 查看当前文件变化状态

git add
→ 把准备提交的修改放进待提交区

git commit
→ 正式在本地创建一个版本记录
```

基本流程：

```text
修改代码
↓
git status
↓
git add
↓
git commit
```

同时明确：

```text
git commit
→ 本地版本记录

git push
→ 才涉及把本地版本同步到远程，例如 GitHub
```

因此：

> `git add` ≠ 创建版本
> `git commit` ≠ 自动上传 GitHub

状态：🟡 第一次接触，只建立最小概念

---

### 11. 对当前 Python 学习进度的判断

以“半年后做初级 AI 应用 / 自动化工作所需要的 Python”为参考，而不是整个 Python 世界。

当前粗略判断：

```text
Python 基础语法
→ 约 60%

Python 实际编程能力
→ 约 30%

就业需要的 Python 工程能力
→ 约 25%
```

这里只用于定位，不是考试成绩。

今天新增内容本身大约相当于“就业够用 Python”中的一小块，重点不在学了多少语法，而在开始形成：

```text
API
→ 异常处理
→ 数据解析
→ 文件保存
→ 文件读取
→ Debug
```

这样的完整程序链。

---

### 12. 对“项目驱动学习”的新理解

今天讨论了一个重要问题：

> 是否可以让零基础的人直接围绕几个中等项目学习，并通过项目获得就业能力？

当前结论：

**可以，而且之后非常适合逐渐采用这种方式。**

但前提是“做完项目”不能只是：

```text
AI 生成
→ 能运行
→ 项目结束
```

真正吃透项目应该包括：

```text
知道项目解决什么问题
→
能讲清数据怎么流动
→
知道核心代码在做什么
→
可以修改功能
→
能处理错误
→
能够使用 AI 辅助 Debug
→
能够测试
→
知道如何部署
→
可以解释为什么这样设计
```

真正判断能力是否属于自己的一个测试：

> 做完几个项目以后，面对一个相似但没有做过的新需求，能否自己拆解问题，并借助 AI 完成开发、Debug 和交付。

因此后续学习方向可以逐渐从：

```text
知识点 → 知识点 → 知识点 → 最后做项目
```

切换成：

```text
项目作为主线
↓
项目需要什么
↓
现场补对应知识
↓
继续做项目
```

未来更适合：

```text
约 70% 项目驱动
+
约 30% 基础补缺
```

核心目标不是“不用 AI 手写大量代码”，而是：

> 能够控制 AI 完成工程，而不是完全依赖 AI 决定工程。

---

### 今日掌握度

🟢 相对稳定：

* 最小 API 请求链
* `response.json()` 得到 Python 数据
* `data["key"]` 基础 Dict 访问
* JSON 文件写入
* JSON 文件读取
* `json.dump()` / `json.load()`
* `"w"` / `"r"`
* 基础 Debug 思路

🟡 需要继续巩固：

* `try / except`
* RequestException
* HTTP 状态错误与 Python Exception 的区别
* 对象属性 / 对象方法
* `.` 和 `["key"]` 的使用场景
* Git `status → add → commit`
* 从空白组织更完整的程序

---

### 今日结论

今天从此前的：

```text
Python 基础语法
+ API 调用
```

进一步进入：

```text
API 请求
→ 判断状态
→ 捕获异常
→ 解析数据
→ 保存本地
→ 重新读取
→ Debug
→ Git 版本管理入门
```

这是从“学习单个语法”向“组织完整小程序”迈出的一步。

接下来学习重点不应只是继续增加 Python 语法数量，而应该逐渐转向：

> 项目驱动 + 遇到缺口再补知识。

长期判断是否达到就业能力的核心标准：

> 面对一个没有完全做过的新需求，能够借助 AI 自己完成分析、开发、Debug、测试、部署，并解释整个项目。

```
```
## 2026-09-12 学习总结

### 今日核心完成

今天完成了第一个比较完整的项目驱动练习：

**Todo API 小统计器 V1**

实现了完整流程：

```text
API 请求
→ 检查 status_code
→ response.json()
→ 获取 Todo 列表
→ for 遍历
→ 根据 completed 统计已完成/未完成
→ 封装成函数
→ return 两个统计结果
→ 打印结果
→ 保存 JSON 文件
→ try / except 处理网络异常
```

最终结果：

```text
总任务：200
已完成：90
未完成：110
```

---

### 今天重点巩固的 Python 知识

#### 1. 计数器必须放在循环外

错误思路：

```python
for todo in data:
    completed_count = 0
```

这样每次循环都会重新清零。

正确思路：

```python
completed_count = 0
unfinished_count = 0

for todo in data:
    ...
```

核心理解：

> 计数器只初始化一次，然后随着循环不断累加。

---

#### 2. return 的位置非常重要

如果写成：

```python
for todo in data:
    ...
    return completed_count, unfinished_count
```

第一次循环结束就会直接退出整个函数，后面的 Todo 不再处理。

正确结构：

```python
for todo in data:
    ...

return completed_count, unfinished_count
```

核心理解：

> `return` 会直接结束函数，所以要等整个循环完成后再返回最终结果。

---

#### 3. 函数可以返回多个值

今天使用：

```python
return completed_count, unfinished_count
```

外部可以这样接：

```python
completed_count, unfinished_count = count_todos(data)
```

理解为：

```text
函数返回两个结果
→ 两个变量分别接住
```

不能直接两次打印：

```python
print(count_todos(data))
```

否则得到的是：

```text
(90, 110)
```

---

#### 4. 函数参数应该匹配函数真正需要的数据

`count_todos(data)` 需要整个 Todo 列表，因为函数内部要：

```python
for todo in data:
```

如果传：

```python
data[0]
```

就只是一条 Todo，而不是整个列表。

今天进一步理解：

> 函数需要什么层级的数据，取决于函数内部要做什么。

---

### 今日 Debug 重点

今天实际遇到并解决了多种结构问题：

```text
计数器放在 for 内
→ 每轮重新清零

return 放在 for 内
→ 第一轮就提前结束函数

else 缩进错误
→ SyntaxError

print / 文件保存放在循环里
→ 会重复执行很多次

函数返回两个值但直接打印函数
→ 得到整个 tuple，而不是单独结果
```

今天对 Python 缩进的理解更进一步：

> 缩进不只是格式，而是在决定代码属于哪个 `if`、`for`、`try` 或函数。

---

### 额外练习：奇偶数统计函数

晚上又做了一次迁移练习：

```python
numbers = [1, 2, 3, 4, 5, 6]
```

写出：

```python
def count_numbers(numbers):
    count = 0
    odd_count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1
        else:
            odd_count += 1

    return count, odd_count
```

运行结果：

```text
偶数：3
奇数：3
```

这里第一次正式接触：

```python
%
```

取余运算符。

例如：

```text
4 % 2 = 0
→ 偶数

5 % 2 = 1
→ 奇数
```

这次练习说明今天 Todo 项目里的函数、循环、计数器和 `return` 已经开始能够迁移到新的问题。

---

### Debug 判断练习

今天又专门练了两个容易混淆的问题。

#### return 在循环里

```python
for number in numbers:
    ...
    return
```

结果：

> 第一轮就结束整个函数。

#### count = 0 在循环里

```python
for number in numbers:
    count = 0
```

结果：

> 每一轮都会重新清零。

需要继续区分：

```text
计数器放错位置
≠
return 放错位置
```

---

### Git 第一次完整实操

今天第一次真正完成 Git 的最小流程。

先理解了：

```text
Git
= 本地版本控制工具

GitHub
= 在线代码托管平台
```

Git 不是 PowerShell 自带功能，而是电脑上安装的独立工具，只是通过终端调用。

完成操作：

```powershell
git init
```

把：

```text
D:\代码学习
```

初始化成 Git 仓库。

然后：

```powershell
git status
```

第一次看到：

```text
Untracked files
```

理解为：

> Git 看见这些文件，但还没有正式跟踪。

然后只添加今天的文件：

```powershell
git add "2026.09/w37/Daily_Sources/practice.7.py"
```

再次执行：

```powershell
git status
```

看到：

```text
Changes to be committed
```

说明文件已进入暂存区。

之后执行：

```powershell
git commit -m "add practice 7"
```

完成第一次本地提交。

最后：

```powershell
git log --oneline -1
```

看到：

```text
a5d816c (HEAD -> master) add practice 7
```

说明本地版本已经真正保存成功。

今天第一次完整走通：

```text
git init
→ git status
→ git add
→ git commit
→ git log
```

同时理解：

```text
git add
= 把当前文件版本放入下一次提交的准备区

git commit
= 正式保存一个本地版本

git push
= 以后才是上传到 GitHub
```

---

### 今日掌握情况

**明显进步：**

* API 基本流程
* `response.status_code`
* `response.json()`
* list / dict
* `for + if`
* 计数
* 函数参数
* 多返回值
* Git 最小操作
* 从一个问题迁移到另一个类似问题

**仍然需要继续巩固：**

* 多层缩进
* `return` 在真实代码中的位置
* 计数器初始化位置
* `try / except` 结构
* 函数数据层判断
* 从零独立写完整程序
* Git 暂存区 / commit / branch 的理解

---

### 今日评价

今天最重要的进步不是又学了多少新语法，而是第一次把很多已经学过的知识串成了一个完整的小项目：

```text
API
→ 数据
→ 循环
→ 条件判断
→ 函数
→ Debug
→ 文件保存
→ Git
```

而且晚上通过奇偶数统计证明，部分知识已经开始从“照着项目做”转向“可以迁移到新问题”。

今天可以判定为：

**Todo API 小统计器 V1：完成**

**Git 最小流程：首次实操完成**

**函数 / return / 循环：仍需继续巩固，但已经明显进步**

## W37 Review｜2026-09-07 ～ 2026-09-13

### 一、本周结论

**W37 状态：PASSED ✅**

本周原始计划的核心目标是完成：

* PowerShell / 命令行基础
* JSON 基础
* HTTP / API 基础
* 初步建立 Python 阅读能力

实际完成内容明显超过原计划，已经进一步进入：

* Python 基础语法与程序逻辑
* 真实 API 调用
* 函数与数据处理
* JSON 文件读写
* 基础异常处理
* Git 第一次完整实操
* 一个 API 数据处理 Mini Exercise
* 一个本地 Todo CLI 的早期版本

本周最大的成果不是“学了多少语法”，而是第一次建立了比较完整的程序思维链：

```text
数据
→ 判断
→ 循环
→ 函数
→ 返回值
→ API / JSON
→ 文件
→ Debug
→ Git
```

同时也确认了一个重要事实：

> 当前学习进度的“广度”明显快于原 Roadmap，但“深度”和独立复现能力还没有同步跟上。

因此 W37 可以通过，但不能把所有接触过的内容都算成“已经掌握”。

---

## 二、本周实际完成内容

### 1. PowerShell / 命令行

实际使用：

```text
pwd
dir
cd
cd ..
mkdir
New-Item
Set-Content
type
python xxx.py
```

能够：

* 查看当前位置
* 查看文件
* 切换目录
* 创建文件/文件夹
* 从 PowerShell 运行 Python 程序

目前这部分属于较稳定能力。

---

### 2. JSON

理解了：

```text
{}
Object / 对象

[]
Array / 数组

Key / Value
String
Number
Boolean
null
```

并能够读取类似：

```json
[
  {
    "title": "学习Python",
    "completed": true
  }
]
```

这样的嵌套数据。

已经能够理解：

```text
JSON Array → Python list
JSON Object → Python dict
```

并能够根据数据层级判断：

```python
data["todos"]
```

什么时候才是真正应该传给某个函数的数据。

---

### 3. HTTP / API

建立了以下基本链路：

```text
Python程序
→ Request
→ Server
→ Response
→ JSON
→ Python数据
```

理解：

* API 是程序之间通信的接口
* GET 用于向服务器获取数据
* Request 是请求
* Response 是服务器返回的 HTTP 响应
* `200 OK` 表示 HTTP 层面的请求成功

实际使用过：

```python
requests.get(url)
response.status_code
response.json()
```

并已经开始区分：

```text
response
response.json()
data
```

目前能够理解它们的总体关系，但精确定义仍需要继续巩固。

---

## 三、Python 本周完成内容

### 1. 基础数据与变量

使用过：

```python
name = "Arlo"
count = 10
completed = True
data = None
```

理解变量是给数据起名字。

---

### 2. list / dict

使用过：

```python
todos = [
    {"title": "学习Python", "completed": True},
    {"title": "健身", "completed": False}
]
```

能够：

```python
todo["title"]
todo["completed"]
```

读取 dict 中的字段。

---

### 3. 条件判断

使用：

```python
if
elif
else
```

理解 Python 会从上向下判断，并执行第一个成立的分支。

---

### 4. for 循环

能够遍历：

```python
for todo in todos:
    ...
```

并结合：

```python
if
```

完成筛选和统计。

---

### 5. 计数器

能够编写：

```python
completed_count = 0

for todo in todos:
    if todo["completed"] == True:
        completed_count += 1
```

本周曾反复出现的错误：

```python
for todo in todos:
    completed_count = 0
```

将计数器放进循环，导致每次遍历重新归零。

到 W37 周测时已经能够独立定位这个 Bug 的原因。

---

### 6. 函数

学习并实际使用：

```python
def function_name(parameter):
    ...
    return result
```

理解：

```text
参数
→ 函数接收的数据

return
→ 把结果返回给调用函数的位置
```

实际写过：

```python
def count_completed(todos):
    ...
```

以及多个 Todo 功能函数。

---

### 7. print / return / None

目前基本理解：

```python
print()
```

主要用于把结果显示出来。

```python
return
```

用于把值返回给调用函数的地方，并结束当前函数。

本周曾多次因为：

```python
return
```

缩进位置错误，导致函数只处理第一条数据。

W37 正式周测中已经能够闭卷正确放置 `return`。

---

### 8. 多返回值

接触并实际使用过：

```python
return completed_count, unfinished_count
```

以及：

```python
completed_count, unfinished_count = count_todos(data)
```

目前属于“接触过”，还不能算稳定掌握。

---

### 9. `.get()`

接触过：

```python
dict.get()
```

理解它可以在 Key 不存在时减少直接 `KeyError` 的风险。

目前仍属于接触级。

---

### 10. enumerate

接触并使用过：

```python
for index, todo in enumerate(todos, start=1):
```

理解可以同时获得：

```text
编号
+
元素
```

主要用于 Todo CLI 的任务编号显示。

目前属于接触级。

---

### 11. append / pop / break

实际使用：

```python
todos.append(todo)
todos.pop(index)
break
```

分别用于：

* 添加任务
* 删除任务
* 找到目标后结束当前循环

目前属于会用但尚未稳定掌握。

---

## 四、真实 API 实操

使用 `requests` 成功调用过真实 Todo API。

完成流程：

```text
requests.get()
→ response
→ status_code
→ response.json()
→ list / dict
→ for
→ if
→ count
→ function
→ return
```

最终成功处理：

```text
总任务：200
已完成：90
未完成：110
```

这次练习是本周第一次把：

```text
API
JSON
Python
函数
循环
统计
```

真正连接起来。

---

## 五、JSON 文件读写

学习：

```python
with open(...)
```

以及：

```python
json.load()
json.dump()
```

正确方向应固定为：

```text
json.load
JSON 文件 → Python 数据

json.dump
Python 数据 → JSON 文件
```

实际完成过：

```python
with open("todo_summary.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
```

并能够读取本地：

```text
todos.json
```

再交给 Python 函数处理。

这一能力当前属于 **🟡 会用但定义还不够稳定**。

---

## 六、异常与 Debug

本周实际遇到或处理过：

```text
NameError
TypeError
KeyError
ModuleNotFoundError
FileNotFoundError
JSONDecodeError
RequestException
SSL / 网络错误
语法错误
缩进错误
数据类型错误
```

目前 Debug 水平：

```text
Level 1：
能够阅读 Traceback
→ 找到报错行
→ 根据错误类型定位大概问题
```

还没有达到：

```text
Level 2：
运行前预测错误

Level 3：
通过代码设计提前避免错误
```

因此：

> “遇到很多报错”本身不算能力。

真正值得保留的是：

> 已经开始形成“看错误 → 找行号 → 判断类型 → 修改 → 重跑”的基本 Debug 流程。

---

## 七、try / except

学习过：

```python
try:
    ...
except:
    ...
```

并开始使用具体异常：

```python
except FileNotFoundError:
```

```python
except json.JSONDecodeError:
```

```python
except requests.exceptions.RequestException:
```

目前理解：

> `except` 不是“第二种方法”，而是发生指定异常后应该如何处理。

同时已经意识到：

> `try` 不应该把整个程序全部包起来，而应该尽量只包含真正可能发生该类异常的代码。

当前状态：**🟡**

---

## 八、Git

第一次实际走通：

```text
git init
→ git status
→ git add
→ git commit
→ git log
```

第一次真实 commit：

```text
a5d816c
add practice 7
```

并在 W37 周测中进一步重新确认：

```text
git add
→ 将本次准备提交的改动放入暂存区

git commit
→ 在本地 Git 仓库创建一个版本记录

git push
→ 将本地 commit 推送到 GitHub / 远程仓库
```

当前 Git 状态：

> 已经理解最基本主流程，但只有一次真正完整实操，因此仍不能算熟练能力。

W38 起 Git 不再作为单独知识点，而是开始作为持续工作习惯使用。

---

## 九、本周完成的练习 / Mini Exercise

### 1. Todo API Analyzer

完成链路：

```text
API
→ JSON
→ list/dict
→ for + if
→ count
→ function
→ exception
→ JSON save
→ Git
```

最终数据：

```text
Total: 200
Completed: 90
Unfinished: 110
```

---

### 2. Local Todo Analyzer

完成：

```text
读取 todos.json
→ Python list/dict
→ count_todos()
→ 返回统计结果
→ 写入 todo_summary.json
```

加入：

```text
FileNotFoundError
JSONDecodeError
```

异常处理。

---

### 3. Todo CLI 基础

进一步开始实现：

```text
Create
Read
Update
Delete
```

即 CRUD：

```text
add_todo()
show_todos()
complete_todo()
delete_todo()
```

并加入：

```text
load_todos()
save_todos()
```

完成 JSON 持久化，以及：

```text
while True
input()
菜单选择
```

这一部分主要发生在 W37 结束到 W38 开始的衔接阶段，因此它会继续作为 W38 的复习载体，而不作为 W37 已完全掌握的能力。

---

# 十、本周最重要的错误记录

### 1. return 放在 for 循环里面

错误：

```python
for todo in todos:
    ...
    return result
```

结果：

> 只处理第一条数据就结束函数。

正确思路：

```python
for todo in todos:
    ...

return result
```

---

### 2. 计数器放进循环

错误：

```python
for todo in todos:
    count = 0
```

结果：

> 每次循环重新归零。

正确：

```python
count = 0

for todo in todos:
    ...
```

---

### 3. 函数接收错误的数据层级

例如：

```python
data = {
    "todos": [...]
}
```

如果函数需要的是任务列表：

```python
def count_completed(todos):
```

应该：

```python
count_completed(data["todos"])
```

而不是：

```python
count_completed(data)
```

---

### 4. response 与 Python 数据混淆

需要继续强化：

```text
response
↓
response.json()
↓
Python list / dict
↓
data
```

---

### 5. input 返回字符串

理解：

```python
input()
```

默认得到：

```text
str
```

需要数字时：

```python
int(input())
```

---

### 6. 字符串与数字误操作

例如：

```python
"utf" - 8
```

会变成：

```text
str - int
```

从而触发 `TypeError`。

正确：

```python
"utf-8"
```

---

## 十一、W37 正式周测

### 闭卷唤醒

覆盖：

* Request / Response
* JSON
* print / return
* return 缩进
* load / dump
* try / except
* Git

总体状态约：

```text
70% 闭卷保留
```

主要问题集中在：

```text
概念边界不够精确
而不是完全忘记
```

---

### Part 1：空白写代码

闭卷完成：

```python
def count_completed(todos):
    completed_count = 0

    for todo in todos:
        if todo["completed"] == True:
            completed_count += 1

    return completed_count
```

成功输出：

```text
2
```

通过：

* 参数
* for
* if
* 计数器
* return

**结果：🟢**

---

### Part 2：Debug

面对：

```python
for todo in todos:
    unfinished_count = 0
```

能够正确指出：

> 计数器不应该在循环内部，否则每次遍历都会重新归零。

但第一次预测最终返回值时回答 `1`，实际应为 `0`，说明：

> Bug 原因已经理解，但逐行模拟程序执行仍需加强。

结果：

```text
Bug 原因：🟢
逐步执行预测：🟡
```

---

### Part 3：概念与数据层级

能够正确判断：

```python
count_completed(data["todos"])
```

并解释：

> `data["todos"]` 才是真正包含 Todo 的 list，函数需要遍历的是这一层。

也能够正确区分：

```text
FileNotFoundError
JSONDecodeError
```

并重新建立：

```text
git add
git commit
git push
```

主流程。

---

## 十二、W37 正式评分

**84 / 100**

该分数表示：

> W37 原计划能力目标已经通过，可以进入下一学习阶段。

它**不代表已经掌握 84% Python**。

评分体现的是：

```text
W37 本周目标完成情况
+
独立复现程度
+
Debug 能力
+
概念准确度
```

---

# 十三、W37 能力分级

## 🟢 比较稳定

* PowerShell 基本导航
* 运行 Python 文件
* JSON `{}` / `[]`
* Key / Value 基础
* Python 变量
* list / dict 基础
* `if / elif / else`
* `for` 基础遍历
* 计数器基本位置
* 简单函数
* 参数基本概念
* `return` 基础位置
* list of dict 数据访问
* Request → Server → Response
* HTTP 200 基础含义
* 函数接收正确数据层级
* `FileNotFoundError`
* `JSONDecodeError`
* Git add / commit / push 基本主链

---

## 🟡 会用，但需要继续强化

* `response` / `response.json()` / `data`
* `json.load()` / `json.dump()` 的准确方向
* `print` / `return` 的完整区别
* `return` 与函数结束
* 逐行模拟循环执行
* 函数参数设计
* try / except 的范围设计
* 较长程序从空白组织
* Git 持续使用
* 从 Traceback 之外进一步主动 Debug

---

## ⚪ 接触过，不计入稳定能力

* `enumerate`
* `append`
* `pop`
* `break`
* `input`
* `int`
* 多返回值
* `.get()`
* `RequestException`
* UTF-8 参数
* 更复杂 Git 操作
* 模块化
* venv
* `.env`
* `.gitignore`

---

# 十四、本周最重要的认识

### 1. Use ≠ Understand

程序成功运行：

> 不代表已经掌握。

真正掌握至少需要能够：

```text
不看旧代码
→ 空白复现
→ 解释数据流
→ 找出 Bug
```

---

### 2. AI 可以帮助写，但本人必须理解关键路径

未来目标不是：

> 完全不用 AI 写代码。

而是：

> AI 可以帮助开发，但我必须知道它改了什么、数据怎么流、哪里可能出错，并对最终结果负责。

---

### 3. 编程学习不能只统计“学过多少知识点”

本周看起来接触了很多内容，但真正稳定的能力明显少于知识清单数量。

以后学习进度使用：

```text
🟢 稳定
🟡 会用
⚪ 接触
```

而不是简单：

```text
学过 / 没学过
```

---

### 4. Debug 是独立能力

未来不能用：

> “我遇到过很多报错”

表示会 Debug。

需要逐渐提升：

```text
看 Traceback
↓
预测错误
↓
定位根因
↓
修改
↓
设计代码避免同类错误
```

---

# 十五、W37 暴露出的主要问题

### 1. 广度明显快于深度

一周内接触了大量概念，但不少仍停留在：

> 有提示能做。

因此不能简单继续无限增加新知识。

---

### 2. 数据层级仍是核心薄弱点

需要反复强化：

```text
response
↓
response.json()
↓
dict/list
↓
正确的数据层级
↓
函数
```

这是以后：

```text
POST
SQLite
FastAPI
LLM API
```

的共同地基。

---

### 3. 程序执行模拟能力不够稳定

例如能够判断计数器位置错误，却第一次算错最终返回值。

W38 需要增加：

> 不运行代码，先预测结果。

---

### 4. 从空白组织较长程序仍不足

目前已经能独立写小函数。

但如果要求从空白组织：

```text
40～80 行
多个函数
文件读写
错误处理
用户交互
```

仍然需要明显提示。

W38 将重点改善这一点。

---

# 十六、W38 带入项

W38 不重新从头复习 W37，而是在新任务中继续把黄色能力磨绿。

重点带入：

```text
1. response / response.json() / data

2. json.load / json.dump

3. return 与缩进

4. 参数和数据层级

5. try / except 边界

6. 逐行模拟程序执行

7. Git 持续实操

8. 从空白组织程序
```

---

# 十七、W37 最终评价

W37 是整个半年路线真正的起点。

本周从：

> “知道 AI、API、Python 是什么”

开始进入：

> “能够自己写出最基本的数据处理逻辑，并开始理解程序为什么这样运行”。

当前还远没有达到独立开发水平。

但已经完成了非常关键的一次转变：

```text
只会使用 AI 工具
↓
开始理解代码
↓
开始自己写代码
↓
开始自己 Debug
```

下一阶段不追求单纯增加更多技术名词。

W38 的核心目标是：

> **把“跟着能做”逐渐变成“自己能组织、能复现、能解释、能修”。**

---

## W37 Final Status

```text
STATUS: PASSED ✅

Score: 84 / 100

Next:
进入 W38
按 V1.1 Gate-based Learning System 执行
```

**W37 正式封账。**

