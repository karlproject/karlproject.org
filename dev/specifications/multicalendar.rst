=======================
Enhanced Multi-Calendar
=======================

Summary
=======

Important OSI users have provided a well-thought explanation of
desired enhancements for calendaring.  This proposal gives a phased
approach to incrementally deliver more valuable calendaring.

Goals
=========

- Partition a community calendar into multiple "named" and "dynamic"
  calendars.

- Allow sharing calendar events between community calendars.

- Improve the general usability of KARL calendaring, including email.

Screenshots
===========

- The :download:`Week View <files/weekly_01.png>` screenshot.  This
  will be the new default view for a calendar.

- The :download:`Day View <files/daily_01.png>` screenshot.

- The :download:`Month View <files/monthly_01.png>` screenshot.

Overview
===========

In this proposal, the first enhancements are aimed at low-hanging
fruit that can be easily delivered, while still giving value.

For instance, the "monthly view" of a calendar has proven less value.
It doesn't provide enough space to see the title or time of an event.
As such, we propose borrowing the view scheme from other calendar
programs such as Google Calendar and Apple's iCal:
Day/Week/Month/Listing views, with Week as the default.

This "weekly view" shows 7 days of information, with rows for each
hour of the day.  The rows are flexible and can wrap, so event
listings can show more of the title.  Also, a gesture will allow
adding an event on that day at that time by clicking in the correct
spot to launch Add Event from that date/time.

In this first round of improvements, we also look at improving the
email alert and sending out reminder emails.  For the first, we extend
the already-completed work on putting more information into the alert
by also attaching a .ics file for loading directly into Outlook etc.
For the latter, we extend the add/edit event forms to allow having a
reminder email sent out some period of time in advance.

The second phase of work is more substantial, focused on the sharing
calendar information between communities.

First, we'll allow multiple "virtual" calendars in a community by
supporting "named calendars".  The concept here matches other systems:
calendar events are assigned to a particular calendar.  In our case we
aren't making "physically" separate calendars in different
folders/containers.  Instead, the moderators define a list of named
calendars, and calendar events are assigned to one of these named
calendars on their add/edit form.

With that, we can then allow segregation of the entire community
calendar into groups of semantically-related events.  (We could use
tags for this, but it isn't clear that the average user will get
events into a pre-defined naming scheme based on tags.)

The next step is to allow "dynamic" calendar groupings.  These allow
the moderators to define groups of events that come from other
communities, using the named calendars defined in the other community.
Later, moderators can filter the grouping beyond name, and base on
criteria (such as tag), for events coming from multiple communities
(including the current one.)

With this, the calendar view will color/symbol code events that appear
in each of the named/dynamic calendars.  The calendar view will
default to showing all events in all named/dynamic calendars, but will
allow users to filter down further and only show certain calendars.

Only calendar events that the currently-requesting user are allowed to
see will be shown.

Jargon
==========

- *Named Calendar*.  Allows events in a community to be assigned, very
   simply, to a moderator-managed list of calendar names.

- *Dynamic Calendar*. Richer set of facilities that allow moderators
   to provide query-driven groupings of events in one or more
   communities, including the local community.

Calendar View
=============

- [1] Get Mike/Derek to suggest ideas on sprucing up the calendar,
  visually.

- [1] Provide day/week/month/listing.

- [1] Day listing and week listing organized by hour, similar to iCal.

- [1] The different views are selectable either from the current
  concept of "submenus" (links under the title) or a push-button
  control similar to iCal, which acts as a radio button with a
  depressed button as the current selection.

- XXX Move the push-buttons to a "filterbar" in a separate spec.

- [1] Each view selection is part of the URL, allowing bookmarks.

- [1] Remove wasted space from <li> bullet, replace with background
  images

- [1] Day and week view allow adding an event that starts on that date
  at that hour.  Month view allows adding an event on that day.  Both
  have some gesture (double-click, a (+) icon, etc.) that triggers the
  event adding.

- [2] A picker above the calendar chooses which calendar should be
  viewed.  This choice changes the URL, to allow bookmarking and RSS
  subscription. This picker also acts as a legend.

- [2] If no named calendars are defined (beyond "Default"), then
  nothing new is shown in the UI.  Behaves the same as now.

- [2] Clicking on an event in another community takes you to that
  other community.

- [2] A named calendar only shows events you are allowed to see
  (security-wise).

- [3] Atom icon provides subscription to current calendar choice

- [2] Colors and symbols/backgrounds to differentiate different
  calendars' events

- [3] A (i) on an event listing in one of the views to see more info,
  perhaps on a day, perhaps on an event.

- [4] Drag-and-drop in day/week/month view to re-schedule.

- [4] Recurring events.

- [3] Change the community's Calendar page to have 3 submenus (under
  the page heading):

  - Active (default, specified elsewhere)

  - All (current view)

  - [4] Global Calendar

Calendar Setup
==============

- [2] Moderators see an action "Setup"

- [2] Named Calendars

  - Editing the list of named calendars can be done by autobox2
    bubbles or some other UI for adding/deleting items in a list.

  - List contains "Default", which isn't deletable.

  - Named Calendars have no state other than their name.

  - Deleting a named calendar finds all events placed in that calendar
    and changes them to be in the Default calendar.

- [3] Dynamic Calendars

  - A calendar that can be browsed in View Calendar, whose events come
    from a query.

  - View list of dynamic calendars, add a dynamic calendar, edit, and
    delete.

  - Each dynamic calendar is a query with one or more criteria, OR'd
    together

  - Each criteria is a "source" (one or more community named
    calendars, including current) and optional filter-by-tags, e.g.::

      Africa Project - Default	  tag1, tag2, tag3
      Africa Project - Holidays	  tag1, tag2, tag4, tag5


Add/EditView Calendar Event
===========================

- [1] Allow assigning an alarm to send an email X hours before the
  event start time.

- [2] Allow assignment of named calendar, from the list of named
  calendars.

- [2] Default choice is "Default" calendar.

- [2] Provide visual cue regarding which named calendar this is when
  viewing calendar event.  Show color/background scheme and calendar
  name.


View Global Calendar
====================

- [4] Global Calendar shows all events, anywhere in KARL (communities,
  intranets) that you are allowed to see.  Like ``all_forums.html``
  this is a view on the container above the communities
  (``/communities/``) which recurses.

- [4] Global Calendar does *not* have calendar picker to choose
  named/dynamic calendars, legend, etc.

- [4] Global Calendar has some of the other enhancements
  (day/week/month/listing, info dialog)


Other
========

- [1] Attach .ics to email (and add extra event info inside email)

- [1] Add Alarm capability on events to allow sending a reminder

- [3] Email-enable the calendar tool, allowing one or more .ics or
  inline-text to be submitted

  - If one event (either inline or .ics), other files are attachments

Questions
===========

- Take a look at Google Calendar to get more info.

- Email Jonathan/Chipp for things that would help them switch

- Review the points on here to see which are feature or UI bloat

- What other info should we be packing into the .ics file?

- If a named calendar is deleted, and another community has a dynamic
  calendar pointing at it, do we cleanup or give up?

- Can we fix the KARL 2 column layout (community layout) to be more
  fluid and give more space to the body?  Otherwise, the 7-day layout
  will have similar space-constrained problems as it currently does.
