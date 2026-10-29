# 單元 3 答案：迴圈與迭代

請先自行作答再查看。題目見 [unit-03-loops.md](unit-03-loops.md)。

## 課堂練習參考解答
1. 程式：[examples/unit03_practice1_solution.py](examples/unit03_practice1_solution.py)

   ```python
   n = int(input("請輸入 n："))

   total = 0
   for i in range(2, n + 1, 2):   # 從 2 開始，每次加 2，終點需 +1
       total += i

   print("1 到", n, "的偶數總和：", total)
   ```

   輸入 `10`，預期輸出：`1 到 10 的偶數總和： 30`（2 + 4 + 6 + 8 + 10）。

2. 程式：[examples/unit03_practice2_solution.py](examples/unit03_practice2_solution.py)

   ```python
   attempts = 0

   while attempts < 3:
       pwd = input("請輸入密碼：")
       if pwd == "python123":
           print("登入成功")
           break
       attempts += 1
       print("密碼錯誤，剩餘次數：", 3 - attempts)

   # 只有連續失敗 3 次，attempts 才會等於 3
   if attempts == 3:
       print("帳號鎖定")
   ```

   | 輸入順序 | 預期輸出 |
   |---|---|
   | `abc`、`python123` | `密碼錯誤，剩餘次數： 2`、`登入成功` |
   | `a`、`b`、`c` | `密碼錯誤，剩餘次數： 2`、`密碼錯誤，剩餘次數： 1`、`密碼錯誤，剩餘次數： 0`、`帳號鎖定` |

## 單元考題標準答案
1. **A**。`range(2, 10, 3)` 依序為 `2, 5, 8`，下一個 `11` 已超過終點 `10`。
2. **C**。`break` 結束整個迴圈；`continue` 只跳過本圈剩下的程式並進入下一圈；兩者在 `for` 與 `while` 都能使用。
3. 第一、二格填 **`1`、`11`**（終點不含在內，所以要 `11`）；忘記更新條件會造成**無限迴圈**。
4. 程式：[examples/unit03_quiz4_solution.py](examples/unit03_quiz4_solution.py)

   ```python
   for i in range(1, 21):
       # 15 的倍數必須最先判斷，否則會被 3 或 5 的條件攔截
       if i % 15 == 0:
           print("FizzBuzz")
       elif i % 3 == 0:
           print("Fizz")
       elif i % 5 == 0:
           print("Buzz")
       else:
           print(i)
   ```

   預期輸出（每行一個）：
   ```
   1
   2
   Fizz
   4
   Buzz
   Fizz
   7
   8
   Fizz
   Buzz
   11
   Fizz
   13
   14
   FizzBuzz
   16
   17
   Fizz
   19
   Buzz
   ```
