================
Policies: Forums
================

Forums provide messageboard functionality for offices.  Many aspects
of a forum are very similar to blogs.

As an "office" tool, Forums have a duality: the UI used for
:term:`KarlAdministrator` functions and the UI used for
:term:`KarlStaff`.  The former is the :ref:`community-layout-policies`
and the latter is :ref:`office-layout-policies`.

A Forum could be used in a regular, non-office community.  In this
case, it would have the wrapper of the community-oriented layout.

.. _admin-list-forums-policies:

Admin List Forums
=================

- Viewed via the :ref:`community-layout-policies` which provides the
  content-administration interface for office content.

- Go to a community (``/osi``, ``/osi/budapest``, ``/africa-project``)
  and click the ``FORUMS`` tab.

- The actions box shows "Add Forum" as the only action

- The "grid" is a tabular listing of all forums


.. _list-forums-policies:

List Forums
===========

- Viewed through the :ref:`office-layout-policies`, not the
  :ref:`community-layout-policies`.

- Only viewable by :term:`KarlStaff`

- Shows listings of forums grouped by some criteria.  Primarily, the
  criteria is "by office".

- Forums that are unique to an office are contained directly within
  the Forums tool for that office/community,
  e.g. /osi/budapest/forums/some-forum.  Forums general to all OSI are
  stored in /osi/forums/another-forum.

- When each form goes "up" to the parents listing of all forums, they
  are going "up" to /osi/forums.  This view flattens the hierarchy and
  shows all forums, directly inside the OSI office/community or within
  a particular office/community, in the appropriate grouping.

- Each grouping shows a header with the label for the grouping, then a
  table showing all forums in that grouping.

- Sort order for forums in a group is reverse chronological order on
  creation date (in KARL2, there is no visible sort order, as create
  date isn't a visible column.)

- The columns are: Forum (as a link to the forum), a count of all
  topics, a count of all comments, and the Last Activity.  The Last
  Activity is a link to the last active topic/comment, plus the name
  of the poster, and the "posted" (created) date for that item.

- There is no security filtering in this (or any) listing in Forums.
  Meaning, everybody that is allowed to see this screen, sees the same
  items and counts.  (There is no Is Private anywhere in Forums.)


.. _add-forum-policies:

Add Forum
=========

- This view can only be reached by a :term:`KarlAdministrator`.

- This action is performed via the :ref:`community-layout-policies`
  which provides the content-administration interface for office
  content.

- To add a forum, first go to the appropriate Forums tool.  If you
  want a forum's "context" to be for all offices, go to the Forums
  tool on the ``/osi`` community.  If you want the forum to be tied to
  an office, go to the Forums tool on that office.

- Click "Add Forum"

- Fields

  - Title (required)

  - Description (optional)

- Both fields contribute to the search content

- A Forum shows up in the "Posts" grouping for livesearch

- Adding a Forum with a Title that is the same as a previous title
  simply appends a unique suffix such as ``-1`` to the URL.  Both show
  up with the same title.

- There is no "is private" or "sendalert" or other such concept in
  forums (or other "office" content)

- When the forum is saved, redirect to the view for the new forum and
  put a status message on the URL saying it was saved.


.. _edit-forum-policies:

Edit Forum
==========

- This view can only be reached by a :term:`KarlAdministrator`.

- This action is performed via the :ref:`community-layout-policies`
  which provides the content-administration interface for office
  content.

- Remainder matches :ref:`add-forum-policies`

- This view can only be reached by a :term:`KarlAdministrator`.

.. _delete-forum-policies:

Delete Forum
============

- Deletion is the same as on all :ref:`delete-resource-policies`.


.. _show-forum-policies:

Show Forum
==========

- Viewed through the :ref:`office-layout-policies`, not the
  :ref:`community-layout-policies`.

- Provide a link that gets back to the :ref:`list-forums-policies`
  screen

- All :term:`KarlStaff` can see this view and sees an action saying
  "Add Forum Topic"

- Show the title of the forum in the page heading area

- A paginated listing with pagination boxes at the top and bottom

- 20 items per page, no security filtering

- 4 columns

  - Topic shows the title of the topic as a hyperlink to the show the
    topic

  - Posted By shows the name of the creator

  - Date shows a longform version of the creation date

  - Comments shows the count of comments to the topic


.. _show-topic-policies:

Show Topic
==========

- Viewed through the :ref:`office-layout-policies`, not the
  :ref:`community-layout-policies`.

- The creator of the topic sees actions of "Edit" and "Delete"

- Show a link to get back to the forum

- Show the title of the topic, followed by the tagbox

- Show a link that says "Reply", which is a jumplink down the page to
  the "Comments" area

- The original text of the topic is displayed in a colored background
  with a "byline" showing who posted it and the "posted" (created)
  date in longform

- Each reply is then shown, same format but:

  - Without background color

  - A right-floated "action" that says "Quote".  Quoting a reply
    shoves the content into the editor, same as on blogs.

  - The creator of the reply also sees links of "Edit" and "Delete"

- At the bottom, a Comments box with a richtext editor

  - The submit button posts to the topic with a status message saying
    "Your reply has been added"

  - The cancel button returns to the topic and discards the typing,
    with a status message saying "Your new reply has been
    cancelled."


.. _edit-reply-policies:

Edit Reply
==========

- Viewed through the :ref:`office-layout-policies`, not the
  :ref:`community-layout-policies`.

- Only the creator of the reply can get to this view.

- A richtext box to edit the content with a submit and cancel button.

- Submit saves and returns to viewing the reply, plus a status
  message.

- Cancel returns to viewing the reply.


.. _delete-reply-policies:

Delete Reply
============

- Viewed through the :ref:`office-layout-policies`, not the
  :ref:`community-layout-policies`.

- Deletion is the same as on all :ref:`delete-resource-policies`.

