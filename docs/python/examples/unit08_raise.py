# 範例 3：raise 主動拋出例外與輸入驗證
def get_age(text):
    age = int(text)                        # 無法轉換時會自動拋出 ValueError
    if age < 0 or age > 120:
        raise ValueError("年齡必須介於 0 到 120")   # 主動拋出例外
    return age


for text in ["25", "abc", "-5"]:
    try:
        print("年齡：", get_age(text))
    except ValueError as e:
        print("輸入錯誤：", e)
