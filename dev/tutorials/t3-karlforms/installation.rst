=====================
Tutorial Installation
=====================

#. Make a virtualenv, source the environment, and install BFG with
   ZODB:

   .. code-block:: bash

     $ path-to-your-python/bin/virtualenv --no-site-packages t3
     New python executable in t3/bin/python2.5
     Also creating executable in t3/bin/python
     Installing setuptools............done.
     bash-3.2$ cd t3
     bash-3.2$ source bin/activate

#. Install lxml using a private copy of libxml2/libxslt:

   .. code-block:: bash

     (t3)bash-3.2$ STATIC_DEPS=true easy_install lxml

#. Install BFG:

   .. code-block:: bash

     (t3)bash-3.2$ easy_install -i http://dist.repoze.org/lemonade/dev/simple repoze.bfg

#. Use paster to make a new BFG-ZODB project:

   .. code-block:: bash

     (t3)bash-3.2$ paster create -t bfg_zodb t3
     (t3)bash-3.2$ cd t3
     (t3)bash-3.2$ python setup.py develop

#. Add a couple more dependencies:

   .. code-block:: bash

     (t3)bash-3.2$ easy_install FormEncode
     (t3)bash-3.2$ easy_install nose
     (t3)bash-3.2$ easy_install -i http://dist.repoze.org/lemonade/dev/simple repoze.folder

