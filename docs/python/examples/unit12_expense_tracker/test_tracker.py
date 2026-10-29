"""簡易測試。執行方式：python test_tracker.py（不需要額外套件）"""
from datetime import date
from pathlib import Path

from models import Expense, InvalidExpenseError
from report import monthly_total, top_expenses, total_amount, total_by_category
from storage import load_expenses, save_expenses


def make_sample():
    return [
        Expense(date(2025, 3, 1), "餐飲", 120, "午餐"),
        Expense(date(2025, 3, 5), "交通", 50),
        Expense(date(2025, 3, 9), "餐飲", 300, "聚餐"),
        Expense(date(2025, 4, 2), "娛樂", 800, "電影"),
    ]


def test_total():
    assert total_amount(make_sample()) == 1270


def test_by_category():
    assert total_by_category(make_sample()) == {"餐飲": 420, "交通": 50, "娛樂": 800}


def test_monthly():
    assert monthly_total(make_sample(), 2025, 3) == 470
    assert monthly_total(make_sample(), 2025, 4) == 800


def test_top():
    top = top_expenses(make_sample(), 2)
    assert [e.amount for e in top] == [800, 300]


def test_invalid_amount():
    try:
        Expense(date(2025, 3, 1), "餐飲", -5)
    except InvalidExpenseError:
        return
    raise AssertionError("金額為負數時應拋出 InvalidExpenseError")


def test_save_and_load():
    path = Path(__file__).parent / "test_expenses.json"
    try:
        save_expenses(path, make_sample())
        loaded = load_expenses(path)
        assert len(loaded) == 4
        assert loaded[0].category == "餐飲"
        assert loaded[3].expense_date == date(2025, 4, 2)
    finally:
        if path.exists():
            path.unlink()                # 測試結束後刪除暫存檔


def test_load_missing_file():
    assert load_expenses(Path(__file__).parent / "no_such_file.json") == []


if __name__ == "__main__":
    tests = [
        test_total,
        test_by_category,
        test_monthly,
        test_top,
        test_invalid_amount,
        test_save_and_load,
        test_load_missing_file,
    ]
    for test in tests:
        test()
        print("通過：", test.__name__)
    print("全部測試通過")
