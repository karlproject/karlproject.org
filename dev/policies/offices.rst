=================
Policies: Offices
=================

Policies related to the office home page and other screens related to
offices.

.. _show-office-policies:

Show Office
===========

This screen is the intranet home page for an office within an
organization.



.. _show-networknews-policies:

Show Network News
=================

- There is a screencast available for this at
  http://carlos.agendaless.com/screencasts.

- You reach this screen from a portlet in the middle column of an
  intranet home page, e.g. '/offices/nyc/'.  The portlet has a link
  say "MORE NETWORK NEWS" that leads to this screen.

- This is a folder at the ``/offices/files/network-news`` location.
  It is a regular Folder, except:

  - A KarlAdmin visited ``/offices/files`` and clicked ``Add Folder``

  - They then made ``network-news``, but when viewing it,
    ``Advanced`` appeared in the actions menu (only for admins)

  - There they chose the Network News "marker" for that folder

  - This is all done by default now for the ``src/osi/osi/run.py``
    loading script

- Note that ``start_over --yes`` creates this folder by default.  It
  is a regulary Folder but with a marker that affects the view used,
  what actions are available, etc.

- Shown in the intranet layout

- Only KarlStaff can visit this screen

- Members of a certain group will get permissions assigned (as part of
  the sync script) that allows editing, which will give them the "Add
  News Item" action (the admin user gets that also).

- There is an "Advanced" action that appears for KarlAdmin users.

- The backlink takes them to the same URL that "HOME" takes them to,
  meaning, their home office.

- The pageheading and title say "Network News".

- Two columns in grid (Title and Date).  The date used in the Date
  column is the publication date, formatted like "March 19, 2009".
  The values for Title are hyperlinks to show the item.

- If there are no items, show "No Items" without any headings.

- Entries are shown sorted by publication date with a pagination box
  at the top and bottom.  Although KARL2 did column sorting, we're
  going to punt on that and approach OSI with a comprehensive approach
  to grids (via Balazs).


.. _add-newsitem-policies:

Add News Item
=============

- This form has the following fields:

  - Title (required)

  - Tags

  - Text

  - Image.  File upload file with a helptext of "Will be shown in the
    news listing, and in the news item itself."  (We don't do
    server-side scaling of images.)

  - Image Caption.  UnicodeString.  Fail validation if it doesn't
    appear to be an image (this is a nice-to-have, not a must-have.)

  - Attachments.  In KARL2 this was just one Upload File.  Let's
    follow the path of Calendar Events and allow multiple attachments.

  - Publication Date. Use a date picker a la Calendar Event.  When
    first visiting the add form, initialize to "now".

- Both of the fields have the same validator and formfield snippet as
  Title and Text used elsewhere.  Also, use the "make_unique_name"
  helper to generate a "-1" duplicate transparently, as in most other
  content add forms.

