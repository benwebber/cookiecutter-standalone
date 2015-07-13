# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name='{{ cookiecutter.repo_name }}',
    version='{{ cookiecutter.package_version }}',
    url='{{ cookiecutter.package_url }}',

    description="{{ cookiecutter.project_short_description }}",
    long_description=open('README.rst').read(),

    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',

    packages=setuptools.find_packages(),

    install_requires=[],

    include_package_data=True,
    zip_safe=False,

    entry_points={
        'console_scripts': [
            '{{ cookiecutter.repo_name }} = {{ cookiecutter.package_name }}.__main__:main',
        ],
    },

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
