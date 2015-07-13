#!/usr/bin/env bash

# Install package and dependencies to build directory.
pip install "dist/${2}" --no-compile --target build/standalone

# Make runnable zip file.
zip -jr "build/${1}.zip" "${1}/__main__.py"

# Install packages to zip file.
cd build/standalone && zip -gr "../${1}.zip" .

# Make zip file executable.
echo '#!/usr/bin/env python' | cat - "build/${1}.zip" > "build/${1}.pyz"
install -m 755 "build/${1}.pyz" "dist/${1}"
