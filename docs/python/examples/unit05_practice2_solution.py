# 練習 2 參考解答：計算平均
def average(numbers):
    """回傳平均值；空 list 回傳 0，避免除以零"""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


print(average([80, 90, 100]))
print(average([]))
