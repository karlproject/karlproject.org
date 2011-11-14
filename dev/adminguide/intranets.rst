====================
Organizing Intranets
====================

The intranets (aka "offices") area of KARL structures content along
organizational lines.  Each intranet/office contains its content,
while some content spans the organization.

This document shows the configuration options related to intranets:

- Managing intranets

- Adding an intranet

- Changing the global "feature"

- Managing information in the cross-intranet "files" section, such as
  network news and events.

- Editing information in an intranet

- Adding a new forum in a particular intranet

- How to delete an intranet

Also, an :download:`audio/video "screencast" is available
<screencast2.mov>` that demonstrates many of these administrative
actions.  The screencast is in QuickTime format.

Managing Intranets
==================

All of the tasks in this document start by getting to the screen for
managing intranets.  This screen isn't linked to from any existing
screen.  To reach this, visit the ``/offices/`` URL for your KARL
site.

This presents a UI that looks similar to a community.  This is for
good reason: ``/offices/`` *is* a community.  Furthermore, each
intranet it holds, such as ``/offices/atlanta``, is a community.  This
means that, in addition to the intranet-oriented UI for intranet
content, there is an additional way to navigate the intranets using
the community UI.  Administrators use the latter to configure
intranets.

#. Log in as a user in the ``KarlAdmin`` group.

#. Visit the ``/offices/`` URL.

#. Note there are tabs for ``Files`` (content that spans
   intranets/offices), ``Forums`` (in case there are forums that span
   intranets/offices) and ``Intranets``.

#. Click on ``Intranets`` to see the listing of all existing
   intranets.

Add an Intranet
===============

Adding an intranet is straightforward:

#. Visit ``Intranets`` as described above.

#. Click ``Add Intranet``.

#. Provide information about the intranet:

  - The ``Title`` serves as the basis for the identifier in the URL.
    Thus, if you want a short ID and longer title, enter the short ID
    as the title, then edit the title later.

  - The address, city, state, country, zip code, and telephone are
    only for display in the footer when navigating the intranets.
    They have no other structural or semantic purpose.

  - The ``Navigation Menu`` is the HTML used in the left-hand column
    for that intranet.  The pull-right submenus use a particular HTML
    structure.

  - The ``Middle Portlets`` and ``Right Portlets`` control which
    portlets appear in which order for that intranet.  Provide the
    path to the container that you would like to appear as a portlet
    (e.g. ``/offices/files/network-events``).  Only certain kinds of
    containers can be used as portlets.

Changing the Global Feature
===========================

The intranet layout uses three columns for the home page of an
intranet: navigation in left column, cross-organizational portlets in
the middle column, and office-specific portlets in the right column.

The top of the middle column shows the "feature", which is a highlight
used for all intranet home pages.  This feature is nothing more than
HTML that is stored on the ``/offices/`` community's edit screen.  In
general, the HTML includes images stored in ``/offices/files/``, which
is the place for content that spans each intranet/office.

#. Visit ``Intranets`` as described above.

#. Click on the ``OVERVIEW`` tab if it isn't currently active.

#. Click the ``Edit`` action.  This provides an edit form similar to
   editing a community.

#. In the ``Feature`` field, provide the HTML used for displaying the
   feature.

Managing Organizational Content
===============================

Some content, such as Network News and Network Events, is not
logically part of one particular intranet/office.  As such, this
content is managed in the ``/offices/`` community, above each
individual intranet/office.

There are two paths to reach such content.

- Visit an intranet home page and click on the ``MORE`` link at the
  bottom of the portlet.  This lets you list existing content,
  add/edit/delete content, and see an ``Advanced`` admin view of the
  folder.

- Visit ``Intranets`` as described above, click on the "FILES" tab,
  and navigate to the folder.  This gives you the community UI for
  managing content.

Edit Intranet Configuration
===========================

To change the values of an intranet's address, portlet configuration,
etc., simply navigate to the edit screen for that intranet:

#. Visit ``Intranets`` as described above.

#. Click the ``Edit`` link for the particular intranet of interest.

#. Change the values and click ``submit``.

Adding Forums
=============

By policy, only ``KarlAdmin`` users can create new forums.  These
forums can exist at the the ``/offices/forums/`` level and span all
offices/intranets, but in general, a forum is associated with a
particular office/intranet.

#. Visit ``Intranets`` as described above.

#. Click the ``Edit`` link for the intranet/office where the forum
   should be added.

#. Click the ``FORUMS`` tab.

#. Click the ``Add Forum`` action to create a new forum in that
   intranet.

Once a forum is created, it can be used as a portlet on an intranet
home page.  Also, you can edit the forum's title and description by
visiting the forum and clicking the ``Edit`` action.

Deleting an Intranet
====================

OSI considered deleting a community to be an unsupported operation in
KARL1 and KARL2.  That is, the "correct" way should be to mark the
community as inactive, rather than lose all the information.  This
"correct" way remains in discussion, and thus, deleting was not really
supported.

In KARL3, deleting is a fully-supported operation.  However, to retain
the "you shouldn't be doing this" policy, there is no link in the UI
to delete a community.  Since each intranet is nothing more than a
community, the policy applies to intranets as well.

To delete an intranet:

#. Visit the "delete" URL for the intranet, such as
   ``/offices/atlanta/delete.html``.

#. Click on the ``ok`` button.

After the click, the intranet **and all its content** are deleted.

