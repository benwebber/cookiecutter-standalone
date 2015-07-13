#!/usr/bin/env bash

mkdir -p build/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

cd build/rpmbuild

cp "../../rpm/${1}.spec" SPECS/
cp ../../scripts/* SOURCES/
cp ../../dist/*.tar.gz SOURCES/

rpmbuild --define "_topdir $(pwd)" -ba "SPECS/${1}.spec"

find . -name '*.rpm' -exec cp {} ../../dist/ \;
