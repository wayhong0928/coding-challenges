#!/usr/bin/env python3
"""
簡易 Scaffold：python scripts/gen_test_stub.py <src_path> <call_expr> <expected>
"""

import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TESTS = ROOT / "tests"


def main():
    src, call_expr, expected = sys.argv[1:]
    src_path = Path(src)
    dest_dir = TESTS / src_path.parent
    dest_dir.mkdir(parents=True, exist_ok=True)
    (dest_dir / "__init__.py").touch(exist_ok=True)

    test_code = textwrap.dedent(
        f"""
        import pytest
        from {src_path.with_suffix("").as_posix().replace("/", ".")} import {src_path.stem}

        @pytest.mark.skip(\"\"\"TODO: 驗證 Sample 與邊界值\"\"\")
        def test_sample():
            assert {call_expr} == {expected}
    """
    ).lstrip()

    (dest_dir / f"test_{src_path.stem}.py").write_text(test_code)
    print("⚡  測試骨架已產生")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit("用法: gen_test_stub.py <src_path> <call_expr> <expected>")
    main()
