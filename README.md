# core-knowledgebase
A project that is capable to build my own knowledge repository within my own Agent.

## Python 教學助教使用說明

### 簡介
手把手、循序漸進的 Python 教學 Agent。每個單元包含概念說明、範例程式、練習題與單元考題。

### 前置需求
- VS Code 與 GitHub Copilot Chat
- 已安裝 Python 3（供執行範例程式）

### 如何啟動
1. 開啟本專案資料夾於 VS Code。
2. 開啟 Copilot Chat，在 Agent 選單選擇「Python 教學助教」。
3. Agent 定義檔：[.github/agents/python-tutor.agent.md](.github/agents/python-tutor.agent.md)
4. 講義目錄與進度：[docs/python/README.md](docs/python/README.md)（目前已完成單元 1-5）

### 課程大綱
| 單元 | 主題 | 重點內容 |
|---|---|---|
| 1 | Python 基礎入門 | 安裝與執行環境、變數、基本型別 |
| 2 | 運算子與條件判斷 | 運算子、`if` / `elif` / `else` |
| 3 | 迴圈與迭代 | `for`、`while`、`break`、`continue` |
| 4 | 容器型別 | list、tuple、dict、set |
| 5 | 函式與作用域 | 定義函式、參數與回傳值、區域/全域變數 |
| 6 | 進階函式 | `lambda`、`map()`、`filter()`、`sorted(key=...)`、推導式 |
| 7 | 字串格式與正規表達式 | 字串方法、切片、f-string、`re` 模組 |
| 8 | 例外處理 | `try` / `except` / `finally` |
| 9 | 檔案讀寫與模組 | 開檔讀寫、`import`、自訂模組 |
| 10 | 物件導向程式設計 | 類別、物件、屬性、方法、繼承 |
| 11 | 標準函式庫與套件管理 | 常用內建模組、`pip` |
| 12 | 綜合實作專案 | 整合前述單元完成小專案 |

### 學習流程
概念說明 → 範例程式 → 練習 → 單元考題 → 公布答案 → 進入下一單元

### 常用指令範例
- 「我是零基礎，從第 1 單元開始」
- 「出第 3 單元的考題」
- 「公布第 3 單元考題答案」
- 「我想直接學第 5 單元：函式」

### 自訂與擴充
編輯 [.github/agents/python-tutor.agent.md](.github/agents/python-tutor.agent.md) 的「課程大綱」段落，即可新增、移除或調整單元。

### 常見問題
- **Agent 選單找不到助教？** 確認已開啟本專案資料夾，且 Agent 檔位於 `.github/agents/`。
- **可以跳過單元嗎？** 可以，明確告知想學的單元即可，但建議循序學習。
- **考題答案在哪？** 預設先隱藏，作答後或要求時才公布。

## 資料庫教學助教使用說明

### 簡介
承繼「Python 教學助教」的進階課程，以 Python 驅動搭配原生查詢語言（SQL、Mongo Shell、Redis CLI、Cypher），系統性教學關聯式、NoSQL 與向量資料庫。每個單元包含概念說明、範例程式、練習題與單元考題。

### 前置需求
- VS Code 與 GitHub Copilot Chat
- 具備 Python 基礎（建議先完成「Python 教學助教」單元 1-9 與 11）
- 已安裝 Docker Desktop（SQLite 與 Chroma 以外的資料庫皆以 Docker 建置）
- 教學測試資料位於 [data/database/](data/database/)，欄位說明見 [data/README.md](data/README.md)

### 如何啟動
1. 開啟本專案資料夾於 VS Code。
2. 開啟 Copilot Chat，在 Agent 選單選擇「資料庫教學助教」。
3. Agent 定義檔：[.github/agents/database-tutor.agent.md](.github/agents/database-tutor.agent.md)

