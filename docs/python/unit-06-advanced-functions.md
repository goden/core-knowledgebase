# 單元 6：進階函式

## 學習目標
- 能使用 `lambda` 撰寫簡短的匿名函式。
- 能運用高階函式 `map()`、`filter()`、`sorted(key=...)` 處理資料。
- 能使用 list、dict、set 推導式，並判斷何時該用、何時不該用。

## 一、概念說明
單元 5 的函式是「有名字的食譜」；本單元的重點是：**函式本身也可以當成資料傳來傳去**。能接收函式當參數的函式，稱為**高階函式**。

### `lambda`（匿名函式）
```python
lambda 參數1, 參數2: 運算式
```
- 只能放**一個運算式**，結果自動回傳，不能寫 `return`，也不能放多行或指派敘述。
- 適合「只用一次的小函式」，通常直接傳給高階函式。
- `lambda x: x ** 2` 等同於 `def f(x): return x ** 2`。

### 常用高階函式
| 函式 | 作用 | 範例 |
|---|---|---|
| `map(func, 資料)` | 對每個元素套用 `func`，回傳新的結果 | `list(map(lambda x: x * 2, [1, 2]))` → `[2, 4]` |
| `filter(func, 資料)` | 只保留 `func` 回傳 `True` 的元素 | `list(filter(lambda x: x > 1, [1, 2]))` → `[2]` |
| `sorted(資料, key=func, reverse=False)` | 依 `func` 的結果排序，回傳新的 list | `sorted(words, key=len)` |
| `max(資料, key=func)`、`min(...)` | 依 `func` 的結果找最大、最小 | `max(students, key=lambda s: s[1])` |

`map()` 與 `filter()` 回傳的是「迭代器」，需用 `list()` 轉成串列才看得到內容。`sorted()` 不會改變原本的資料，這點與 `list.sort()` 不同。

### 推導式（Comprehension）
用一行建立容器，是 `map` / `filter` 更常見的替代寫法。

| 種類 | 語法 | 範例 |
|---|---|---|
| list | `[運算式 for 變數 in 資料 if 條件]` | `[x ** 2 for x in nums if x > 1]` |
| dict | `{鍵: 值 for 變數 in 資料}` | `{x: x ** 2 for x in range(3)}` |
| set | `{運算式 for 變數 in 資料}` | `{len(w) for w in words}` |

- `if` 放在最後是**篩選**；若要依條件決定**值**，寫成 `[A if 條件 else B for x in 資料]`。
- 推導式可有多層 `for`，但太複雜時改寫成一般迴圈，可讀性更重要。

## 二、範例程式

### 範例 1：`lambda` 與 `map()`、`filter()`
程式：[examples/unit06_lambda_map_filter.py](examples/unit06_lambda_map_filter.py)

```python
square = lambda x: x ** 2
print(square(5))

add = lambda a, b: a + b
print(add(3, 4))

nums = [1, 2, 3, 4, 5, 6]
squares = list(map(lambda x: x ** 2, nums))
print(squares)

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
```

預期輸出：
```
25
7
[1, 4, 9, 16, 25, 36]
[2, 4, 6]
```

### 範例 2：`sorted(key=...)` 與 `max(key=...)`
程式：[examples/unit06_sorted_key.py](examples/unit06_sorted_key.py)

```python
students = [("小明", 85), ("小華", 92), ("小美", 78)]

by_score = sorted(students, key=lambda s: s[1], reverse=True)
print(by_score)

words = ["banana", "kiwi", "apple", "fig"]
print(sorted(words, key=len))
print(words)

print(max(students, key=lambda s: s[1]))
```

預期輸出：
```
[('小華', 92), ('小明', 85), ('小美', 78)]
['fig', 'kiwi', 'apple', 'banana']
['banana', 'kiwi', 'apple', 'fig']
('小華', 92)
```

### 範例 3：推導式
程式：[examples/unit06_comprehension.py](examples/unit06_comprehension.py)

