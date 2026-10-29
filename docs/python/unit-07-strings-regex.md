# 單元 7：字串格式與正規表達式

## 學習目標
- 能使用字串方法與切片處理文字。
- 能使用 f-string 與 `format()` 輸出整齊的格式。
- 能使用 `re` 模組的 `match`、`search`、`findall`、`sub` 與分組擷取文字中的特定內容。

## 一、概念說明

### 字串方法與切片
字串是**不可變**的：所有方法都回傳新字串，不會改動原字串。

| 方法 | 說明 | 範例 → 結果 |
|---|---|---|
| `strip()` | 去除前後空白 | `" hi ".strip()` → `"hi"` |
| `upper()` / `lower()` | 轉大寫 / 小寫 | `"Ab".lower()` → `"ab"` |
| `replace(舊, 新)` | 取代 | `"cat".replace("c", "b")` → `"bat"` |
| `split(分隔)` | 切成 list | `"a,b".split(",")` → `["a", "b"]` |
| `join(list)` | 串成字串 | `"-".join(["a", "b"])` → `"a-b"` |
| `find(子字串)` | 回傳位置，找不到為 `-1` | `"hello".find("l")` → `2` |
| `count(子字串)` | 計算出現次數 | `"banana".count("a")` → `3` |
| `startswith()` / `endswith()` | 判斷開頭 / 結尾 | `"hello".startswith("he")` → `True` |

切片語法 `s[起點:終點:步進]`，終點不含；`s[::-1]` 可反轉字串。

### 字串格式化
**f-string**（推薦）：在字串前加 `f`，用 `{}` 放入變數或運算式。`{值:格式}` 可指定格式：

| 格式 | 說明 | 範例（`x = 1234.5`） | 結果 |
|---|---|---|---|
| `:.2f` | 小數 2 位 | `f"{x:.2f}"` | `1234.50` |
| `:,` | 千分位 | `f"{x:,}"` | `1,234.5` |
| `:05d` | 寬度 5、補 0 的整數 | `f"{7:05d}"` | `00007` |
| `:<5`、`:^5`、`:>5` | 靠左、置中、靠右（寬度 5） | `f"{'a':>5}"` | `"    a"` |
| `:.1%` | 百分比 | `f"{0.256:.1%}"` | `25.6%` |

**`format()`**：`"{} 的成績是 {}".format("小明", 95)`，也可用索引 `"{1} 與 {0}"`。舊式的 `%` 寫法（如 `"%d" % 5`）仍會在舊程式中看到，新程式建議使用 f-string。

### 正規表達式（Regular Expression）
用「規則」描述文字的樣子，再去文字中尋找、取代。規則字串前請加 `r`（raw string），避免反斜線被 Python 當成跳脫字元。

| 符號 | 意義 | 範例 |
|---|---|---|
| `.` | 任意一個字元（不含換行） | `a.c` 符合 `abc` |
| `\d` / `\w` / `\s` | 數字 / 文字（含中文、底線） / 空白 | `\d\d` 符合 `12` |
| `[abc]`、`[0-9]` | 括號內任一字元 | `[A-Z]` 符合大寫字母 |
| `*` / `+` / `?` | 0 次以上 / 1 次以上 / 0 或 1 次 | `\d+` 符合 `2025` |
| `{n}`、`{n,m}` | 剛好 n 次、n 到 m 次 | `\d{4}` 符合 4 位數字 |
| `^` / `$` | 字串開頭 / 結尾 | `^abc` |
| `\|` | 或 | `cat\|dog` |
| `( )` | 分組，可單獨取出 | `(\d+)-(\d+)` |

`re` 模組常用函式：

| 函式 | 作用 | 回傳 |
|---|---|---|
| `re.match(規則, 字串)` | 只比對字串**開頭** | Match 物件或 `None` |
| `re.search(規則, 字串)` | 找**第一個**符合的位置 | Match 物件或 `None` |
| `re.findall(規則, 字串)` | 找出**所有**符合的內容 | list |
| `re.sub(規則, 取代, 字串)` | 取代符合的內容 | 新字串 |

Match 物件用 `.group()` 取得整段符合內容，`.group(1)`、`.group(2)` 取得第 1、2 個分組。

## 二、範例程式

### 範例 1：字串方法、索引與切片
程式：[examples/unit07_string_methods.py](examples/unit07_string_methods.py)

```python
s = "  Hello, Python World!  "
text = s.strip()
print(text)

print(text.upper())
print(text.lower())
print(text.replace("World", "學習者"))
print(text.split(", "))
print("-".join(["a", "b", "c"]))

print(text[0], text[-1], text[7:13])
print(text[::-1])

print(text.find("Python"), text.count("o"), text.startswith("Hello"))
```

預期輸出：
```
Hello, Python World!
HELLO, PYTHON WORLD!
hello, python world!
Hello, Python 學習者!
['Hello', 'Python World!']
a-b-c
H ! Python
!dlroW nohtyP ,olleH
7 3 True
```

### 範例 2：f-string 與 `format()`
程式：[examples/unit07_format.py](examples/unit07_format.py)

