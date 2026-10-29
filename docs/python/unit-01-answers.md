# 單元 1 答案：Python 基礎入門

請先自行作答再查看。題目見 [unit-01-basics.md](unit-01-basics.md)。

## 課堂練習參考解答
1. 程式：[examples/unit01_practice1_solution.py](examples/unit01_practice1_solution.py)

   ```python
   name = "小華"
   birth_year = 2000
   weight = 65.5

   print(name, type(name))
   print(birth_year, type(birth_year))
   print(weight, type(weight))
   ```

2. 程式：[examples/unit01_practice2_solution.py](examples/unit01_practice2_solution.py)

   ```python
   a = int(input("請輸入第一個整數："))
   b = int(input("請輸入第二個整數："))
   print("和：", a + b)
   print("3" + "5")   # 輸出 35，字串相加是串接
   ```

## 單元考題標準答案
1. **B**。`3.0` 有小數點，型別為 `float`。
2. **C**。`2name` 以數字開頭，`my-name` 含減號，`class` 是保留字。
3. `type(age)` 為 **`str`**（`input()` 一律回傳字串）；轉成整數寫 `age = `**`int`**`(age)`。
4. 程式：[examples/unit01_quiz4_solution.py](examples/unit01_quiz4_solution.py)

   ```python
   radius = float(input("請輸入半徑："))
   area = 3.14159 * radius ** 2
   print("圓面積：", round(area, 2))
   ```

   輸入 `2`，預期輸出：`圓面積： 12.57`
