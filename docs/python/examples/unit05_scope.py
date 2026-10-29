# 範例 3：區域變數與全域變數
count = 0                 # 全域變數


def add_one():
    count = 100           # 區域變數，與全域的 count 是不同的變數
    return count + 1


print(add_one())
print(count)              # 全域的 count 沒有被改變


def increase():
    global count          # 宣告要修改的是全域變數
    count += 1


increase()
increase()
print(count)

# 函式內建立的區域變數在函式外無法使用，例如在此處讀取 add_one 內的變數會發生 NameError
