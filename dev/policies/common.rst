================
Policies: Common
================

The KARL UI contains a number of snippets and patterns that appear in
different places on multiple screens. This document describes each of
these.

.. _delete-resource-policies:

Delete Resource
===============

In most cases, deleting a resource is the same for all kinds of
resources.

- The ``Delete`` action goes to a confirmation screen with OK and a
  Cancel buttons

- Cancel takes you back to the parent

- OK leads to deleting the resource, which then redirects you to the
  parent with a status message saying the deletion took place.


.. _screen-title-policies:

Screen Title
============

- Show the appropriate screen title, in the same place of the screen, in
  same font

- Display a "private" badge if needed.

- Don't show the private badge on a resource in a private community


.. _is-private-field-policies:

Is Private Field
================

- Appears when adding a community, adding or editing a resource in a
  public community

- Should not appear when adding/editing a resource in a private
  community

- A modified version appears when making a community private, different
  label

- Making something private triggers a JavaScript confirmation

- You can't make a private community public.

.. _send-alert-field-policies:

Send Alert Field
================

- A boolean Yes/No field asking the question "Send email alert to
  community members?"

- Default is Yes

- Editing an existing resource sets the choice to the existing
  selection

- Choosing "Yes" sends an email alert under the conditions of the
  alert policy, where community members can turn alerts on/off or
  choose daily alerts.


.. _status-box-policies:

Status Box
==========

- If there is a portal status message, or warning, display above the
  screen title


.. _atom-feed-policies:

Atom Feed
=========

- Show the 20 most recent entries as an valid Atom feed

- Only show results that the person is allowed to see, security-wise

- Support IE and Firefox using cookie authentication, as well as other
  blog tools that support basic authentication.

- Set the correct MIME type on the response and omit any DTD

- The ``<content>`` element is filled simply by the body of blog entry
  or comment, modification date, and author info.

.. _sending-alert-policies:

Sending Alerts
==============

- An email is sent out when the creator of a resource indicates on the
  form that an alert should be sent, or when a blog entry or blog
  comment are created via email

- An alert goes to everyone in the community that has alerts enabled
  for that community.

- Alerts can also go out by "digest" for a community.  In that case,
  once a day an email is sent with a listing of all "alertable"
  changes in the community.

- Emails go both to the creator of the resource and people in the
  community

- In non-blog cases, the "from" address is a system-level no-reply
  kind of email address, combined with a friendly label.  For example:
  ``Person Name | System Name <alert@systemdomain>``

- The "to" address is a human-friendly combination of the person's
  full name and their email address.  For example: ``Some Person
  <some.person@place.com>``

  .. note::

    In KARL2 we sent all the email alerts at once using a long BCC
    line and a To address that was bogus.  Let's go back to something
    people will understand, namely, that the email should come to
    them.

- The "subject" is the name of the community in brackets combined with
  the title.  For example: ``[Some Community] Some new item's title``

- No file attachments on emails (other than blog entry and blog
  comment).

- The HTML body (there is no text version) contains:

  - A line with: "A new [Content Type] was created by Person Name in
    the Community Title community", where [Content Type] is a
    hyperlink to the resource.

  - A line of dashes.

  - An ``<h2>`` with the title of the resource

  - A hyperlink with the full URL

  - A short line of dashes.

  - A prominent message saying "do not reply to this mail"

  - A footer with::

     REPLIES TO THIS MESSAGE WILL BE SENT TO THE COMMUNITY
     To view this community, visit: https://communityurl
     To stop these alerts, visit: https://manage-my-community-url

.. _community-tags-portlet-policies:

Community Tags Portlet
======================

This portlet box appears on most of the screens in a community. It
shows:

