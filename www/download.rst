Download and Installation
*************************

Not a developer?  There is also an online :doc:`KARL Demo <demo>` to evaluate the features and functionality of KARL.

As of the 3.0 release, KARL is relatively straightforward for both
developers and evaluators to download and install.  In particular,
there is **no installation for Windows**. See the :doc:`FAQ <faq>` for
an explanation and suggestion.

.. note::
    Note: The most up-to-date installation information is in the
    `developer installation page <http://dev.karlproject.org/devguide/installation.html>`_  
    and the ``README.txt`` that comes in the software.

KARL is typically deployed as a customizable buildout per customer.  We
have created a customized buildout for "karlsample" to provide an evaluation
of KARL for developers.

Prerequisites for Evaluation
============================

To get KARL running quickly as an evaluation, you can skip many of the steps
used in deployment. Before getting started, make sure you have the following
setup.

1. **Python 2.6.x**. While you can use a Python package installed by your
   system, we HIGHLY recommend that you build your own Python. Make sure you
   include SSL support in the Python.

2. **Version Control**. You need a way to check out the KARL software from the
   repository and keep it up to date. Both git and svn are required.

3. *virtualenv* (optional but recommended). Use Python's ``easy_install`` to
   install ``virtualenv`` and isolate it from changes in your Python
   configuration.

4. *Converters* (optional but recommended). Indexing content in PDF,
   Word, etc. requires some add-on packages. Look in the software's
   ``README.txt`` for more detail. This is optional and can be done
   after an installation of KARL.

Installation for the Impatient
==============================

Want to see what's involved before reading the `developer installation
instructions <http://dev.karlproject.org/devguide/installation.html>`_
or the ``README.txt``? Here are the immediate steps to get a running
KARL.

1. ``git clone git://github.com/karlproject/dev-buildout.git karl3``

2. ``cd karl3``

3. ``/path/to/your/python/bin/virtualenv --no-site-packages .``

4. ``bin/python ./bootstrap.py``

5. ``bin/buildout -U``

6. Wait a number of minutes while lots of work is done.

7. ``bin/supervisord``

8. Visit in your browser: `http://localhost:6543/fs/ <http://localhost:6543/fs/>`_
   and login as username ``admin`` and password ``admin``

9. When finished: ``bin/supverisorctl shutdown``

Much more detail, along with a number of options for starting KARL, stopping
KARL, and working productively are detailed in the ``README.txt`` in your
top-level ``karl3`` directory.
