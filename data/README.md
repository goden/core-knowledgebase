# 教學測試資料

供各教學助教的範例與練習使用。所有資料皆為虛構（人名、商品、評論、新聞），無個資與授權疑慮。

## 重新產生

```powershell
python data/generate_data.py
```

僅使用標準函式庫，固定亂數種子（`SEED = 42`），重複執行結果相同。`.html`、`.txt`、`.jsonl` 等檔案為手寫，不會被覆蓋。

## 資料集

### data-mining/（資料探勘教學助教）
| 檔案 | 說明 | 練習重點 |
|---|---|---|
| `sales_raw.csv` | 銷售明細約 515 筆 | 刻意含缺值、重複列、異常值（數量 99 / 500 / -3、單價放大 100 倍）、日期格式不一致、付款方式字串不一致 |
| `customers.csv` | 客戶 200 筆 | 年齡缺值；與銷售資料以 `customer_id` 合併 |
| `basket_transactions.csv` | 購物籃 1000 筆交易（長格式：`transaction_id`, `item`） | 內建關聯組合（麵包+牛奶、啤酒+尿布、薯片+可樂等），供 Apriori / FP-Growth |
| `sensor_readings.csv` | 30 天逐時溫濕度 | 時間序列、缺值、折線圖 |

### database/（資料庫教學助教）
| 檔案 | 說明 | 對應單元 |
|---|---|---|
| `departments.csv`、`employees.csv` | 部門與員工（含 `manager_id` 自我關聯） | SQL、`JOIN`、自我關聯 |
| `customers.csv`、`products.csv`、`orders.csv`、`order_items.csv` | 訂單關聯表（已維持參照完整性） | MySQL、Oracle、聚合與交易 |
| `product_documents.json` | 商品文件（巢狀 `specs`、`reviews`，部分欄位缺漏） | MongoDB |
| `graph_nodes.csv`、`graph_relationships.csv` | 人物 / 公司 / 城市節點與 `WORKS_AT`、`LIVES_IN`、`FRIEND_OF` 關係 | Neo4j（Cypher） |
| `vector_corpus.jsonl` | 30 則中文短文（科技、美食、旅遊、運動、財經各 6 則） | Embedding、Chroma、Milvus、Elasticsearch、RAG |

### crawler/（爬蟲大師）
| 檔案 | 說明 | 練習重點 |
|---|---|---|
| `sample_page.html` | 離線 HTML 頁面 | CSS Selector、XPath、表格、分頁連結、內嵌 JSON、缺漏欄位 |
| `robots.txt` | 範例 robots.txt | 解析 `Disallow` / `Crawl-delay`（`urllib.robotparser`） |
| `api_posts_page1.json`、`api_posts_page2.json` | 分頁 API 回應 | 巢狀 JSON、`null`、`next_page` 翻頁、`json_normalize` |

### tokenization/（爬蟲大師 jieba 單元）
| 檔案 | 說明 |
|---|---|
| `news_corpus.txt` | 12 段虛構新聞，供斷詞與詞頻 |
| `reviews.csv` | 100 則商品評論（含評分） |
| `custom_dict.txt` | jieba 自訂詞典（格式：詞 詞頻 詞性） |
| `stopwords.txt` | 停用詞表 |

## 公開資料集（選用，需自行下載）

使用前請確認各資料集的授權與引用規範；本專案不內建這些資料。

| 來源 | 適用 | 說明 |
|---|---|---|
| `scikit-learn` 內建資料集 | 資料探勘 | `load_iris`、`load_wine`、`load_diabetes` 隨套件附帶，免下載 |
| `seaborn` 範例資料集 | 資料探勘 | `sns.load_dataset("tips")` 等，首次使用需連網下載 |
| 政府資料開放平臺（data.gov.tw） | 資料探勘、爬蟲 | 台灣政府開放資料，請依各資料集的開放授權條款使用 |
| UCI Machine Learning Repository | 資料探勘 | 如 Online Retail 交易資料可用於關聯規則；請依各資料集授權引用 |
| 練習用爬蟲站台（`quotes.toscrape.com`、`books.toscrape.com`） | 爬蟲 | 專為爬蟲練習設計，仍須遵守限速與禮貌爬取 |
