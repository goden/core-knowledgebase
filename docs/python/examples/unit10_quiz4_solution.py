# 考題 4 參考解答：購物車類別
class ShoppingCart:
    def __init__(self):
        self.items = []                    # 每個購物車物件各自擁有自己的 list

    def add(self, name, price):
        self.items.append((name, price))

    def count(self):
        return len(self.items)

    def total(self):
        total = 0
        for name, price in self.items:
            total += price
        return total


cart = ShoppingCart()
cart.add("滑鼠", 590)
cart.add("鍵盤", 2480)

print("商品數：", cart.count())
print("總金額：", cart.total())
