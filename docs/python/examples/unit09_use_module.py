# 範例 3：匯入標準模組與自訂模組（需與 unit09_mymath.py 放在同一個資料夾）
import math
import unit09_mymath
from unit09_mymath import is_even

print(unit09_mymath.PI)
print(round(unit09_mymath.circle_area(3), 2))   # 以「模組名稱.名稱」使用
print(is_even(10))                               # from ... import 可直接使用名稱

print(math.sqrt(16))
print(math.pi)
