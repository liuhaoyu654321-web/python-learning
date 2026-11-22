# 决策转盘核心逻辑（全项目只需要看和改这一个文件！）
# 【看懂优先级】🔴 现在要看懂（核心基本功）｜🟡 看大意就行（先不抠细节）｜🟢 现在完全不用管（工具套话，跳过）

import json
import os
import random


# 🟡 看大意就行：从 JSON 读数据，没有文件就返回空结构
def load_data(filepath):
    if not os.path.exists(filepath):
        return {"items": [], "history": []}
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


# 🟡 看大意就行：把最新选项和历史记录存回 JSON 文件
def save_data(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# 🔴 现在要看懂：按最高预算和排除标签筛选候选列表（max_price 为 0 表示不限预算）
def filter_items(items, max_price=0, exclude_tags=None):
    exclude_tags = exclude_tags or []
    result = []
    for item in items:
        if max_price > 0 and item["price"] > max_price:
            continue
        if any(tag in item["tags"] for tag in exclude_tags):  # 🟢 any(...) 不用背：只要踩中任一避雷标签就跳过
            continue
        result.append(item)
    return result


# 🔴 现在要看懂：从筛选后的候选列表里随机抽 1 个中奖者
def pick_winner(candidates):
    if not candidates:
        return None
    return random.choice(candidates)


# 🔴 现在要看懂：用字典统计每个分类各抽中过几次（驱动网页右侧战绩榜）
def count_by_category(history):
    stats = {}
    for record in history:
        cat = record["category"]
        stats[cat] = stats.get(cat, 0) + 1
    return stats


# 🔴 现在要看懂：按屏幕上看到的 1 号、2 号编号删除选项（列表下标从 0 开始，所以减 1）
def delete_item(items, number):
    if 1 <= number <= len(items):
        return items.pop(number - 1)
    return None
