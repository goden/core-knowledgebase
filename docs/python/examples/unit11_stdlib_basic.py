# 範例 1：math、random 與 statistics
import math
import random
import statistics

print(math.sqrt(16), math.ceil(2.1), math.floor(2.9), math.pi)

# 亂數每次結果不同；固定種子（seed）後，結果就能重現
random.seed(42)
a = random.randint(1, 100)
random.seed(42)
b = random.randint(1, 100)
print(a == b)

print(1 <= random.randint(1, 6) <= 6)                 # 骰子點數一定在 1 到 6
print(random.choice(["a", "b", "c"]) in ["a", "b", "c"])

deck = [1, 2, 3, 4, 5]
random.shuffle(deck)                                  # 原地洗牌
print(sorted(deck))                                   # 洗牌後排序，內容不變

data = [2, 4, 4, 4, 5, 5, 7, 9]
print(statistics.mean(data), statistics.median(data), statistics.mode(data))
print(statistics.pstdev(data))                        # 母體標準差
