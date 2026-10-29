# 單元 9：檔案讀寫與模組

## 學習目標
- 能使用 `with open(...)` 讀取、寫入與附加文字檔，並正確指定編碼。
- 能使用 `json` 模組儲存與讀取結構化資料。
- 能使用 `import` 匯入標準模組，並建立與使用自訂模組。

## 一、概念說明
變數裡的資料在程式結束後就消失了；把資料存進**檔案**，才能長期保存、與別的程式交換。**模組**則是把程式碼拆成多個檔案，方便重複使用與維護。

### 開啟檔案
```python
with open("檔名", 模式, encoding="utf-8") as f:
    f.read() 或 f.write(...)
```

| 模式 | 說明 | 檔案不存在時 |
|---|---|---|
| `"r"` | 讀取（預設） | 發生 `FileNotFoundError` |
| `"w"` | 寫入，**會清空**既有內容 | 建立新檔 |
| `"a"` | 附加，內容加在最後 | 建立新檔 |

重點：
- **`with` 區塊**結束時會自動關閉檔案，即使中途發生例外也不例外，比手動 `close()` 安全，請固定使用。
- **一定要指定 `encoding="utf-8"`**。Windows 預設編碼不是 UTF-8，不指定時中文可能亂碼或出錯。
- 相對路徑是以「執行指令時所在的資料夾」為基準。

### 讀寫方法
| 方法 | 說明 |
|---|---|
| `f.read()` | 讀取全部內容，回傳一個字串 |
| `f.readline()` | 讀取一行 |
| `f.readlines()` | 讀取全部，回傳每行組成的 list |
| `for line in f:` | 逐行讀取（適合大檔案） |
| `f.write(字串)` | 寫入字串，**不會自動換行**，需自行加 `"\n"` |

讀出的每一行結尾都帶有換行字元，常搭配 `line.strip()` 去除。

### JSON：儲存結構化資料
`json` 模組可把 `dict`、`list` 等資料存成文字檔，也能讀回來。
- `json.dump(資料, f, ensure_ascii=False, indent=2)`：寫入檔案。`ensure_ascii=False` 讓中文保持原樣，`indent` 讓排版易讀。
- `json.load(f)`：從檔案讀回 Python 資料。
- Python 的 `True` / `None` 在 JSON 中是 `true` / `null`。

### 模組與 `import`
**模組**就是一個 `.py` 檔，檔名（不含 `.py`）即模組名稱。

| 寫法 | 使用方式 |
|---|---|
| `import math` | `math.sqrt(16)` |
| `from math import sqrt` | `sqrt(16)` |
| `import math as m` | `m.sqrt(16)` |

- Python 內建許多標準模組（`math`、`json`、`re`、`datetime`…），下一單元會再介紹。
- **自訂模組**：把函式與常數寫在 `mytools.py`，在同資料夾的其他程式中 `import mytools` 即可。
- `if __name__ == "__main__":`：區塊內的程式只在「直接執行該檔案」時才會跑，被 `import` 時不會執行，常用來放測試程式。
- 檔名不要和標準模組同名（如 `random.py`、`math.py`），否則會蓋掉標準模組。

## 二、範例程式

### 範例 1：文字檔的寫入、附加與讀取
程式：[examples/unit09_files.py](examples/unit09_files.py)

```python
FILE = "unit09_notes.txt"

with open(FILE, "w", encoding="utf-8") as f:
    f.write("第一行：Python\n")
    f.write("第二行：檔案讀寫\n")

with open(FILE, "a", encoding="utf-8") as f:
    f.write("第三行：附加的內容\n")

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()
print(content, end="")

print("--- 逐行讀取 ---")
with open(FILE, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

with open(FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()
print("共", len(lines), "行")
```

預期輸出：
```
第一行：Python
第二行：檔案讀寫
第三行：附加的內容
--- 逐行讀取 ---
第一行：Python
第二行：檔案讀寫
第三行：附加的內容
共 3 行
```

### 範例 2：JSON 讀寫與 `FileNotFoundError`
程式：[examples/unit09_json_error.py](examples/unit09_json_error.py)

```python
import json

data = {"name": "小明", "scores": [85, 92], "passed": True}

with open("unit09_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("unit09_data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded)
print(loaded["scores"][1])

try:
    with open("no_such_file.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("找不到檔案")
```

預期輸出：
```
{'name': '小明', 'scores': [85, 92], 'passed': True}
92
找不到檔案
```

產生的 `unit09_data.json` 內容：
```json
{
  "name": "小明",
  "scores": [
    85,
    92
  ],
  "passed": true
}
```

