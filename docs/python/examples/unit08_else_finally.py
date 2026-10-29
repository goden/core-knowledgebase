# 範例 2：as、else 與 finally
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:     # as e 取得例外物件
        print("發生錯誤：", e)
        return None
    else:                              # 沒有發生例外才執行
        print("計算成功")
        return result
    finally:                           # 無論有沒有例外都會執行
        print("結束計算")


print(safe_divide(10, 2))
print(safe_divide(1, 0))
