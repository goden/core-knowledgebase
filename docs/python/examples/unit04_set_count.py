# 範例 3：set 的去重與集合運算，以及用 dict 統計次數
numbers = [1, 2, 2, 3, 3, 3, 4]
print(set(numbers))                  # 去除重複元素

a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a & b)                         # 交集
print(a | b)                         # 聯集
print(a - b)                         # 差集

# 用 dict 統計每個單字出現的次數
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1   # 不存在時從 0 開始累加
print(count)
