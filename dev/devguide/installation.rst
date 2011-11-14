==========================
Installation and Running
==========================

It is easy to get a developer sandbox running for KARL3. (Deployment
sandboxes are covered elsewhere.)


Before Installation
====================

KARL3 is a :mod:`repoze.bfg` application, which means it needs Python
and some core Python tools before starting.

#. If you haven't made your own build of Python, download Python 2.6.x
   and compile it.

#. Make sure that your Python environment has `setuptools
   <http://pypi.python.org/pypi/setuptools>`_ installed, and that the
   correct `easy_install` is available in that environment.

#. Ditto for `virtualenv <http://pypi.python.org/pypi/virtualenv>`_.
   As the :mod:`repoze.bfg` docs explain, you can install virtualenv
   using easy_install.

These steps are fairly common for mainstream Python web development,
meaning they are well-documented and reliable.


Installation
============

.. code-block:: bash

  $ git clone git://github.com/karlproject/dev-buildout.git karl3
  $ cd karl3
  $ /path/to/your/python/bin/virtualenv --no-site-packages .
  $ bin/python ./bootstrap.py
  $ bin/buildout -U
  $ bin/supervisord

After five or ten seconds, visit in your browser:
http://localhost:6543/fs/ and login as username admin and password admin.

Much more installation information is available in the ``README.txt``
at the top of the checkout.

Writable Checkouts
==================

A writable checkout requires access to the github repository.

Once access is granted, check out the buildout as follows:

  $ git clone git@github.com:karlproject/dev-buildout.git karl3

And then create the virtualenv and run the buildout as above::

  $ cd karl3
  $ /path/to/correct/virtualenv --no-site-packages .
  $ bin/python ./bootstrap.py
  $ bin/buildout -U
  $ bin/supervisord
