# 單元 8：例外處理

## 學習目標
- 能閱讀錯誤訊息（Traceback），辨識常見的例外類型。
- 能使用 `try` / `except` / `else` / `finally` 處理例外。
- 能使用 `raise` 主動拋出例外，並養成只捕捉明確例外的習慣。

## 一、概念說明
程式執行時遇到無法處理的狀況（如把 `"abc"` 轉成整數、除以 0、讀不存在的檔案），Python 會拋出**例外**，若沒人處理，程式就會中斷並顯示錯誤訊息。

例外處理像是替程式準備「安全網」：先嘗試做事，出問題時走備案，而不是整個崩潰。

### 讀懂 Traceback
```
Traceback (most recent call last):
  File "demo.py", line 2, in <module>
    n = int("abc")
ValueError: invalid literal for int() with base 10: 'abc'
```
由下往上看：**最後一行**是例外類型與原因，上面是出錯的檔案與行號。

### 常見例外類型
| 例外 | 常見原因 | 範例 |
|---|---|---|
| `ValueError` | 值的格式不對 | `int("abc")` |
| `TypeError` | 型別不符 | `"3" + 5` |
| `ZeroDivisionError` | 除以 0 | `10 / 0` |
| `IndexError` | list 索引超出範圍 | `[1, 2][5]` |
| `KeyError` | dict 的鍵不存在 | `{"a": 1}["b"]` |
| `FileNotFoundError` | 開啟不存在的檔案 | `open("nofile.txt")` |
| `NameError` | 使用未定義的變數 | `print(x)` |
| `AttributeError` | 物件沒有該屬性或方法 | `"abc".foo()` |

### 語法
```python
try:
    可能出錯的程式
except 例外類型 as e:
    發生該例外時執行
else:
    沒有發生例外時執行
finally:
    無論如何都會執行（常用於收尾與釋放資源）
```
- 可有多個 `except`，由上而下比對，**第一個符合**的會執行。
- 同時處理多種例外：`except (ValueError, TypeError):`。
- `as e` 可取得例外物件，`print(e)` 顯示原因。
- `raise 例外類型("說明")` 可主動拋出例外。

## 二、範例程式

### 範例 1：`try` / `except` 處理不同的例外
程式：[examples/unit08_try_except.py](examples/unit08_try_except.py)

```python
try:
    n = int(input("請輸入整數："))
    print("100 除以", n, "=", 100 / n)
except ValueError:
    print("請輸入有效的整數")
except ZeroDivisionError:
    print("不能除以 0")
```

| 輸入 | 預期輸出 |
|---|---|
| `4` | `100 除以 4 = 25.0` |
| `abc` | `請輸入有效的整數` |
| `0` | `不能除以 0` |

### 範例 2：`as`、`else` 與 `finally`
程式：[examples/unit08_else_finally.py](examples/unit08_else_finally.py)

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("發生錯誤：", e)
        return None
    else:
        print("計算成功")
        return result
    finally:
        print("結束計算")


print(safe_divide(10, 2))
print(safe_divide(1, 0))
```

預期輸出（錯誤訊息文字可能依 Python 版本略有不同）：
```
計算成功
結束計算
5.0
發生錯誤： division by zero
結束計算
None
```
注意：即使 `return` 之後，`finally` 仍會先執行再離開函式。

### 範例 3：`raise` 與輸入驗證
程式：[examples/unit08_raise.py](examples/unit08_raise.py)

```python
def get_age(text):
    age = int(text)
    if age < 0 or age > 120:
        raise ValueError("年齡必須介於 0 到 120")
    return age


for text in ["25", "abc", "-5"]:
    try:
        print("年齡：", get_age(text))
    except ValueError as e:
        print("輸入錯誤：", e)
```

預期輸出：
```
年齡： 25
輸入錯誤： invalid literal for int() with base 10: 'abc'
輸入錯誤： 年齡必須介於 0 到 120
```

## 三、常見錯誤
| 做法 | 問題 | 建議 |
|---|---|---|
| `except:`（裸 `except`） | 連 `Ctrl+C` 中斷等例外都吞掉，錯誤難以追查 | 明確寫出例外類型，如 `except ValueError:` |
| `except Exception: pass` | 錯誤被默默吞掉，程式出錯卻毫無跡象 | 至少印出或記錄錯誤原因，或讓例外繼續往外傳 |
| 把整個程式都包在一個 `try` | 分不清是哪一行出錯 | `try` 只包住可能出錯的少數幾行 |
| 範圍大的例外放在前面 | 例如先寫 `except Exception`，後面的 `except ValueError` 永遠不會被執行 | 具體的例外在前，廣泛的在後 |
| 用例外取代一般的判斷 | 可用 `if` 事先檢查時，不需要 `try` | 可預期的情況用 `if`，無法預期的錯誤才用 `try` |

## 四、課堂練習
1. 寫函式 `safe_int(text)`：成功轉成整數就回傳該整數，失敗回傳 `None`。以 `"42"`、`"4.5"`、`"abc"` 測試。
   - 提示：`int("4.5")` 也會發生 `ValueError`。
2. 重複要求使用者輸入整數，直到輸入合法才結束，並印出「你輸入的是 …」；輸入不合法時印出「輸入錯誤，請重新輸入」。
   - 提示：`while True` 搭配 `try` / `except`，成功後用 `break`。

## 五、單元考題
1. **選擇題**：執行 `int("abc")` 會發生哪一種例外？
   - A. `TypeError`　B. `ValueError`　C. `NameError`　D. `KeyError`
2. **選擇題**：關於 `finally` 區塊，下列何者正確？
   - A. 只有發生例外才會執行
   - B. 只有沒發生例外才會執行
   - C. 無論有沒有發生例外都會執行
   - D. 一定要搭配 `else` 才能使用
3. **填空題**：
   ```python
   try:
       d = {"a": 1}
       print(d["b"])
   except ______:
       print("找不到鍵")
   ```
   空格應填入的例外類型是 ______；若要在 `except ValueError ____ e:` 取得例外物件，空格應填 ______。
4. **程式題**：寫函式 `safe_get(lst, index)`，回傳 list 指定索引的元素；索引超出範圍時回傳 `"索引超出範圍"`，索引不是整數時回傳 `"索引必須是整數"`。以 `safe_get([10, 20, 30], 1)`、`safe_get([10, 20, 30], 5)`、`safe_get([10, 20, 30], "a")` 測試。

答案與參考解答請作答後再查看：[unit-08-answers.md](unit-08-answers.md)

## 六、重點整理
- 例外是執行時的錯誤；Traceback 最後一行是例外類型與原因。
- `try` 放可能出錯的程式，`except` 處理錯誤，`else` 處理成功，`finally` 一定執行。
- 只捕捉明確的例外類型，避免裸 `except` 與默默吞掉錯誤。
- `raise` 可主動拋出例外；可預期的情況用 `if` 判斷，無法預期的錯誤才用 `try`。

下一單元：檔案讀寫與模組
