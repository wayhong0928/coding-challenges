# coding-challenges

本專案用來統整並管理我在 LeetCode 與 HackerRank 的解題紀錄，同時藉由實作流程學習測試與 CI/CD 實務；更重要的是，透過持續練習來鍛鍊思考與解決問題能力。

This project consolidates and manages my LeetCode and HackerRank solutions while giving me hands-on practice with testing and CI/CD workflows. More importantly, the continual practice sharpens my reasoning and problem-solving skills.

---

## 📂 Directory Layout

```text
coding-challenges/
├─ HackerRank/
│  ├─ python/algorithms/warm-up/
│  │   ├─ __init__.py
│  │   └─ a_very_big_sum.py          # Solution
│  └─ sql/basic_select/
│      ├─ __init__.py
│      └─ weather_observation_station_06.sql  # MSSQL Solution
├─ LeetCode/
│  └─ python/
│      ├─ __init__.py
│      └─ _1_two_sum.py              # class Solution
├─ tests/                            # 由 scripts/sync_tests.py 自動鏡像
│  └─ HackerRank/python/algorithms/warm-up/
│      └─ test_a_very_big_sum.py
├─ scripts/
│  ├─ sync_tests.py                  # 補 tests/ 鏡像 + __init__.py
│  └─ gen_test_stub.py               # 產生 pytest 雛形
├─ .github/workflows/ci.yml          # lint / mypy / pytest
├─ requirements-dev.txt              # pytest / ruff / black / mypy
├─ pytest.ini                        # pytest 全域設定
└─ README.md
```

---

### 🔖 Naming Rules

| Platform                | Path / Filename Pattern      | Example                                           |
| ----------------------- | ---------------------------- | ------------------------------------------------- |
| **HackerRank (Python)** | `<track>/<category>/slug.py` | `algorithms/warm-up/a_very_big_sum.py`            |
| **HackerRank (MSSQL)**  | `<category>/slug.sql`        | `basic_select/weather_observation_station_06.sql` |
| **LeetCode (Python)**   | `_####_<slug>.py`            | `_1_two_sum.py`                                   |
| **LeetCode (MSSQL)**    | `_####_<slug>.sql`           | `_175_combine_two_tables.sql`                     |

> Python 資料夾每層都含 `__init__.py`，IDE / mypy / pytest 才能正確 import。
> SQL 資料夾可選擇性加 `__init__.py`，但非必要。

---

### ⚙️ Local Dev Workflow

```powershell
# 1⃣  Python 3.11 venv
py -3.11 -m venv .venv
.\.venv\Scripts\activate          # mac/Linux: source .venv/bin/activate

# 2⃣  安裝 dev 依賴
pip install -r requirements-dev.txt

# 3⃣  同步 tests 鏡像 (補 __init__.py)
python scripts/sync_tests.py

# 4⃣  檢查
ruff check .
ruff format --check .
mypy HackerRank LeetCode
pytest -q

```

### 常見錯誤

| 訊息                                    | 解法                                                                       |
| --------------------------------------- | -------------------------------------------------------------------------- |
| `ERROR: file or directory not found: #` | 刪除 `pytest.ini` 行尾註解，或執行 `Remove-Item Env:PYTEST_ADDOPTS`        |
| `Duplicate module "python"`             | 在 `HackerRank/`、`LeetCode/` 加 `__init__.py`（`sync_tests.py` 會自動補） |
| `Need type annotation …`                | 為可變容器加型別，例如 `num_to_idx: dict[int, int] = {}`                   |

> 註：本專案目前不對 SQL 檔做自動 lint 或測試；僅保留解題紀錄。如將來要加入 SQL 測試或 lint，可在 CI 中另行設定。

---

## ➕ Adding a New Problem

```bash
# ❶  將 Solution 置入既定路徑
# ❷  python scripts/sync_tests.py        # 建 tests 鏡像
# ❸  python scripts/gen_test_stub.py <src.py> <call> <expected>
#      # 或手寫 tests/.../test_<slug>.py
# ❹  ruff / mypy / pytest
# ❺  git add . && git commit -m "feat: add <slug>" && git push
```
