============================
Getting Closer to FormEncode
============================

Let's get rid of the hard-wired fields and validators and jump
straight into :mod:`FormEncode.schema`.

This isn't a complete jump: we're still using our own
``baseform.validate`` method.  We'll get more FormEncode-onic in
following steps.

Still, we can see from the request/second in the footer that this
thing is pretty fast.

Basing on Schema
======================

#. The``BaseForm`` at ``t3/baseform.py`` is now a subclass of Schema:

   .. literalinclude:: src-03/baseform.py
      :linenos:
      :language: py

   - The ``validate`` method tells FormEncode to do most of the work.
     We use the error messages it produces.  This method can probably
     go away when we get more FormEncode-onic.

#. The ``t3/views.py`` module gets more realistic:

   .. literalinclude:: src-03/views.py
      :linenos:
      :language: py

   - We make a form ``MyAge`` with a FormEncode validator, then make a
     module-level instance we can re-use between requests.

   - Checking ``is_submitted`` sets the start_time for measurement.
     This breaks the no-state rule.

   - Validation returns converted values and field-level error
     messages.

   - If there were no errors, we can do the part where we
     create/update content.

   - If the form wasn't submitted, set some default values for the
     field values.  We could use FormEncode for this, but then the
     most common case (the first GET) would trigger the complete
     validation machinery, breaking one of our goals.

#. The ``t3/templates/myform.pt`` form grows a place to show a form
   message:

   .. literalinclude:: src-03/templates/myform.pt
      :linenos:
      :language: html

Notes
=========

- As you can see, there is no state that changes inside a KarlForm
  after it is constructed.  We pass data in and out (primarily, the
  field values and the errors.)
