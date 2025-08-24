## 1️⃣ SQL — Basic Select

### 🎯 核心目標：熟悉資料查詢語法

- SELECT 基本語法
- DISTINCT
- WHERE 條件（=, <, >, BETWEEN, LIKE, IN）
- ORDER BY
- LIMIT / TOP

| 功能      | MSSQL                               | PostgreSQL                     | MySQL         |
| --------- | ----------------------------------- | ------------------------------ | ------------- |
| 基本查詢  | `SELECT col FROM table;`            | 同 MSSQL                       | 同 MSSQL      |
| 全部欄位  | `SELECT * FROM table;`              | 同 MSSQL                       | 同 MSSQL      |
| 去重      | `SELECT DISTINCT col FROM table;`   | 同 MSSQL                       | 同 MSSQL      |
| 篩選      | `WHERE col = 10`                    | 同 MSSQL                       | 同 MSSQL      |
| 範圍      | `WHERE col BETWEEN 1 AND 10`        | 同 MSSQL                       | 同 MSSQL      |
| 多值比對  | `WHERE col IN (1,2,3)`              | 同 MSSQL                       | 同 MSSQL      |
| 模糊比對  | `WHERE col LIKE 'A%'`               | `LIKE` 或 `ILIKE` (不分大小寫) | `LIKE`        |
| 排序      | `ORDER BY col ASC/DESC`             | 同 MSSQL                       | 同 MSSQL      |
| 取前 N 筆 | `SELECT TOP 5 col`                  | `LIMIT 5`                      | `LIMIT 5`     |
| 分頁      | `OFFSET` 不支援 → 用 `ROW_NUMBER()` | `LIMIT 5 OFFSET 10`            | `LIMIT 10, 5` |
| 別名      | `SELECT col AS alias`               | 同 MSSQL                       | 同 MSSQL      |

✅ 常見陷阱

- LIKE `%` 多字元，`_` 單字元
- NULL ≠ `''`
- 排序預設 `ASC`
