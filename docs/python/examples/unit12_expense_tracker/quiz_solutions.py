"""單元 12 考題的參考解答。執行方式：python quiz_solutions.py"""
from datetime import date

from models import Expense
from report import total_amount


def average_amount(expenses):
    """平均每筆支出；沒有資料時回傳 0，避免除以零"""
    if not expenses:
        return 0
    return total_amount(expenses) / len(expenses)


def filter_by_category(expenses, category):
    """回傳指定類別的支出清單"""
    return [e for e in expenses if e.category == category]


if __name__ == "__main__":
    sample = [
        Expense(date(2025, 3, 1), "餐飲", 100),
        Expense(date(2025, 3, 5), "交通", 200),
        Expense(date(2025, 3, 9), "餐飲", 300),
    ]
    print(average_amount(sample))
    print(average_amount([]))
    print([e.amount for e in filter_by_category(sample, "餐飲")])
