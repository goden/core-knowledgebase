# 練習 1 參考解答：計算 1 到 n 的偶數總和
n = int(input("請輸入 n："))

total = 0
for i in range(2, n + 1, 2):   # 從 2 開始，每次加 2，終點需 +1
    total += i

print("1 到", n, "的偶數總和：", total)
