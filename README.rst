cookiecutter-pypackage-tool
===========================

Cookiecutter_ template designed for command-line tools.

Usage
-----

Install Cookiecutter_, then run:

.. code-block:: bash

    cookiecutter https://github.com/benwebber/cookiecutter-pypackage-tool.git

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
* self-contained RPM

License
-------

MIT

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _setuptools: https://pythonhosted.org/setuptools/
.. _runpy: https://docs.python.org/3.4/library/runpy.html
