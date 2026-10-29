# 練習 1 參考解答：安全的整數轉換
def safe_int(text):
    """轉換成功回傳整數，失敗回傳 None"""
    try:
        return int(text)
    except ValueError:
        return None


print(safe_int("42"))
print(safe_int("4.5"))   # int() 不能直接轉換含小數點的字串
print(safe_int("abc"))
