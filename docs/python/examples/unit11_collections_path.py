# 範例 3：collections 與 pathlib
from collections import Counter, defaultdict
from pathlib import Path

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(words)                   # 自動統計每個元素出現的次數
print(counter)
print(counter.most_common(2))              # 出現次數最多的前 2 名

groups = defaultdict(list)                 # 鍵不存在時，自動建立空 list
for name, dept in [("小明", "研發"), ("小華", "業務"), ("小美", "研發")]:
    groups[dept].append(name)
print(dict(groups))

p = Path("data") / "report.txt"            # 用 / 組合路徑，自動使用符合系統的分隔符號
print(p.name, p.suffix, p.stem)            # 檔名、副檔名、不含副檔名的檔名
print(p.exists())                          # 檢查路徑是否存在
