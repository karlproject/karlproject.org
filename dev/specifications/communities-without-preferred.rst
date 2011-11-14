================================
My Communities without Preferred
================================

Users with a long list of communities need a way to curate the list.  

Product Backlog Description
===========================

As a user who has not chosen to set “preferred” communities, I see the
My Communities box on my profile and the Communities home page the
same is it currently looks but with a link at the bottom to “Set
Preferred Communities” (with inline help next to it explaining the
option).

Requirements
============

- People with long lists of communities need a way to "curate" that
  list on an ongoing basis

- Should still work for the majority case that choose not to curate,
  or don't face the problem

- Even people that curate their list of communities should be able to
  see the full listing

- Provide a button that goes back to the pre-curated mode

- Applies to all occurences of this portlet (``COMMUNITIES`` tab and
  ``MY PROFILE``)

- When looking at someone else's profile, you do not see a curated
  list of their communities, even if *they* see one when looking at
  the communities portlet on their profile.  Instead, you see the
  current behavior: a listing of all communities they are in (which
  you are allowed to see).

.. _communities-portlet-curating-label:

Implementation
==============

- Add a ``set preferred`` link at the bottom of the ``My Communities``
  portlet

- This link leads to a screen that lets you "curate" your list

- Has an alphabetical listing of the titles (no hyperlinks) of all the
  communities you are in, with a checkbox in front.

- The checkbox signifies inclusion in the manually edited (curated) list

- One button that says "Update", one that says "Clear Preferred"

- The "Clear Preferred" removes all filtering data and returns the user to
  the same state they were in before they started curating.

- Some help text above the grid that explains all this.  Include a
  reminder that if you are in curated mode and you get added to a
  community, it won't appear in ``My Communities`` until you do the
  checkbox.

- Once in curated mode:

  * The bottom of the portlet shows the links ``edit preferred`` (same
    as ``set preferred``) and ``show all``.

  * ``show all`` does an Ajax in-page replacement of the portlet box
    with the contents they would see if they weren't curating.  It
    also changes the ``show all`` link to ``show preferred`` to return
    to the curated view.

- Don't blow up if the community is deleted, or you are removed (or
  leave) the community.

- Make sure each of the portlet links have some helpful title
  attribute text for onhover help text

