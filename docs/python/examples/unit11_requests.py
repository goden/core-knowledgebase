# 範例 4：使用第三方套件 requests（需先 pip install requests，且需連網）
import requests

try:
    response = requests.get(
        "https://httpbin.org/get",
        params={"q": "python"},
        timeout=10,                        # 一定要設定逾時，避免程式卡住
    )
    print(response.status_code)
    print(response.json()["args"])
except requests.exceptions.RequestException as e:
    print("連線失敗：", e)
