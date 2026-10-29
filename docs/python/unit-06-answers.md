# 單元 6 答案：進階函式

請先自行作答再查看。題目見 [unit-06-advanced-functions.md](unit-06-advanced-functions.md)。

## 課堂練習參考解答
1. 程式：[examples/unit06_practice1_solution.py](examples/unit06_practice1_solution.py)

   ```python
   words = ["python", "is", "fun", "and", "powerful"]

   # 方法一：map + lambda
   print(list(map(lambda w: len(w), words)))

   # 方法二：list 推導式
   print([len(w) for w in words])
   ```

   預期輸出（兩行相同）：
   ```
   [6, 2, 3, 3, 8]
   [6, 2, 3, 3, 8]
   ```

   補充：`map(len, words)` 可直接傳入內建函式，不一定要包成 `lambda`。

2. 程式：[examples/unit06_practice2_solution.py](examples/unit06_practice2_solution.py)

   ```python
   products = [("滑鼠", 590), ("鍵盤", 2480), ("耳機", 1890), ("充電器", 450)]

   print(sorted(products, key=lambda p: p[1], reverse=True))
   print([name for name, price in products if price >= 1000])
   ```

   預期輸出：
   ```
   [('鍵盤', 2480), ('耳機', 1890), ('滑鼠', 590), ('充電器', 450)]
   ['鍵盤', '耳機']
   ```

## 單元考題標準答案
1. **B**。`map` 對每個元素加 1，結果為 `[2, 3, 4]`。
2. **B**。`[x for x in nums if x > 3]` 結果為 `[5, 8]`。A 會得到布林值串列；C 的參數順序應為 `filter(函式, 資料)`，且需 `list()` 轉換；D 的條件運算式缺少 `else`，會 `SyntaxError`。
3. 第一格填 **`len`**；第二格填 **`reverse`**。
4. 程式：[examples/unit06_quiz4_solution.py](examples/unit06_quiz4_solution.py)

   ```python
   scores = {"小明": 85, "小華": 58, "小美": 92, "小傑": 47}

   status = {name: ("及格" if score >= 60 else "不及格") for name, score in scores.items()}
   print(status)

   for name, score in sorted(scores.items(), key=lambda item: item[1], reverse=True):
       print(name, score)
   ```

   預期輸出：
   ```
   {'小明': '及格', '小華': '不及格', '小美': '及格', '小傑': '不及格'}
   小美 92
   小明 85
   小華 58
   小傑 47
   ```
