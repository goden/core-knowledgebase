# 考題 4 參考解答：及格判斷與成績排序
scores = {"小明": 85, "小華": 58, "小美": 92, "小傑": 47}

# dict 推導式：姓名對應及格狀態
status = {name: ("及格" if score >= 60 else "不及格") for name, score in scores.items()}
print(status)

# 依分數由高到低排序後逐行印出
for name, score in sorted(scores.items(), key=lambda item: item[1], reverse=True):
    print(name, score)
