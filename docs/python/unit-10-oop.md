# 單元 10：物件導向程式設計

## 學習目標
- 能定義類別並建立物件，使用屬性與方法。
- 能理解 `self`、`__init__` 與 `__str__` 的用途，並以封裝保護資料。
- 能使用繼承、覆寫與 `super()`，並理解多型的意義。

## 一、概念說明
到目前為止，資料（變數）與處理資料的動作（函式）是分開的。**物件導向**把兩者綁在一起：
- **類別（class）**：藍圖，描述「這類東西有哪些資料、能做哪些事」。
- **物件（object）**：依藍圖建立出來的實體，也稱為**實例**。
- **屬性（attribute）**：物件擁有的資料，如姓名、分數。
- **方法（method）**：物件能執行的動作，即定義在類別內的函式。

比喻：「學生」這個類別像是學籍表格的格式；小明、小華各填一份，就是兩個學生物件，各自有自己的姓名與分數。

### 定義類別
```python
class 類別名稱:
    def __init__(self, 參數):
        self.屬性 = 參數

    def 方法(self, 參數):
        ...
```
- 類別名稱慣例使用**大駝峰**（每個字首大寫），如 `ShoppingCart`。
- `__init__`：建構方法，建立物件時自動執行，用來設定初始屬性。
- `self`：代表「正在操作的這個物件」，每個方法的第一個參數都必須是 `self`，呼叫時不需要傳入。
- `__str__`：定義 `print(物件)` 時顯示的文字。
- **實例屬性**（`self.name`）每個物件各自擁有；**類別屬性**（寫在類別內、方法外）由所有物件共用。

### 封裝
把資料與操作資料的規則放在同一個類別，外部透過方法存取，由方法檢查資料是否合法（如存款金額必須大於 0）。Python 以**命名慣例**表示內部使用：屬性名稱以單底線開頭（如 `_balance`），提醒外部不要直接修改，但這並非強制限制。

### 繼承
子類別繼承父類別的屬性與方法，只需寫出差異的部分。
```python
class Dog(Animal):
    ...
```
- **覆寫（override）**：子類別定義與父類別同名的方法，改變其行為。
- **`super()`**：呼叫父類別的方法，常用於 `super().__init__(...)`。
- **多型**：不同類別的物件都有同名方法，呼叫端不需要分辨類別，各物件會執行自己版本的方法。
- `isinstance(物件, 類別)` 可判斷物件是否屬於某類別（含其子類別）。

### 自訂例外
繼承 `Exception`（或其子類別）即可建立自己的例外，讓錯誤訊息更明確，呼叫端也能針對性地處理：
```python
class InsufficientFundsError(Exception):
    """餘額不足時拋出的例外"""
```

## 二、範例程式

### 範例 1：類別、物件、屬性與方法
程式：[examples/unit10_student.py](examples/unit10_student.py)

```python
class Student:
    school = "Python 學院"

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_passed(self):
        return self.score >= 60

    def add_score(self, points):
        self.score += points

    def __str__(self):
        return f"{self.name}（{self.score} 分）"


s1 = Student("小明", 85)
s2 = Student("小華", 58)

print(s1)
print(s2.is_passed())
s2.add_score(5)
print(s2.score, s2.is_passed())
print(s1.school, Student.school)
```

預期輸出：
```
小明（85 分）
False
63 True
Python 學院 Python 學院
```

### 範例 2：封裝與自訂例外
程式：[examples/unit10_bank.py](examples/unit10_bank.py)

```python
class InsufficientFundsError(Exception):
    """餘額不足時拋出的例外"""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金額必須大於 0")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsError("餘額不足")
        self._balance -= amount

    def get_balance(self):
        return self._balance


account = BankAccount("小明", 1000)
account.deposit(500)
print(account.get_balance())

try:
    account.withdraw(2000)
except InsufficientFundsError as e:
    print("提款失敗：", e)

account.withdraw(300)
print(account.get_balance())
```

預期輸出：
```
1500
提款失敗： 餘額不足
1200
```

### 範例 3：繼承、覆寫與多型
程式：[examples/unit10_inherit.py](examples/unit10_inherit.py)

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def intro(self):
        return f"我是 {self.name}，我會說：{self.speak()}"


