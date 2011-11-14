=======
Tagging
=======

The KARL project has a number of facilities that provide "knowledge
management" across the community, intranet, and people facilities.
Tagging is one of these facilities.

This specification documents the existing requirements of this
facility along with a proposal for re-implementation as part of KARL3.
It is not expected that tagging will be enhanced with new features on
the way to KARL 3.0.

Background
==========

KARL1 (and KARL2) envisioned a tagging facility largely modeled after
delicious (insert periods as needed).  This facility provided tagging
of resources, including people, as well as viewing tags globally,
within a community, or for a person.

KARL1 tagging worked as an external REST service that ran outside of
KARL's Zope/Plone stack.  This service used "Tasty", a Python
application written using an old version of TurboGears and SQLObject.
The deployment of KARL1 was on Windows, and thus SQL Server was used
as the database driver.

There was a fairly never-ending set of problems with the tagging
service.  Tasty itself wasn't written particularly well and has been
abandoned.  Allegedly the transaction semantics used by SQLObject
didn't play nice with SQL Server, causing many deadlocks that were
extremely hard to debug.  The REST service had authentication
drawbacks.  Ultimately the REST service was avoided and KARL grew
direct tentacles (via SQL queries) into the database.

Notably, OSI never asked for a sevice that could tag resources outside
of KARL.

Next to cataloging, the tagging system is the biggest source of bit
rot, bugs, performance problems, and architectural accretion.  For
KARL3, we need a service that is narrowly-focused, fit-for-purpose,
reliable, and performant.

At the same time, tagging has proven to be a little-used feature of
KARL.  Perhaps this is due to the problems and unreliability, but more
likely, this is because tagging is an alien idea to the (somewhat
older) audience of KARL.  Therefore, tagging can't get a big slice of
the budget.

Functionality
=============

Resource Tagging
----------------

- Visit a resource and see a "tag box" listing of tags applied to that
  resource, e.g.::

   tagA (3), tagB (7), tagC (4)

- tagA is a hyperlink to view that tag page for tagA and 3 is a
  hyperlink to view the "tag users" for tagA.

- The "tag users" is a page that shows which people taggged a resource
  with a certain tag

- A tag can contain any letter, number, underscore, or dash. No
  spaces, symbols, or punctuation are allowed.  Tags are converted to
  lower case, preferably as people type in the Ajax widget. Note that
  we might have to live with migrated data that breaks the rules.

- The tag box also has a "+" symbol which opens the tag editor widget.

- The tag editor widget allows you to add, edit, and remove tags that
  are on a resource.  Only *your* tags, however.

- The tag editor contains an autocomplete widget.  As you type, this
  autocomplete widget shows you any tag used anywhere in the system
  which starts with the currently-typed letter.

- Autocomplete works for whatever word in the tag list the cursor is
  currently inside.

- You can use the mouse to select a tag.  You can also use up-down to
  navigate through the tag list and escape to dismiss the
  autocomplete.

- The tag editing widget should throttle the pings to the server by
  storing up keypresses for 1 second.

- Editing the tag list makes the appropriate add/edit/delete
  operations on the tag list.

Global Tags
-----------

- On tag view (or any place where resources are listed), do not list
  any resources that are not viewable to you.

- On tag view, the heading says ``KARL / Tags / [sometag]``.  In this,
  ``sometag`` is an input box.  You can edit it and press enter,
  jumping to the tag page for some new tag.

- On tag view, each resource is listed showing its title (as a
  hyperlink to its resource), whether it is private, its description,
  what kind of thing it is, and a "Tagged by 2 people", where 2 people
  is a hyperlink to the "tag users" page.  This is a paginated
  listing, with a pagination box at the bottom.

- The tag view screen also has a "Related Tags" portlet, listing other
  tags that are "related" as a hyperlink to the tag page for that tag.
  Tags are related purely when they are used on a common resource.

- The tag users screen lists each person that tagged a resource (as a
  hyperlink to their profile), plus all the other tags that person put
  on the resource (as hyperlinks to those tag pages).

- The global "Tags" tab is not shown to affiliates.

- This link goes to the global tag cloud, showing the 100 most
  important tags in up to 7 font sizes.  Each tag is a link to the
  global tag page for that tag.  There is also a link to the global
  tag listing.

- The global tag listing provides a paginated listing of each tag,
  sorted alphabetically, and the count of times it has been used.
  Each tag is a hyperlink to the global tag page for that tag.  There
  is also a link back to the global tag cloud.

