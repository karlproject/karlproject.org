============================
Speedup, Edit, Lookup
============================

This section tackles a number of useful speedups common patterns:

- *Speedup with pre-built fields*.  Lots of sites use the same
   "fields" over an over.  Why reconfigure their validators
   repeatedly?  Define them once and re-use them, getting a
   performance boost at startup time.

- *Macros for "fields"*.  Similarly, why make a "name" field in all
   your ZPTs when it is the same ``<fieldset>`` over and over?  ZPT
   has a facility for sharing (macros), so let's put it to use.

- *Edit existing data*.  Add some links in the sidebar that allow
   editing existing data.  Makes the view more clumsy, as we'd prefer
   an edit view registered against an instance's interface.  Instead,
   we put more branching in our view.

   We'll fix this in the next step.

- *Vocabulary lookup*. Add a field for ``Country`` that comes from a
   vocabulary, as part of the "application".  Let ZPT iterate over
   this to generate the ``<select>`` and make sure the validator
   enforces it.

The Files
=========

#. The ``BaseForm`` at ``t3/baseform.py``:

   .. literalinclude:: src-04/baseform.py
      :linenos:
      :language: py

   - Make a mapping of some vocabularies.

   - Create some "fields" at startup time that are pre-configured and
     can be used in multiple schemas.  One of these fields
     (``country``) is a controlled vocabulary.  Values provided are
     checked against the vocabulary.

#. The view at ``t3/views.py`` handles more cases:

   .. literalinclude:: src-04/views.py
      :linenos:
      :language: py

   - Use the three pre-configured fields in the ``MyInfo`` form.

   - Make some data at ``records`` simulating some model data

   - In the view, see if we were handed an id as ``GET`` data.

   - Do some tests to whether to grab existing data.

   - Get the vocabulary data from the other module and pass it into
     the ZPT for the form.

#. The form template is now really small at ``t3/templates/myform.pt``:

   .. literalinclude:: src-04/templates/myform.pt
      :linenos:
      :language: html

   - Point at macros in ``formfields.pt`` for all the form fields.

#. Common fields are shared as ZPT macros in ``t3/templates/formfields.pt``:

   .. literalinclude:: src-04/templates/formfields.pt
      :linenos:
      :language: html

   - A macro for each field, plus the message and the buttons.

   - The ``country`` field iterates over the vocabulary, making
     ``<option>`` nodes.
