# 範例 2：成績等級判斷
score = int(input("請輸入分數："))

# 由高到低依序判斷，條件順序很重要
if score >= 90:
    print("等級：A")
elif score >= 80:
    print("等級：B")
elif score >= 60:
    print("等級：C")
else:
    print("等級：不及格")
