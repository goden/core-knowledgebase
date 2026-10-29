# 單元 10 答案：物件導向程式設計

請先自行作答再查看。題目見 [unit-10-oop.md](unit-10-oop.md)。

## 課堂練習參考解答
1. 程式：[examples/unit10_practice1_solution.py](examples/unit10_practice1_solution.py)

   ```python
   class Rectangle:
       def __init__(self, width, height):
           self.width = width
           self.height = height

       def area(self):
           return self.width * self.height

       def perimeter(self):
           return 2 * (self.width + self.height)

       def __str__(self):
           return f"長方形 {self.width}x{self.height}"


   r = Rectangle(3, 4)
   print(r)
   print(r.area())
   print(r.perimeter())
   ```

   預期輸出：
   ```
   長方形 3x4
   12
   14
   ```

2. 程式：[examples/unit10_practice2_solution.py](examples/unit10_practice2_solution.py)

   ```python
   class Employee:
       def __init__(self, name, salary):
           self.name = name
           self.salary = salary

       def annual_salary(self):
           return self.salary * 12


   class Manager(Employee):
       def __init__(self, name, salary, bonus):
           super().__init__(name, salary)
           self.bonus = bonus

       def annual_salary(self):
           return super().annual_salary() + self.bonus


   print(Employee("小明", 40000).annual_salary())
   print(Manager("小華", 60000, 100000).annual_salary())
   ```

   預期輸出：
   ```
   480000
   820000
   ```

   計算：小明 40000 × 12 = 480000；小華 60000 × 12 + 100000 = 820000。

## 單元考題標準答案
1. **B**。類別是藍圖，物件是依藍圖建立的實體；一個類別可以建立很多個物件。
2. **B**。`self` 代表呼叫該方法的那個物件，Python 會在呼叫時自動傳入。
3. 第一格填 **`super()`**；第二格填 **覆寫**（override）。
4. 程式：[examples/unit10_quiz4_solution.py](examples/unit10_quiz4_solution.py)

   ```python
   class ShoppingCart:
       def __init__(self):
           self.items = []

       def add(self, name, price):
           self.items.append((name, price))

       def count(self):
           return len(self.items)

       def total(self):
           total = 0
           for name, price in self.items:
               total += price
           return total


   cart = ShoppingCart()
   cart.add("滑鼠", 590)
   cart.add("鍵盤", 2480)

   print("商品數：", cart.count())
   print("總金額：", cart.total())
   ```

   預期輸出：
   ```
   商品數： 2
   總金額： 3070
   ```

   重點：`items` 在 `__init__` 中以 `self.items = []` 建立，每個購物車物件才會各自擁有一份，不會互相影響。
