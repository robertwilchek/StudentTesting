#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python -m py_compile "${SCRIPT_DIR}/main.py"
python "${SCRIPT_DIR}/main.py"
