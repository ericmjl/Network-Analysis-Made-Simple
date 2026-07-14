#!/usr/bin/env bash
# Export all marimo .py notebooks to .ipynb for the mkdocs build.
# The .ipynb files are gitignored artifacts — they are regenerated from
# the marimo .py source files each time the docs are built.
set -euo pipefail

grep -rl "import marimo" notebooks/ --include="*.py" | sort | while read -r py_file; do
    ipynb_file="${py_file%.py}.ipynb"
    echo "Exporting $py_file -> $ipynb_file"
    marimo export ipynb "$py_file" --output "$ipynb_file"
done
