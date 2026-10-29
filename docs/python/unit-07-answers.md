# 單元 7 答案：字串格式與正規表達式

請先自行作答再查看。題目見 [unit-07-strings-regex.md](unit-07-strings-regex.md)。

## 課堂練習參考解答
1. 程式：[examples/unit07_practice1_solution.py](examples/unit07_practice1_solution.py)

   ```python
   email = "  Alice.Smith@Example.COM  "

   email = email.strip().lower()
   user, domain = email.split("@")

   print(f"帳號：{user}")
   print(f"網域：{domain}")
   ```

   預期輸出：
   ```
   帳號：alice.smith
   網域：example.com
   ```

2. 程式：[examples/unit07_practice2_solution.py](examples/unit07_practice2_solution.py)

   ```python
   import re

   log = "2025-03-01 ERROR 資料庫連線失敗；2025-03-02 INFO 備份完成；2025-03-05 ERROR 磁碟空間不足"

   print(re.findall(r"\d{4}-\d{2}-\d{2}", log))
   print(re.sub(r"ERROR", "錯誤", log))
   ```

   預期輸出：
   ```
   ['2025-03-01', '2025-03-02', '2025-03-05']
   2025-03-01 錯誤 資料庫連線失敗；2025-03-02 INFO 備份完成；2025-03-05 錯誤 磁碟空間不足
   ```

## 單元考題標準答案
1. **B**。切片 `[1:4]` 取索引 1、2、3，即 `y`、`t`、`h`。
2. **B**。`:,.2f` 同時加上千分位與小數 2 位；A 沒有千分位；C 會輸出 `1,234.5`；D 的 `d` 只適用於整數，會發生 `ValueError`。
3. 第一格填 **`findall`**；第二格填 **`match`**。
4. 程式：[examples/unit07_quiz4_solution.py](examples/unit07_quiz4_solution.py)

   ```python
   import re

   text = "訂單 A001 金額 1200 元，訂單 B002 金額 850 元，訂單 C003 金額 2300 元"

   orders = re.findall(r"訂單 (\w+) 金額 (\d+) 元", text)
   print(orders)

   total = 0
   for order_id, amount in orders:
       total += int(amount)

   print(f"總金額：{total:,} 元")
   ```

   預期輸出：
   ```
   [('A001', '1200'), ('B002', '850'), ('C003', '2300')]
   總金額：4,350 元
   ```

   重點：兩組括號讓 `findall` 回傳 `(訂單編號, 金額)` 的 tuple；擷取到的金額是字串，加總前需 `int()` 轉換。
