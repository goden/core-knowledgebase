# 練習 2 參考解答：購物折扣
amount = float(input("請輸入購物金額："))

# 由金額大的條件開始判斷
if amount >= 3000:
    payable = amount * 0.8
elif amount >= 1000:
    payable = amount * 0.9
else:
    payable = amount

print("應付金額：", round(payable, 1))
