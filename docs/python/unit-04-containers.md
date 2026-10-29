# 單元 4：容器型別

## 學習目標
- 能分辨 `list`、`tuple`、`dict`、`set` 的特性與適用情境。
- 能建立容器並進行新增、讀取、修改、刪除與走訪。
- 能搭配迴圈與條件判斷處理容器中的資料。

## 一、概念說明
單一變數只能放一份資料，容器則像收納盒，能把多份資料整理在一起。

| 型別 | 符號 | 有序 | 可修改 | 允許重複 | 適合用途 |
|---|---|---|---|---|---|
| `list` | `[1, 2, 3]` | 是 | 是 | 是 | 一串會增減的資料 |
| `tuple` | `(1, 2, 3)` | 是 | 否 | 是 | 固定不變的一組值（如座標） |
| `dict` | `{"a": 1}` | 是（依加入順序） | 是 | 鍵不可重複 | 用名稱查找資料 |
| `set` | `{1, 2, 3}` | 否 | 是 | 否 | 去重與集合運算 |

### list（串列）
- 索引從 `0` 開始，`-1` 代表最後一個。
- 切片 `lst[起點:終點]` 不含終點。
- 常用操作：

| 操作 | 說明 |
|---|---|
| `append(x)` | 加到最後 |
| `insert(i, x)` | 插入到索引 `i` |
| `remove(x)` | 移除第一個值為 `x` 的元素 |
| `pop()` / `pop(i)` | 取出並移除最後 / 指定位置的元素 |
| `len(lst)`、`x in lst` | 長度、是否包含 |
| `lst.sort()`、`sorted(lst)` | 原地排序、回傳排序後的新 list |
| `max()`、`min()`、`sum()` | 最大、最小、總和 |

### tuple（元組）
建立後不能修改。可「解包」成多個變數：`x, y = (3, 4)`。只有一個元素時要加逗號：`(1,)`。

### dict（字典）
用「鍵（key）」查找「值（value）」。
- 讀取：`d["key"]`（鍵不存在會 `KeyError`），或 `d.get("key", 預設值)`。
- 新增/修改：`d["key"] = value`；刪除：`del d["key"]`。
- 走訪：`d.keys()`、`d.values()`、`d.items()`。

### set（集合）
元素不重複、無固定順序。常用於去重與集合運算：`&` 交集、`|` 聯集、`-` 差集。

## 二、範例程式

### 範例 1：list 的建立與常用操作
程式：[examples/unit04_list.py](examples/unit04_list.py)

```python
fruits = ["蘋果", "香蕉", "橘子"]
print(fruits[0], fruits[-1])

fruits.append("葡萄")
fruits.insert(1, "芒果")
print(fruits)

fruits.remove("香蕉")
last = fruits.pop()
print(last, fruits)
print(len(fruits), "芒果" in fruits)

numbers = [5, 2, 9, 1]
print(numbers[1:3])
numbers.sort()
print(numbers)
```

預期輸出：
```
蘋果 橘子
['蘋果', '芒果', '香蕉', '橘子', '葡萄']
葡萄 ['蘋果', '芒果', '橘子']
3 True
[2, 9]
[1, 2, 5, 9]
```

### 範例 2：tuple 與 dict
程式：[examples/unit04_tuple_dict.py](examples/unit04_tuple_dict.py)

```python
point = (3, 4)
x, y = point
print(x, y)

student = {"name": "小明", "age": 20, "score": 85}
print(student["name"])

student["score"] = 90
student["city"] = "台北"
print(student.get("phone", "未提供"))
del student["age"]

for key, value in student.items():
    print(key, value)
print(len(student))
```

預期輸出：
```
3 4
小明
未提供
name 小明
score 90
city 台北
3
```

### 範例 3：set 與用 dict 統計次數
程式：[examples/unit04_set_count.py](examples/unit04_set_count.py)

```python
numbers = [1, 2, 2, 3, 3, 3, 4]
print(set(numbers))

a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a & b)
print(a | b)
print(a - b)

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
print(count)
```

預期輸出（集合無序，元素顯示順序可能不同）：
```
{1, 2, 3, 4}
{3, 4}
{1, 2, 3, 4, 5}
{1, 2}
{'apple': 3, 'banana': 2, 'cherry': 1}
```

## 三、常見錯誤
| 錯誤 | 原因 | 修正 |
|---|---|---|
| `IndexError: list index out of range` | 索引超出範圍（長度為 3 的 list 最大索引是 2） | 檢查 `len()`，或使用迴圈走訪 |
| `KeyError: 'phone'` | 讀取不存在的鍵 | 改用 `d.get("phone", 預設值)`，或先用 `in` 檢查 |
| `TypeError: 'tuple' object does not support item assignment` | 嘗試修改 tuple | 改用 list，或建立新的 tuple |
| `{}` 不是空集合 | `{}` 預設是空 `dict` | 空集合要寫 `set()` |
| `a = a.sort()` 之後 `a` 變成 `None` | `sort()` 原地排序並回傳 `None` | 直接呼叫 `a.sort()`，或用 `a = sorted(a)` |

## 四、課堂練習
1. 有 `scores = [72, 88, 95, 60, 83]`，印出最高分、最低分、總和與平均。
   - 提示：使用 `max()`、`min()`、`sum()` 與 `len()`。
2. 建立一個通訊錄 `dict`（姓名對應電話，內容自訂虛構資料），讓使用者輸入姓名查詢電話，查不到時印出「查無此人」。
   - 提示：使用 `get()` 並設定預設值。

## 五、單元考題
1. **選擇題**：下列哪一種型別建立後，內容不可修改？
   - A. `list`　B. `tuple`　C. `dict`　D. `set`
2. **選擇題**：`nums = [10, 20, 30, 40, 50]`，`nums[1:4]` 的結果是？
   - A. `[10, 20, 30]`　B. `[20, 30, 40]`　C. `[20, 30, 40, 50]`　D. `[10, 20, 30, 40]`
3. **填空題**：想從字典 `d` 安全取得可能不存在的鍵 `"key"`，避免 `KeyError`，應寫 `d.______("key", 預設值)`；想移除 list 中的重複元素，可先轉成 ______ 型別。
4. **程式題**：有 `scores = {"小明": 85, "小華": 58, "小美": 92, "小傑": 47}`，用迴圈印出所有不及格（低於 60 分）的學生姓名，最後印出不及格人數。

答案與參考解答請作答後再查看：[unit-04-answers.md](unit-04-answers.md)

## 六、重點整理
- `list` 有序可改、`tuple` 有序不可改、`dict` 以鍵查值、`set` 不重複且無序。
- list 索引從 0 開始，切片不含終點；`dict` 取值建議用 `get()`。
- 空集合要寫 `set()`，單元素 tuple 要加逗號。
- 容器常與 `for` 迴圈搭配走訪，`dict` 用 `items()` 同時取得鍵與值。

下一單元：函式與作用域
