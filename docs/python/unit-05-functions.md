# 單元 5：函式與作用域

## 學習目標
- 能使用 `def` 定義函式，並正確使用參數與 `return`。
- 能運用預設參數、關鍵字引數，並回傳多個值。
- 能分辨區域變數與全域變數，理解 `global` 的用途與風險。

## 一、概念說明
函式像一份「食譜」或「自動販賣機」：投入材料（參數），照固定步驟處理，吐出結果（回傳值）。把重複的程式碼包成函式，可以少寫、好改、好測試。

### 定義與呼叫
```python
def 函式名稱(參數1, 參數2):
    """說明文字（docstring）"""
    要執行的程式
    return 回傳值
```
- 定義只是「寫好食譜」，要**呼叫**（`函式名稱(引數)`）才會執行。
- 函式名稱比照變數：小寫加底線。
- 第一行字串為 docstring，用來說明函式用途。

### `return` 與 `print` 的差別
| | `print()` | `return` |
|---|---|---|
| 作用 | 把內容顯示在畫面上 | 把結果交還給呼叫者，並結束函式 |
| 後續使用 | 無法再拿來運算 | 可存入變數或繼續運算 |

沒有 `return` 的函式，預設回傳 `None`。`return` 之後的程式碼不會執行。

### 參數的種類
- **預設參數**：`def power(base, exponent=2)`，呼叫時可省略 `exponent`。預設參數要放在沒有預設值的參數後面。
- **關鍵字引數**：呼叫時指定名稱 `power(exponent=3, base=2)`，順序可以不同。
- **回傳多個值**：`return a, b` 實際回傳一個 `tuple`，可用解包接收：`x, y = f()`。

### 作用域（Scope）
| 種類 | 定義位置 | 可使用範圍 |
|---|---|---|
| 區域變數 | 函式內 | 只有該函式內 |
| 全域變數 | 函式外（檔案最上層） | 整個檔案，函式內可讀取 |

- 函式內若對與全域同名的變數指派，會建立一個新的**區域變數**，不影響全域變數。
- 要在函式內修改全域變數，需先寫 `global 變數名稱`；但過度使用 `global` 會讓程式難以追蹤，建議改以參數傳入、`return` 傳出。

## 二、範例程式

### 範例 1：定義與呼叫函式
程式：[examples/unit05_basic.py](examples/unit05_basic.py)

```python
def greet(name):
    """回傳問候語"""
    return "哈囉，" + name + "！"


def add(a, b):
    return a + b


def say_hi():
    print("Hi")


message = greet("小明")
print(message)
print(add(3, 5))

result = say_hi()
print(result)
```

預期輸出：
```
哈囉，小明！
8
Hi
None
```

### 範例 2：預設參數、關鍵字引數與回傳多個值
程式：[examples/unit05_params.py](examples/unit05_params.py)

```python
def power(base, exponent=2):
    return base ** exponent


print(power(5))
print(power(2, 10))
print(power(exponent=3, base=2))


def min_max(numbers):
    return min(numbers), max(numbers)


low, high = min_max([4, 9, 1, 7])
print(low, high)
```

預期輸出：
```
25
1024
8
1 9
```

### 範例 3：區域變數與全域變數
程式：[examples/unit05_scope.py](examples/unit05_scope.py)

```python
count = 0


def add_one():
    count = 100
    return count + 1


print(add_one())
print(count)


def increase():
    global count
    count += 1


increase()
increase()
print(count)
```

預期輸出：
```
101
0
2
```

## 三、常見錯誤
| 錯誤 | 原因 | 修正 |
|---|---|---|
| 結果印出 `None` | 函式忘了 `return`，只用了 `print` | 改用 `return` 回傳結果 |
| `TypeError: add() missing 1 required positional argument: 'b'` | 呼叫時引數數量不足或過多 | 對照定義補齊引數 |
| `NameError: name 'x' is not defined` | 在函式外使用函式內的區域變數 | 以 `return` 傳出，或改在外面定義 |
| `UnboundLocalError` | 函式內寫 `count += 1`，卻沒宣告 `global`，Python 視 `count` 為區域變數 | 加上 `global count`，或改用參數與 `return` |
| 預設參數使用 `[]`（如 `def f(x, lst=[])`） | 預設的 list 只建立一次，多次呼叫會共用 | 預設值改用 `None`，在函式內再建立 list |

## 四、課堂練習
1. 寫一個函式 `bmi(height_cm, weight_kg)`，回傳 BMI（取到小數第 1 位）。以 `bmi(175, 70)` 與 `bmi(160, 50)` 測試。
   - 提示：沿用單元 1 的公式，注意用 `return` 而不是 `print`。
2. 寫一個函式 `average(numbers)`，回傳 list 中數字的平均值；若 list 是空的，回傳 `0`。
   - 提示：先用 `len()` 判斷是否為空，避免除以零。

## 五、單元考題
1. **選擇題**：關於 `return`，下列敘述何者正確？
   - A. 函式一定要有 `return`
   - B. `return` 之後的程式碼仍會繼續執行
   - C. 沒有 `return` 的函式，預設回傳 `None`
   - D. `return` 與 `print` 的作用完全相同
2. **選擇題**：下列程式的輸出為何？
   ```python
   x = 10

   def f():
       x = 5
       return x * 2

   print(f(), x)
   ```
   - A. `10 10`　B. `10 5`　C. `20 10`　D. `20 5`
3. **填空題**：定義函式使用的關鍵字是 ______；要在函式內修改全域變數 `count`，需先寫 ______ `count`。
4. **程式題**：寫一個函式 `is_prime(n)`，若 `n` 為質數回傳 `True`，否則回傳 `False`（小於 2 的數不是質數），並用迴圈印出 1 到 20 之間所有質數（同一行，以空白分隔）。

答案與參考解答請作答後再查看：[unit-05-answers.md](unit-05-answers.md)

## 六、重點整理
- `def` 定義函式，呼叫時才會執行；`return` 回傳結果並結束函式，沒寫則回傳 `None`。
- 預設參數放在後面，關鍵字引數可不依順序；`return a, b` 回傳 `tuple`。
- 函式內的變數是區域變數；修改全域變數需 `global`，但建議優先用參數與 `return`。
- 把重複的邏輯包成函式，是撰寫可維護程式的基本功。

下一單元：進階函式
