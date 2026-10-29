# 練習 2 參考解答：密碼驗證，最多嘗試 3 次
attempts = 0

while attempts < 3:
    pwd = input("請輸入密碼：")
    if pwd == "python123":
        print("登入成功")
        break
    attempts += 1
    print("密碼錯誤，剩餘次數：", 3 - attempts)

# 只有連續失敗 3 次，attempts 才會等於 3
if attempts == 3:
    print("帳號鎖定")
