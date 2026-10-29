# 考題 4 參考解答：安全取得 list 元素
def safe_get(lst, index):
    """回傳指定索引的元素；索引錯誤時回傳說明文字"""
    try:
        return lst[index]
    except IndexError:
        return "索引超出範圍"
    except TypeError:
        return "索引必須是整數"


print(safe_get([10, 20, 30], 1))
print(safe_get([10, 20, 30], 5))
print(safe_get([10, 20, 30], "a"))
