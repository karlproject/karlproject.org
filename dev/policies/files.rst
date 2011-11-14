===============
Policies: Files
===============

UI policies for the Files tool in a community.

.. _show-file-policies:

Show File
================

- This screen applies to a File in a community folder, a File in an
  intranet office folder, a File as an attachment, and a File in a
  reference manual.

- When showing a file in a community, highlight the FILES tab and use
  the community layout.  When showing in an office, use the intranet
  layout.  When showing above an office, show the generic layout.

- A "Back to " link shows the title of the parent as a link, *except*
  in the case of a File acting as an attachment.  In that case, the
  backlink points to the grandparent (the Calendar Event or Blog Entry
  or Blog Comment containing an attachments folder).

- Show the title then the tagbox

- Provide an icon that shows the flavor of file type.  E.g. a Word
  icon for Word files.

- Provide a link to download the file.  If the file is an image, it
  can be displayed directly in the browser.

- Show the file size in a friendly (e.g. 1.5 MB) format, followed by
  the "type" of file.

- Members of the community, or KarlAdmin, see an action box with Edit
  and Delete


.. _show-folder-policies:

Show Folder
===========

- This screen applies to the top-level folder in the FILES tool, a
  subfolder in the FILES tool, and the top-level or subfolder in an
  office.

- When showing a Folder in a community, highlight the FILES tab and
  use the community layout.  When showing in an office, use the
  intranet layout.  When showing above an office, show the generic
  layout.

- The backlink shows the parent title as a hyperlink.

- Show the title then the tagbox.

- Members of the community, KarlAdmin, and any special groups managed
  in GSA (then sync'd using the gsa_sync script, which applies the
  security permissions to the folder) see an actions box.  This
  actions box contains: the addables (see next bullet), Edit, and
  Delete.  KarlAdmin sees Advanced.

- The "addables" is the list of content items that can be added in a
  particular context.  In a community, this is only "Folder" and
  "File".  In a generic office folder, this can be other installed
  content.  In a "Reference Manuals" folder (indicated by the Advanced
  screen), only a Reference Manual will be addable.  For Network News,
  only a News Item.  For Network Events, only an Event.

- If there are more than two kinds of things that can be added to a
  folder, we use a drop-down menu.

- The root folder of the FILES tool does not have an Edit or Delete
  action.

- The root folder of the FILES tool outside the intranet has an Feed
  icon.

- The contents of the folder are displayed using the
  :ref:`grid-table-policies` with the following policies:

  - Use Type, Title, and Last Modified columns

  - Type shows an icon with a hover title, icons matching a "flavor"
    as appropriate.

  - Title, ascending, is the default sort order.

  - Last Modified is shown as "04/17/2009" format.



.. _add-folder-policies:

Add Folder
==========

- When showing the screen in a community, highlight the FILES tab and
  use the community layout.  When showing in an office, use the
  intranet layout.  When showing above an office, show the generic
  layout.

- No actions box or backlink

- Title is "Add Folder"

- Fields are:

  - Title (required)

  - Tags

  - If outside an intranet, show an "Is Private" field

- The title is used to make an id, appending a number (e.g. ``-1``) to
  make it unique as needed.


.. _add-file-policies:

Add File
========

- When showing the screen in a community, highlight the FILES tab and
  use the community layout.  When showing in an office, use the
  intranet layout.  When showing above an office, show the generic
  layout.

- No actions box or backlink.

- Title is "Add File".

- Fields are:

  - Title (required)

  - Tags

  - File (required) for an upload file.

  - If outside an intranet, show a "Send email" field and an "Is
    Private" field

- The id for the item in the folder comes from the upload file, not
  the title.  Thus, the upload filename must be unique in the folder,
  else a validation error.

- Saving a file means:

  - Indexing the title and contents of the file for searching


.. _advanced-folder-policies:

Advanced Folder
===============

- Available to KarlAdmin

- No specification currently provided


.. _edit-folder-policies:

Edit Folder
===========

- Don't show "sendalert"


.. _edit-file-policies:

Edit File
=========

- Preserve the uploaded file

- Don't show "sendalert"



.. _download-file-policies:

Download File
=============

- A URL that downloads the contents of the file (or, for content that
  can be shown directly such as an image, shown in browser)


