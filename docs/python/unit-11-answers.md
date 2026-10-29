# 單元 11 答案：標準函式庫與套件管理

請先自行作答再查看。題目見 [unit-11-stdlib-pip.md](unit-11-stdlib-pip.md)。

## 課堂練習參考解答
1. 程式：[examples/unit11_practice1_solution.py](examples/unit11_practice1_solution.py)

   ```python
   from collections import Counter

   text = "mississippi"
   counter = Counter(text)
   print(counter.most_common(2))
   ```

   預期輸出：
   ```
   [('i', 4), ('s', 4)]
   ```

   說明：`mississippi` 中 `i` 與 `s` 各出現 4 次、`p` 2 次、`m` 1 次；次數相同時，依第一次出現的順序排列。

2. 操作步驟（Windows PowerShell）：

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   python -m pip install requests
   python -m pip list
   python -m pip show requests
   python -m pip freeze > requirements.txt
   ```

   確認重點：
   - 啟用後提示符前出現 `(.venv)`。
   - `pip list` 會看到 `requests`，以及它依賴的套件（如 `urllib3`、`certifi`）。
   - `requirements.txt` 內容為「套件==版本」的清單；如需重建環境，執行 `python -m pip install -r requirements.txt`。

## 單元考題標準答案
1. **C**。`datetime` 是標準函式庫；`requests`、`pandas`、`numpy` 都是第三方套件，需要 `pip` 安裝。
2. **B**。`pip freeze > requirements.txt` 會把已安裝的套件與版本輸出到檔案。
3. 第一格填 **`venv`**；第二格填 **`-r`**。
4. 程式：[examples/unit11_quiz4_solution.py](examples/unit11_quiz4_solution.py)

   ```python
   from datetime import date, timedelta

   start = date(2025, 1, 1)
   end = date(2025, 12, 31)

   print("相差天數：", (end - start).days)
   print("100 天後：", (start + timedelta(days=100)).strftime("%Y/%m/%d"))
   ```

   預期輸出：
   ```
   相差天數： 364
   100 天後： 2025/04/11
   ```

   說明：2025 年不是閏年，共 365 天，1 月 1 日到 12 月 31 日相差 364 天；1 月 1 日加 100 天為 4 月 11 日。