```python
nums = [1, 2, 3, 4, 5, 6]

squares = [x ** 2 for x in nums]
print(squares)

evens = [x for x in nums if x % 2 == 0]
print(evens)

labels = ["偶數" if x % 2 == 0 else "奇數" for x in nums]
print(labels)

square_map = {x: x ** 2 for x in range(1, 5)}
print(square_map)

lengths = {len(w) for w in ["apple", "fig", "kiwi", "pear"]}
print(lengths)
```

預期輸出（集合的顯示順序可能不同）：
```
[1, 4, 9, 16, 25, 36]
[2, 4, 6]
['奇數', '偶數', '奇數', '偶數', '奇數', '偶數']
{1: 1, 2: 4, 3: 9, 4: 16}
{3, 4, 5}
```

## 三、常見錯誤
| 錯誤 | 原因 | 修正 |
|---|---|---|
| 印出 `<map object at 0x...>` | `map()` / `filter()` 回傳迭代器 | 用 `list(...)` 轉換後再印出 |
| `SyntaxError` | 在 `lambda` 內寫了 `return`、多行或指派 | `lambda` 只能是單一運算式，複雜邏輯改用 `def` |
| `[x for x in nums if x > 3]` 與 `[x > 3 for x in nums]` 結果不同 | 前者篩選元素，後者把每個元素轉成 `True` / `False` | 篩選條件放最後，轉換放最前 |
| `NameError` 讀取推導式中的變數 | 推導式內的變數只在推導式內有效 | 需要時另外存入其他變數 |
| 推導式寫得又長又複雜，難以閱讀 | 為了「一行寫完」而過度濃縮 | 超過一個 `for` 加一個 `if` 時，改用一般迴圈 |

## 四、課堂練習
1. 有 `words = ["python", "is", "fun", "and", "powerful"]`，分別用 `map()` 搭配 `lambda`，以及 list 推導式，取得每個單字的長度。
   - 提示：長度用 `len()`。
2. 有 `products = [("滑鼠", 590), ("鍵盤", 2480), ("耳機", 1890), ("充電器", 450)]`，用 `sorted()` 依價格由高到低排序，再用推導式取出價格 1000 以上的商品名稱。
   - 提示：`key` 取每個 tuple 的第 2 個元素。

## 五、單元考題
1. **選擇題**：`list(map(lambda x: x + 1, [1, 2, 3]))` 的結果是？
   - A. `[1, 2, 3]`　B. `[2, 3, 4]`　C. `[1, 2, 3, 1]`　D. 會發生錯誤
2. **選擇題**：`nums = [1, 5, 2, 8, 3]`，下列哪一個運算式可取出大於 3 的元素？
   - A. `[x > 3 for x in nums]`
   - B. `[x for x in nums if x > 3]`
   - C. `filter(nums, lambda x: x > 3)`
   - D. `[x if x > 3 for x in nums]`
3. **填空題**：要將 `words` 依字串長度由長到短排序，應寫 `sorted(words, key=______, ______=True)`。
4. **程式題**：有 `scores = {"小明": 85, "小華": 58, "小美": 92, "小傑": 47}`。
   - (a) 用 dict 推導式產生「姓名對應 `及格` 或 `不及格`」的字典（60 分以上及格）並印出。
   - (b) 用 `sorted()` 搭配 `lambda`，依分數由高到低逐行印出「姓名 分數」。

答案與參考解答請作答後再查看：[unit-06-answers.md](unit-06-answers.md)

## 六、重點整理
- `lambda 參數: 運算式` 是單行匿名函式，適合傳給高階函式；複雜邏輯用 `def`。
- `map` 轉換、`filter` 篩選，兩者都要用 `list()` 取出結果；`sorted(key=...)` 依指定規則排序且不改動原資料。
- 推導式可建立 list、dict、set，語法為「運算式 + for + 選用 if」。
- 可讀性優先：太複雜的推導式或 `lambda`，改寫成一般迴圈或 `def`。

下一單元：字串格式與正規表達式