```python
name = "小明"
age = 20
price = 1234567.891
seat = 7

print(f"{name} 今年 {age} 歲")
print(f"價格：{price:,.2f}")
print(f"座號：{seat:03d}")
print(f"{'L':<5}|{'C':^5}|{'R':>5}|")
print(f"{0.256:.1%}")

print("{} 的成績是 {}".format(name, 95))
print("{1} 與 {0}".format("A", "B"))
```

預期輸出：
```
小明 今年 20 歲
價格：1,234,567.89
座號：007
L    |  C  |    R|
25.6%
小明 的成績是 95
B 與 A
```

### 範例 3：`re` 模組
程式：[examples/unit07_regex.py](examples/unit07_regex.py)

```python
import re

text = "聯絡人：小明，電話 0912-345-678，Email：ming@example.com；備用 0922-111-222"

print(re.match(r"聯絡人", text) is not None)
print(re.match(r"電話", text))
print(re.search(r"\d{4}-\d{3}-\d{3}", text).group())
print(re.findall(r"\d{4}-\d{3}-\d{3}", text))
print(re.sub(r"\d{4}-\d{3}-\d{3}", "****", text))

m = re.search(r"(\w+)@(\w+)\.com", text)
print(m.group(0), m.group(1), m.group(2))

dates = "2025-03-01, 2025-12-25"
print(re.findall(r"(\d{4})-(\d{2})-(\d{2})", dates))
```

預期輸出：
```
True
None
0912-345-678
['0912-345-678', '0922-111-222']
聯絡人：小明，電話 ****，Email：ming@example.com；備用 ****
ming@example.com ming example
[('2025', '03', '01'), ('2025', '12', '25')]
```

## 三、常見錯誤
| 錯誤 | 原因 | 修正 |
|---|---|---|
| `TypeError: 'str' object does not support item assignment` | 想用 `s[0] = "h"` 修改字串 | 字串不可變，用 `replace()` 或切片組合出新字串 |
| `re.match` 找不到明明存在的內容 | `match` 只比對字串開頭 | 改用 `re.search` |
| `AttributeError: 'NoneType' object has no attribute 'group'` | `search` / `match` 找不到時回傳 `None` | 先判斷 `if m:` 再呼叫 `.group()` |
| `SyntaxWarning: invalid escape sequence '\d'` | 規則字串沒加 `r` | 寫成 `r"\d+"` |
| `findall` 結果變成 tuple 的 list | 規則中有分組（括號），回傳的是各分組 | 需要整段內容時，不加括號或改用 `(?:...)` |
| 擷取的數字無法計算 | 擷取結果是字串 | 用 `int()` 或 `float()` 轉換 |
| 對齊的中文字欄位歪掉 | 全形字元在畫面上占兩格，但格式化只算 1 個字元 | 中文對齊不要依賴寬度格式，或改用等寬處理套件 |

## 四、課堂練習
1. 有 `email = "  Alice.Smith@Example.COM  "`，去除前後空白並轉成小寫後，用 f-string 印出「帳號：…」與「網域：…」。
   - 提示：`strip()`、`lower()`、`split("@")`。
2. 有 `log = "2025-03-01 ERROR 資料庫連線失敗；2025-03-02 INFO 備份完成；2025-03-05 ERROR 磁碟空間不足"`，用正規表達式取出所有日期，並把 `ERROR` 取代為 `錯誤`。
   - 提示：日期規則 `\d{4}-\d{2}-\d{2}`，搭配 `findall` 與 `sub`。

## 五、單元考題
1. **選擇題**：`"Python"[1:4]` 的結果是？
   - A. `"Pyt"`　B. `"yth"`　C. `"ytho"`　D. `"ython"`
2. **選擇題**：`price = 1234.5`，哪一個寫法會輸出 `價格：1,234.50`？
   - A. `f"價格：{price:.2f}"`
   - B. `f"價格：{price:,.2f}"`
   - C. `f"價格：{price:,}"`
   - D. `f"價格：{price:05d}"`
3. **填空題**：要找出字串中「所有」符合的內容，使用 `re.______()`；只比對字串「開頭」，使用 `re.______()`。
4. **程式題**：有 `text = "訂單 A001 金額 1200 元，訂單 B002 金額 850 元，訂單 C003 金額 2300 元"`，用正規表達式取出每筆「訂單編號」與「金額」並印出，再計算總金額，以 f-string 加上千分位印出「總金額：…元」。

答案與參考解答請作答後再查看：[unit-07-answers.md](unit-07-answers.md)

## 六、重點整理
- 字串不可變，方法皆回傳新字串；切片終點不含，`[::-1]` 可反轉。
- f-string 以 `{值:格式}` 控制小數、千分位、補零與對齊；新程式優先使用 f-string。
- 正規表達式規則字串加 `r`；`match` 比對開頭、`search` 找第一個、`findall` 找全部、`sub` 取代。
- 括號分組可單獨取出內容；`search` / `match` 回傳 `None` 時需先判斷。

下一單元：例外處理
