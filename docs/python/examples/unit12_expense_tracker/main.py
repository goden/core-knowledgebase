"""記帳本主程式。執行方式：python main.py"""
from datetime import datetime
from pathlib import Path

from models import Expense
from report import monthly_total, top_expenses, total_amount, total_by_category
from storage import load_expenses, save_expenses

# 資料檔放在與本程式相同的資料夾
DATA_FILE = Path(__file__).parent / "expenses.json"

MENU = """
===== 記帳本 =====
1. 新增支出
2. 查看全部
3. 分類統計
4. 月份統計
0. 儲存並離開
"""


def add_expense(expenses):
    try:
        expense_date = datetime.strptime(input("日期（YYYY-MM-DD）："), "%Y-%m-%d").date()
        category = input("類別：")
        amount = int(input("金額："))
        note = input("備註（可空白）：")
        expenses.append(Expense(expense_date, category, amount, note))
        print("已新增")
    except ValueError as e:       # 涵蓋日期、金額格式錯誤與 InvalidExpenseError
        print("輸入錯誤：", e)


def show_expenses(expenses):
    if not expenses:
        print("目前沒有資料")
        return
    for e in sorted(expenses, key=lambda e: e.expense_date):
        print(e)
    print(f"總支出：NT${total_amount(expenses):,}")


def show_report(expenses):
    if not expenses:
        print("目前沒有資料")
        return
    totals = total_by_category(expenses)
    for category, amount in sorted(totals.items(), key=lambda item: item[1], reverse=True):
        print(f"{category}：NT${amount:,}")
    print("金額最高的 3 筆：")
    for e in top_expenses(expenses):
        print(" ", e)


def show_monthly(expenses):
    try:
        target = datetime.strptime(input("請輸入月份（YYYY-MM）："), "%Y-%m")
    except ValueError:
        print("月份格式錯誤")
        return
    amount = monthly_total(expenses, target.year, target.month)
    print(f"{target.year} 年 {target.month} 月支出：NT${amount:,}")


def main():
    try:
        expenses = load_expenses(DATA_FILE)
    except (ValueError, KeyError) as e:
        # 資料檔損毀時直接結束，避免之後儲存時把原檔覆蓋成空資料
        print("資料檔讀取失敗：", e)
        return

    # 以 dict 對應選項與函式，省去一長串 if / elif
    actions = {"1": add_expense, "2": show_expenses, "3": show_report, "4": show_monthly}

    while True:
        print(MENU)
        choice = input("請選擇：").strip()
        if choice == "0":
            save_expenses(DATA_FILE, expenses)
            print("已儲存，再見！")
            break
        action = actions.get(choice)
        if action is None:
            print("無效的選項")
        else:
            action(expenses)


if __name__ == "__main__":
    main()
