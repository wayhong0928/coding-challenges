## 3️⃣ SQL — Aggregation

### 🎯 核心目標：彙總資料

- COUNT, SUM, AVG, MIN, MAX
- GROUP BY
- HAVING

| 功能              | MSSQL   aggregation                   | PostgreSQL | MySQL    |
| ----------------- | -------------------------- | ---------- | -------- |
| 計數（全部）      | `COUNT(*)`                 | 同 MSSQL   | 同 MSSQL |
| 計數（忽略 NULL） | `COUNT(col)`               | 同 MSSQL   | 同 MSSQL |
| 加總              | `SUM(col)`                 | 同 MSSQL   | 同 MSSQL |
| 平均              | `AVG(col)`                 | 同 MSSQL   | 同 MSSQL |
| 最大/最小         | `MAX(col), MIN(col)`       | 同 MSSQL   | 同 MSSQL |
| 分組              | `GROUP BY col`             | 同 MSSQL   | 同 MSSQL |
| 彙總條件          | `HAVING COUNT(*) > 1`      | 同 MSSQL   | 同 MSSQL |
| 分組排序          | `ORDER BY COUNT(col) DESC` | 同 MSSQL   | 同 MSSQL |
| 不重複計數        | `COUNT(DISTINCT col)`      | 同 MSSQL   | 同 MSSQL |

✅ 常見陷阱

- `COUNT(col)` 不會算 NULL，但 `COUNT(*)` 會算全部。
- `WHERE` 用於聚合前，`HAVING` 用於聚合後。
- 在 SELECT 子句裡，非聚合欄位必須出現在 `GROUP BY`。
