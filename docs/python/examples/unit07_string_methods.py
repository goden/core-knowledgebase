# 範例 1：字串方法、索引與切片
s = "  Hello, Python World!  "
text = s.strip()                          # 去除前後空白
print(text)

print(text.upper())                       # 全部大寫
print(text.lower())                       # 全部小寫
print(text.replace("World", "學習者"))    # 取代（回傳新字串，原字串不變）
print(text.split(", "))                   # 依分隔符號切成 list
print("-".join(["a", "b", "c"]))          # 用符號把 list 串成字串

print(text[0], text[-1], text[7:13])      # 索引與切片（終點不含）
print(text[::-1])                         # 步進 -1：反轉字串

print(text.find("Python"), text.count("o"), text.startswith("Hello"))
