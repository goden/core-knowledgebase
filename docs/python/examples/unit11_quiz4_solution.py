# 考題 4 參考解答：日期計算
from datetime import date, timedelta

start = date(2025, 1, 1)
end = date(2025, 12, 31)

print("相差天數：", (end - start).days)
print("100 天後：", (start + timedelta(days=100)).strftime("%Y/%m/%d"))
