"""
====================================================================
2026-11-24 Python 专项小测（闭卷）
====================================================================
【本次定位】第 1 章（1.5 / 1.6 / 1.7 / 1.8）专项巩固：三段式手写 + 字典 + JSON
【试卷难度】基础巩固 → 适中
【满分与时间】满分 100 分｜建议用时 15~25 分钟
【作答纪律】
  1. 闭卷独立完成，不翻看旧代码、不查资料；
  2. 卡住可以向老师要提示，但会按提示阶梯酌情扣分（1 级扣 20%，2 级扣 40%，3~4 级不计独立得分）；
  3. 写完直接回复“交卷”，由老师运行验证并逐题批改记分。
====================================================================
"""

import json


# ====================================================================
# 第 1 题（20 分｜读代码找 Bug，共 4 处，每处 5 分）
# 考察点：容器类型、字典键引号、json.dump 参数顺序、return 位置
#
# 下面的函数想实现：统计 records 里每个部门（"dept"）的人数，存入 JSON 文件并返回统计字典。
# 请找出代码中的 4 处错误，在下方 "# 作答：" 处写明【行号/错在哪/怎么改】（无需运行此段代码）。
#
#   1  def save_dept_count(records, filepath):
#   2      counts = []
#   3      for r in records:
#   4          dept = r[dept]
#   5          counts[dept] = counts.get(dept, 0) + 1
#   6      return counts
#   7      with open(filepath, "w", encoding="utf-8") as f:
#   8          json.dump(filepath, f, ensure_ascii=False, indent=2)
#
# 作答：
# 错误 1：Return应该是放在最后，不应该放在中间。
# 错误 2：应该是r["dept"]
# 错误 3：json.dump(counts)
# 错误 4：counts = {}
# ====================================================================


# ====================================================================
# 第 2 题（25 分｜核心函数手写：条件筛选）
# 考察点：三段式（空列表 -> for 循环筛选 -> 循环外 return）、字典取值
#
# 任务：从玩家战绩列表 records 中，找出所有分数 >= min_score 的玩家姓名，装进新列表返回。
#
# 输入样例：
#   records = [
#       {"name": "小明", "score": 12},
#       {"name": "小红", "score": 5},
#       {"name": "小刚", "score": 18},
#   ]
#   min_score = 10
# 期望输出：
#   ["小明", "小刚"]
# ====================================================================
def get_top_players(records, min_score):
    # TODO: 请在此作答
    name = []
    for record in records:
        if record["score"] >= min_score:
            name.append(record["name"])
    return name        

# ====================================================================
# 第 3 题（25 分｜核心函数手写：字典分类汇总）
# 考察点：空字典 {}、字典 .get(key, 0) 累加金额（注意不是数次数，是算总价！）
#
# 任务：遍历点餐列表 orders，统计每个分类（"category"）一共花了多少钱，返回汇总字典。
#
# 输入样例：
#   orders = [
#       {"name": "拉面", "category": "面食", "price": 18},
#       {"name": "黄焖鸡", "category": "中餐", "price": 24},
#       {"name": "河粉", "category": "面食", "price": 25},
#   ]
# 期望输出：
#   {"面食": 43, "中餐": 24}
# ====================================================================
def sum_price_by_category(orders):
    # TODO: 请在此作答
    total_prices = {}
    for s in orders:
        cat =s["category"]
        total_prices[cat] = total_prices.get(cat,0) + s["price"]
    return total_prices    



# ====================================================================
# 第 4 题（30 分｜核心函数手写：清洗过滤 + 字典组装 + JSON 存盘）
# 考察点：.strip() 真假值过滤、字典赋值 d[k] = v、with open + json.dump、return 位置
#
# 任务：
#   1. 遍历原始歌词列表 raw_lines，去掉每行首尾空格；忽略空行或纯空格行，
#      把剩下的有效歌词依次放进列表 clean_lines。
#   2. 建一个字典 data，把 title 作为键、clean_lines 作为值存进去（如 {"晴天": [...]}）。
#   3. 把 data 用 UTF-8 编码、ensure_ascii=False、indent=2 写入 filepath 对应的 JSON 文件。
#   4. 返回 data。
#
# 输入样例：
#   title = "晴天"
#   raw_lines = ["  故事的小黄花  ", "   ", "", "从出生那年就飘着 "]
#   filepath = "song_test.json"
# 期望输出：
#   {"晴天": ["故事的小黄花", "从出生那年就飘着"]}（同时生成内容一致的 song_test.json）
# ====================================================================
def save_clean_song(title, raw_lines, filepath):
    # TODO: 请在此作答
    clean_lines = []
    for lines in raw_lines:
        if lines.strip():
            clean_lines.append(lines.strip())
    data = {}
    data[title] = clean_lines 
    with open (filepath,"w", encoding= "utf-8")as f:
        json.dump(data,f,ensure_ascii= False,indent= 2)       
    return data
