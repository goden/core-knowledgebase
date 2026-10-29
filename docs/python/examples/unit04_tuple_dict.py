# 範例 2：tuple 與 dict
point = (3, 4)
x, y = point                         # 解包：把 tuple 的值分別指派給變數
print(x, y)
# point[0] = 10                      # 會發生 TypeError，tuple 不可修改

student = {"name": "小明", "age": 20, "score": 85}
print(student["name"])               # 用鍵取值

student["score"] = 90                # 修改既有的鍵
student["city"] = "台北"             # 新增鍵值對
print(student.get("phone", "未提供")) # 鍵不存在時回傳預設值，不會出錯
del student["age"]                   # 刪除鍵值對

for key, value in student.items():   # 同時走訪鍵與值
    print(key, value)
print(len(student))
