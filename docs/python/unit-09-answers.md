# 單元 9 答案：檔案讀寫與模組

請先自行作答再查看。題目見 [unit-09-files-modules.md](unit-09-files-modules.md)。

## 課堂練習參考解答
1. 程式：[examples/unit09_practice1_solution.py](examples/unit09_practice1_solution.py)

   ```python
   names = ["小明", "小華", "小美"]

   with open("unit09_names.txt", "w", encoding="utf-8") as f:
       for name in names:
           f.write(name + "\n")

   with open("unit09_names.txt", "r", encoding="utf-8") as f:
       lines = f.readlines()

   print("共", len(lines), "行")
   for line in lines:
       print(line.strip())
   ```

   預期輸出：
   ```
   共 3 行
   小明
   小華
   小美
   ```

2. 模組：[examples/unit09_temperature.py](examples/unit09_temperature.py)，使用程式：[examples/unit09_practice2_solution.py](examples/unit09_practice2_solution.py)

   ```python
   # unit09_temperature.py
   def c_to_f(c):
       return c * 9 / 5 + 32


   def f_to_c(f):
       return (f - 32) * 5 / 9
   ```

   ```python
   # unit09_practice2_solution.py
   from unit09_temperature import c_to_f, f_to_c

   print(c_to_f(100))
   print(f_to_c(32))
   ```

   預期輸出：
   ```
   212.0
   0.0
   ```

## 單元考題標準答案
1. **B**。`"w"` 會先清空既有內容再寫入；若要保留舊內容，應使用 `"a"`。
2. **B**。`with` 區塊結束時會自動關閉檔案，即使中途發生例外也一樣。
3. 第一格填 **`utf-8`**；第二格填 **`__main__`**。
4. 程式：[examples/unit09_quiz4_solution.py](examples/unit09_quiz4_solution.py)

   ```python
   import json

   scores = {"小明": 85, "小華": 58, "小美": 92}

   with open("unit09_scores.json", "w", encoding="utf-8") as f:
       json.dump(scores, f, ensure_ascii=False)

   with open("unit09_scores.json", "r", encoding="utf-8") as f:
       loaded = json.load(f)

   average = sum(loaded.values()) / len(loaded)
   print("平均分數：", round(average, 1))
   ```

   預期輸出：
   ```
   平均分數： 78.3
   ```

   計算：(85 + 58 + 92) / 3 = 78.333…，取到小數第 1 位為 78.3。
