# 練習 1 參考解答：把名單寫入檔案再讀回
names = ["小明", "小華", "小美"]

with open("unit09_names.txt", "w", encoding="utf-8") as f:
    for name in names:
        f.write(name + "\n")          # 每個名字一行

with open("unit09_names.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("共", len(lines), "行")
for line in lines:
    print(line.strip())
