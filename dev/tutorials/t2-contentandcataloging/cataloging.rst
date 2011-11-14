==========
Cataloging
==========


Getting Setup
=============

.. code-block:: bash

  $ easy_install -i http://dist.repoze.org/lemonade/dev/simple repoze.catalog

Cataloging Support in Models
============================

Add a catalog to the root object by modifying ``models/site.py``:

.. literalinclude:: feedstool-03/models/site.py
   :linenos:
   :language: py

- More imports

- Two functions to get representations of an object during indexing

- An ``__init__`` in ``Site`` that sets up the catalog.  **This means
  blow away Data.fs and friends!**

- Explain ``document_map``


Update tests to make sure a catalog (and document map) exists by
editing ``models/tests/test_site.py``:

.. literalinclude:: feedstool-03/models/tests/test_site.py
   :linenos:
   :language: py

- New test for verifying the presence of a catalog and document_map

Now run the tests and see if you have ``Ran 11 tests in 0.7 sec``.

Since we have a catalog in place, we can update
``models/subscribers.py`` to actually index on add events:

.. literalinclude:: feedstool-03/models/subscribers.py
   :linenos:
   :language: py

Adding a Search Form to Views
=============================

We have a search engine, let's put it to use.  First, let's have a box
appear on every page by editing ``views/templates/layout.pt``:

.. literalinclude:: feedstool-03/views/templates/layout.pt
   :linenos:
   :language: html

- We're adding the ``<form>`` in the sidebar

This submits to a URL ``/search.html`` to show the search results, so
we need a view in ``views/site.py``:

.. literalinclude:: feedstool-03/views/site.py
   :linenos:
   :language: py

- New imports

- We added a ``search_view`` but also a helper function
  ``catalog_search``

- The latter builds the query, issues the search, and "flattens" the
  result into boring Python data.  This makes it easier to deal with
  in the templates.  Plus, lots of times we want to modify the data
  for view purposes (e.g. date formatting).

- We try to use iterators

A view is needed at ``templates/search.pt`` to display the search
results:

.. literalinclude:: feedstool-03/views/templates/search.pt
   :linenos:
   :language: html

Wire up the view in ``views/configure.zcml``:

.. literalinclude:: feedstool-03/views/configure.zcml
   :linenos:
   :language: xml

- Last directive at the end

Add another view test at ``SiteViewTests.test_search_view`` in
``views/test_site.py``:

.. literalinclude:: feedstool-03/views/tests/test_site.py
   :linenos:
   :language: py

All 12 tests should now pass.  Delete your Data.fs and restart the server::

.. code-block:: bash

  $ rm Data.*
  $ paster serve FeedsTool.ini --reload

Add a new ``Feed`` with a title of ``The first feed``.  Then do a
search for ``first`` and a search for ``second``.