### 課程大綱
| 單元 | 類別 | 主題 | 重點內容 |
|---|---|---|---|
| 1 | 基礎 | 資料庫基礎觀念與環境 | 資料庫類型、ACID / CAP、正規化、Docker 入門 |
| 2 | 關聯式 | SQLite | `sqlite3`、DDL / DML、基本 CRUD |
| 3 | 關聯式 | SQL 進階 | `JOIN`、聚合、子查詢、視圖、索引、交易 |
| 4 | 關聯式 | MySQL | InnoDB、使用者與權限、預存程序 |
| 5 | 關聯式 | Oracle Database | 與 MySQL 的差異、PL/SQL 入門、`python-oracledb` |
| 6 | 關聯式 | 關聯式實作 | 連線池、參數化查詢、SQLAlchemy、選型比較 |
| 7 | NoSQL | MongoDB | 文件模型、CRUD、聚合管線、索引 |
| 8 | NoSQL | Redis | 資料結構、TTL 與快取、發布/訂閱、持久化 |
| 9 | NoSQL | Neo4j | 圖形模型、Cypher、路徑查詢 |
| 10 | NoSQL | NoSQL 綜合實作 | 快取 + 文件 + 圖形的小型應用 |
| 11 | 向量 | 向量資料庫基礎 | Embedding、相似度度量、ANN 索引 |
| 12 | 向量 | Chroma | Collection、中繼資料過濾、本機持久化 |
| 13 | 向量 | Milvus | Schema、索引建立、向量搜尋 |
| 14 | 向量 | Elasticsearch | Mapping、全文檢索、向量與混合搜尋 |
| 15 | 向量 | 簡易 RAG 實作 | 文件切塊、向量檢索、組合提示詞 |
| 16 | 綜合 | 綜合專案與選型 | 整合前述單元並比較三大類資料庫 |

### 學習流程
環境建置 → 概念說明 → 範例程式（原生語言 + Python）→ 練習 → 單元考題 → 公布答案 → 進入下一單元

### 常用指令範例
- 「我已完成 Python 基礎，從第 1 單元開始」
- 「我想直接學第 7 單元：MongoDB」
- 「出第 4 單元的考題」
- 「公布第 4 單元考題答案」

### 自訂與擴充
編輯 [.github/agents/database-tutor.agent.md](.github/agents/database-tutor.agent.md) 的「課程大綱」段落，即可新增、移除或調整單元。

### 常見問題
- **Docker 範例的密碼可用於正式環境嗎？** 不可以，僅供本機學習；帳密請改用環境變數或 `.env`，且勿提交至版本控制。
- **範例資料從哪來？** 使用 `data/database/` 的虛構資料（關聯表、商品文件、圖形節點與關係、向量語料）；如需重新產生，執行 `python data/generate_data.py`。
- **Oracle 或 Milvus 容器啟動很慢？** 首次需下載映像檔且初始化較久，請待容器健康檢查通過後再連線。
- **可以跳過單元嗎？** 可以，明確告知想學的單元即可，但建議依序學習。

## 爬蟲大師使用說明

### 簡介
承繼「Python 教學助教」的進階課程，從爬蟲原理到實作，完成「擷取 → 解析 → 整理 → 分析」的完整流程，涵蓋爬蟲套件、網頁內容萃取、JSON 操作與爬蟲物件設計，並以 jieba 斷詞、Pandas 整理資料。每個單元包含概念說明、範例程式、練習題與單元考題。

### 前置需求
- VS Code 與 GitHub Copilot Chat
- 具備 Python 基礎（建議先完成「Python 教學助教」單元 1-11）
- 資料儲存單元可銜接「資料庫教學助教」（選修）
- 離線教學資料位於 [data/crawler/](data/crawler/) 與 [data/tokenization/](data/tokenization/)，欄位說明見 [data/README.md](data/README.md)

### 如何啟動
1. 開啟本專案資料夾於 VS Code。
2. 開啟 Copilot Chat，在 Agent 選單選擇「爬蟲大師」。
3. Agent 定義檔：[.github/agents/crawler-master.agent.md](.github/agents/crawler-master.agent.md)

