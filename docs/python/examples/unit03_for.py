# 範例 1：for 迴圈與 range()
# range(5) 產生 0, 1, 2, 3, 4（不含終點）
for i in range(5):
    print(i, end=" ")   # end=" " 讓輸出不換行
print()                 # 單獨換行

# 累加 1 到 100
total = 0
for n in range(1, 101):
    total += n
print("1 到 100 的總和：", total)

# 走訪字串中的每個字元
for ch in "Python":
    print(ch)
