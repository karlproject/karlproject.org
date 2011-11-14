================
Wiki Safety Belt
================

Oxfam users have reported pain regarding collaborative authoring on
wiki pages.  They are have examples of people losing their edits (in
obviously a mysterious way), with people resorting to weird
worarounds.

This proposal comes from Duncan Booth for a very near-term fix.

Proposal
========

Put a "safety belt" in the page that notices, upon save, that the wiki
page was edited by someone else since the start of your editing.

Out of Scope
============

The key to this proposal is to do something immediate that doesn't
require heavy analysis and funding.  As an example, something that
could be done in less than 4 hours.  Thus the following are not in
scope:

- Any other content except a wiki page

- Locking

- Versioning

- History

- Diff

Details
=======

- When an author clicks "Edit" on a wiki page and gets back the form
  for editing, include a hidden field that contains the modification
  date/time of the previous edit.

- When the author saves their changes, compare that date-time to the
  modification date-time just before saving.

- If the wiki pages has a more recent modification date-time, trigger
  a form error.

- Return the editing form, with:

  - A form error saying the page has been modified since you started
    editing.  Provide the first and last name of the person that did
    the editing.

  - Include any unsaved changes to any of the fields, particularly the
    text field.

  - Show a widget that asks if they want to overwrite the previous
    person's edits.

  - An updated hidden field with the date-time of the more recent
    edit.

- Clicking save then submits and overwrites that person's edits,
  *unless* it had been modified *again* while the form error was being
  processed.  If so, repeat error process.

Alternatives
============

We could choose to invest a bit more money and throw some AJAX at
this, to improve the user experience.

For example, clicking the "save" button could issue an AJAX request
checking to see if it had changed, then popping up a dialog showing
the name of the more-recent modifier.  This would be inconsistent with
other form-saving error displays, so probably not worth it.

We could let the person know sooner by pinging the server every 15
seconds and showing a message.  This is notably more complex and
increases the load on the server.
