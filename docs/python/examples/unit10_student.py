# 範例 1：類別、物件、屬性與方法
class Student:
    """學生類別"""
    school = "Python 學院"              # 類別屬性：所有物件共用

    def __init__(self, name, score):    # 建構方法：建立物件時自動執行
        self.name = name                 # 實例屬性：每個物件各自擁有
        self.score = score

    def is_passed(self):
        return self.score >= 60

    def add_score(self, points):
        self.score += points

    def __str__(self):                   # print(物件) 時顯示的文字
        return f"{self.name}（{self.score} 分）"


s1 = Student("小明", 85)
s2 = Student("小華", 58)

print(s1)
print(s2.is_passed())
s2.add_score(5)
print(s2.score, s2.is_passed())
print(s1.school, Student.school)
