# 範例 2：while 迴圈與 break（猜數字）
answer = 7

while True:                  # 無限迴圈，靠 break 結束
    guess = int(input("猜一個 1-10 的整數："))
    if guess == answer:
        print("答對了！")
        break                # 結束整個迴圈
    elif guess < answer:
        print("太小了")
    else:
        print("太大了")
