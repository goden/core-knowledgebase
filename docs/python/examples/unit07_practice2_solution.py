# 練習 2 參考解答：解析日誌
import re

log = "2025-03-01 ERROR 資料庫連線失敗；2025-03-02 INFO 備份完成；2025-03-05 ERROR 磁碟空間不足"

print(re.findall(r"\d{4}-\d{2}-\d{2}", log))   # 取出所有日期
print(re.sub(r"ERROR", "錯誤", log))            # 把 ERROR 取代為 錯誤
