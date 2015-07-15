#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

PROJECT=$1
PACKAGE=$2
WHEEL=$3

# Install package and dependencies to build directory.
pip install "dist/${WHEEL}" --no-compile --target build/standalone

# Make runnable zip file.
zip -jr "build/${PROJECT}.zip" "${PACKAGE}/__main__.py"

# Install packages to zip file.
(cd build/standalone && zip -gr "../${PROJECT}.zip" .)

# Make zip file executable.
echo '#!/usr/bin/env python' | cat - "build/${PROJECT}.zip" > "build/${PROJECT}.pyz"
install -m 755 "build/${PROJECT}.pyz" "dist/${PROJECT}"
