# 考題 4 參考解答：FizzBuzz（1 到 20）
for i in range(1, 21):
    # 15 的倍數必須最先判斷，否則會被 3 或 5 的條件攔截
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
