"""產生教學用模擬資料（固定亂數種子，結果可重複產生）。

用法：python data/generate_data.py
僅使用標準函式庫，所有人名、商品與評論皆為虛構。
"""
import csv
import json
import math
import random
from datetime import date, datetime, timedelta
from pathlib import Path

SEED = 42
ROOT = Path(__file__).resolve().parent

PRODUCTS = [
    ("P001", "無線滑鼠", "3C", 590),
    ("P002", "機械鍵盤", "3C", 2480),
    ("P003", "藍牙耳機", "3C", 1890),
    ("P004", "行動電源", "3C", 890),
    ("P005", "USB 集線器", "3C", 450),
    ("P006", "即溶咖啡", "食品", 220),
    ("P007", "綜合堅果", "食品", 350),
    ("P008", "燕麥片", "食品", 180),
    ("P009", "礦泉水箱", "食品", 260),
    ("P010", "收納箱", "居家", 320),
    ("P011", "香氛蠟燭", "居家", 480),
    ("P012", "保溫杯", "居家", 690),
    ("P013", "毛巾組", "居家", 390),
    ("P014", "素色T恤", "服飾", 450),
    ("P015", "牛仔褲", "服飾", 1280),
    ("P016", "運動外套", "服飾", 1690),
    ("P017", "帆布包", "服飾", 760),
    ("P018", "原子筆組", "文具", 120),
    ("P019", "筆記本", "文具", 160),
    ("P020", "桌上型便利貼", "文具", 90),
]
REGIONS = ["北區", "中區", "南區", "東區"]
PAYMENTS = ["信用卡", "行動支付", "現金", "轉帳"]
CITIES = ["台北", "新北", "桃園", "台中", "台南", "高雄"]
SURNAMES = ["陳", "林", "黃", "張", "李", "王", "吳", "劉", "蔡", "楊"]
GIVEN_NAMES = ["怡君", "志明", "雅婷", "建宏", "宗翰", "淑芬", "佳穎", "家豪",
                "美玲", "冠宇", "詩涵", "承恩", "雅雯", "柏翰", "育廷"]


