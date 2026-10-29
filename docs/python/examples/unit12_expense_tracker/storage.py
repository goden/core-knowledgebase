"""記帳本的檔案存取：以 JSON 儲存支出清單。"""
import json

from models import expense_from_dict


def load_expenses(path):
    """讀取支出清單；檔案不存在時回傳空 list。

    檔案內容損毀時，會拋出 ValueError 或 KeyError，由呼叫端決定如何處理。
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except FileNotFoundError:
        return []
    return [expense_from_dict(item) for item in raw]


def save_expenses(path, expenses):
    """把支出清單存成 JSON 檔（保留中文）"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump([e.to_dict() for e in expenses], f, ensure_ascii=False, indent=2)
