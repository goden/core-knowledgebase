# 考題 4 參考解答：質數判斷
def is_prime(n):
    """n 為質數回傳 True，否則回傳 False"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:     # 找到因數就不是質數，立刻回傳
            return False
    return True


for num in range(1, 21):
    if is_prime(num):
        print(num, end=" ")
print()
