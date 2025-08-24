## 4️⃣ SQL — Basic Join

### 🎯 核心目標：熟悉資料表連接

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- CROSS JOIN

| 功能     | MSSQL                                                           | PostgreSQL | MySQL    |
| -------- | --------------------------------------------------------------- | ---------- | -------- |
| 內連接   | `SELECT a.col, b.col FROM t1 a INNER JOIN t2 b ON a.id = b.id;` | 同 MSSQL   | 同 MSSQL |
| 左連接   | `SELECT a.col, b.col FROM t1 a LEFT JOIN t2 b ON a.id = b.id;`  | 同 MSSQL   | 同 MSSQL |
| 右連接   | `SELECT a.col, b.col FROM t1 a RIGHT JOIN t2 b ON a.id = b.id;` | 同 MSSQL   | 同 MSSQL |
| 交叉連接 | `SELECT a.col, b.col FROM t1 a CROSS JOIN t2 b;`                | 同 MSSQL   | 同 MSSQL |

✅ 常見陷阱

- `INNER JOIN`：只取符合條件的紀錄。
- `LEFT JOIN`：保留左表所有紀錄，右表沒對應的會出現 `NULL`。
- `RIGHT JOIN`：保留右表所有紀錄，左表沒對應的會出現 `NULL`。
- `CROSS JOIN`：笛卡兒積，n × m 筆資料。
- 多表連接要注意 **順序與條件**，否則容易產生爆炸性的結果。
