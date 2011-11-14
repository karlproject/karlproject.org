===============
More Validators
===============

We have a strong basis in place now:

- A sample application that lists people, along with add/edit/view
  person

- Validators from FormEncode and markup from ZPT

We can now explore some other validators and patterns:

- *``is_cancelled`` support*.  Forms should have a cancel button that
  bails out on the form and takes you back to the parent.

- *Confirm password*.  Have a password field with a minimal length
  that must match another field.

#. The ``t3/baseform.py``:

   .. literalinclude:: src-06/baseform.py
      :linenos:
      :language: py

#. The views at ``t3/views.py``:

   .. literalinclude:: src-06/views.py
      :linenos:
      :language: py

