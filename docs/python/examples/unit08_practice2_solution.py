# 練習 2 參考解答：重複詢問直到輸入合法的整數
while True:
    try:
        n = int(input("請輸入整數："))
        break                           # 轉換成功才離開迴圈
    except ValueError:
        print("輸入錯誤，請重新輸入")

print("你輸入的是", n)
