# 考題 4 參考解答：判斷閏年
year = int(input("請輸入年份："))

# 能被 4 整除且不能被 100 整除，或能被 400 整除
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("閏年")
else:
    print("平年")
