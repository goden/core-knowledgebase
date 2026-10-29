"""記帳本的資料模型。"""
from datetime import datetime


class InvalidExpenseError(ValueError):
    """支出資料不合法時拋出的例外"""


class Expense:
    """一筆支出"""

    def __init__(self, expense_date, category, amount, note=""):
        if amount <= 0:
            raise InvalidExpenseError("金額必須大於 0")
        if not category.strip():
            raise InvalidExpenseError("類別不可為空白")
        self.expense_date = expense_date     # datetime.date 物件
        self.category = category.strip()
        self.amount = amount
        self.note = note

    def to_dict(self):
        """轉成可存入 JSON 的 dict（日期轉成字串）"""
        return {
            "date": self.expense_date.strftime("%Y-%m-%d"),
            "category": self.category,
            "amount": self.amount,
            "note": self.note,
        }

    def __str__(self):
        date_text = self.expense_date.strftime("%Y-%m-%d")
        return f"{date_text}  {self.category}  NT${self.amount:,}  {self.note}"


def expense_from_dict(data):
    """由 dict 還原成 Expense 物件"""
    expense_date = datetime.strptime(data["date"], "%Y-%m-%d").date()
    return Expense(expense_date, data["category"], data["amount"], data.get("note", ""))
