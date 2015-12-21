#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os.path
import sys


ASSET_TEMPLATE = """# -*- coding: utf-8 -*-

from __future__ import absolute_import

import contextlib

import pkg_resources


@contextlib.contextmanager
def asset(path, package=None):
    package = package if package else __name__
    yield pkg_resources.resource_stream(package, path)
"""


def main():
    {% if cookiecutter.assets == 'yes' %}
    try:
        path = '{{ cookiecutter.package_name }}/{{ cookiecutter.asset_package }}'
        os.makedirs(path)
        with open(os.path.join(path, '__init__.py'), 'w') as f:
            f.write(ASSET_TEMPLATE)
    except Exception as e:
        print(e, file=sys.stderr)
        return 1
    {% endif %}
    return


if __name__ == '__main__':
    sys.exit(main())