- Indexing

  - Use the TitleAndFile adapter to make the contents searchable,
    including the attached files.  (Note: it's possible that Calendar
    Events doesn't index attachments.  Just do whatever it does.)

  - Show the results under "Other" in LiveSearch


.. _show-newsitem-policies:

Show News Item
==============

- This is the default view of a News Item

- Use the intranet layout.  (Communities don't get News Items
  currently, so this can be the default layout.)

- A backlink has "Back to Network News"

- Members of a certain editorial group see actions of "Edit" and
  "Delete" (as well as KarlAdmin.)

- Above the title of the News Item, we show the Publication Date
  formatted as "Wednesday, Mar 25, 2009".  (Hopefully our IKarlDates
  adapter has this as a "flavor".

- We right-float the image that was uploaded (using the
  ``newsitemImage`` CSS class.)  Under that, we have the caption, if
  present.

- Then the tagbox, then the attachments (using the snippet for
  displaying attachments.)

- Finally the text.


.. _edit-newsitem-policies:

Edit News Item
==============

- Same as :ref:`add-newsitem-policies` except:

  - Use the widget that preserves the uploaded file field as used in
    Edit File

  - Put in a status message on the URL when redirecting to the view,
    to say "Your News Item has been saved."


.. _show-networknews-portlet-policies:

Show Network News Portlet
=========================

- This is a portlet that appears in the middle column for all office
  home pages.

- It has a heading "Network News", then up to five of the upcoming
  news items, starting from today and using publication date as the
  search criteria.

- There is a hyperlink at the bottom of the portlet that says "MORE
  <PORTLET TITLE>" which goes to :ref:`show-networknews-policies`.

- These portlets are currently implemented using adapters.  See
  ``src.osi.osi.views.retail._get_portlet_html``.  To follow this
  pattern, make an adapter for the INetworkNewsMarker interface.
 

.. _show-networkevents-policies:

Show Network Events
===================

- There is a screencast available for this at
  http://carlos.agendaless.com/screencasts.

- You reach this screen from a portlet in the middle column of an
  intranet home page, e.g. '/offices/nyc/'.  The portlet has a link
  say "MORE NETWORK EVENTS" that leads to this screen.

- This is a folder at the ``/offices/files/network-events`` location.
  It is a regular Folder, except:

  - A KarlAdmin visited ``/offices/files`` and clicked ``Add Folder``

  - They then made ``network-events``, but when viewing it,
    ``Advanced`` appeared in the actions menu (only for admins)

  - There they chose the Network Events "marker" for that folder

  - This is all done by default now for the ``src/osi/osi/run.py``
    loading script

- Note that ``start_over --yes`` creates this folder by default.  It
  is a regulary Folder but with a marker that affects the view used,
  what actions are available, etc.

- Shown in the intranet layout

- Only KarlStaff can visit this screen

- Members of a certain group will get permissions assigned (as part of
  the sync script) that allows editing, which will give them the "Add
  Event" action (the admin user gets that also).

- There is an "Advanced" action that appears for KarlAdmin users.

- The backlink takes them to the same URL that "HOME" takes them to,
  meaning, their home office.

- The pageheading and title say "Network Events".

- We show two columns: Title and Date, where "Date" is the start date
  of the event to the end date, using a short form such as "March
  27-29, 2009".  In KARL2, those two columns claimed to be sortable,
  but they actually weren't.  Thus, for 3.0 we can skip the sorting.

- The values for Title are hyperlinks to show the item.

- By default the listing shows events sorted in chronological order,
  starting at "today", and going forward in time.  We use a pagination
  box at the top and bottom.  We can use the same pagination box used
  in forum topics.

- If there are no items, show "No Items" without any headings.

- There is a link "Show Past Events" that toggles the direction of the
  listings.  Clicking this link takes you to today, but sorted
  backwards in time.  (That link then changes to say "Show Upcoming
  Events".)

- Above the grid we have a filterbar defined by
  :ref:`filterbar-policies`.

- The add/show/edit calendar event is the same as in
  :ref:`add-event-policies` except:

  - Displayed in the intranet layout

  - Sendalert and is private are not visible

  - The backlink is "Back to Network Events"


.. _show-networkevents-portlet-policies:

Show Network Events Portlet
===========================

- This is a portlet that appears in the middle column for all office
  home pages.

- It has a heading "Network Events", then up to five of the upcoming
  events, starting from today and using publication date as the search
  criteria.

- There is a hyperlink at the bottom of the portlet that says "MORE
  <PORTLET TITLE>" which goes to :ref:`show-networkevents-policies`.

- These portlets are currently implemented using adapters.  See
  ``src.osi.osi.views.retail._get_portlet_html``.  To follow this
  pattern, make an adapter for the INetworkEventsMarker interface.



.. _filterbar-policies:

Filterbar
=========

- There is a "filterbar" that affects the current listings, whether in
  Past or Upcoming mode.  You can supply a searchterm (which uses the
  'texts' index), a Year, and a Month.

- Year is a single-select dropdown showing all the years from 2007 to
  the current year.  There is also a choice of "All" which is the
  default.

- Month is a dropdown showing all the months in a year.  There is also
  a choice of "All" which is the default.

- If someone choose a Month but not a Year, implicitly add the current
  year to the filter.

- Choices made in the "filterbar" are preserved on the next results
  screen, so people can see what filter they have applied (done via
  QUERY_STRING preservation.)  This also holds true when going
  backwards and forwards through batches.

