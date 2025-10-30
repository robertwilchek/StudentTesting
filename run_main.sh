#!/usr/bin/env bash
set -euo pipefail

python -m py_compile main.py
python main.py