- The top five (or fewer, if there aren't five) tags in a community

- For each item, show:

  - The tag count for its use in that community

  - The tag, as a hyperlink to the communitytag_view screen


.. _blog-archive-portlet-policies:

Blog Archive Portlet
====================

This portlet box appears in the blog tool for a community, below the tag
portlet. It shows:

- The five most recent months that have at least one blog entry that the
  :term:`Requesting User` is allowed to see

- For each line, show:

  - MMMM YYYY (count)

  - The MMMM YYYY is the full month name and full year as a hyperlink to
    that batch of blog entries

  - The count is the number of items in that month that the
    :term:`Requesting User` is allowed to see


.. _calendar-widget-policies:

Calendar Widget
===============

Used primarily on the add/edit calendar event screen.

- Popup calendar should show the currently-set date/time for edit event,
  and "now" for new events

- Changing the start date should change the end date by XXX ?

- The format of the date should be XXX?


.. _letter-box-policies:

Letter Box
==========

- Provide a way to filter the current list by first letter.

- (New in KARL3) Only show hyperlinks on letters when there is at
  least one item starting with that letter.  (Note: security filtering
  doesn't apply, so you might click on a letter and see no results
  because you aren't allowed to see them.)

- Once clicked, the current letter gets bolded, without a hyperlink,
  while all the other letters remain hyperlinks

.. _pagination-box-policies:

Pagination Box
==============

- Show results in batches

- Display the current starting and ending points, as well as the total
  count


.. _active-people-portlet-policies:

Active People Portlet
=====================

This box appears in the most of the screens in a community in the right
column.

- List the five (or fewer) most recent changes in a community that the
  :term:`Requesting User` is allowed to see

- Don't show an item that is private to a non-member of the community

- For each item, show:

  - The author's name, but not as a profile link

  - The content type, as a hyperlink to the resource

  - The modification date, in MM/DD/YYYY format

.. _description-extraction-policies:

Description Extraction
======================

Several content types (blog entries and comments, wiki pages) need a
"description" value to display a summary in a listing such as search
results, but the add/edit forms don't have a field for it.  (We didn't
want to force authors to fill in yet-another field.)

Instead, we extract a summary for the description field, using the
HTML in the text field.  The policy:

- Take the string of HTML and parse it with lxml.html.  If it fails,
  return None.

- Grab all the text nodes with //text()

- Skip empty strings in the list.

- For each string, split on blank spaces and toss out any empty
  strings.

- Return the first 50 words.  If over 50 words, add an ellipsis.

- Store that on the instance, so we don't recompute it 20 times when
  showing a blog or search results (since we aren't showing contextual
  highlighting on search results.)

.. _email-text-scrubbing-policies:

Email Text Scrubbing
====================

Content can be created via incoming email.  A blog entry can be
created by email, and you can reply to a blog entry/comment email
alert to create a new comment.  In both cases, the text needs to be
"scrubbed" according to some policies:

Both Cases
----------

The following apply to either a new blog entry created by mail or a
blog commment created as a reply to another mail:

- We presume the mail message has both a ``text/html`` and a
  ``text/plain`` multiparts

- We toss out the HTML version and use the plaintext version

- Use `Markdown <http://code.google.com/p/python-markdown2/>`_ to
  convert to HTML

Email Replies
-------------

We don't want the blog comment display to be polluted with long,
indented repititions of text.  Thus, we want to chop out the quoted
part, knowing it has some downsides (e.g. inline comments are lost):

- The previous points

- Everything on or after the ``--- Reply ABOVE THIS LINE to post a
  comment`` line is tossed out



.. _grid-table-policies:

Grid Table
==========

The GridTable is an Ajax widget for high-speed browsing of resources
in a container.

- Show a certain number of items (default is 10) at a time.

- In bottom left, show which start-stop batch you are currently on,
  along with the total (estimated) number.

- Provide pagination buttons, to go forwards/backwards as well as
  directly to a neighboring batch.

- The grid has a number of columns.  Some columns are sortable, some
  aren't.  One column is the default sort.

- You change the column sorting by clicking on a different column.
  Clicking again on the same column reverses the ordering of the
  search.  A visual indicator shows current sort column and current
  sort direction.

- As you paginate through batches, the column sorting is preserved.

- Pagination happens without complete page reloads. The first batch
  doesn't require a separate server request.

- Contents are filtered based on security.
