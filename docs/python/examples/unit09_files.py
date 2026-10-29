# 範例 1：文字檔的寫入、附加與讀取
FILE = "unit09_notes.txt"    # 檔案會建立在執行指令時所在的資料夾

# "w"：寫入，檔案已存在時會先清空
with open(FILE, "w", encoding="utf-8") as f:
    f.write("第一行：Python\n")
    f.write("第二行：檔案讀寫\n")

# "a"：附加，內容加在檔案最後
with open(FILE, "a", encoding="utf-8") as f:
    f.write("第三行：附加的內容\n")

# 一次讀取全部內容
with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()
print(content, end="")       # 內容本身已含換行，所以 print 不再換行

# 逐行讀取，並以 strip() 去除行尾的換行字元
print("--- 逐行讀取 ---")
with open(FILE, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# readlines() 回傳每一行組成的 list
with open(FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()
print("共", len(lines), "行")
