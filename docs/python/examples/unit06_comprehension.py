# 範例 3：list、dict、set 推導式
nums = [1, 2, 3, 4, 5, 6]

squares = [x ** 2 for x in nums]                         # 轉換每個元素
print(squares)

evens = [x for x in nums if x % 2 == 0]                  # 加上篩選條件
print(evens)

labels = ["偶數" if x % 2 == 0 else "奇數" for x in nums]  # 以條件運算式決定值
print(labels)

square_map = {x: x ** 2 for x in range(1, 5)}           # dict 推導式
print(square_map)

lengths = {len(w) for w in ["apple", "fig", "kiwi", "pear"]}  # set 推導式，自動去重
print(lengths)
