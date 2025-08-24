## 6️⃣ SQL — Alternative Queries

### 🎯 核心目標：用不同寫法解決相同問題

- Subquery（子查詢）
- EXISTS / NOT EXISTS
- ANY / ALL
- WITH (CTE, Common Table Expressions)

| 功能                          | MSSQL                                                                         | PostgreSQL | MySQL           |
| ----------------------------- | ----------------------------------------------------------------------------- | ---------- | --------------- |
| 子查詢 (Subquery)             | `SELECT col FROM t1 WHERE col IN (SELECT col FROM t2);`                       | 同 MSSQL   | 同 MSSQL        |
| EXISTS                        | `SELECT col FROM t1 WHERE EXISTS (SELECT 1 FROM t2 WHERE t1.id = t2.id);`     | 同 MSSQL   | 同 MSSQL        |
| NOT EXISTS                    | `SELECT col FROM t1 WHERE NOT EXISTS (SELECT 1 FROM t2 WHERE t1.id = t2.id);` | 同 MSSQL   | 同 MSSQL        |
| 任一符合 (ANY / SOME)         | `WHERE col = ANY (SELECT col FROM t2)`                                        | 同 MSSQL   | 同 MSSQL        |
| 全部符合 (ALL)                | `WHERE col > ALL (SELECT col FROM t2)`                                        | 同 MSSQL   | 同 MSSQL        |
| CTE (Common Table Expression) | `WITH cte AS (SELECT ... FROM t1) SELECT * FROM cte;`                         | 同 MSSQL   | MySQL 8.0+ 支援 |

✅ 常見陷阱

- **Subquery vs JOIN**：子查詢可讀性高，但效能通常比 JOIN 差。
- **EXISTS vs IN**：
  - 小資料集 → `IN` 速度快。
  - 大資料集 → `EXISTS` 通常更有效率。
- `ANY` 與 `SOME` 在 SQL 標準中等價。
- CTE 在 MySQL **8.0 以前不支援**，但在 MSSQL / PostgreSQL 是常用語法。
