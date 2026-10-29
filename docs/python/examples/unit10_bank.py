# 範例 2：封裝與自訂例外
class InsufficientFundsError(Exception):
    """餘額不足時拋出的例外"""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance      # 底線開頭：慣例上視為內部使用，請透過方法存取

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金額必須大於 0")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsError("餘額不足")
        self._balance -= amount

    def get_balance(self):
        return self._balance


account = BankAccount("小明", 1000)
account.deposit(500)
print(account.get_balance())

try:
    account.withdraw(2000)
except InsufficientFundsError as e:
    print("提款失敗：", e)

account.withdraw(300)
print(account.get_balance())
