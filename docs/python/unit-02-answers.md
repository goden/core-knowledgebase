# 單元 2 答案：運算子與條件判斷

請先自行作答再查看。題目見 [unit-02-operators-conditions.md](unit-02-operators-conditions.md)。

## 課堂練習參考解答
1. 程式：[examples/unit02_practice1_solution.py](examples/unit02_practice1_solution.py)

   ```python
   n = int(input("請輸入一個整數："))

   if n % 2 == 0:   # 除以 2 的餘數為 0 即為偶數
       print("偶數")
   else:
       print("奇數")
   ```

   輸入 `8` 輸出 `偶數`；輸入 `7` 輸出 `奇數`。

2. 程式：[examples/unit02_practice2_solution.py](examples/unit02_practice2_solution.py)

   ```python
   amount = float(input("請輸入購物金額："))

   # 由金額大的條件開始判斷
   if amount >= 3000:
       payable = amount * 0.8
   elif amount >= 1000:
       payable = amount * 0.9
   else:
       payable = amount

   print("應付金額：", round(payable, 1))
   ```

   | 輸入 | 預期輸出 |
   |---|---|
   | `3500` | `應付金額： 2800.0` |
   | `1200` | `應付金額： 1080.0` |
   | `800` | `應付金額： 800.0` |

   若先判斷 `amount >= 1000`，輸入 `3500` 會被誤判為 9 折，所以條件要由大到小排列。

## 單元考題標準答案
1. **B**。`7 // 2` 為 `3`（整數除法），`7 % 2` 為 `1`（餘數）。
2. **B**。`not (3 > 5)` 即 `not False`，結果為 `True`；A 為 `True and False`，C、D 皆為 `False`。
3. 第一格填 **`%`**，第二格填 **`==`**。
4. 程式：[examples/unit02_quiz4_solution.py](examples/unit02_quiz4_solution.py)

   ```python
   year = int(input("請輸入年份："))

   # 能被 4 整除且不能被 100 整除，或能被 400 整除
   if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
       print("閏年")
   else:
       print("平年")
   ```

   | 輸入 | 預期輸出 |
   |---|---|
   | `2024` | `閏年` |
   | `1900` | `平年` |
   | `2000` | `閏年` |
   | `2023` | `平年` |
