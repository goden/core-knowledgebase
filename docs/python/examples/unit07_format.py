# 範例 2：f-string 與 format() 格式化
name = "小明"
age = 20
price = 1234567.891
seat = 7

print(f"{name} 今年 {age} 歲")                 # 直接在 {} 放入變數
print(f"價格：{price:,.2f}")                    # 千分位並取到小數第 2 位
print(f"座號：{seat:03d}")                      # 寬度 3，不足補 0
print(f"{'L':<5}|{'C':^5}|{'R':>5}|")          # 靠左、置中、靠右對齊
print(f"{0.256:.1%}")                           # 百分比

print("{} 的成績是 {}".format(name, 95))        # format() 依序填入
print("{1} 與 {0}".format("A", "B"))            # 以索引指定順序
