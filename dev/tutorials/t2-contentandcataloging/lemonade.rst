==================================================
 Formal Content Types with :mod:`repoze.lemonade`
==================================================

In the initial development of KARL3, we kept the "framework" very
thin.  Our "pay only for what you eat" mantra helped us see the virtue
of creating just the scaffolding we needed.

Along the way, we saw that the :mod:`CMF` pattern of a formal "content
type", known system wide and with some extra metadata, was useful.
The (*very* tiny) :mod:`repoze.lemonade` package grew to support these
very few demands.  The `Lemonade
<http://static.repoze.org/bfgdocs/narr/install.html#how-to-install>`_
docs attest to how focused the mini-framework was kept.

In particular, Lemonade lets the Zope Component Architecture do most
of the work.

In this tutorial, we will convert our "content types" (content managed
through-the-web and later, indexed in a catalog) into Lemonade content
types.  We will then leverage this facility to introduce event
subscribers triggered by changes in content.

Tasks
=====

#. Install :mod:`repoze.lemonade` into your sandbox.

#. Change the ZCML to use the Lemonade directives.

#. Update the views to use Lemonade facilities for creating content.

#. Write and register our first event subscriber.

Install :mod:`repoze.lemonade`
==============================

Before using Lemonade, we need to install it into our sandbox:

.. code-block:: bash

  $ easy_install -i http://dist.repoze.org/lemonade/dev/simple repoze.lemonade


Lemonade Directives in ZCML
===========================

.. literalinclude:: feedstool-02/models/configure.zcml
   :linenos:
   :language: xml

- add xmlns

- include lemonade directives

- 3 directives

Use `create_content` In Views
=============================

.. literalinclude:: feedstool-02/views/site.py
   :linenos:
   :language: py

- do imports

- remove the import of Feed (since we don't make instances ourselves)

- create_content in add_feed_view


First Event Subscriber
======================

.. literalinclude:: feedstool-02/models/subscribers.py
   :linenos:
   :language: py

- new module

Restart the server, visit ``http://localhost:6543/``, and add a feed.
In your server window you should see:

.. code-block:: bash

  $ paster serve FeedsTool.ini --reload
  Starting subprocess with file monitor
  Starting server in PID 19498.
  serving on 0.0.0.0:6543 view at http://127.0.0.1:6543
  No handlers could be found for logger "ZODB.FileStorage"
  Object added My First Feed

As you can see on the last line, our event subscriber was run when the
``IObjectAddedEvent`` event was triggered, as configured in the
``models/configure.zcml`` subscriber.

Subscribers make a nice way for external packages to get plugged-in
and watch for things that are of interest to them.  This further
re-inforces the utility of ZCML as a configuration language.

