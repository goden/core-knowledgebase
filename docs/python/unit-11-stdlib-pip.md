# 單元 11：標準函式庫與套件管理

## 學習目標
- 認識常用的標準函式庫模組，並能查閱官方文件使用它們。
- 能使用 `venv` 建立虛擬環境，並用 `pip` 安裝、查詢、移除第三方套件。
- 能以 `requirements.txt` 記錄與重建專案的套件環境。

## 一、概念說明
Python 的口號是「內建電池」：安裝後就附帶一大批現成工具，稱為**標準函式庫**，`import` 就能用。不夠用時，再從 **PyPI**（Python 套件庫）安裝別人寫好的**第三方套件**，如 `requests`、`pandas`。

| 類型 | 來源 | 是否需要 `pip install` | 範例 |
|---|---|---|---|
| 標準函式庫 | 隨 Python 安裝 | 否 | `math`、`random`、`datetime`、`json`、`re` |
| 第三方套件 | PyPI | 是 | `requests`、`numpy`、`pandas` |
| 自訂模組 | 自己寫的 `.py` | 否 | 單元 9 的 `unit09_mymath` |

### 常用標準函式庫
| 模組 | 用途 | 常用內容 |
|---|---|---|
| `math` | 數學運算 | `sqrt()`、`ceil()`、`floor()`、`pi` |
| `random` | 亂數 | `randint(a, b)`、`choice(list)`、`shuffle(list)`、`sample()`、`seed()` |
| `statistics` | 基本統計 | `mean()`、`median()`、`mode()`、`stdev()`、`pstdev()` |
| `datetime` | 日期與時間 | `date`、`datetime`、`timedelta`、`strftime()`、`strptime()` |
| `collections` | 進階容器 | `Counter`（計數）、`defaultdict`（預設值字典） |
| `pathlib` | 檔案路徑 | `Path`、`/` 組合路徑、`.name`、`.suffix`、`.exists()` |
| `json`、`re` | JSON、正規表達式 | 單元 7、9 已介紹 |

日期格式碼：`%Y` 四位數年、`%m` 月、`%d` 日、`%H` 時（24 小時制）、`%M` 分、`%S` 秒。

查閱文件：遇到不熟的模組，可用 `help(模組)`、`dir(模組)`，或查閱官方文件，培養「自己查文件」的能力。

### 虛擬環境（venv）
每個專案需要的套件與版本不盡相同，全部裝在同一個地方容易互相衝突。**虛擬環境**為每個專案建立獨立的套件空間。

```powershell
python -m venv .venv              # 建立虛擬環境（資料夾名稱慣例為 .venv）
.venv\Scripts\Activate.ps1        # Windows PowerShell 啟用
source .venv/bin/activate         # macOS / Linux 啟用
deactivate                        # 離開虛擬環境
```
啟用後，終端機提示符前會出現 `(.venv)`。
- PowerShell 若因執行原則無法啟用，可先執行 `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`（只影響目前這個視窗）。
- 在 VS Code 以「Python: Select Interpreter」選擇 `.venv` 內的 Python，編輯器才會使用該環境。
- `.venv` 資料夾不要提交到版本控制。

### pip：套件管理
建議一律使用 `python -m pip`，確保裝到目前使用的那個 Python。

| 指令 | 說明 |
|---|---|
| `python -m pip install requests` | 安裝套件（最新版） |
| `python -m pip install requests==2.32.3` | 安裝指定版本 |
| `python -m pip install --upgrade requests` | 升級套件 |
| `python -m pip uninstall requests` | 移除套件 |
| `python -m pip list` | 列出已安裝的套件 |
| `python -m pip show requests` | 查看套件的版本與說明 |
| `python -m pip freeze > requirements.txt` | 把目前套件與版本輸出成清單 |
| `python -m pip install -r requirements.txt` | 依清單一次安裝所有套件 |

`requirements.txt` 範例：
```
requests==2.32.3
pandas==2.2.3
```
把它與程式碼一起保存，別人（或未來的你）就能用一行指令重建相同環境。

### 安裝套件的安全提醒
- 只安裝知名、有維護的套件，並仔細確認套件**名稱拼字**，避免誤裝名稱相似的惡意套件。
- 正式專案固定套件版本（如 `==2.32.3`），避免更新後行為改變。
- 不要在 `requirements.txt` 或程式碼中放入帳號、密碼或金鑰。

## 二、範例程式

### 範例 1：`math`、`random`、`statistics`
程式：[examples/unit11_stdlib_basic.py](examples/unit11_stdlib_basic.py)

```python
import math
import random
import statistics

print(math.sqrt(16), math.ceil(2.1), math.floor(2.9), math.pi)

random.seed(42)
a = random.randint(1, 100)
random.seed(42)
b = random.randint(1, 100)
print(a == b)

print(1 <= random.randint(1, 6) <= 6)
print(random.choice(["a", "b", "c"]) in ["a", "b", "c"])

deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
print(sorted(deck))

data = [2, 4, 4, 4, 5, 5, 7, 9]
print(statistics.mean(data), statistics.median(data), statistics.mode(data))
print(statistics.pstdev(data))
```

預期輸出：
```
4.0 3 2 3.141592653589793
True
True
True
[1, 2, 3, 4, 5]
5 4.5 4
2.0
```
亂數每次的實際數值不同，所以範例列印的是「一定成立」的判斷；固定相同的 `seed` 就能重現相同結果，常用於測試與機器學習實驗。

### 範例 2：`datetime`
程式：[examples/unit11_datetime.py](examples/unit11_datetime.py)

