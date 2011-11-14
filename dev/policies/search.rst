================
Policies: Search
================

UI policies for search-oriented screens.


.. _advanced-search-policies:

Advanced Search
===============

- Generic layout, available to staff and affiliates

- No action box

- Title is "Advanced Search"

- Fields

  - Keyword provides the search term. Matches in any field that
    LiveSearch would match on.

  - Author matches on a word in the first/last name of any creators of
    content.  That is, it first finds all the profiles that match that
    search.  It then makes a list of usernames for all those people.
    Finally, a match is made on any resource whose creator is in that
    list.

  - Type restricts results by content type.

  - Tag gets all the tags from the tag cloud (not *all* the tags, as
    that could present a list thousands of items long to scroll
    through.)

  - Year shows all years from 2007 to the current year (won't break in
    2010 like KARL1/2 did). Choice is a single-select and chooses
    content created in that year.

  - These fields are all joined with an "AND", meaning all conditions
    must match.


.. _search-results-policies:

Search Results
==============

- If coming from :ref:`advanced-search-policies` the "show the query"
  box would say something like: ``Your search for x and Wiki Page and
  2008 returned 9 matches.``.

- If no search criteria were supplied, you would see "No Search
  Parameters Supplied".

.. _community-search-policies:

Community Search
================


