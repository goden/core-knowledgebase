# 練習 1 參考解答：統計字元出現次數
from collections import Counter

text = "mississippi"
counter = Counter(text)
print(counter.most_common(2))
