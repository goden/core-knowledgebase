# 範例 3：re 模組（match / search / findall / sub / 分組）
import re

text = "聯絡人：小明，電話 0912-345-678，Email：ming@example.com；備用 0922-111-222"

# match 只比對「開頭」
print(re.match(r"聯絡人", text) is not None)
print(re.match(r"電話", text))

# search 找「第一個」符合的位置，用 group() 取出內容
print(re.search(r"\d{4}-\d{3}-\d{3}", text).group())

# findall 找出「所有」符合的內容
print(re.findall(r"\d{4}-\d{3}-\d{3}", text))

# sub 取代
print(re.sub(r"\d{4}-\d{3}-\d{3}", "****", text))

# 分組：用括號取出部分內容
m = re.search(r"(\w+)@(\w+)\.com", text)
print(m.group(0), m.group(1), m.group(2))

# 有分組時，findall 回傳每筆的分組 tuple
dates = "2025-03-01, 2025-12-25"
print(re.findall(r"(\d{4})-(\d{2})-(\d{2})", dates))
