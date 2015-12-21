#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

PROJECT=$1
VERSION=$2
PACKAGE=$3
WHEEL=$4
PLATFORM="$(python -c 'import setuptools; print(setuptools.distutils.util.get_platform())')"
ARTIFACT="${PROJECT}-${VERSION}-${PLATFORM}"
BUILD_DIR="build/standalone.${PLATFORM}/build"
OUTPUT_DIR="build/standalone.${PLATFORM}/output"

# Make separate directories to install package and collect output.
mkdir -p "${BUILD_DIR}"
mkdir -p "${OUTPUT_DIR}"

# Install package and dependencies to build directory.
pip install "dist/${WHEEL}" --no-compile --target "${BUILD_DIR}"

# Make runnable zip file.
zip -jr "${OUTPUT_DIR}/${ARTIFACT}.zip" "${PACKAGE}/__main__.py"

# Install packages to zip file.
(cd "${BUILD_DIR}" && zip -gr "../output/${ARTIFACT}.zip" .)

# Make zip file executable.
echo '#!/usr/bin/env python' | cat - "${OUTPUT_DIR}/${ARTIFACT}.zip" > "${OUTPUT_DIR}/${ARTIFACT}"
install -m 755 "${OUTPUT_DIR}/${ARTIFACT}" "dist/${ARTIFACT}"