Community
---------

- There is a "Tags" link that appears on every screen in a community
  that goes to the "community tag cloud" screen.

- There is also a "Tags" portlet that appears on every screen, showing
  up to 5 of the most popular tags, sorted by descending frequency,
  with a hyperlink to the community tag page for that tag.  The
  frequency is a count of the number of times that tag was used on
  resources inside that community.

- The community tag cloud page shows the same as the global tag cloud,
  but the ranking is based on times used inside the community.

- The community tag cloud page has a link to the community tag listing
  page. Same as global tag listing, but with a count for each tag that
  shows time used in the community.

Profile
-------

- On a person's profile page, there is a "Paul's Tags" portlet that
  lists up to 10 tags, sorted by highest tag count.  Each row shows
  the tag count and a hyperlink to view the tag.  At the bottom is a
  link "All Paul's Tags" that goes to a personal tags view, giving a
  listing of all that person's tags, sorted alphabetically.

- A person's profile is a resource that can can be tagged, just like a
  Page.

- When a person visits their profile page, they see a "Manage Tags"
  link that goes to the personal tag management screen.  This screen
  allows renaming and deleting your own tags (but nobody elses).

- Rename lists all of your tags in a single-select box, with an input
  widget that allows you to change a tag to a new spelling.

- Delete allows you to select a single tag and delete it.

Requirements
============

- Tagging does not have to span multiple applications.

- Ensure that deleting a resource (and other relevant content model
  changes) takes the "appropriate action" in the tag system, removing
  all tag statements that point at that resource.  Stated differently,
  take extra care that the content model and tag model don't get out
  of sync.

- Provide a REST interface available via Ajax, solely for the purpose
  of allowing in-page tag operations.

- Ensure that modifying a person's tags triggers
  authentication/authorization checks.

- Making a tagging system that is abstract enough to be adopted
  outside KARL is a non-goal.

- Although KARL might run support multiple customers in a hosted
  environment, it is expected that each tag space is completely
  isolated from every other tagspace.  Thus, it is a non-requirement
  to have tagging support different KARL customers internally.

- Tags can be Unicode.

Proposal
========

- Write a repoze.bfg library for tagging that uses Zope events to
  connect the tagging system to the content model.  As such, stay in
  the transaction space, to avoid the out-of-sync issues of the past.

- Future work might attempt to take this tagging system outside of the
  WSGI application and work across multiple applications.  Don't do
  anything explicitly to achieve this, however.

- Instead of wiring this up to KARL, write a sample application that
  performs the work of the various screens.

- Do not attempt to provide REST modularization from/to other
  applications.

- Use repoze.who for shared authentication.

- Anticipate the usage of Ajax for tag editing.

- The data storage model is flexible.  Choices are: ZODB (with a
  catalog or btrees or whatever for performance), SQL Alchemy, or
  native PostgreSQL.  Steer in the direction of reliability and
  simplicity, versus abstraction and astronauting.

- The schema is also flexible.  Do not feel confined by the existing
  (poorly designed) schema.

- Work done in later iterations needs to take on the (crummy) task of
  migrating the existing tagbase to the new data model.

- If possible, use URL traversal (/tags/sometag) instead of the
  current approach (/tagpage.html?tag=advocacy).  Plan, though, to
  allow requests to the old-style to get redirected to the new-style.
  (Most likely this will be handled by something outside of this
  proposal.)

- At some iteration in this project, we will need the tagging sample
  app to plug in the widgets using the KARL3 UI system.  This can
  either be done by Mike, Balazs, Paul, or some combination thereof.

- If there are cases where the tagging model and the content model can
  get out of sync, provide a UI that re-indexes the tag model.

Changes from KARL2
==================

- The taglist in KARL2 is shown on every taggged resource.  It
  includes, for each tag, a number showing the count of other people
  that have tagged that resource, with a hyperlink.  This is an
  expensive operation (both in Tasty and in K3 tagging.)  We would
  like to not do this automatically.  Instead, we either drop that
  requirement, or we get users to gesture when they are actually
  interested in this information.

Questions
=========

- How does tagging in a private community, or on a private resource,
  affect the tagging system?

- Does Mike need a KARL login to see some of the existing behavior?

- Do tag pages need to show up in search results? OSI's preference is,
  instead of tags showing up in search results, they influence
  relevance.  This would fall under the budget of enhancements that
  has ten percent of the total budget.

