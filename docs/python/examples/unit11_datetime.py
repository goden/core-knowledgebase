# 範例 2：datetime 與 timedelta
from datetime import date, datetime, timedelta

d = date(2025, 3, 1)
print(d)
print(d + timedelta(days=30))              # 日期加減用 timedelta
print(d.weekday())                         # 星期一為 0，星期日為 6

print(d.strftime("%Y/%m/%d"))              # 日期轉成指定格式的字串

# strptime：把字串依格式解析成 datetime
dt = datetime.strptime("2025-12-25 18:30", "%Y-%m-%d %H:%M")
print(dt)

# 兩個日期相減得到 timedelta，.days 取天數
print((date(2025, 12, 25) - d).days)

# datetime.now() 取得目前時間，每次執行結果不同，故此處不列印
