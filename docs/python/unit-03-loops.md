# 單元 3：迴圈與迭代

## 學習目標
- 能使用 `for` 搭配 `range()` 與字串進行迭代。
- 能使用 `while` 依條件重複執行，並避免無限迴圈。
- 能使用 `break` 與 `continue` 控制迴圈流程，並撰寫簡單的巢狀迴圈。

## 一、概念說明
迴圈讓程式把相同的動作重複做很多次，就像洗衣機「注水 → 洗滌 → 脫水」依設定的圈數轉動，不必把同一段程式碼複製貼上。
- **`for`**：知道要跑幾次，或要逐一處理一批資料時使用。
- **`while`**：不確定跑幾次，只要條件成立就繼續時使用。

### `for` 與 `range()`
```python
for 變數 in 可迭代的資料:
    每一圈要做的事
```

| 寫法 | 產生的數字 |
|---|---|
| `range(5)` | `0, 1, 2, 3, 4` |
| `range(1, 6)` | `1, 2, 3, 4, 5` |
| `range(0, 10, 2)` | `0, 2, 4, 6, 8`（第三個參數為間隔） |
| `range(5, 0, -1)` | `5, 4, 3, 2, 1`（遞減） |

`range()` 的終點**不包含**在內。

### `while`
```python
while 條件:
    條件成立時重複執行
```
迴圈內必須有讓條件最終變成不成立的動作（如計數器加 1），否則會變成**無限迴圈**（終端機以 `Ctrl+C` 中斷）。

### `break` 與 `continue`
| 關鍵字 | 作用 |
|---|---|
| `break` | 立刻結束整個迴圈 |
| `continue` | 跳過本圈剩下的程式，直接進入下一圈 |

### 累加器與巢狀迴圈
- **累加器**：先設初始值（如 `total = 0`），在迴圈中逐步更新。
- **巢狀迴圈**：迴圈裡再放迴圈，外層跑一圈，內層完整跑一輪。

## 二、範例程式

### 範例 1：`for` 迴圈與 `range()`
程式：[examples/unit03_for.py](examples/unit03_for.py)

```python
for i in range(5):
    print(i, end=" ")   # end=" " 讓輸出不換行
print()                 # 單獨換行

total = 0
for n in range(1, 101):
    total += n
print("1 到 100 的總和：", total)

for ch in "Python":
    print(ch)
```

預期輸出：
```
0 1 2 3 4
1 到 100 的總和： 5050
P
y
t
h
o
n
```

### 範例 2：`while` 與 `break`（猜數字）
程式：[examples/unit03_guess.py](examples/unit03_guess.py)

```python
answer = 7

while True:
    guess = int(input("猜一個 1-10 的整數："))
    if guess == answer:
        print("答對了！")
        break
    elif guess < answer:
        print("太小了")
    else:
        print("太大了")
```

依序輸入 `3`、`9`、`7`，預期輸出：
```
太小了
太大了
答對了！
```

### 範例 3：`continue` 與巢狀迴圈
程式：[examples/unit03_continue_nested.py](examples/unit03_continue_nested.py)

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()
```

預期輸出：
```
1 3 5 7 9
1 2 3
2 4 6
3 6 9
```

## 三、常見錯誤
| 錯誤 | 原因 | 修正 |
|---|---|---|
| 程式一直跑不停 | `while` 條件永遠成立（忘了更新計數器） | 確認迴圈內有讓條件改變的動作，必要時 `Ctrl+C` 中斷 |
| 少算或多算一次 | `range()` 終點不含在內（Off-by-one） | 要包含 `n`，寫 `range(1, n + 1)` |
| `print` 的位置錯誤 | 縮排決定是否在迴圈內，如累加結果印在迴圈內會重複輸出 | 檢查縮排層級 |
| `TypeError: 'str' object cannot be interpreted as an integer` | 把 `input()` 的字串直接放進 `range()` | 先用 `int()` 轉換 |

## 四、課堂練習
1. 讓使用者輸入 `n`，用 `for` 計算 1 到 `n` 之間所有偶數的總和並印出。
   - 提示：用 `range()` 的第三個參數，或搭配 `if` 與 `%`。
2. 密碼驗證：讓使用者重複輸入密碼，輸入 `python123` 時印出「登入成功」並結束；連續錯誤 3 次，印出「帳號鎖定」。
   - 提示：用變數記錄失敗次數，搭配 `while` 與 `break`。

## 五、單元考題
1. **選擇題**：下列程式的輸出為何？
   ```python
   for i in range(2, 10, 3):
       print(i, end=" ")
   ```
   - A. `2 5 8`　B. `2 5 8 11`　C. `3 6 9`　D. `2 4 6 8`
2. **選擇題**：關於 `break` 與 `continue`，下列敘述何者正確？
   - A. 兩者都會結束整個迴圈
   - B. `break` 跳過本圈，`continue` 結束整個迴圈
   - C. `break` 結束整個迴圈，`continue` 跳過本圈並進入下一圈
   - D. 兩者都只能用在 `while` 迴圈
3. **填空題**：要計算 1 到 10 的總和，應寫 `for i in range(____, ____): total += i`；`while` 迴圈若忘記更新條件，會造成 ______。
4. **程式題**：用迴圈印出 1 到 20 的 FizzBuzz：3 的倍數印 `Fizz`，5 的倍數印 `Buzz`，同時是 3 與 5 的倍數印 `FizzBuzz`，其餘印數字本身（每個結果一行）。

答案與參考解答請作答後再查看：[unit-03-answers.md](unit-03-answers.md)

## 六、重點整理
- `for` 用於已知次數或逐一走訪資料；`while` 用於依條件重複。
- `range(起點, 終點, 間隔)` 不含終點。
- `break` 結束整個迴圈，`continue` 跳過本圈進入下一圈。
- 累加器需先設初始值；`while` 迴圈必須有讓條件結束的機制。
- 巢狀迴圈中，外層每跑一圈，內層完整跑一輪。

下一單元：容器型別
