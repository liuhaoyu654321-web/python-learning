"""
====================================================================
2026-11-26 Python 专项小测（闭卷）
====================================================================
【本次定位】第 1 章（1.5 / 1.6 / 1.7 / 1.8）通关验收：容器选型 + 引号规则 + 双层循环 + JSON
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
# 考察点：容器类型、写死字段名引号 vs 变量键名、open() 写入模式
#
# 下面的函数想实现：统计 items 里每个标签（"tags"）出现的次数，存入 JSON 文件并返回统计字典。
# 请找出代码中的 4 处错误，在下方 "# 作答：" 处写明【行号/错在哪/怎么改】（无需运行此段代码）。
#
#   1  def save_tag_counts(items, filepath):
#   2      counts = []
#   3      for item in items:
#   4          for tag in item[tags]:
#   5              counts["tag"] = counts.get(tag, 0) + 1
#   6      with open(filepath, encoding="utf-8") as f:
#   7          json.dump(counts, f, ensure_ascii=False, indent=2)
#   8      return counts
#
# 作答：
# 错误 1：26，不该用[],counts = {}
# 错误 2：28, []里面加引号,item["tags"]
# 错误 3：29，[]里的tag不用加引号，tag是变量，counts[tag]
# 错误 4：30,with open里面加"w",with open(filepath, encoding="utf-8") as f:
# ====================================================================


# ====================================================================
# 第 2 题（20 分｜核心函数手写：数字累加求和）
# 考察点：纯数字累加、字典取值、空列表边界处理
#
# 任务：遍历打牌记录列表 rounds，计算并返回所有记录中 "points" 的总和。
#       如果 rounds 是空列表 []，返回 0。
#
# 输入样例：
#   rounds = [
#       {"player": "小明", "points": 3},
#       {"player": "小红", "points": 5},
#   ]
# 期望输出：
#   8
# ====================================================================
def total_points(rounds):
    # TODO: 请在此作答
    total_points = 0
    for round in rounds:
        total_points += round["points"]
    return total_points    
    


# ====================================================================
# 第 3 题（25 分｜核心函数手写：字典分类累加）
# 考察点：空字典、分类作键、.get(key, 0) 累加数值、循环外 return
#
# 任务：遍历多局得分记录 records，统计每位玩家（"player"）累计得了多少分（"points"），
#       返回汇总字典 {玩家名: 总分}。
#
# 输入样例：
#   records = [
#       {"player": "小明", "points": 2},
#       {"player": "小红", "points": 3},
#       {"player": "小明", "points": 4},
#   ]
# 期望输出：
#   {"小明": 6, "小红": 3}
# ====================================================================
def sum_points_by_player(records):
    # TODO: 请在此作答
    score = {}
    for record in records:
        s = record["player"]
        score[s] = score.get(s,0) + record["points"]
    return score    


# ====================================================================
# 第 4 题（35 分｜核心函数手写：双层循环统计 + JSON 存盘）
# 考察点：双层 for 循环、变量键计数、with open + json.dump、return 位置
#
# 任务：
#   1. 遍历歌单列表 songs，每首歌有一个情绪标签列表 "moods"。
#      统计每种情绪标签一共出现了几次，存进字典 stats。
#   2. 把 stats 用 UTF-8 编码、ensure_ascii=False、indent=2 写入 filepath 对应的 JSON 文件。
#   3. 返回 stats。
#
# 输入样例：
#   songs = [
#       {"title": "晴天", "moods": ["怀旧", "温柔"]},
#       {"title": "七里香", "moods": ["怀旧"]},
#   ]
#   filepath = "mood_stats.json"
# 期望输出：
#   {"怀旧": 2, "温柔": 1}（同时生成内容一致的 mood_stats.json）
# ====================================================================
def save_mood_stats(songs, filepath):
    # TODO: 请在此作答
    status = {}
    for song in songs:
        moods = song["moods"]
        for mood in moods:
            status[mood] = status.get(mood,0) + 1
    with open(filepath,"w",encoding="utf-8") as f:
        json.dump(status,f,ensure_ascii=False,indent=2)
    return status    