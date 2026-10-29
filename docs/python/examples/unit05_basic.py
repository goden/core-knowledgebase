# 範例 1：定義與呼叫函式
def greet(name):
    """回傳問候語"""
    return "哈囉，" + name + "！"


def add(a, b):
    return a + b


def say_hi():
    print("Hi")          # 只印出內容，沒有 return


message = greet("小明")
print(message)
print(add(3, 5))

result = say_hi()        # 沒有 return 的函式，預設回傳 None
print(result)