### 課程大綱
| 單元 | 類別 | 主題 | 重點內容 |
|---|---|---|---|
| 1 | 原理 | 爬蟲原理 | HTTP、Cookie / Session、DOM、`robots.txt`、法律與倫理 |
| 2 | 原理 | `requests` 基礎 | GET / POST、Headers、`timeout`、Session、重試 |
| 3 | 萃取 | HTML 解析 | `BeautifulSoup`、`lxml`、CSS Selector、分頁追蹤 |
| 4 | 萃取 | XPath 與正規表達式 | `parsel` / `lxml` XPath、`re` 擷取、方法比較 |
| 5 | JSON | JSON 與 API | `json` 模組、巢狀走訪與攤平、以 DevTools 找 XHR API |
| 6 | 物件 | 爬蟲物件設計 | 類別封裝、`dataclass`、物件與 JSON 互轉、日誌 |
| 7 | 效能 | 非同步爬蟲 | `httpx` + `asyncio`、併發控制、限速、退避 |
| 8 | 框架 | Scrapy | Spider、Item、Pipeline、Middleware |
| 9 | 整理 | 資料儲存 | JSON Lines、CSV、SQLite、去重與增量更新 |
| 10 | 整理 | jieba 中文斷詞 | 斷詞模式、自訂詞典、停用詞、詞頻、關鍵字萃取 |
| 11 | 整理 | Pandas 資料整理 | `DataFrame`、`json_normalize`、清洗、`groupby`、輸出 |
| 12 | 綜合 | 綜合專案 | 爬取 → 封裝 → JSON → 斷詞 → 詞頻報表 |

### 學習流程
概念說明 → 範例程式 → 練習 → 單元考題 → 公布答案 → 進入下一單元

### 常用指令範例
- 「我已完成 Python 基礎，從第 1 單元開始」
- 「我想直接學第 5 單元：JSON 與 API」
- 「出第 10 單元的考題」
- 「公布第 10 單元考題答案」

### 自訂與擴充
編輯 [.github/agents/crawler-master.agent.md](.github/agents/crawler-master.agent.md) 的「課程大綱」段落，即可新增、移除或調整單元。

### 常見問題
- **可以教 Selenium、Cypress 或 Playwright 嗎？** 不可以，本課程刻意不使用瀏覽器自動化工具；動態網頁改以分析 XHR / JSON API 的方式處理。
- **可以爬任何網站嗎？** 不可以，請遵守 `robots.txt` 與服務條款，練習以專為爬蟲練習的站台為主；課程不涵蓋繞過驗證碼、登入、封鎖等反爬機制。
- **沒有網路或不想爬真實站台怎麼練習？** 使用 `data/crawler/` 的離線 HTML 與 API 回應樣本，以及 `data/tokenization/` 的斷詞語料。
- **可以跳過單元嗎？** 可以，明確告知想學的單元即可，但建議依序學習。

## 資料探勘教學助教使用說明

### 簡介
承繼「Python 教學助教」的進階課程，帶領學生完成「資料載入 → 清洗 → 轉換 → 探索 → 視覺化 → 關聯分析」的完整資料探勘流程，並深入介紹 NumPy（`ndarray`）、Pandas、Matplotlib 等套件，每個單元皆附完整可執行的範例、練習題與單元考題。

### 前置需求
- VS Code 與 GitHub Copilot Chat
- 具備 Python 基礎（建議先完成「Python 教學助教」單元 1-11）
- 安裝套件：`numpy`、`pandas`、`matplotlib`、`seaborn`、`mlxtend`、`scikit-learn`、`openpyxl`（建議使用 `venv`）
- 教學測試資料位於 [data/data-mining/](data/data-mining/)，欄位說明見 [data/README.md](data/README.md)

### 如何啟動
1. 開啟本專案資料夾於 VS Code。
2. 開啟 Copilot Chat，在 Agent 選單選擇「資料探勘教學助教」。
3. Agent 定義檔：[.github/agents/data-mining-tutor.agent.md](.github/agents/data-mining-tutor.agent.md)

