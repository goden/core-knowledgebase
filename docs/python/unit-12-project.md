# 單元 12：綜合實作專案——個人記帳本

## 學習目標
- 整合單元 1-11 的觀念，完成一個可執行的命令列小專案。
- 學會把程式依職責拆成多個模組，並撰寫簡單的自動化測試。
- 練習從需求出發，規劃、實作、測試與擴充程式。

## 一、專案需求
開發一個「個人記帳本」，在終端機操作：

| 編號 | 功能 | 說明 |
|---|---|---|
| 1 | 新增支出 | 輸入日期、類別、金額、備註，並檢查輸入是否合法 |
| 2 | 查看全部 | 依日期排序列出所有支出與總額 |
| 3 | 分類統計 | 依類別統計金額（由高到低），並列出金額最高的 3 筆 |
| 4 | 月份統計 | 輸入年月，顯示該月的支出總額 |
| 0 | 儲存並離開 | 資料存成 JSON 檔，下次執行自動載入 |

## 二、專案架構
程式放在 [examples/unit12_expense_tracker/](examples/unit12_expense_tracker/)，依職責拆成四個模組加一個測試檔：

| 檔案 | 職責 | 運用的單元 |
|---|---|---|
| [models.py](examples/unit12_expense_tracker/models.py) | `Expense` 類別、自訂例外、與 dict 互相轉換 | 5、8、10 |
| [storage.py](examples/unit12_expense_tracker/storage.py) | 以 JSON 讀寫檔案 | 8、9 |
| [report.py](examples/unit12_expense_tracker/report.py) | 總額、分類統計、月份統計、前 N 名 | 4、6、11 |
| [main.py](examples/unit12_expense_tracker/main.py) | 選單與使用者互動 | 2、3、5、6、7、9 |
| [test_tracker.py](examples/unit12_expense_tracker/test_tracker.py) | 自動化測試 | 5、8、9 |

設計原則：**職責分離**。資料模型、存取、統計、介面各管各的，彼此改動不會牽一髮動全身，也方便單獨測試。

```
main.py ──► models.py
   │          ▲
   ├──► report.py
   └──► storage.py ─┘
```

## 三、逐步實作

### 步驟 1：資料模型（models.py）
```python
from datetime import datetime


class InvalidExpenseError(ValueError):
    """支出資料不合法時拋出的例外"""


class Expense:
    def __init__(self, expense_date, category, amount, note=""):
        if amount <= 0:
            raise InvalidExpenseError("金額必須大於 0")
        if not category.strip():
            raise InvalidExpenseError("類別不可為空白")
        self.expense_date = expense_date
        self.category = category.strip()
        self.amount = amount
        self.note = note

    def to_dict(self):
        return {
            "date": self.expense_date.strftime("%Y-%m-%d"),
            "category": self.category,
            "amount": self.amount,
            "note": self.note,
        }

    def __str__(self):
        date_text = self.expense_date.strftime("%Y-%m-%d")
        return f"{date_text}  {self.category}  NT${self.amount:,}  {self.note}"


def expense_from_dict(data):
    expense_date = datetime.strptime(data["date"], "%Y-%m-%d").date()
    return Expense(expense_date, data["category"], data["amount"], data.get("note", ""))
```
重點：
- 在建構方法檢查資料，不合法就拋出**自訂例外**（單元 8、10）；`InvalidExpenseError` 繼承 `ValueError`，呼叫端以 `except ValueError` 即可一併處理。
- 日期存成 JSON 時要轉成字串（`strftime`），讀回時再用 `strptime` 還原（單元 11）。

### 步驟 2：檔案存取（storage.py）
```python
import json

from models import expense_from_dict


def load_expenses(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except FileNotFoundError:
        return []
    return [expense_from_dict(item) for item in raw]


def save_expenses(path, expenses):
    with open(path, "w", encoding="utf-8") as f:
        json.dump([e.to_dict() for e in expenses], f, ensure_ascii=False, indent=2)
```
重點：第一次執行時檔案不存在，視為「沒有資料」回傳空 list；檔案內容損毀時不在這裡硬處理，讓例外往外傳，由主程式決定怎麼辦。

