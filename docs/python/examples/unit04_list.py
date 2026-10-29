# 範例 1：list 的建立與常用操作
fruits = ["蘋果", "香蕉", "橘子"]
print(fruits[0], fruits[-1])         # 索引從 0 開始，-1 代表最後一個

fruits.append("葡萄")                # 加到最後
fruits.insert(1, "芒果")             # 插入到索引 1 的位置
print(fruits)

fruits.remove("香蕉")                # 移除指定的值
last = fruits.pop()                  # 取出並移除最後一個
print(last, fruits)
print(len(fruits), "芒果" in fruits) # 長度與成員判斷

numbers = [5, 2, 9, 1]
print(numbers[1:3])                  # 切片：索引 1 到 2（不含 3）
numbers.sort()                       # 原地排序，不會回傳新 list
print(numbers)
