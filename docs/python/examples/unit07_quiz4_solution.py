# 考題 4 參考解答：解析訂單並加總金額
import re

text = "訂單 A001 金額 1200 元，訂單 B002 金額 850 元，訂單 C003 金額 2300 元"

# 兩個分組：訂單編號、金額
orders = re.findall(r"訂單 (\w+) 金額 (\d+) 元", text)
print(orders)

total = 0
for order_id, amount in orders:
    total += int(amount)          # 擷取到的是字串，需轉成整數才能加總

print(f"總金額：{total:,} 元")