### 課程大綱
| 單元 | 類別 | 主題 | 重點內容 |
|---|---|---|---|
| 1 | 概觀 | 資料探勘概觀與環境 | KDD / CRISP-DM、任務類型、環境建置、套件總覽 |
| 2 | 數值運算 | NumPy 基礎 | `ndarray` 建立、`shape` / `dtype`、索引切片、重塑 |
| 3 | 數值運算 | NumPy 進階 | 向量化、廣播、`axis` 運算、線性代數 |
| 4 | 載入/清洗/轉換 | Pandas 資料結構 | `Series`、`DataFrame`、`loc` / `iloc`、`describe()` |
| 5 | 載入/清洗/轉換 | 資料載入 | CSV、Excel、JSON、資料庫、`chunksize` |
| 6 | 載入/清洗/轉換 | 資料清洗 | 缺值、重複、異常值（IQR、Z-score）、型別轉換 |
| 7 | 載入/清洗/轉換 | 資料轉換 | 分箱、編碼、標準化、`groupby`、`merge` |
| 8 | 探索/視覺化 | 探索式資料分析（EDA） | 描述統計、分布、群組摘要、相關係數矩陣 |
| 9 | 探索/視覺化 | Matplotlib 視覺化 | `Figure` / `Axes`、常見圖表、子圖、中文字型 |
| 10 | 探索/視覺化 | 進階視覺化 | Seaborn、Pandas 內建繪圖、圖表選擇 |
| 11 | 關聯分析 | 相關性分析 | Pearson / Spearman、熱圖、卡方檢定概念 |
| 12 | 關聯分析 | 關聯規則探勘 | 支持度 / 信賴度 / 提升度、Apriori、FP-Growth |
| 13 | 綜合 | 綜合專案 | 載入 → 清洗 → 轉換 → EDA → 視覺化 → 關聯分析 → 報告 |

### 學習流程
概念說明 → 套件介紹 → 完整範例 → 練習 → 單元考題 → 公布答案 → 進入下一單元

### 常用指令範例
- 「我已完成 Python 基礎，從第 1 單元開始」
- 「用 `sales_raw.csv` 教我資料清洗」
- 「我想直接學第 12 單元：關聯規則」
- 「出第 6 單元的考題」
- 「公布第 6 單元考題答案」

### 自訂與擴充
編輯 [.github/agents/data-mining-tutor.agent.md](.github/agents/data-mining-tutor.agent.md) 的「課程大綱」段落，即可新增、移除或調整單元。

### 常見問題
- **範例資料從哪來？** 優先使用 `data/data-mining/` 的虛構資料；如需重新產生，執行 `python data/generate_data.py`。
- **Matplotlib 中文顯示成方框？** 需設定支援中文的字型，單元 9 會說明做法。
- **清洗時會修改原始資料嗎？** 不會，課程要求保留原始檔，結果輸出到新變數或新檔案。
- **可以跳過單元嗎？** 可以，明確告知想學的單元即可，但建議依序學習。

## 機器學習教學助教使用說明

### 簡介
承繼「Python 教學助教」與「資料探勘教學助教」的進階課程，系統性教學回歸、分類、分群等機器學習模型，並以仿安隆案的員工資料完成分類實作。每個單元包含概念與直覺、完整範例、練習題與單元考題。

### 前置需求
- VS Code 與 GitHub Copilot Chat
- 具備 Python 基礎（「Python 教學助教」單元 1-11），以及 NumPy、Pandas、Matplotlib 與資料清洗轉換（「資料探勘教學助教」單元 2-10）
- 安裝套件：`scikit-learn`、`numpy`、`pandas`、`matplotlib`、`seaborn`、`scipy`、`joblib`、`jieba`（選用：`imbalanced-learn`、`xgboost`、`lightgbm`）
- 教學測試資料位於 [data/machine-learning/](data/machine-learning/)，欄位說明見 [data/README.md](data/README.md)

### 如何啟動
1. 開啟本專案資料夾於 VS Code。
2. 開啟 Copilot Chat，在 Agent 選單選擇「機器學習教學助教」。
3. Agent 定義檔：[.github/agents/ml-tutor.agent.md](.github/agents/ml-tutor.agent.md)

