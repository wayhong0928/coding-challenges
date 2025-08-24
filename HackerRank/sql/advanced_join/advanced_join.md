## 5️⃣ SQL — Advanced Join

### 🎯 核心目標：更複雜的多表操作

- SELF JOIN
- FULL OUTER JOIN
- 多層 JOIN + 聚合
- UNION vs UNION ALL

| 功能                       | MSSQL                                                                | PostgreSQL        | MySQL                                               |
| -------------------------- | -------------------------------------------------------------------- | ----------------- | --------------------------------------------------- |
| 自連接 (Self Join)         | `SELECT a.col, b.col FROM t1 a JOIN t1 b ON a.pid = b.id;`           | 同 MSSQL          | 同 MSSQL                                            |
| 全外連接 (Full Outer Join) | `SELECT a.col, b.col FROM t1 a FULL OUTER JOIN t2 b ON a.id = b.id;` | `FULL OUTER JOIN` | ❌ 無，需 `LEFT JOIN ... UNION ... RIGHT JOIN` 模擬 |
| 多層 JOIN                  | `SELECT ... FROM t1 JOIN t2 ON ... JOIN t3 ON ...;`                  | 同 MSSQL          | 同 MSSQL                                            |
| 合併結果 (去重)            | `SELECT col FROM t1 UNION SELECT col FROM t2;`                       | 同 MSSQL          | 同 MSSQL                                            |
| 合併結果 (保留重複)        | `SELECT col FROM t1 UNION ALL SELECT col FROM t2;`                   | 同 MSSQL          | 同 MSSQL                                            |

✅ 常見陷阱

- `SELF JOIN` 必須使用 **別名**，否則無法區分同一張表的不同角色。
- `FULL OUTER JOIN`：MySQL **不支援**，需用 `UNION` 模擬。
- `UNION`：自動去重 → 可能比 `UNION ALL` 慢。
- `UNION ALL`：效率較高，但會保留重複紀錄。
