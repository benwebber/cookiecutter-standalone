#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

PROJECT=$1

mkdir -p build/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

cd build/rpmbuild

cp "../../rpm/${PROJECT}.spec" SPECS/
cp ../../scripts/* SOURCES/
cp ../../dist/*.tar.gz SOURCES/

rpmbuild --define "_topdir $(pwd)" -ba "SPECS/${PROJECT}.spec"

find . -name '*.rpm' -exec cp {} ../../dist/ \;
