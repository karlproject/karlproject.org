==================
Policies: Calendar
==================

The calendar tool provides a single calendar for a community.

.. _calendar-monthly-policies:

Calendar Monthly
================

- Members of the community see an "Add Event" action

- Page heading shows the date, e.g. "March 2009"

- Submenu with "Monthly View" and "Listing View" options.
  Currently-selected view is not a hyperlink.

- Links to the earlier and later months of the calendar

- Monthly layout

- Clicking on the calendar tool goes by default to the current month/year

- If viewing the current month/year, the current day has a light
  orange background color

- Show the days of the week at the top, starting with Sun (then Mon,
  Tues, Wed, Thurs, Fri, Sat)

- Days with events on that day have a hyperlink going to the listing
  view with that day as the jumplink

- For each day with events that are "on" that day:

  - Make a bulleted list showing up to 2 of the entries

  - Each item shows the first 20 characters of the title as a
    hyperlink, with the full title as the hover value (title
    attribute).

  - If over 20 characters, truncate with an ellipsis

- Only show events that the :term:`Requesting User` is allowed to see

- Multi-day events get listed on each day

- Show an syndication feed icon


.. _calendar-listing-policies:

Calendar Listing
================

- Members of the community see an "Add Event" action

- Submenu with "Monthly View" and "Listing View" options.
  Currently-selected view is not a hyperlink.

- Page title is Calendar Listing, with a centered heading of date
  (e.g. March 2009) under the submenu

- For each day of the month where there are events that the
  :term:`Requesting User` is allowed to see:

  - Make a jumplink for that day of the month

  - Show day of the week then day of the month, e.g. "Saturday, 7"

  - Provide a listing of all the events on that day, with a background
    color on the listing

  - Each is the title of the event as a hyperlink



.. _add-event-policies:

Add Event
=========

- Title is a required field

- Tags field

- "Event Starts" is a required field defaulting to today's
  year/month/day/hour, plus a minutes slot for each 15 min segment

- "Event Ends" is a required field defaulting to today's
  year/month/day/hour, plus a minutes slot for each 15 min segment

- Both have calendar popups

- "Event body text" richtext field which contributes to indexing

- Attendees list with a value per line.  Other than being mapped to a
  sequence, this has no particular meaning.

- Contact name field, free text, no constraints.

- Contact email field, free text, no constraints.

- Optional upload file field which contributes to indexing.

- :ref:`is-private-field-policies` 

- :ref:`send-alert-field-policies`

- Submit goes to view the new event with a status message indicating
  success

- Cancel goes back to the calendar monthly view


.. _view-event-policies:

View Event
==========

- Link that gets back to the calendar

- Page heading showing title of event

- All community members see actions for Edit and Delete

- Tagbox

- Event Starts and Event Ends dates

- Description, showing the "Event Body Text" if provided

- Attachments, if provided

- A link that says "Save to Outlook" that provides
  :ref:`download-event-policies`


.. _download-event-policies:

Download Event
==============

- Provides an ICS-compatible view that saves into Outlook and other
  systems


.. _edit-event-policies:

Edit Event
==========

- No special rules here


.. _delete-event-policies:

Delete Event
============

- Deletion is the same as all :ref:`delete-resource-policies`.


.. _atom-calendar-policies:

Atom Calendar
=============

- Provide the 20 most recent calendar events following the general
  :ref:`atom-feed-policies`.

