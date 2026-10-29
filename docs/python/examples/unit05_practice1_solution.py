# 練習 1 參考解答：BMI 函式
def bmi(height_cm, weight_kg):
    """依身高（公分）與體重（公斤）回傳 BMI，取到小數第 1 位"""
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)


print(bmi(175, 70))
print(bmi(160, 50))