### 步驟 3：統計報表（report.py）
```python
from collections import defaultdict


def total_amount(expenses):
    return sum([e.amount for e in expenses])


def total_by_category(expenses):
    totals = defaultdict(int)
    for e in expenses:
        totals[e.category] += e.amount
    return dict(totals)


def monthly_total(expenses, year, month):
    return sum([
        e.amount
        for e in expenses
        if e.expense_date.year == year and e.expense_date.month == month
    ])


def top_expenses(expenses, n=3):
    return sorted(expenses, key=lambda e: e.amount, reverse=True)[:n]
```
重點：這個模組只做計算，不做輸入輸出，所以容易測試；用到推導式、`defaultdict`、`sorted(key=...)` 與切片。

### 步驟 4：主程式（main.py）
主程式負責與使用者互動，結構如下：

```python
def main():
    try:
        expenses = load_expenses(DATA_FILE)
    except (ValueError, KeyError) as e:
        print("資料檔讀取失敗：", e)
        return

    actions = {"1": add_expense, "2": show_expenses, "3": show_report, "4": show_monthly}

    while True:
        print(MENU)
        choice = input("請選擇：").strip()
        if choice == "0":
            save_expenses(DATA_FILE, expenses)
            print("已儲存，再見！")
            break
        action = actions.get(choice)
        if action is None:
            print("無效的選項")
        else:
            action(expenses)
```
重點：
- **以 `dict` 對應選項與函式**（單元 4、6），取代一長串 `if` / `elif`。
- **載入失敗就結束**：若資料檔損毀卻用空 list 繼續執行，離開時存檔會把原檔覆蓋成空資料，造成資料遺失。
- 資料檔路徑用 `Path(__file__).parent / "expenses.json"`（單元 11），無論從哪個資料夾執行，檔案都放在程式旁邊。
- `add_expense()` 以 `try` / `except ValueError` 同時處理日期格式錯誤、金額不是數字與自訂的 `InvalidExpenseError`。

完整程式請見 [main.py](examples/unit12_expense_tracker/main.py)。

### 步驟 5：自動化測試（test_tracker.py）
測試用 `assert` 檢查結果：條件為 `False` 時會拋出 `AssertionError`，代表有錯。

```python
def make_sample():
    return [
        Expense(date(2025, 3, 1), "餐飲", 120, "午餐"),
        Expense(date(2025, 3, 5), "交通", 50),
        Expense(date(2025, 3, 9), "餐飲", 300, "聚餐"),
        Expense(date(2025, 4, 2), "娛樂", 800, "電影"),
    ]


def test_total():
    assert total_amount(make_sample()) == 1270


def test_by_category():
    assert total_by_category(make_sample()) == {"餐飲": 420, "交通": 50, "娛樂": 800}
```
完整測試共 7 項（總額、分類、月份、前 N 名、金額不合法、存檔讀檔、檔案不存在），見 [test_tracker.py](examples/unit12_expense_tracker/test_tracker.py)。測試先行有個好處：修改程式後重跑一次，就能確認沒有改壞既有功能。

## 四、執行方式
```powershell
cd docs\python\examples\unit12_expense_tracker
python test_tracker.py       # 先跑測試
python main.py               # 再執行記帳本
```

測試預期輸出：
```
通過： test_total
通過： test_by_category
通過： test_monthly
通過： test_top
通過： test_invalid_amount
通過： test_save_and_load
通過： test_load_missing_file
全部測試通過
```

操作範例：依序新增 `2025-03-01 餐飲 120 午餐`、`2025-03-05 交通 50`（備註留空）、`2025-03-09 餐飲 300 聚餐` 後：

- 選 `2`（查看全部）：
  ```
  2025-03-01  餐飲  NT$120  午餐
  2025-03-05  交通  NT$50
  2025-03-09  餐飲  NT$300  聚餐
  總支出：NT$470
  ```
- 選 `3`（分類統計）：
  ```
  餐飲：NT$420
  交通：NT$50
  金額最高的 3 筆：
    2025-03-09  餐飲  NT$300  聚餐
    2025-03-01  餐飲  NT$120  午餐
    2025-03-05  交通  NT$50
  ```
