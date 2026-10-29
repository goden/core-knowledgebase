"""記帳本的統計報表。"""
from collections import defaultdict


def total_amount(expenses):
    """全部支出的總金額"""
    return sum([e.amount for e in expenses])


def total_by_category(expenses):
    """各類別的支出總額，回傳 {類別: 金額}"""
    totals = defaultdict(int)
    for e in expenses:
        totals[e.category] += e.amount
    return dict(totals)


def monthly_total(expenses, year, month):
    """指定年月的支出總額"""
    return sum([
        e.amount
        for e in expenses
        if e.expense_date.year == year and e.expense_date.month == month
    ])


def top_expenses(expenses, n=3):
    """金額最高的前 n 筆支出"""
    return sorted(expenses, key=lambda e: e.amount, reverse=True)[:n]
