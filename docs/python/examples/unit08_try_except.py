# 範例 1：try / except 處理不同的例外
try:
    n = int(input("請輸入整數："))     # 輸入非數字會發生 ValueError
    print("100 除以", n, "=", 100 / n)  # 輸入 0 會發生 ZeroDivisionError
except ValueError:
    print("請輸入有效的整數")
except ZeroDivisionError:
    print("不能除以 0")