### 範例 3：匯入標準模組與自訂模組
自訂模組：[examples/unit09_mymath.py](examples/unit09_mymath.py)，使用程式：[examples/unit09_use_module.py](examples/unit09_use_module.py)（兩個檔案需放在同一個資料夾）。

```python
# unit09_mymath.py
"""自訂模組：簡單的數學工具。"""
PI = 3.14159


def circle_area(r):
    return PI * r ** 2


def is_even(n):
    return n % 2 == 0


if __name__ == "__main__":
    print("測試 circle_area(2)：", round(circle_area(2), 2))
```

```python
# unit09_use_module.py
import math
import unit09_mymath
from unit09_mymath import is_even

print(unit09_mymath.PI)
print(round(unit09_mymath.circle_area(3), 2))
print(is_even(10))

print(math.sqrt(16))
print(math.pi)
```

執行 `python unit09_use_module.py` 預期輸出（匯入時不會執行 `__main__` 區塊的測試）：
```
3.14159
28.27
True
4.0
3.141592653589793
```

直接執行 `python unit09_mymath.py` 則輸出：`測試 circle_area(2)： 12.57`

## 三、常見錯誤
| 錯誤 | 原因 | 修正 |
|---|---|---|
| `FileNotFoundError` | 路徑錯誤，或執行指令的資料夾與預期不同 | 確認檔名與目前所在資料夾，或改用完整路徑 |
| 中文亂碼或 `UnicodeDecodeError` | 沒指定編碼，或讀寫的編碼不一致 | 讀寫都加上 `encoding="utf-8"` |
| 原本的檔案內容不見了 | 以 `"w"` 開啟會清空既有內容 | 要保留舊內容請用 `"a"` |
| 檔案寫入後內容沒出現 | 沒有關閉檔案，資料還留在緩衝區 | 一律使用 `with` 區塊 |
| 第二次 `f.read()` 得到空字串 | 讀完後游標已在檔案結尾 | 重新開啟檔案，或用 `f.seek(0)` 回到開頭 |
| Windows 路徑 `"C:\new\test.txt"` 讀不到 | `\n`、`\t` 被當成跳脫字元 | 路徑字串前加 `r`，或改用 `/` |
| `ModuleNotFoundError` | 模組不在同一資料夾，或檔名拼錯 | 確認檔案位置與名稱，且不要與標準模組同名 |

## 四、課堂練習
1. 把 `names = ["小明", "小華", "小美"]` 每個名字一行寫入 `unit09_names.txt`，再讀回來，印出「共 N 行」與每一行的內容。
   - 提示：寫入時記得加 `"\n"`，讀回後用 `strip()` 去除換行。
2. 建立自訂模組 `unit09_temperature.py`，含 `c_to_f(c)`（攝氏轉華氏：`c * 9 / 5 + 32`）與 `f_to_c(f)`（華氏轉攝氏），再寫另一支程式匯入並印出 `c_to_f(100)` 與 `f_to_c(32)`。
   - 提示：兩個檔案放在同一個資料夾。

## 五、單元考題
1. **選擇題**：以 `"w"` 模式開啟一個已存在的檔案，會發生什麼事？
   - A. 內容附加在檔案最後
   - B. 清空原有內容後再寫入
   - C. 只能讀取，不能寫入
   - D. 一定會發生錯誤
2. **選擇題**：使用 `with open(...) as f:` 的主要好處是？
   - A. 讀取速度更快
   - B. 離開區塊時會自動關閉檔案
   - C. 不需要指定編碼
   - D. 可以同時開啟多個檔案
3. **填空題**：讀寫含中文的檔案時，應指定 `encoding="______"`；當模組被直接執行時，`__name__` 的值是 `"______"`。
4. **程式題**：把 `scores = {"小明": 85, "小華": 58, "小美": 92}` 以 JSON 存入 `unit09_scores.json`（保留中文），再讀回來，計算並印出平均分數（取到小數第 1 位）。

答案與參考解答請作答後再查看：[unit-09-answers.md](unit-09-answers.md)

## 六、重點整理
- 用 `with open(檔名, 模式, encoding="utf-8")` 讀寫檔案：`"r"` 讀、`"w"` 覆蓋寫、`"a"` 附加。
- `write()` 不會自動換行；逐行讀取時用 `strip()` 去除換行。
- `json.dump` / `json.load` 可存取 `dict`、`list` 等結構化資料，中文需 `ensure_ascii=False`。
- 模組就是 `.py` 檔，用 `import` 或 `from ... import` 使用；`if __name__ == "__main__":` 區塊只在直接執行時才會跑。

下一單元：物件導向程式設計
