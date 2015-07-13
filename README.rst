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

* Flexible entry points. Covers all the bases with setuptools_ and runpy_::

  - Install and run from your setuptools_ install path:

      .. code-block:: bash

        $ pip install tool
        $ tool

  - Install and run as a module:

        .. code-block:: bash

         $ python -m tool

  - Run from the source directory:

        .. code-block:: bash

         $ python tool/

  - Run from a self-contained zip archive:

        .. code-block:: bash

         $ ./tool

* Flexible packaging. Supports:

  - source distribution
  - wheel
  - self-contained executable archive
  - self-contained RPM

License
-------

MIT

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _setuptools: https://pythonhosted.org/setuptools/
.. _runpy: https://docs.python.org/3.4/library/runpy.html