def write_csv(path, header, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def make_customers(rng):
    rows = []
    for i in range(1, 201):
        signup = date(2023, 1, 1) + timedelta(days=rng.randint(0, 900))
        rows.append({
            "customer_id": f"C{i:04d}",
            "name": f"客戶{i:04d}",
            "gender": rng.choice(["男", "女"]),
            # 約 4% 年齡缺值，供清洗練習
            "age": "" if rng.random() < 0.04 else rng.randint(18, 70),
            "city": rng.choice(CITIES),
            "signup_date": signup.isoformat(),
            "member_level": rng.choices(["一般", "銀卡", "金卡"], weights=[6, 3, 1])[0],
        })
    return rows


def make_dirty_sales(rng, customers):
    """產生含缺值、重複、異常值與格式不一致的銷售資料。"""
    rows = []
    start = date(2025, 1, 1)
    for i in range(1, 501):
        _, name, category, price = rng.choice(PRODUCTS)
        order_date = start + timedelta(days=rng.randint(0, 364))
        row = {
            "order_id": f"O{i:05d}",
            "order_date": order_date.isoformat(),
            "customer_id": rng.choice(customers)["customer_id"],
            "product": name,
            "category": category,
            "quantity": rng.randint(1, 5),
            "unit_price": price,
            "region": rng.choice(REGIONS),
            "payment": rng.choice(PAYMENTS),
        }
        if rng.random() < 0.05:
            row["quantity"] = ""
        if rng.random() < 0.04:
            row["region"] = ""
        if rng.random() < 0.03:
            row["unit_price"] = ""
        if rng.random() < 0.03:
            row["order_date"] = order_date.strftime("%Y/%m/%d")
        if rng.random() < 0.05:
            row["payment"] = rng.choice([" 信用卡", "Credit Card", "行動支付 ", "cash"])
        if rng.random() < 0.01:
            row["quantity"] = rng.choice([99, 500, -3])
        if rng.random() < 0.01 and row["unit_price"] != "":
            row["unit_price"] = row["unit_price"] * 100
        rows.append(row)
    rows.extend(dict(r) for r in rng.sample(rows, 15))
    return rows


def make_basket(rng):
    items = ["麵包", "牛奶", "雞蛋", "啤酒", "尿布", "薯片", "可樂", "義大利麵", "番茄醬",
             "咖啡", "砂糖", "香蕉", "蘋果", "優格", "起司", "衛生紙", "洗髮精", "礦泉水",
             "餅乾", "果汁"]
    # 內建關聯組合，供 Apriori / FP-Growth 練習
    rules = [(("麵包", "牛奶"), 0.30), (("啤酒", "尿布"), 0.15), (("薯片", "可樂"), 0.25),
             (("義大利麵", "番茄醬", "起司"), 0.12), (("咖啡", "砂糖"), 0.20)]
    rows = []
    for t in range(1, 1001):
        basket = set()
        for combo, prob in rules:
            if rng.random() < prob:
                basket.update(combo)
        basket.update(rng.sample(items, rng.randint(0, 3)))
        if not basket:
            basket.add(rng.choice(items))
        rows.extend({"transaction_id": f"T{t:04d}", "item": item} for item in sorted(basket))
    return rows


def make_sensor(rng):
    rows = []
    start = datetime(2025, 6, 1)
    for h in range(24 * 30):
        ts = start + timedelta(hours=h)
        temp = 27 + 5 * math.sin((ts.hour - 9) / 24 * 2 * math.pi) + rng.gauss(0, 0.8)
        humidity = 75 - 1.5 * (temp - 27) + rng.gauss(0, 3)
        rows.append({
            "timestamp": ts.strftime("%Y-%m-%d %H:%M:%S"),
            "temperature": "" if rng.random() < 0.02 else round(temp, 1),
            "humidity": "" if rng.random() < 0.02 else round(humidity, 1),
        })
    return rows


def make_employees(rng):
    departments = [
        {"department_id": "D01", "name": "研發部", "location": "台北"},
        {"department_id": "D02", "name": "業務部", "location": "台北"},
        {"department_id": "D03", "name": "人資部", "location": "台中"},
        {"department_id": "D04", "name": "財務部", "location": "台北"},
        {"department_id": "D05", "name": "客服部", "location": "高雄"},
    ]
    employees = []
    for idx in range(40):
        if idx == 0:
            title, manager = "總經理", ""
        elif idx < 5:
            title, manager = "經理", "E001"
        else:
            title, manager = rng.choice(["工程師", "專員", "資深專員"]), f"E{(idx % 5) + 1:03d}"
        hired = date(2015, 1, 1) + timedelta(days=rng.randint(0, 3650))
        employees.append({
            "employee_id": f"E{idx + 1:03d}",
            "name": rng.choice(SURNAMES) + rng.choice(GIVEN_NAMES),
            "department_id": departments[idx % 5]["department_id"],
            "title": title,
            "salary": rng.randint(40, 120) * 1000,
            "hire_date": hired.isoformat(),
            "manager_id": manager,
        })
    return departments, employees


def make_orders(rng, customers):
    orders, items = [], []
    start = date(2025, 1, 1)
    for i in range(1, 301):
        order_id = f"O{i:05d}"
        orders.append({
            "order_id": order_id,
            "customer_id": rng.choice(customers)["customer_id"],
            "order_date": (start + timedelta(days=rng.randint(0, 364))).isoformat(),
            "status": rng.choices(["已完成", "已出貨", "處理中", "已取消"], weights=[6, 2, 1, 1])[0],
        })
        for pid, _, _, price in rng.sample(PRODUCTS, rng.randint(1, 4)):
            items.append({"order_id": order_id, "product_id": pid,
                          "quantity": rng.randint(1, 5), "unit_price": price})
    return orders, items


def make_documents(rng):
    tag_pool = ["熱銷", "新品", "限量", "特價", "環保", "送禮"]
    comments = ["很好用", "價格合理", "包裝完整", "功能普通", "不太耐用", "會再回購"]
    docs = []
    for pid, name, category, price in PRODUCTS:
        specs = {"重量_g": rng.randint(50, 2000), "產地": rng.choice(["台灣", "日本", "越南"])}
        # 部分文件缺少保固欄位，示範文件模型的彈性結構
        if rng.random() < 0.7:
            specs["保固月數"] = rng.choice([0, 6, 12, 24])
        docs.append({
            "sku": pid,
            "name": name,
            "category": category,
            "price": price,
            "tags": rng.sample(tag_pool, rng.randint(1, 3)),
            "specs": specs,
            "reviews": [{"user": f"客戶{rng.randint(1, 200):04d}",
                         "rating": rng.randint(1, 5),
                         "comment": rng.choice(comments)}
                        for _ in range(rng.randint(0, 3))],
        })
    return docs


def make_graph(rng):
    combos = [s + g for s in SURNAMES for g in GIVEN_NAMES]
    names = rng.sample(combos, 20)
    companies = ["星河科技", "遠見顧問", "綠野食品", "海岸物流", "山城製造"]
    nodes = [{"id": f"p{i + 1:02d}", "label": "Person", "name": n} for i, n in enumerate(names)]
    nodes += [{"id": f"c{i + 1}", "label": "Company", "name": n} for i, n in enumerate(companies)]
    nodes += [{"id": f"city{i + 1}", "label": "City", "name": n} for i, n in enumerate(CITIES)]

    rels = []
    for i in range(20):
        pid = f"p{i + 1:02d}"
        rels.append({"start_id": pid, "end_id": f"c{rng.randint(1, 5)}", "type": "WORKS_AT"})
        rels.append({"start_id": pid, "end_id": f"city{rng.randint(1, 6)}", "type": "LIVES_IN"})
    friends = set()
    while len(friends) < 35:
        a, b = sorted(rng.sample(range(1, 21), 2))
        friends.add((a, b))
    rels += [{"start_id": f"p{a:02d}", "end_id": f"p{b:02d}", "type": "FRIEND_OF"}
             for a, b in sorted(friends)]
    return nodes, rels


def make_api_pages(rng):
    tags = ["python", "爬蟲", "資料庫", "資料分析", "AI", "雲端"]
    posts = []
    for i in range(1, 21):
        posts.append({
            "id": i,
            "title": f"範例文章 {i}",
            "author": {"id": rng.randint(1, 5), "name": rng.choice(["小明", "小華", "小美", "小傑", "小雅"])},
            "tags": rng.sample(tags, rng.randint(1, 3)),
            "stats": {"views": rng.randint(10, 5000), "likes": rng.randint(0, 300)},
            "published_at": (datetime(2025, 1, 1) + timedelta(hours=rng.randint(0, 8000))).isoformat(),
            # 部分欄位為 null，供 JSON 空值處理練習
            "summary": None if rng.random() < 0.3 else f"這是第 {i} 篇文章的摘要。",
            "comments": [{"user": f"user{rng.randint(1, 50)}", "text": rng.choice(["讚", "學到了", "請問來源？"])}
                         for _ in range(rng.randint(0, 3))],
        })
    return [
        {"page": 1, "per_page": 10, "total": 20, "next_page": 2, "data": posts[:10]},
        {"page": 2, "per_page": 10, "total": 20, "next_page": None, "data": posts[10:]},
    ]


def make_reviews(rng):
    positive = ["{p}品質很好，使用起來很順手，值得推薦", "出貨速度快，{p}包裝完整，非常滿意",
                "{p}的性價比很高，會再回購", "客服態度親切，{p}符合描述"]
    neutral = ["{p}普通，沒有特別驚豔，價格還算合理"]
    negative = ["{p}用了一週就壞掉，品質令人失望", "物流太慢，{p}到貨時外盒已經破損",
                "{p}與商品描述不符，不推薦", "客服回覆很慢，{p}有瑕疵還不給退"]
    rows = []
    for i in range(1, 101):
        product = rng.choice(PRODUCTS)[1]
        kind = rng.choices(["pos", "neu", "neg"], weights=[5, 2, 3])[0]
        template, rating = {
            "pos": (rng.choice(positive), rng.randint(4, 5)),
            "neu": (rng.choice(neutral), 3),
            "neg": (rng.choice(negative), rng.randint(1, 2)),
        }[kind]
        rows.append({
            "review_id": f"R{i:04d}",
            "product": product,
            "rating": rating,
            "text": template.format(p=product),
            "date": (date(2025, 1, 1) + timedelta(days=rng.randint(0, 364))).isoformat(),
        })
    return rows


def main():
    rng = random.Random(SEED)
    customers = make_customers(rng)

    mining = ROOT / "data-mining"
    write_csv(mining / "customers.csv", list(customers[0]), customers)
    sales = make_dirty_sales(rng, customers)
    write_csv(mining / "sales_raw.csv", list(sales[0]), sales)
    basket = make_basket(rng)
    write_csv(mining / "basket_transactions.csv", list(basket[0]), basket)
    sensor = make_sensor(rng)
    write_csv(mining / "sensor_readings.csv", list(sensor[0]), sensor)

    db = ROOT / "database"
    departments, employees = make_employees(rng)
    write_csv(db / "departments.csv", list(departments[0]), departments)
    write_csv(db / "employees.csv", list(employees[0]), employees)
    write_csv(db / "customers.csv", list(customers[0]), customers)
    products = [{"product_id": p, "name": n, "category": c, "price": pr, "stock": rng.randint(0, 200)}
                for p, n, c, pr in PRODUCTS]
    write_csv(db / "products.csv", list(products[0]), products)
    orders, items = make_orders(rng, customers)
    write_csv(db / "orders.csv", list(orders[0]), orders)
    write_csv(db / "order_items.csv", list(items[0]), items)
    write_json(db / "product_documents.json", make_documents(rng))
    nodes, rels = make_graph(rng)
    write_csv(db / "graph_nodes.csv", list(nodes[0]), nodes)
    write_csv(db / "graph_relationships.csv", list(rels[0]), rels)

    pages = make_api_pages(rng)
    for page in pages:
        write_json(ROOT / "crawler" / f"api_posts_page{page['page']}.json", page)

    reviews = make_reviews(rng)
    write_csv(ROOT / "tokenization" / "reviews.csv", list(reviews[0]), reviews)

    print("資料產生完成：", ROOT)


if __name__ == "__main__":
    main()
