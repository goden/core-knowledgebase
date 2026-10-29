# 單元 1：Python 基礎入門

## 學習目標
- 能安裝 Python 並以互動模式與腳本模式執行程式。
- 能正確命名並使用變數。
- 能分辨 `int`、`float`、`str`、`bool`，並使用 `type()` 與型別轉換函式。

## 一、安裝與執行環境
1. 到 python.org 下載 Python 3，安裝時務必勾選 **Add Python to PATH**。
2. 在 VS Code 安裝「Python」擴充套件。
3. 開啟終端機，確認安裝成功：

```powershell
python --version
```

輸出類似 `Python 3.13.5` 即成功。有兩種執行方式：
- **互動模式**：輸入 `python`，逐行輸入並立即看到結果，離開用 `exit()`。
- **腳本模式**：把程式存成 `hello.py`，執行 `python hello.py`。

## 二、變數：貼在資料上的標籤
變數像是貼在箱子上的標籤，箱子裡裝資料，`=` 表示「把標籤貼到這份資料上」。
- 名稱只能用英文字母、數字、底線，且不能以數字開頭。
- 區分大小寫（`Age` 與 `age` 不同）。
- 不能使用保留字（如 `class`、`if`）。
- 慣例使用小寫加底線，如 `my_name`。

## 三、四種基本資料型別
| 型別 | 說明 | 範例 |
|---|---|---|
| `int` | 整數 | `20`、`-5` |
| `float` | 小數 | `175.5`、`3.14` |
| `str` | 字串（文字） | `"小明"`、`'Hello'` |
| `bool` | 布林值 | `True`、`False`（首字母大寫） |

## 四、範例程式

### 範例 1：宣告變數並查看型別
程式：[examples/unit01_variables.py](examples/unit01_variables.py)

```python
name = "小明"        # 字串
age = 20             # 整數
height = 175.5       # 浮點數
is_student = True    # 布林值

print(name, age, height, is_student)
print(type(name), type(age), type(height), type(is_student))
```

預期輸出：
```
小明 20 175.5 True
<class 'str'> <class 'int'> <class 'float'> <class 'bool'>
```

變數可以重新指派，型別會跟著資料改變，例如 `age = "二十"` 之後 `age` 就變成 `str`。

### 範例 2：輸入與型別轉換（BMI 計算）
程式：[examples/unit01_bmi.py](examples/unit01_bmi.py)

```python
# input() 取得的內容一律是字串，必須轉換型別才能計算
height_cm = float(input("請輸入身高（公分）："))
weight_kg = float(input("請輸入體重（公斤）："))

height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)
print("你的 BMI 是：", round(bmi, 1))
```

輸入 `175`、`70`，預期輸出：
```
你的 BMI 是： 22.9
```

`/`、`**` 是運算子，單元 2 會詳細說明。型別轉換函式有 `int()`、`float()`、`str()`、`bool()`。

## 五、常見錯誤
| 錯誤訊息 | 原因 | 修正 |
|---|---|---|
| `NameError: name 'x' is not defined` | 使用了尚未指派的變數，或名稱大小寫打錯 | 先指派再使用，檢查拼字 |
| `TypeError: can only concatenate str (not "int") to str` | 字串與整數用 `+` 相加 | 以 `str()` 或 `int()` 統一型別 |
| `ValueError: invalid literal for int()` | 轉換的內容不是合法數字（如 `int("abc")`） | 確認輸入內容 |

## 六、課堂練習
1. 宣告 `name`（字串）、`birth_year`（整數）、`weight`（小數）三個變數，印出它們的值與型別。
   - 提示：參考範例 1。
2. 讓使用者輸入兩個整數，印出它們的和。
   - 提示：`input()` 回傳字串，需用 `int()` 轉換。可先試試不轉換時 `"3" + "5"` 的結果，觀察差異。

## 七、單元考題
1. **選擇題**：`type(3.0)` 的結果是哪一個？
   - A. `int`　B. `float`　C. `str`　D. `bool`
2. **選擇題**：下列哪一個是合法的變數名稱？
   - A. `2name`　B. `my-name`　C. `my_name`　D. `class`
3. **填空題**：執行 `age = input("年齡：")` 並輸入 `18` 後，`type(age)` 的結果是 ______；若要轉成整數，應寫 `age = ______(age)`。
4. **程式題**：讓使用者輸入圓的半徑（可為小數），計算圓面積（π 取 `3.14159`），並以 `round()` 取到小數第 2 位後印出。

答案與參考解答請作答後再查看：[unit-01-answers.md](unit-01-answers.md)

## 八、重點整理
- 變數是資料的標籤，型別由資料決定，可重新指派。
- 四種基本型別：`int`、`float`、`str`、`bool`。
- `input()` 一律回傳 `str`，計算前需轉換型別。
- `type()` 可查看型別，`int()` / `float()` / `str()` / `bool()` 可轉換型別。

下一單元：運算子與條件判斷
