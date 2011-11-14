================
Processing Feeds
================

Getting Setup
=============

.. code-block:: bash

  $ easy_install FeedParser

Making a Console Script
=======================

- Add a ``feedstool/scripts`` dir and make the following in
  ``feedstool/scripts/update_feeds.py``:

.. literalinclude:: feedstool-03/scripts/update_feeds.py
   :linenos:
   :language: py


- Usually we edit ``setup.py`` to add an entry point which
  ``buildout`` would use to generate something in ``bin``.  For now,
  we'll just run it from the command line.

- Feed parsing

  - easy_install FeedParser

  - command-line script to handle feeds

  - Use catalog to display feedentry content in folder (interface,
    sorting, batching)

- Delete Data.fs, start server, add a Feed pointed at the URL of
  ``http://feedparser.org/docs/examples/atom10.xml``

- Make sure you are in a prompt that did ``source bin/activate`` and
  then run:

.. code-block:: bash

  $ python feedstool/scripts/update_feeds.py
