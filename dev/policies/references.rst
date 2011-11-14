====================
Policies: References
====================

The reference manual functionality in KARL2 is moving to a generic
"tool" that can go on any community.  


.. _list-referencemanuals-policies:

List Reference Manuals
======================

- Since reference manuals span offices, they will be in the
  /offices/files/referencemanuals area using the generic layout, so
  they won't look like they are in a particular office.

- Only KarlStaff and KarlAdmin can see this, affiliates can't.

- KarlAdmin and people in a particular group see actions of "Add
  Reference Manual", "Edit", "Delete", and "Advanced"

- Show a backling of "Back to <office name>" with a hyperlink to their
  home url.

- Title is "Reference Manuals" with a tagbox underneath

- The :ref:`grid-table-policies` has columns: Type, Title, and Last
  Modified.



.. _add-referencemanual-policies:

Add Reference Manual
====================

- KarlAdmin and people in a particular group can get here, others see
  "Forbidden"

- Shown in generic layout.

- Form fields: title (required), tags, description

- Cancel goes back to reference manuals folder

- Submit adds a reference manual, makes a duplicate identifier if one
  exists at that name.


.. _show-referencemanual-policies:

Show Reference Manual
=====================

- Only KarlStaff and KarlAdmin can see this URL.

- Uses GenericLayout.

- KarlAdmin and people in a particular group see actions of "Add
  Section", "Edit", and "Delete"

- Backlink goes back to the reference manuals folder

- Show title and tagbox, then description.

- Provide a rightfloat link to :ref:`print-referencemanual-policies`.

- Listing of contents

  - Reference manual content is organized in an outline.  Sections are
    numbered 1-2-3 etc., then items in each section are a-b-c.

  - Provide lines as separators.

  - On the right, allow re-ordering of content using up and down
    arrows.  Something on the bottom is moved to the top and vice
    versa.

  - After every click of these move up/down pickers, the page
    refreshes and a status message says what was changed.


.. _print-referencemanual-policies:

Print Reference Manual
======================

- Only KarlStaff and KarlAdmin can see this URL.

- Uses GenericLayout.

- No actions are displayed.

- Backlink goes back to the reference manuals folder

- Show title and tagbox, then description.

- Provide a rightfloat link to :ref:`show-referencemanual-policies`.

- Another indented, numbered listing of content.  In this case, show
  the HTML body on pages and the descripton on sections.

.. _edit-referencemanual-policies:

Edit Reference Manual
=====================

- Same as :ref:`add-referencemanual-policies`


.. _add-referencesection-policies:

Add Section
===========

- KarlAdmin and people in a particular group can get here, others see
  "Forbidden"

- Shown in generic layout.

- Form fields: title (required), tags, description

- Cancel goes back to reference manual

- Submit adds a reference section, makes a duplicate identifier if one
  exists at that name.

- Content is always added to the end of the ordering.


.. _view-referencesection-policies:

View Section
============

- Only KarlStaff and KarlAdmin can see this URL.

- Uses GenericLayout.

- KarlAdmin and people in a particular group see actions of "Add
  File", "Add Page", "Edit", and "Delete"

- Backlink goes back to the reference manuals folder

- Show title and tagbox, then description.

- List section contents

  - Use ``a.`` and ``b.`` etc. for numbering

  - Each item has the title as a hyperlink to the file or page

- At the bottom, provide the title as a hyperlink of the "previous"
  and "next" items in the ordering for that section.  If on the first
  section, only show the next section if there is one.  If on the
  last, only show the previous.



.. _edit-referencesection-policies:

Edit Section
============

- Same as :ref:`add-referencesection-policies`


.. _delete-referencesection-policies:

Delete Section
==============



.. _add-referencepage-policies:

Add Page
========

- KarlAdmin and people in a particular group can get here, others see
  "Forbidden"

- Shown in generic layout.

- Form fields: title (required), tags, text, attachments

- Cancel goes back to reference section

- Submit adds a page, makes a duplicate identifier if one exists at
  that name.

- Content is always added to the end of the ordering.



.. _view-referencepage-policies:

View Page
=========

- Only KarlStaff and KarlAdmin can see this URL.

- Uses GenericLayout.

- KarlAdmin and people in a particular group see actions of "Edit",
  and "Delete"

- Backlink goes back to the reference section.

- Show title and tagbox, then description, then the attachments using
  the normal attachments display.

- Also show the pagination at the bottom to move to previous/next as
  discussed above.


.. _edit-referencepage-policies:

Edit Page
=========

- Same as :ref:`add-referencepage-policies`


