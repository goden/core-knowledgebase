# 範例 1：lambda 與 map()、filter()
square = lambda x: x ** 2        # 等同於 def square(x): return x ** 2
print(square(5))

add = lambda a, b: a + b
print(add(3, 4))

nums = [1, 2, 3, 4, 5, 6]

# map：對每個元素套用函式，回傳 map 物件，需用 list() 轉成串列
squares = list(map(lambda x: x ** 2, nums))
print(squares)

# filter：只保留函式回傳 True 的元素
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
