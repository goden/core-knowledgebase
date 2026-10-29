# 練習 1 參考解答：長方形類別
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
