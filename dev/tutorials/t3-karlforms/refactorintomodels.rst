====================
Refactor Into Models
====================

We've come quite far with the basic investigation of using FormEncode,
lxml.html, and ZPT to handle our form needs.  Our "form system" is
under 80 lines.

Let's take this chance to refactor into a more regular style of
application:

- *Focus on tests*.  So far the tutorial has taken an approach of
   writing code, then reloading in a browser to see if it
   worked. Running tests is the better pattern for the code-check-fix
   cycle.  Also, we need to make sure we are design a forms system
   that can test the various flows of control inside a view.

- *Actual models with persisten ZODB content*.  Using interfaces and
  classes, we can have edit forms that better match the form patterns
  we'll actually be using.

We will also change the templates to load jQuery (used in later
installments).  We will also try to leverage the FormEncode concept of
application "state" which can be passed into the validators.

Fix Tests
=========

Currently, if we run the tests, we see that both are broken:

   .. code-block:: bash

     (t3)bash-3.2$ python setup.py test
     [snip]
     ======================================================================
     FAIL: test_my_view (t3.tests.ViewIntegrationTests)
     ----------------------------------------------------------------------
     Traceback (most recent call last):
       File "/Users/paul/venvs/t3/t3/t3/tests.py", line 68, in test_my_view
           self.failUnless('Welcome to' in body)
     AssertionError

     ======================================================================
     FAIL: test_my_view (t3.tests.ViewTests)
     ----------------------------------------------------------------------
     Traceback (most recent call last):
       File "/Users/paul/venvs/t3/t3/t3/tests.py", line 31, in test_my_view
           renderer.assert_(project='t3')
       File "testing.py", line 215, in assert_
	   'A value for key "%s" was not passed to the renderer' % k)
     AssertionError: A value for key "project" was not passed to the renderer

     ----------------------------------------------------------------------
     Ran 2 tests in 1.091s

     FAILED (failures=2)

This is simple to fix: we changed the templates to no longer require
the project name to be passed in, and instead hard-coded them in the
template.  Three small changes in ``t3/tests.py``.

  .. code-block:: python

  	# Line 31
        self.assert_(hasattr(renderer, 'layout'))

	# Line 68
	self.failUnless('KARL3 Forms' in body)


Now the tests run again and we can start refactoring.

Models and Content
==================

Let's start by doing some refactoring that has little to do with
building a form system, and more to do with how we'll use forms.
Let's convert the application to add/view/edit/delete ``Person``
content.

#. Make a ``t3/interfaces.py``:

   .. literalinclude:: src-05/interfaces.py
      :linenos:
      :language: py

#. Change our ``t3/models.py`` to use different jargon, assert
   interfaces, use a constructor, etc.

   .. literalinclude:: src-05/models.py
      :linenos:
      :language: py

#. The ZCML needs to reflect the new order, as well as point at
   appropriate views:

   .. literalinclude:: src-05/configure.zcml
      :linenos:
      :language: xml

#. Finally, update the tests in ``t3/tests.py``:

   .. literalinclude:: src-05/tests.py
      :linenos:
      :language: py


Fix Views
=========

We made some changes to both the ZCML, so we need to change the views
and view tests.

#. Changes in ``t3/views.py``:

   .. literalinclude:: src-05/views.py
      :linenos:
      :language: py

#. Also in ``t3/baseform.py``:

   .. literalinclude:: src-05/views.py
      :linenos:
      :language: py

#. Finally the fields in ``t3/templates/formfields.pt``:

   .. literalinclude:: src-05/templates/formfields.pt
      :linenos:
      :language: html

We also made new templates for each the views mentioned.  The
``layout.pt`` got a better right-column menu, as well as three lines
for including jQuery and jQuery UI, plus our own ``t3.js``.
