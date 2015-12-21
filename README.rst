cookiecutter-standalone
=======================

Cookiecutter_ template designed for self-contained command-line tools.

Requires Cookiecutter_ 1.1 or later.

Usage
-----

Install Cookiecutter_, then run:

.. code-block:: bash

    cookiecutter https://github.com/benwebber/cookiecutter-standalone.git

Features
--------

Flexible entry points
~~~~~~~~~~~~~~~~~~~~~

Cover all the bases with setuptools_ and runpy_:

* Install and run from your setuptools_ install path::

    $ pip install tool
    $ tool

* Install and run as a module::

    $ python -m tool

* Run from the source directory::

    $ python tool/

* Run from a self-contained zip archive::

    $ ./tool

Flexible packaging
~~~~~~~~~~~~~~~~~~

Supports:

* source distribution
* wheel
* self-contained executable archive
* RPM containing isolated virtual environment

Asset management
~~~~~~~~~~~~~~~~

Optionally bundle assets with your application.

If enabled, the cookiecutter will create an ``assets`` package and ``assets.asset()`` context manager. Install your assets to the sub-package:

.. code-block::

    example
    ├── __init__.py
    ├── __main__.py
    ├── assets
    │   ├── __init__.py
    │   └── example.txt
    └── cli.py

Then access them like so:

.. code-block:: python

    from .assets import asset

    with asset('example.txt') as f:
        print(f.read())

Thanks to the magic of pkg_resources_, this even works inside standalone archives.

Note that this technique adds setuptools_ as an install dependency. You probably want to pin setuptools_ to a specific version.

License
-------

MIT

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _setuptools: https://pythonhosted.org/setuptools/
.. _runpy: https://docs.python.org/3.4/library/runpy.html
.. _pkg_resources: https://pythonhosted.org/setuptools/pkg_resources.html