```python
from datetime import date, datetime, timedelta

d = date(2025, 3, 1)
print(d)
print(d + timedelta(days=30))
print(d.weekday())

print(d.strftime("%Y/%m/%d"))

dt = datetime.strptime("2025-12-25 18:30", "%Y-%m-%d %H:%M")
print(dt)

print((date(2025, 12, 25) - d).days)
```

預期輸出：
```
2025-03-01
2025-03-31
5
2025/03/01
2025-12-25 18:30:00
299
```
`weekday()` 星期一為 `0`、星期日為 `6`，2025-03-01 是星期六，所以是 `5`。`datetime.now()` 可取得目前時間，結果每次不同。

### 範例 3：`collections` 與 `pathlib`
程式：[examples/unit11_collections_path.py](examples/unit11_collections_path.py)

```python
from collections import Counter, defaultdict
from pathlib import Path

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(words)
print(counter)
print(counter.most_common(2))

groups = defaultdict(list)
for name, dept in [("小明", "研發"), ("小華", "業務"), ("小美", "研發")]:
    groups[dept].append(name)
print(dict(groups))

p = Path("data") / "report.txt"
print(p.name, p.suffix, p.stem)
print(p.exists())
```

預期輸出：
```
Counter({'apple': 3, 'banana': 2, 'cherry': 1})
[('apple', 3), ('banana', 2)]
{'研發': ['小明', '小美'], '業務': ['小華']}
report.txt .txt report
False
```
對照單元 4 手動用 `dict` 統計次數的寫法，`Counter` 一行就完成。

### 範例 4：使用第三方套件 `requests`
程式：[examples/unit11_requests.py](examples/unit11_requests.py)。需先在虛擬環境中執行 `python -m pip install requests`，且需連網。

```python
import requests

try:
    response = requests.get(
        "https://httpbin.org/get",
        params={"q": "python"},
        timeout=10,
    )
    print(response.status_code)
    print(response.json()["args"])
except requests.exceptions.RequestException as e:
    print("連線失敗：", e)
```

預期輸出（連線成功時）：
```
200
{'q': 'python'}
```
重點：`timeout` 一定要設定；網路請求容易失敗，需搭配單元 8 的例外處理。尚未安裝套件就執行，會出現 `ModuleNotFoundError: No module named 'requests'`。

## 三、常見錯誤
| 錯誤 | 原因 | 修正 |
|---|---|---|
| `ModuleNotFoundError: No module named 'xxx'` | 套件沒安裝，或裝在別的 Python / 沒有啟用虛擬環境 | 啟用虛擬環境後用 `python -m pip install xxx`，並確認 VS Code 選對直譯器 |
| `pip` 不是內部或外部命令 | `pip` 不在 PATH | 改用 `python -m pip ...` |
| PowerShell 無法執行 `Activate.ps1` | 系統的指令碼執行原則限制 | 執行 `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned` 後再啟用 |
| 匯入的是自己的檔案而不是標準模組 | 自己的檔案名稱與標準模組相同（如 `random.py`） | 重新命名自己的檔案，並刪除 `__pycache__` |
| 每次執行亂數結果不同，無法重現 | 沒有固定種子 | 需要重現時用 `random.seed(數字)` |
| `ValueError: time data ... does not match format` | `strptime` 的格式碼與字串不符 | 對照字串逐一檢查 `%Y`、`%m`、`%d` 與分隔符號 |

## 四、課堂練習
1. 用 `Counter` 找出字串 `"mississippi"` 中出現次數最多的 2 個字元與次數。
   - 提示：`Counter(字串)` 會統計每個字元，再用 `most_common(2)`。
2. 操作練習：在專案資料夾建立虛擬環境 `.venv` 並啟用，安裝 `requests`，用 `pip list` 與 `pip show requests` 確認，最後輸出 `requirements.txt`。
   - 提示：指令請參考「虛擬環境」與「pip」兩個表格。

## 五、單元考題
1. **選擇題**：下列哪一個屬於標準函式庫，不需要用 `pip` 安裝？
   - A. `requests`　B. `pandas`　C. `datetime`　D. `numpy`
2. **選擇題**：要把目前環境已安裝的套件與版本輸出成清單檔，應使用哪個指令？
   - A. `pip install requirements.txt`
   - B. `pip freeze > requirements.txt`
   - C. `pip show requirements.txt`
   - D. `pip save requirements.txt`
3. **填空題**：建立虛擬環境的指令是 `python -m ______ .venv`；依清單檔安裝所有套件是 `pip install ____ requirements.txt`。
4. **程式題**：用 `datetime` 計算 2025-01-01 到 2025-12-31 相差幾天，並印出 2025-01-01 之後 100 天的日期（格式 `年/月/日`），輸出為「相差天數：…」與「100 天後：…」。

答案與參考解答請作答後再查看：[unit-11-answers.md](unit-11-answers.md)

## 六、重點整理
- 標準函式庫隨 Python 附帶，`import` 即可使用；第三方套件要先用 `pip` 安裝。
- 常用模組：`math`、`random`、`statistics`、`datetime`、`collections`、`pathlib`。
- 每個專案使用獨立的虛擬環境（`python -m venv .venv`），避免套件互相衝突。
- 以 `python -m pip` 安裝與管理套件，用 `requirements.txt` 記錄並重建環境。
- 安裝套件要確認名稱與來源，並固定版本；網路請求要設定 `timeout` 並處理例外。

下一單元：綜合實作專案
