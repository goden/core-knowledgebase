# 考題 4 參考解答：以 JSON 儲存成績並計算平均
import json

scores = {"小明": 85, "小華": 58, "小美": 92}

with open("unit09_scores.json", "w", encoding="utf-8") as f:
    json.dump(scores, f, ensure_ascii=False)     # 保留中文

with open("unit09_scores.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

average = sum(loaded.values()) / len(loaded)
print("平均分數：", round(average, 1))
