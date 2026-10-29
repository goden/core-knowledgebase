# 單元 4 答案：容器型別

請先自行作答再查看。題目見 [unit-04-containers.md](unit-04-containers.md)。

## 課堂練習參考解答
1. 程式：[examples/unit04_practice1_solution.py](examples/unit04_practice1_solution.py)

   ```python
   scores = [72, 88, 95, 60, 83]

   print("最高分：", max(scores))
   print("最低分：", min(scores))
   print("總和：", sum(scores))
   print("平均：", sum(scores) / len(scores))
   ```

   預期輸出：
   ```
   最高分： 95
   最低分： 60
   總和： 398
   平均： 79.6
   ```

2. 程式：[examples/unit04_practice2_solution.py](examples/unit04_practice2_solution.py)

   ```python
   contacts = {"小明": "0911-111-111", "小華": "0922-222-222", "小美": "0933-333-333"}

   name = input("請輸入姓名：")
   print(contacts.get(name, "查無此人"))
   ```

   | 輸入 | 預期輸出 |
   |---|---|
   | `小華` | `0922-222-222` |
   | `小強` | `查無此人` |

## 單元考題標準答案
1. **B**。`tuple` 建立後不可修改；`list`、`dict`、`set` 皆可修改。
2. **B**。切片 `nums[1:4]` 取索引 1、2、3，不含 4，結果為 `[20, 30, 40]`。
3. 第一格填 **`get`**；第二格填 **`set`**（例如 `list(set(lst))`，但會失去原本順序）。
4. 程式：[examples/unit04_quiz4_solution.py](examples/unit04_quiz4_solution.py)

   ```python
   scores = {"小明": 85, "小華": 58, "小美": 92, "小傑": 47}

   count = 0
   for name, score in scores.items():
       if score < 60:
           print(name)
           count += 1

   print("不及格人數：", count)
   ```

   預期輸出：
   ```
   小華
   小傑
   不及格人數： 2
   ```
