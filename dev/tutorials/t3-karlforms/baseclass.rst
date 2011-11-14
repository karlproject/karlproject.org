================
First Base Class
================

The previous step showed how to do the basics: let ZPT do most of the
work and apply :mod:`lxml.html` to shove values in.

Obviously the previous step was very hard-wired.  In this step we make
a base class for the form that starts to move some of the work out of
the view and into a form.  We won't, in this step, introduce the
concept of multiple fields with declarative validators.  But we will
follow some of the same jargon we'll use later with :mod:`FormEncode`
schemas.

Plug in the Base Class
======================

#. Add a module for a ``BaseForm`` at ``t3/baseform.py``:

   .. literalinclude:: src-02/baseform.py
      :linenos:
      :language: py

   - Sure, we're hardwiring in a bunch of stuff as class attributes.

   - The constructor gets the ``request`` passed into it.

   - An ``is_submitted`` property lets us know if the form was posted
     or not.  If not, the view can skip much of the work.

   - A ``validate`` method does some logic and updated ``formerror``
     and ``fielderrors``.  It also updated ``fieldvalues``, as a way
     to let the outside system be told when to shove in the default
     value or a transient value.

   - The ``render`` method uses :mod:`lxml.html` to shove the correct
     form values into the correct fields.

#. The ``t3/views.py`` module gets a lot simpler:

   .. literalinclude:: src-02/views.py
      :linenos:
      :language: py

#. The ``t3/templates/myform.pt`` form becomes more generic when
   grabbing errors:

   .. literalinclude:: src-02/templates/myform.pt
      :linenos:
      :language: html
