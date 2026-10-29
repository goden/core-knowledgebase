# 範例 2：輸入與型別轉換（BMI 計算）
# input() 取得的內容一律是字串，必須轉換型別才能計算
height_cm = float(input("請輸入身高（公分）："))
weight_kg = float(input("請輸入體重（公斤）："))

height_m = height_cm / 100            # 公分換算成公尺
bmi = weight_kg / (height_m ** 2)     # BMI = 體重 / 身高平方
print("你的 BMI 是：", round(bmi, 1)) # round() 取到小數第 1 位
