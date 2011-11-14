=================
Simple Validation
=================

In this first step we make a view with a self-posting form, but no
machinery at all.  No validators, no majik.  Instead, we show:

- In KARL, if the machinery ever gets in the way, just do things
  manually.

- A brief introduction to :mod:`lxml.html` and its form-filling
  capability.

Getting Started
================

#. cd to the ``t3`` directory, the one containing ``setup.py``.

#. Edit ``setup.py`` and say that this package uses :mod:`nose` as its
   test runner.  Do this by replacing the existing ``test_suite`` line
   with the following:

   .. code-block:: ini

      test_suite="nose.collector",

   KARL3 uses :mod:`nose` as its test suite runner.

#. Make sure the tests still run.  From the top ``t3`` directory:

   .. code-block:: bash

      (t3)bash-3.2$ python ./setup.py test
      running test
      running egg_info
      writing requirements to t3.egg-info/requires.txt
      writing t3.egg-info/PKG-INFO
      writing top-level names to t3.egg-info/top_level.txt
      writing dependency_links to t3.egg-info/dependency_links.txt
      writing entry points to t3.egg-info/entry_points.txt
      reading manifest file 't3.egg-info/SOURCES.txt'
      writing manifest file 't3.egg-info/SOURCES.txt'
      running build_ext
      test_my_view (t3.tests.ViewIntegrationTests) ... ok
      test_my_view (t3.tests.ViewTests) ... ok

      Ran 2 tests in 0.243s

      OK

#. Add some error logging middleware in your ``t3.ini`` file:

   .. code-block:: ini

     [DEFAULT]
     debug = true

     [app:zodb]
     use = egg:FeedsTool#app
     reload_templates = true
     debug_authorization = false
     debug_notfound = false
     zodb_uri = file://%(here)s/Data.fs?connection_cache_size=20000

     [pipeline:main]
     pipeline =
         egg:Paste#cgitb
         egg:repoze.zodbconn#closer
         egg:repoze.tm#tm
         zodb

     [server:main]
     use = egg:Paste#http
     host = 0.0.0.0
     port = 6543
   
#. Run the server:

   .. code-block:: bash

      (t3)bash-3.2$ paster serve t3.ini --reload

#. Visit ``http://localhost:6543/`` in your browser.  You should see
   the colorful BFG intro screen.

Make a Macro
============

To shorten the ZPT, let's have a "theme".

#. Create a ``t3/templates/layout.pt``:

   .. literalinclude:: src-01/templates/layout.pt
      :linenos:
      :language: html

   .. note::

     We include a spot in the footer to measure the performance of the
     form system part of the request.

#. This theme includes a new ``t3/templates/static/t3.css``:

   .. literalinclude:: src-01/templates/static/t3.css
      :linenos:
      :language: css

#. Change ``t3/templates/mytemplate.pt`` to fill the slot:

   .. literalinclude:: src-01/templates/mytemplate.pt
      :linenos:
      :language: html

#. We render the form separately from the page so we can use
   :mod:`lxml.html` to hack it.  The form is in
   ``t3/templates/myform.pt``:

   .. literalinclude:: src-01/templates/myform.pt
      :linenos:
      :language: html

   - Visually marking something "required" is simply a matter of
     markup.  No HTML generation.

   - We include a conditional spot to put an error message for the
     field.

#. The ``t3/views.py`` file does more work:

   .. literalinclude:: src-01/views.py
      :linenos:
      :language: py

   - Load the "layout" and pass it into the renderer.

   - Set ``formerror`` and ``fielderror`` to ``None`` by default, then
     make sure to pass it into the renderer.

   - Choose a ``default_age`` of ``40`` and a ``max_age`` of 200.  Set
     the default as the value we plan to shove into the form later
     using :mod:`lxml.html`.

   - Check to see if ``form.submitted`` is in the POST data.  If so,
     the form was submitted.

   - Grab the value of ``age``.  We want to consider this a required
     field.  So if it is missing or empty, flag an error.

   - Apply some primitive validation tests to ``age``.  Keep track of
     why it fails. Make sure to set the value we plan to shove into
     the form to what the user typed in.

   - Grab the ``myform.pt`` form definition and render it.  

   - Use :mod:`lxml.html` and its form machinery to parse the form, do
     some form-filling, and serialize the result.

#. Go to ``http://localhost:6543/`` in your browser and you should see
   the form.
