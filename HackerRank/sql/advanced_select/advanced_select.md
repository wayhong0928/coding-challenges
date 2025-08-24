## 2️⃣ SQL — Advanced Select

### 🎯 核心目標：進一步控制查詢結果

- CASE WHEN THEN ELSE
- 日期 / 時間函數
- 字串處理（LEFT, RIGHT, SUBSTRING, CONCAT, LENGTH）
- 空值處理（COALESCE / IFNULL）

| 功能       | MSSQL                                    | PostgreSQL                          | MySQL                                      |
| ---------- | ---------------------------------------- | ----------------------------------- | ------------------------------------------ |
| 條件判斷   | `CASE WHEN cond THEN val ELSE other END` | 同 MSSQL                            | 同 MSSQL                                   |
| NULL 判斷  | `IS NULL / IS NOT NULL`                  | 同 MSSQL                            | 同 MSSQL                                   |
| 空值處理   | `ISNULL(col, val)`                       | `COALESCE(col, val)`                | `IFNULL(col, val)` 或 `COALESCE(col, val)` |
| 合併字串   | `CONCAT(col1, col2)` 或 `col1 + col2`    | `col1 \|\| col2` 或 `CONCAT()`      | `CONCAT(col1, col2)`                       |
| 字串長度   | `LEN(col)`                               | `LENGTH(col)`                       | `LENGTH(col)`                              |
| 子字串     | `SUBSTRING(col, start, len)`             | `SUBSTRING(col FROM start FOR len)` | `SUBSTRING(col, start, len)`               |
| 取左 N 字  | `LEFT(col, n)`                           | `LEFT(col, n)`                      | `LEFT(col, n)`                             |
| 取右 N 字  | `RIGHT(col, n)`                          | `RIGHT(col, n)`                     | `RIGHT(col, n)`                            |
| 大小寫轉換 | `UPPER(col), LOWER(col)`                 | 同 MSSQL                            | 同 MSSQL                                   |
| 去空白     | `LTRIM(), RTRIM()`                       | `TRIM(), BTRIM()`                   | `TRIM()`                                   |
| 當前時間   | `GETDATE()`                              | `NOW()`                             | `NOW()`                                    |
| 日期加減   | `DATEADD(DAY,1,GETDATE())`               | `d + interval '1 day'`              | `DATE_ADD(d, INTERVAL 1 DAY)`              |
| 日期差     | `DATEDIFF(DAY, d1, d2)`                  | `AGE(d1, d2)` 或 `d1 - d2`          | `DATEDIFF(d1, d2)`                         |

✅ 常見陷阱

- 日期函數三家差異大：MSSQL 用 `DATEADD/DATEDIFF`，PostgreSQL 用 `interval` 與 `AGE`，MySQL 用 `DATE_ADD/DATE_SUB`。
- CASE 條件判斷從上到下執行，先符合就結束。
- 字串串接：PostgreSQL 習慣用 `||`，MSSQL/MySQL 習慣用 `CONCAT`。
