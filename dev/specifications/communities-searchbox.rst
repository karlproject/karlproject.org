=====================
Communities Searchbox
=====================

Add a People-like searchbox to the communities page.

Product Backlog Description
===========================

As a user viewing the Communities home page, I can search for
communities by entering a search term in a search box and submitting
the search which will reload the page showing only the communities
matching my search.

Specification
=============

- Integrated just above the letter boxes.

- Visually similar, and behavior similar, to searchbox on the ``All
  KARL`` subtab of ``People``.  That is, a border-wrapped combination
  box of letter links and search box.

- Matches on text in community title+overview.

- If someone clicked a letter, does NOT narrow in both directions.  In
  the M44 iteration planning call, we misspoke and said ``People``
  behaves this way.  Instead, ``People`` treats letter-narrowing and
  searching as mutually exclusive, each clearing the other.

- Pressing enter in the searchbox or clicking the ``Go`` button both
  submit the search.

- Display the searchterm above the communities listing.

- Retain searchterm when paginating through batches.

- This is not a implicitly-prefixed search.  The entire searchterm is
  a word, not a prefix.

Integration With Active Communities Tab
=======================================

We have work progressing on :doc:`active-communities-tab`.  This
searchbox work relates to that work:

- The searchbox appears on both tabs.

- Just like on ``People``, searchterm in one tab, doesn't affect the
  other tab.
