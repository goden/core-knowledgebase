# 考題 4 參考解答：找出不及格的學生
scores = {"小明": 85, "小華": 58, "小美": 92, "小傑": 47}

count = 0
for name, score in scores.items():
    if score < 60:
        print(name)
        count += 1

print("不及格人數：", count)
