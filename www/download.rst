Download and Installation
*************************

Not a developer?  There is also an online :doc:`KARL Demo <demo>` to evaluate the features and functionality of KARL.

As of the 3.0 release, KARL is relatively straightforward for both
developers and evaluators to download and install.  In particular,
there is **no installation for Windows**. See the :doc:`FAQ <faq>` for
an explanation and suggestion.

Prerequisites for Evaluation
============================

To get KARL running quickly as an evaluation, you can skip many of the steps
used in deployment. Before getting started, make sure you have the following
setup.

1. **Python 2.6.x**. While you can use a Python package installed by your
   system, we HIGHLY recommend that you build your own Python. Make sure you
   include SSL support in the Python.

2. **Version Control**. You need a way to check out the KARL software from the
   repository and keep it up to date. Git is required.

3. *virtualenv* (optional but recommended). Use Python's ``easy_install`` to
   install ``virtualenv`` and isolate it from changes in your Python
   configuration.

4. *Converters* (optional but recommended). Indexing content in PDF,
   Word, etc. requires some add-on packages. Look in the software's
   ``README.txt`` for more detail. This is optional and can be done
   after an installation of KARL.

Installation Instructions
=========================

The most up to date instructions can be found at the dev buildout on `github <https://github.com/karlproject/dev-buildout>`_.
