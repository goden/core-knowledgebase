# 練習 1 參考解答：拆解電子郵件
email = "  Alice.Smith@Example.COM  "

email = email.strip().lower()      # 先去空白再轉小寫
user, domain = email.split("@")    # 以 @ 切成兩段並解包

print(f"帳號：{user}")
print(f"網域：{domain}")
