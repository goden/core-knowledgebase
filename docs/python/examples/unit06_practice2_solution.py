# 練習 2 參考解答：依價格排序並篩選高價商品
products = [("滑鼠", 590), ("鍵盤", 2480), ("耳機", 1890), ("充電器", 450)]

# 依價格由高到低排序
print(sorted(products, key=lambda p: p[1], reverse=True))

# 推導式取出價格 1000 以上的商品名稱
print([name for name, price in products if price >= 1000])
