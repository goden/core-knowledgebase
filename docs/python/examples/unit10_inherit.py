# 範例 3：繼承、覆寫與多型
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def intro(self):
        return f"我是 {self.name}，我會說：{self.speak()}"


class Dog(Animal):                 # Dog 繼承 Animal
    def speak(self):               # 覆寫父類別的方法
        return "汪汪"


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)     # 呼叫父類別的 __init__ 設定 name
        self.color = color

    def speak(self):
        return "喵喵"


animals = [Dog("小黑"), Cat("小花", "白色"), Animal("路人")]

# 多型：同樣呼叫 intro()，不同類別會有不同的 speak() 結果
for a in animals:
    print(a.intro())

print(isinstance(animals[0], Animal), isinstance(animals[0], Cat))
print(animals[1].color)
