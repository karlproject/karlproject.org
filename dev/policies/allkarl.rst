===================
Policies: All KARL2
===================

There are some policies that apply to all pages in the various "layouts"
of KARL. This document describes each policy, organized by the layout.

All
===

The following policies apply no matter the layout.

- The KARL logo appears in the top right screen and is clickable, taking
  you to the :term:`Root URL` (e.g. https://karl.soros.org/).

- Going to the :term:`Root URL` redirects you to the correct place,
  depending on circumstances:

  - If you have not logged in, or your login is invalid, you are
    redirected to login-edit.

  - If you are logged in, and you are KarlStaff, you are sent to the
    :ref:`office-view` for your screen as your :term:`Home URL`

  - If you are logged in, and you are not KarlStaff, you are sent to the
    /communities page as you :term:`Home URL`

- Support a print CSS layout as well as a screen layout

- Allow versioning of URLs to static resources, for caching purposes

- Inject Google analytics JS at the end of the </body>

- Inspect karlfunctions.xsl for some mapping of htmltitle per screen



Header
------

- The "Home" link takes you to your :term:`Home URL` (see above)

- The "My Profile" link takes you to your profile

- The LiveSearch box is described below

- The searchbox has a GO button that performs a search and shows the
  results on a new page

- There is a link to "Advanced Search"

- A row of tabs presents 3 global tools

  - If the user is KarlStaff, show a Tags tab which links to
    tagcloud-view

  - Show a People tab. For KarlStaff, this links to osipeople-view. For
    KarlAffiliate, this links to allkarl-view.

  - A Communities tab which links to communities-view

- If there is a portal status message, display it in the
  :ref:`status-box-policies`.


LiveSearch
----------

- After the third key is pressed, search is triggered

- Queue up keypresses and only search-and-update every 2 sec

- Perform a search and group results by "Kind"

- Show up to 5 results for each Kind

- Display "No Matches" in a Kind group that has no results

- Each result has a link to visit that result

- Each group has a link to do searchresults on just that group

- A "Show All" link goes to searchresults for any group

- Pressing Escape or clicking outside the box makes the results box
  disappear

- Arrow keys move between results

- Pressing enter is equivalent to clicking on a result

- Pressing backspace generates a new search, caching where possible



Footer
------

- An image for the :term:`Hosting Organization` logo

- If you are KarlStaff, a series of links to each office:

  - The links are sorted alphabetically

- Links to Help, Contact, and Legal

- A copyright statement for the :term:`Hosting Organization` that is
  running the KARL

.. _office-layout-policies:

Office Layout
=============

- In the footer, bold the the office that the current URL lives under
  and show its address *if* it isn't the National Foundation


.. _community-layout-policies:

Community Layout
================

- Display the community name, with the privacy badge and a left-floated
  community search box

- The community search box is NOT livesearchish

- Display a row of tabs for each tool, then float-right links to People
  and Tags (tag cloud)

- The "current" tab is white, the others grayed out

- The :term:`Root Community URL` for a community (e.g.
  /communities/mycommunity) leads to the default tool. If the
  community has not assigned a "Default Tool", then this URL shows the
  :ref:`show-community-policies` as the default. If a different
  tool is set as the default, then the user is redirected from the
  Root Community URL to the tool URL (e.g. mycommunity/blog).

- All community screens have a right column with portlet-like
  information

- On most screens, this right column is the
  :ref:`community-tags-portlet-policies` and the
  :ref:`active-people-portlet-policies` portlet

- Blog entry view instead shows :ref:`community-tags-portlet-policies` and
  :ref:`blog-archive-portlet-policies` as portlets



Generic KARL Layout
===================

This layout handles screens that aren't in a community or an office.
Examples include: communities-view, people screens, search results, and
global tag views.




Anonymous Layout
=================

This layout handles the few screens you can see when you are not yet
logged in. E.g. login, logout, acceptinvitation, recover password.

- Don't inject Google Analytics

- Never show actions box
