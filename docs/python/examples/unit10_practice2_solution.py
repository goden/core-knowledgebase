# 練習 2 參考解答：員工與經理（繼承）
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
        # 覆寫：沿用父類別的計算，再加上獎金
        return super().annual_salary() + self.bonus


print(Employee("小明", 40000).annual_salary())
print(Manager("小華", 60000, 100000).annual_salary())
