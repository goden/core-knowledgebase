# 練習 1 參考解答：取得每個單字的長度
words = ["python", "is", "fun", "and", "powerful"]

# 方法一：map + lambda
print(list(map(lambda w: len(w), words)))

# 方法二：list 推導式
print([len(w) for w in words])
