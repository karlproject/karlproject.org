======================
Active Communities Tab
======================

Provide multiple views of ``Communities``.

Product Backlog Description
===========================

As a user viewing the Communities home page, I am shown All
Communities (I can see) by default but can opt to show only Active
Communities (any community updated in the last X months).

Specification
=============

- Very similar to sub-tabs in ``People``.  Active tab has one style,
  other tabs have another style.  Each tab, including the default tab,
  has a ``@name`` on the view.

- The ``My Communities`` portlet appears on both tabs, but is outside
  (to the right of) the tab "frame".

- Both tabs get the letterbox/searchbox combo.

- Two tabs: ``All`` and ``Active``.  The former is the current
  ``Communities`` view.  On the latter, make the tab name have an
  onhover which explains the policy for "Active" by saying:
  "Communities last updated in previous six months".

- Active means, filter out all communities that weren't active in last
  six months

- ``All`` is the default tab.  Clicking on ``Communities`` should
  redirect to the view for ``All`` (as it currently does.)

- If possible, use a cookie to make the choice of tab "sticky", as we
  do in calendar views.  That is, if you click on a non-default tab,
  it sets a cookie saying you prefer that view.  Later, when you click
  on ``Communities``, before doing the redirect, see if there is a
  cookie choosing a non-default view.  If so, redirect there.

- Tres made a previous stab at all this, but with a UI that wasn't
  right. Get with him to find out what parts he did and what might
  need to be ripped out.
