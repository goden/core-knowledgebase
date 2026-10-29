# 範例 2：sorted(key=...) 與 max(key=...)
students = [("小明", 85), ("小華", 92), ("小美", 78)]

# key 指定排序依據：取每個 tuple 的第 2 個元素（分數），reverse=True 為由大到小
by_score = sorted(students, key=lambda s: s[1], reverse=True)
print(by_score)

words = ["banana", "kiwi", "apple", "fig"]
print(sorted(words, key=len))             # 依字串長度由短到長
print(words)                              # sorted 不會改變原本的 list

print(max(students, key=lambda s: s[1]))  # 分數最高的學生
