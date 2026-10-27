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
- **Oracle 或 Milvus 容器啟動很慢？** 首次需下載映像檔且初始化較久，請待容器健康檢查通過後再連線。
- **可以跳過單元嗎？** 可以，明確告知想學的單元即可，但建議依序學習。

## 爬蟲大師使用說明

### 簡介
承繼「Python 教學助教」的進階課程，從爬蟲原理到實作，完成「擷取 → 解析 → 整理 → 分析」的完整流程，涵蓋爬蟲套件、網頁內容萃取、JSON 操作與爬蟲物件設計，並以 jieba 斷詞、Pandas 整理資料。每個單元包含概念說明、範例程式、練習題與單元考題。

### 前置需求
- VS Code 與 GitHub Copilot Chat
- 具備 Python 基礎（建議先完成「Python 教學助教」單元 1-11）
- 資料儲存單元可銜接「資料庫教學助教」（選修）

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
- **可以跳過單元嗎？** 可以，明確告知想學的單元即可，但建議依序學習。
