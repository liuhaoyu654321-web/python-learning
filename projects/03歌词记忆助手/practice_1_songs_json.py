# 🟡 挖空练习 1：添加新歌并保存到 JSON 曲库（巩固循环清洗 + 字典赋值 + JSON 存盘）
# 【看懂优先级】🔴 现在要看懂（核心基本功）｜🟡 看大意就行（先不抠细节）｜🟢 现在完全不用管（工具套话/进阶语法，直接跳过）
# 目标：独立写出 1 个清洗多行歌词、加入曲库字典并保存为 JSON 文件的函数（约 8 行）

# 🟢 不用管：固定工具配置（导入 JSON 和文件路径模块）
import json
import os


# 🔴 现在要看懂并亲手写：核心挖空函数（循环清洗歌词 + 存字典 + JSON 存盘）
def add_and_save_song(filepath, songs, title, raw_lyrics):
    """清洗多行歌词、加入曲库字典 songs，并把整个 songs 保存到指定 JSON 文件。

    功能要求：
    1. 创建一个空列表 lines
    2. 遍历 raw_lyrics.splitlines() 中的每一行 s：
       如果 s.strip() 不是空的，就把 s.strip() 加进 lines 列表
    3. 把清洗好的歌词列表存进曲库字典：让 songs 里 key 为 title 的值等于 lines
    4. 用 with open(...) 以写入模式 ("w")、encoding="utf-8" 打开 filepath，
       再用 json.dump(...) 把整个 songs 写入文件（记得加 ensure_ascii=False, indent=2）
    5. 返回 lines

    输入样例与期望行为：
    - songs = {"送别": ["长亭外，古道边", "芳草碧连天"]}
    - title = "测试新歌"
    - raw_lyrics = "\n  第一句歌词  \n\n  第二句歌词\n   \n第三句歌词  "
    - 返回 ["第一句歌词", "第二句歌词", "第三句歌词"]
    - 同时 songs 里新增了 "测试新歌" 这一项，且 filepath 文件里保存了包含两首歌的 JSON
    """
    # TODO: 请在这里补全代码（约 8 行，写完删掉下面的 pass）
    lines = []
    for s in raw_lyrics.splitlines():
        if  s.strip():
            lines.append(s.strip())
    songs[title] = lines
    with open(filepath,"w",encoding="utf-8") as f :
        json.dump(songs,f,ensure_ascii=False,indent = 2)
    return lines    

                   
    



# --- 下方是配套读档函数与测试外壳，不用修改 ---

# 🟡 看大意就行：如果 JSON 曲库文件存在就读出来返回字典，否则返回 None
def load_songs(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


# 🟢 不用管：自动测试外壳，运行本文件会自动检查你写的函数对不对
if __name__ == "__main__":
    test_file = os.path.join(os.path.dirname(__file__), "test_songs.json")
    test_songs = {"送别": ["长亭外，古道边", "芳草碧连天"]}
    raw = "\n  第一句歌词  \n\n  第二句歌词\n   \n第三句歌词  "

    result = add_and_save_song(test_file, test_songs, "测试新歌", raw)
    print("清洗后的歌词列表：", result)
    assert result == ["第一句歌词", "第二句歌词", "第三句歌词"], f"返回值不对哦，实际拿到：{result}"
    assert test_songs.get("测试新歌") == result, "别忘了把清洗好的 lines 存进 songs[title]！"

    loaded = load_songs(test_file)
    print("从 JSON 读回来的曲库：", loaded)
    assert loaded is not None, "没有读到 JSON 文件，检查 with open 和 json.dump 是否正确写入！"
    assert loaded.get("测试新歌") == result, "JSON 文件里没找到新歌，检查是不是把整个 songs 存进去了！"
    assert loaded.get("送别") == ["长亭外，古道边", "芳草碧连天"], "原有歌曲丢了，确认保存的是整个 songs 字典！"

    os.remove(test_file)  # 测完顺手删掉临时测试文件
    print("[测试通过] 新歌清洗与 JSON 曲库存盘都搞定了！")
