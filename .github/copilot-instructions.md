# core-knowledgebase 開發規範

## 教學 Agent 與測試資料
- 新增教學類 Agent（`.github/agents/*.agent.md`）時，需依課程規劃評估所需的範例與練習資料，並將資料產出至 `data/<課程名稱>/`。
- 可程式產生的表格或 JSON 資料，新增函式至 `data/generate_data.py`（固定亂數種子、僅使用標準函式庫）；手寫內容（HTML、文字語料等）直接建立檔案。
- 資料一律虛構，不含真實個資與有授權疑慮的內容；需要時刻意加入缺值、異常值等練習用瑕疵。
- 同步更新 `data/README.md`（檔案說明與練習重點）、Agent 內「教學資料」指示，以及根目錄 `README.md` 的對應使用說明。
