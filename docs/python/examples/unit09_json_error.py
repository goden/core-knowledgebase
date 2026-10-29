# 範例 2：JSON 讀寫與 FileNotFoundError
import json

data = {"name": "小明", "scores": [85, 92], "passed": True}

# ensure_ascii=False 讓中文照原樣寫入；indent=2 讓檔案排版易讀
with open("unit09_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("unit09_data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded)
print(loaded["scores"][1])

# 讀取不存在的檔案會發生 FileNotFoundError
try:
    with open("no_such_file.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("找不到檔案")
