# 範例 2：預設參數、關鍵字引數與回傳多個值
def power(base, exponent=2):     # exponent 有預設值 2
    return base ** exponent


print(power(5))                  # 只傳 base，exponent 用預設值
print(power(2, 10))              # 依位置傳入
print(power(exponent=3, base=2)) # 以關鍵字傳入，順序可以不同


def min_max(numbers):
    return min(numbers), max(numbers)   # 以 tuple 同時回傳兩個值


low, high = min_max([4, 9, 1, 7])       # 解包接收
print(low, high)
