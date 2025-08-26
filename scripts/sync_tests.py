#!/usr/bin/env python3
"""
sync_tests.py
  1. 掃 HackerRank/、LeetCode/ 內所有資料夾
  2. 在 tests/ 建鏡像資料夾
  3. 每層放 __init__.py，確保可匯入
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TESTS = ROOT / "tests"
SOURCES = [ROOT / "HackerRank", ROOT / "LeetCode"]


def main() -> None:
    TESTS.mkdir(exist_ok=True)
    (TESTS / "__init__.py").touch(exist_ok=True)

    for pkg in SOURCES:
        if pkg.exists():
            (pkg / "__init__.py").touch(exist_ok=True)

    created = 0
    created_paths = []
    for src_root in SOURCES:
        if not src_root.exists():
            continue
        for folder in src_root.rglob("*"):
            if folder.is_dir():
                dest = TESTS / folder.relative_to(ROOT)
                dest.mkdir(parents=True, exist_ok=True)
                init = dest / "__init__.py"
                if not init.exists():
                    init.touch()
                    created += 1
                    created_paths.append(str(init))
    print(f"✅ sync_tests 完成，新建 {created} 個 __init__.py")
    if created_paths:
        print("新建的 __init__.py 路徑如下：")
        for p in created_paths:
            print(p)


if __name__ == "__main__":
    main()
