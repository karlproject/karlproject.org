.. _people-tab-label:

===================
People Tab in KARL3
===================

The People Tab is a reporting facility on information stored in user
profiles.  It provides a convenient, useful way to browse various
groupings of people, as well as search within certain groupings.

Background
------------

KARL2 had 3 top-level tabs: People, Tagging, and Communities.  The
People tab, as it turned out, had a fair amount of "policy" in it: who
was allowed to see what, different listings for different audiences,
hosting-organization-specific views, and policies about profile fields
and editing.

More specifically, OSI wanted the People tab to be an extension of
internal business applications, rather than a generic facility.  As
the pilot organizations came onboard, it became clear that a
one-size-fits-all would not work.

This specification attempts to document the assumptions, then proposes
how KARL3 will implement a People tab.

Goals
----------

- Provide efficient browsing and searching of people in KARL

- Balance the generic needs of pilots versus internal, custom needs of
  OSI (or anybody else that needs something unique)

- Ensure that the people directory is coherent with the architecture
  and easy to maintain during upgrades over the life of KARL

- Obey the security policies (who is allowed to see what) in as simple
  a manner as possible

Requirements
---------------

- Easy to include new information in a profile when it is extended

- The "facets" needed for grouping include the following:

  - Permission (am I allowed to see this profile)

  - First letter (for letter links)

  - "Office"

  - Community

  - Department

Non-Requirements
------------------

- This is not intended to be an application for bulk management of
  personnel.

- Nothing in the People directory will change any content.  It is
  purely a reporting application, read-only.

Architecture
----------------

- This will not run as a separate application.

- The People directory is simply a reporting tool on information
  stored in profiles. It uses whatever fields are defined on profiles,
  along with whatever indices are available on profiles.

- Profile content are simple "model" objects stored in the ZODB.

- Querying is done by searches against indices setup in the catalog
  for that site.

- The queries that you issue to select profiles for display must use
  catalog indices to maintain performance.  The list of indices needs
  to be known beforehand, in the software.

- User and group information is not part of the profile per se.  Thus,
  any queries that need this information for groupings, need to have
  the profile mediate this access.  This also means you can remove a
  person as a user, but their profile will remain as useful content.

- The only "groups" that are needed for searching are communities and
  offices.  Everything else (e.g. department) is data stored directly
  on a profile.  We will probably remove the distinction by having a
  property accessor on the profile that returns the security grouping
  information, to completely remove the word "group" when discussing
  the people directory.

- To avoid ballooning the index, some columns in a batch listing might
  not be sortable.

- Unlike Plone, the catalog in KARL doesn't store metadata and doesn't
  return brains.  Instead, you get back identifiers you can use to
  wake up the object and display what you need.  As it turns out, this
  is a billion percent the right way to do things.

- The requirements will, as much as possible, be steered in the
  direction of matching the Ajax work for the grid widget.  See Ajax
  below.

- Different organizations will have different ideas about who is
  allowed to see what profiles.  For example, some might allow
  "affiliates" to see "staff".

Ajax
-----------

- The "grid" widget provides in-page, server-driven navigation.
  Meaning, you can move from batch-to-batch, sort, etc. without
  reloading a page.

- JS communicates with the server via URL parameters which indicate
  batch position, sort column, sort order, etc.  These are supplied to
  a BFG view which performs a catalog query and returns the results.

- Results are currently done as HTML. This allows the first batch to
  be returned in the payload of the response, to avoid waiting to see
  the results.

- Columns of data can be presented.  Sorting can be done on columns.

- Letter links are currently possible, though not moved into the grid.
  The letter link implementation has the benefit that it only links to
  letters that actually have results.

Pluggability
---------------

Different customers can plug-in new definitions of profiles, thus
providing different fields of data on the "model" objects (profile
instances).  These can then be displayed in a custom People directory
by plugging in a new implementation of the people views and templates.

However, if extra data are needed as part of the queries (e.g. a new
facet to drill down into), then the custom field needs to be indexed.
Chris will have to confirm, but I think this means your add-on package
will register an event handler that indexes this custom information.

Extended Requirements
------------------------

Collect, but unscheduled, requirements (meaning, weren't part of the 2
major enhancements approved in December):


- Allow profiles to say "make my profile viewable for these people"

- We'll try to prevent auto-generated links to follow a profile when
  they aren't allowed to see the profile (visible)

Proposed UI
--------------------

The generic KARL will get away from tabs that try to portray different
groupings to different people.  Instead, a UI similar to Network News,
using drill-down dropdown menus, could be effective.

- At the top, a series of drop-down menus allowing you to choose an
  office, a department, or another pre-indexed facet.

- On the right, same row, a search box that allowed narrowing within
  the drill-down.

- Below that, letter-links that allow skipping the the first letter of
  the current result set.

- Column sorting can also help navigation.
