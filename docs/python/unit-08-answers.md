# 單元 8 答案：例外處理

請先自行作答再查看。題目見 [unit-08-exceptions.md](unit-08-exceptions.md)。

## 課堂練習參考解答
1. 程式：[examples/unit08_practice1_solution.py](examples/unit08_practice1_solution.py)

   ```python
   def safe_int(text):
       """轉換成功回傳整數，失敗回傳 None"""
       try:
           return int(text)
       except ValueError:
           return None


   print(safe_int("42"))
   print(safe_int("4.5"))
   print(safe_int("abc"))
   ```

   預期輸出：
   ```
   42
   None
   None
   ```

2. 程式：[examples/unit08_practice2_solution.py](examples/unit08_practice2_solution.py)

   ```python
   while True:
       try:
           n = int(input("請輸入整數："))
           break
       except ValueError:
           print("輸入錯誤，請重新輸入")

   print("你輸入的是", n)
   ```

   依序輸入 `abc`、`3.5`、`7`，預期輸出：
   ```
   輸入錯誤，請重新輸入
   輸入錯誤，請重新輸入
   你輸入的是 7
   ```

## 單元考題標準答案
1. **B**。`"abc"` 是字串，但內容無法轉成整數，屬於「值不合法」的 `ValueError`。
2. **C**。`finally` 無論有沒有例外都會執行；`else` 才是沒有例外時執行，且兩者都可單獨使用。
3. 第一格填 **`KeyError`**（讀取不存在的鍵）；第二格填 **`as`**。
4. 程式：[examples/unit08_quiz4_solution.py](examples/unit08_quiz4_solution.py)

   ```python
   def safe_get(lst, index):
       """回傳指定索引的元素；索引錯誤時回傳說明文字"""
       try:
           return lst[index]
       except IndexError:
           return "索引超出範圍"
       except TypeError:
           return "索引必須是整數"


   print(safe_get([10, 20, 30], 1))
   print(safe_get([10, 20, 30], 5))
   print(safe_get([10, 20, 30], "a"))
   ```

   預期輸出：
   ```
   20
   索引超出範圍
   索引必須是整數
   ```

   重點：list 索引超出範圍是 `IndexError`；用字串當索引是 `TypeError`，兩種例外分開處理，給使用者更明確的訊息。