class Dog(Animal):
    def speak(self):
        return "汪汪"


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return "喵喵"


animals = [Dog("小黑"), Cat("小花", "白色"), Animal("路人")]

for a in animals:
    print(a.intro())

print(isinstance(animals[0], Animal), isinstance(animals[0], Cat))
print(animals[1].color)
```

預期輸出：
```
我是 小黑，我會說：汪汪
我是 小花，我會說：喵喵
我是 路人，我會說：...
True False
白色
```

## 三、常見錯誤
| 錯誤 | 原因 | 修正 |
|---|---|---|
| `TypeError: method() takes 1 positional argument but 2 were given` | 方法忘了寫 `self` 參數 | 每個方法第一個參數都要是 `self` |
| `AttributeError: 'Student' object has no attribute 'name'` | `__init__` 內寫成 `name = name`，沒有加 `self.`；或 `__init__` 拼錯（需前後各兩個底線） | 使用 `self.name = name`，並確認 `__init__` 拼寫 |
| 子類別出現 `AttributeError` | 子類別有自己的 `__init__`，卻沒有呼叫 `super().__init__(...)` | 在子類別的 `__init__` 呼叫 `super().__init__(...)` |
| 多個物件的資料互相影響 | 把可變的 list 或 dict 寫成類別屬性，所有物件共用同一份 | 可變資料放在 `__init__` 中，以 `self.items = []` 建立 |
| 以為 `_balance` 無法被外部修改 | 單底線只是慣例，並非強制限制 | 遵守慣例，透過方法存取；不要在類別外直接改動 |
| 類別名稱寫成 `student` | 不符慣例，易與變數混淆 | 類別使用大駝峰，如 `Student` |

## 四、課堂練習
1. 設計 `Rectangle` 類別：屬性 `width`、`height`；方法 `area()`（面積）、`perimeter()`（周長）；並以 `__str__` 讓 `print(Rectangle(3, 4))` 顯示 `長方形 3x4`。印出 `Rectangle(3, 4)` 的面積與周長。
   - 提示：屬性在 `__init__` 中以 `self.` 設定。
2. 設計 `Employee`（屬性 `name`、`salary` 月薪；方法 `annual_salary()` 回傳月薪 × 12），再設計繼承它的 `Manager`，多一個屬性 `bonus`，並覆寫 `annual_salary()`，結果要再加上 `bonus`。測試 `Employee("小明", 40000)` 與 `Manager("小華", 60000, 100000)`。
   - 提示：覆寫時用 `super().annual_salary()` 取得父類別的結果。

## 五、單元考題
1. **選擇題**：類別與物件的關係，下列何者正確？
   - A. 物件是藍圖，類別是依藍圖建立的實體
   - B. 類別是藍圖，物件是依藍圖建立的實體
   - C. 兩者完全相同
   - D. 一個類別只能建立一個物件
2. **選擇題**：方法的第一個參數 `self` 代表什麼？
   - A. 類別本身　B. 呼叫該方法的那個物件　C. 父類別　D. 方法的回傳值
3. **填空題**：
   ```python
   class Dog(Animal):
       def __init__(self, name, breed):
           ______.__init__(name)
           self.breed = breed
   ```
   空格應填 ______；子類別定義與父類別同名的方法來改變其行為，稱為 ______。
4. **程式題**：設計 `ShoppingCart` 類別，方法 `add(name, price)` 加入商品，`count()` 回傳商品數量，`total()` 回傳總金額。依序加入 `("滑鼠", 590)` 與 `("鍵盤", 2480)` 後，印出「商品數：…」與「總金額：…」。

答案與參考解答請作答後再查看：[unit-10-answers.md](unit-10-answers.md)

## 六、重點整理
- 類別是藍圖，物件是實體；屬性是資料，方法是動作。
- `__init__` 設定初始屬性，`self` 代表當前物件，`__str__` 決定 `print` 顯示的文字。
- 封裝：外部透過方法存取資料，由方法檢查合法性；單底線只是慣例。
- 繼承：`class 子類別(父類別)`，用覆寫改變行為，用 `super()` 呼叫父類別；多型讓不同物件以同樣方式被呼叫。
- 自訂例外繼承 `Exception`，讓錯誤訊息更明確。

下一單元：標準函式庫與套件管理
