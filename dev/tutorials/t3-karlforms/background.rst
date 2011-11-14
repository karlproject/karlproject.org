
.. _forms-tutorial-background:

======================
KARL3 Forms Background
======================

Goals
=====

#. *Fast*.  The :mod:`tw.forms` system wasn't nearly fast enough.  We
   want something very fast, especially for the common case (first
   retrieval.)  Stated differently: "Keep the simple case FAST!"

#. *Simple*. The KARL3 developers found the earlier approach
   (FormEncode plus tw.forms + a formcontroller) to be indecipherable,
   both on simple functionality and on debugging.  Of course, part of
   simple means "leverage things you already understand", leading to
   the next point.  In particular: "Keep the simple case SIMPLE."

#. *Leverage ZPT*.  Move more of the work into a template, where form
   developers are probably comfortable on idioms where markup is
   produced.

   - *Be "field-oriented"*.  Meaning, don't try to make re-usable
     widgets with knobs that set CSS etc.  Instead, make a "title"
     field, instead of a TextInput that is configured with
     settings. If you need CSS, just put it in the ZPT for that HTML
     node.

   - *Say it in ZPT*.  Similar to the above.  Is "Age" required on a
      form?  Then put ``class="required`` on the ``<label>``.  Need to
      translate the label?  Use the ZPT facility for localization.
      Need help text?  Put it just under the label.  Need a background
      image on a sidebar?  Put ``<div class="sidebar">`` and float it.
      Error messages?  Let ZPT decide where to put it.

#. *Less Magic*.  Instead of trying to solve every possible problem
   with deep voodoo, do less.  Try to keep more of the UI in the realm
   of ZPT.  Also, keep strict lines between the form and the view and
   the model.  Don't let, for example, the form auto-populate values
   from the model.  Pass them in explicitly.  More work up front, but
   it prevents premature hair loss.

#. *Use existing tools*.  A tiny layer over existing, stable
   technology that is familiar to your target audience is better than
   a self-contained stack.  With FormEncode validators and schemas,
   lxml.html's form filling, ZPT, and perhaps the component
   architecture, lots of the work is already done.

#. *Testability*. We might do things a bit more verbose, or require a
   bit more typing.  But the views we make, and the code path through
   them, should lend themselves to writing good unit tests.
