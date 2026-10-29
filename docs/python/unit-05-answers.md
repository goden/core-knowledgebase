# 單元 5 答案：函式與作用域

請先自行作答再查看。題目見 [unit-05-functions.md](unit-05-functions.md)。

## 課堂練習參考解答
1. 程式：[examples/unit05_practice1_solution.py](examples/unit05_practice1_solution.py)

   ```python
   def bmi(height_cm, weight_kg):
       """依身高（公分）與體重（公斤）回傳 BMI，取到小數第 1 位"""
       height_m = height_cm / 100
       return round(weight_kg / (height_m ** 2), 1)


   print(bmi(175, 70))
   print(bmi(160, 50))
   ```

   預期輸出：
   ```
   22.9
   19.5
   ```

2. 程式：[examples/unit05_practice2_solution.py](examples/unit05_practice2_solution.py)

   ```python
   def average(numbers):
       """回傳平均值；空 list 回傳 0，避免除以零"""
       if len(numbers) == 0:
           return 0
       return sum(numbers) / len(numbers)


   print(average([80, 90, 100]))
   print(average([]))
   ```

   預期輸出：
   ```
   90.0
   0
   ```

## 單元考題標準答案
1. **C**。沒有 `return` 的函式預設回傳 `None`；函式不一定要有 `return`，`return` 之後的程式碼不會執行，`return` 與 `print` 也不同。
2. **A**。`f()` 內的 `x = 5` 是區域變數，回傳 `5 * 2 = 10`；全域的 `x` 仍是 `10`，所以輸出 `10 10`。
3. 第一格填 **`def`**；第二格填 **`global`**。
4. 程式：[examples/unit05_quiz4_solution.py](examples/unit05_quiz4_solution.py)

   ```python
   def is_prime(n):
       """n 為質數回傳 True，否則回傳 False"""
       if n < 2:
           return False
       for i in range(2, n):
           if n % i == 0:     # 找到因數就不是質數，立刻回傳
               return False
       return True


   for num in range(1, 21):
       if is_prime(num):
           print(num, end=" ")
   print()
   ```

   預期輸出：
   ```
   2 3 5 7 11 13 17 19
   ```

   進階：因數只需檢查到 `n` 的平方根，可改寫為 `range(2, int(n ** 0.5) + 1)` 以加快速度。
