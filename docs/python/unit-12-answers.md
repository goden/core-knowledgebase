# 單元 12 答案：綜合實作專案——個人記帳本

請先自行作答再查看。題目見 [unit-12-project.md](unit-12-project.md)。

## 專案實作任務參考做法
以下為參考做法，並未實際執行驗證，請自行測試後再整合進 `main.py`。

1. **刪除支出**

   ```python
   def delete_expense(expenses):
       if not expenses:
           print("目前沒有資料")
           return

       expenses.sort(key=lambda e: e.expense_date)   # 先排序，讓編號與畫面一致
       number = 1
       for e in expenses:
           print(number, e)
           number += 1

       try:
           index = int(input("要刪除第幾筆："))
       except ValueError:
           print("請輸入數字")
           return

       if not 1 <= index <= len(expenses):            # 避免 0 或負數造成 pop(-1) 誤刪最後一筆
           print("編號超出範圍")
           return

       removed = expenses.pop(index - 1)
       print("已刪除：", removed)
   ```

   再把 `"5": delete_expense` 加進 `actions`，並在 `MENU` 加上「5. 刪除支出」。

2. **預算提醒**

   ```python
   MONTHLY_BUDGET = 10000


   def show_monthly(expenses):
       try:
           target = datetime.strptime(input("請輸入月份（YYYY-MM）："), "%Y-%m")
       except ValueError:
           print("月份格式錯誤")
           return
       amount = monthly_total(expenses, target.year, target.month)
       print(f"{target.year} 年 {target.month} 月支出：NT${amount:,}")
       if amount > MONTHLY_BUDGET:
           print("已超過預算")
   ```

## 單元考題標準答案
1. **B**。拆成多個模組是為了職責分離，讓各部分能獨立修改與測試；並不會讓程式更快。
2. **B**。該區塊只在直接執行檔案時才會跑；被其他程式 `import` 時不會執行，所以不會意外觸發測試。
3. 避免資料遺失。資料檔損毀只是「讀不出來」，原檔內容仍可能修復；若改用空 list 繼續，使用者離開時 `save_expenses()` 會用空資料覆蓋原檔，原本的紀錄就永遠消失了。
4. 程式：[quiz_solutions.py](examples/unit12_expense_tracker/quiz_solutions.py)

   ```python
   from report import total_amount


   def average_amount(expenses):
       if not expenses:
           return 0
       return total_amount(expenses) / len(expenses)
   ```

   重點：先判斷空 list，避免除以零；重用既有的 `total_amount()`，不重複寫加總邏輯。

5. 程式：[quiz_solutions.py](examples/unit12_expense_tracker/quiz_solutions.py)

   ```python
   def filter_by_category(expenses, category):
       return [e for e in expenses if e.category == category]
   ```

   以範例資料（金額 `100` 餐飲、`200` 交通、`300` 餐飲）執行 `python quiz_solutions.py`，預期輸出：
   ```
   200.0
   0
   [100, 300]
   ```