### 課程大綱
| 單元 | 類別 | 主題 | 重點內容 | 教學資料 |
|---|---|---|---|---|
| 1 | 基礎 | 機器學習基礎介紹 | 學習類型、流程、`scikit-learn` 介面、過擬合、偏差與變異 | 內建資料集 |
| 2 | 基礎 | 資料準備與模型評估 | 切分、交叉驗證、`Pipeline`、回歸與分類指標、類別不平衡 | 內建資料集 |
| 3 | 回歸/分類 | 回歸分析 | 線性回歸、多項式、Ridge / Lasso、殘差分析 | `advertising.csv`、`housing.csv` |
| 4 | 回歸/分類 | 邏輯斯迴歸 | Sigmoid、門檻、勝算比、正則化 | 內建資料集 |
| 5 | 回歸/分類 | 決策樹模型 | Gini / 熵、剪枝、特徵重要性、視覺化 | 內建資料集 |
| 6 | 回歸/分類 | 支持向量機（SVM） | 最大邊界、核函數、`C` / `gamma`、調參 | 內建資料集 |
| 7 | 回歸/分類 | 樸素貝氏 | 貝氏定理、三種變體、中文文字分類 | `tokenization/reviews.csv` |
| 8 | 回歸/分類 | 類神經網路 | MLP、激活函數、反向傳播概念、早停 | 內建資料集 |
| 9 | 回歸/分類 | 集成式學習 | 隨機森林、Boosting、Voting、Stacking | 內建資料集 |
| 10 | 案例實作 | 安隆案預測模型 | 異常值、缺值、特徵工程、不平衡、多模型比較與解讀 | `enron_style_employees.csv` |
| 11 | 分群 | 分群基礎 | 距離度量、K-Means、肘部法、輪廓係數 | `customer_rfm.csv` |
| 12 | 分群 | 階層式分群（凝聚式） | 連結方式、樹狀圖判讀 | `customer_rfm.csv` |
| 13 | 分群 | 分裂式分群 | Bisecting K-Means、DIANA 概念 | `customer_rfm.csv` |
| 14 | 分群 | 密度式分群 | DBSCAN、`eps` / `min_samples`、離群點 | `shapes_2d.csv` |
| 15 | 分群 | 分群案例實作 | 顧客 RFM 分群與四種方法比較 | `customer_rfm.csv`、`shapes_2d.csv` |
| 16 | 綜合 | 綜合專案 | 端到端流程、模型儲存、報告與選型 | 自選 |

### 學習流程
概念與直覺 → 套件介紹 → 完整範例 → 練習 → 單元考題 → 公布答案 → 進入下一單元

### 常用指令範例
- 「我已具備資料探勘基礎，從第 1 單元開始」
- 「用 `advertising.csv` 教我多元線性回歸」
- 「我想直接做第 10 單元：安隆案預測」
- 「出第 9 單元的考題」
- 「公布第 9 單元考題答案」

### 自訂與擴充
編輯 [.github/agents/ml-tutor.agent.md](.github/agents/ml-tutor.agent.md) 的「課程大綱」段落，即可新增、移除或調整單元。

### 常見問題
- **安隆案用的是真實資料嗎？** 不是，使用的是由 `python data/generate_data.py` 產生的虛構員工資料，不含真實人名；真實安隆資料集屬公開資料，可作為選用延伸，使用前請確認授權。
- **為什麼不能只看準確率？** 安隆資料的 POI 僅約 12%，只預測「非 POI」也有高準確率，課程會搭配 Precision、Recall、F1 與 ROC-AUC 說明。
- **有深度學習嗎？** 單元 8 以 `scikit-learn` 的 MLP 為主，並簡介 PyTorch / TensorFlow 的定位，不深入框架實作。
- **邏輯斯迴歸為何排在決策樹之前？** 它延續回歸分析的概念，作為分類的銜接；若偏好依原順序，可告知助教調整。
- **可以跳過單元嗎？** 可以，明確告知想學的單元即可，但建議依序學習。
