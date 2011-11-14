===========
Preparation
===========

#. Make your own Python 2.5 and put its `bin` directory first in
   your `PATH`.

#. Install latest `setuptools` into that Python.

#. Use that Python's `bin/easy_install` to install `virtualenv`.

#. Read the `repoze.bfg Introduction
   <http://static.repoze.org/bfgdocs/narr/introduction.html>`_ and
   perform the steps in the `Installing repoze.bfg
   <http://static.repoze.org/bfgdocs/narr/install.html>`_ and
   `Creating a repoze.bfg Project
   <http://static.repoze.org/bfgdocs/narr/project.html>`_ sections,
   **using the bfg_zodb** Paster template!!:

   .. code-block:: bash

     $ paster create -t bfg_zodb

   Name your project ``FeedsTool``.

   .. note::

     If you have trouble installing :mod:`repoze.bfg` due to
     compilation issues for lxml and libxml2, try the following
     command::

       $ STATIC_DEPS=true easy_install lxml

     This installs the lxml package directly, giving it options for
     getting a new, up-to-date version of libxml2.

#. Consider running the ``source bin/activate`` to make your shell
   environment wired to use the virtualenv.

#. Make sure you do the testing step and the startup step at the end
   of the "Creating a Project" section.

#. Read the `repoze.lemonade
   <http://static.repoze.org/lemonadedocs/>`_ docs.