- 選 `4`（月份統計），輸入 `2025-03`：`2025 年 3 月支出：NT$470`
- 選 `0` 離開後，程式旁邊會出現 `expenses.json`，下次執行會自動載入。

## 五、常見錯誤
| 錯誤 | 原因 | 修正 |
|---|---|---|
| `ModuleNotFoundError: No module named 'models'` | 不是在專案資料夾內執行，或檔案不在同一資料夾 | 先 `cd` 到 `unit12_expense_tracker` 再執行 |
| 輸入日期後出現「輸入錯誤」 | 日期格式不是 `YYYY-MM-DD`（如 `2025/3/1`） | 依提示格式輸入，月份與日期補零 |
| 查詢月份統計得到 `NT$0` | 該月份沒有資料，或輸入的年月與資料不符 | 先用「查看全部」確認資料的日期 |
| `資料檔讀取失敗` | `expenses.json` 被手動修改而損毀 | 修正檔案內容，或刪除後重新建立（會遺失舊資料，請先備份） |
| 測試後留下 `test_expenses.json` | 測試中途失敗，暫存檔未被刪除 | 手動刪除即可；測試程式以 `finally` 盡量確保清除 |

## 六、專案實作任務
在完成基本功能後，試著自己擴充：

1. **刪除支出**：新增選項 `5`，列出編號後讓使用者選擇刪除哪一筆。
   - 提示：先把 `expenses` 排序，編號才會和畫面一致；注意編號範圍檢查，`0` 與負數不能傳給 `pop()`。
2. **預算提醒**：設定每月預算（如 10000 元），「月份統計」時若超過預算，額外顯示「已超過預算」。
   - 提示：定義常數 `MONTHLY_BUDGET`，在 `show_monthly()` 加一個 `if`。

## 七、單元考題
1. **選擇題**：專案將程式拆成 `models`、`storage`、`report`、`main` 四個模組，主要目的是？
   - A. 讓程式執行速度更快
   - B. 職責分離，各模組可獨立修改與測試
   - C. 讓檔案數量變多
   - D. 避免使用函式
2. **選擇題**：`test_tracker.py` 最下方的 `if __name__ == "__main__":` 區塊有什麼作用？
   - A. 讓測試每次都失敗
   - B. 只有直接執行該檔案時才跑測試，被其他程式匯入時不會執行
   - C. 讓檔案能被匯入
   - D. 自動安裝套件
3. **簡答題**：`main()` 在載入資料檔失敗時直接 `return`，而不是用空 list 繼續執行。為什麼？
4. **程式題**：在 `report.py` 風格下，寫函式 `average_amount(expenses)`，回傳平均每筆支出；沒有資料時回傳 `0`。
5. **程式題**：寫函式 `filter_by_category(expenses, category)`，回傳指定類別的支出 list（請用推導式）。

答案與參考解答請作答後再查看：[unit-12-answers.md](unit-12-answers.md)

## 八、重點整理
- 好的程式從拆解需求開始：先決定有哪些功能，再依職責拆成資料模型、存取、統計、介面。
- 把「計算」與「輸入輸出」分開，計算部分才容易測試。
- 在資料進入物件時就驗證（建構方法拋出自訂例外），並在使用者輸入處以 `try` / `except` 處理錯誤。
- 讀檔失敗時要避免覆蓋原有資料；存取外部資料一律指定 `encoding="utf-8"`。
- 用簡單的 `assert` 測試守住既有功能，修改程式後重跑即可。

## 課程回顧與下一步
完成 12 個單元後，你已具備 Python 的基礎能力：變數與型別、流程控制、容器、函式、字串與正規表達式、例外處理、檔案與模組、物件導向，以及套件與虛擬環境。

接下來可依興趣選擇進階課程：
- 資料儲存與查詢：「資料庫教學助教」（SQL、NoSQL、向量資料庫）
- 網路資料蒐集：「爬蟲大師」（requests、解析、jieba 與 Pandas）
- 資料分析與視覺化：「資料探勘教學助教」（NumPy、Pandas、Matplotlib）
- 預測與分群：「機器學習教學助教」（回歸、分類、分群）
