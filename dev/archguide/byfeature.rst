==============================
KARL3 Architecture By Feature
==============================


People
======

The core user data will be stored in PostgreSQL.  It is probable that
additional profile information, possibly using an extensible facility
requested by Synergos, will be manged as "content" in the ZODB.  As
such, the People directory and the profile viewing will become much
more distinct, architecturally.

When users search via LiveSearch or Advanced Search, they need to
match on user data and profile data in ways similar to other content
(prefix matches, stopwords, relevance ranking on results.)  Therefore
people data will be reflected into the catalog in some fashion.

KARL3 will only ship with the "All KARL" tab, which will be changed to
have a columnar, paginated listing of several columns.  The columns
won't be sortable and there will not be an additional search box in
the listing.  Letter links, however, will be available.

Tagging
=======

Tagging will be completely re-implemented.  It will be far more
integrated into the transaction space, eliminating the accumulation of
dead data.  The datastructures will be based on IIOBtrees, very
specifically written for the unique nature of OSI's tagging needs
(e.g. community tags.)

Community tags will be implemented by treating a community as a user
that has tags.

Search
======

As discussed in the by-technology section, KARL3 will use standard
Zope indexing and searching, re-packaged with fewer dependencies as
repoze.catalog.  All indexing will be done real-time.  Indexing of
binaries will be done as child processes, although not using the
TextIndexNG3 package.

Instead of attempting to use the context summary highlighting in
search results, we will instead show the first 200 letters of the
result "description".  If contextual summaries are needed, a post-3.0
research project can look at stemming and highlighting either by brute
force (simple, but performance hit) or done in advance.

Communities
===========

In KARL2, a Community was a fairly heavy content type: a Plone Folder
with event subscribers and marker interfaces, ultimately constituting
thousands of lines of code.  This will be far simpler in KARL3.  We
expect "Community" to be a couple of hundred lines, including the
underlying infrastructure.

Adding a community should be at least 100x faster in KARL3.

Also, the listing of communities used Xapian to get batches in KARL2.
For KARL3 we will use the catalog to get paginated, permissions-based
results.

Membership
==========

KARL2 managed invitations as content on a community and the member
list using grups.  KARL3 will be similar.

Alerts
======

TBD.

Files
=====

- versioning, diff, resurrect

Wiki
====

Although KARL2 used Plone 2.5, the decision was made to use the same
Wiki enging (wicked) slated for arrival in Plone 3.  Unfortunately,
Plone 3 now regrets that decision, as wicked isn't actively supported.

KARL3 has very simple needs from a Wiki.  As such, a 200 line wiki
implementation was written for KARL3 and was available in the initial
prototype.

Blog
====

KARL2 used a custom Archetype content type for blog entries and
comments, with attachments stored in the Files tool using a URL
convention as the reference.  KARL2 will be similar, but not using
Archetypes.

Calendar
========

The Calendar tool in KARL2 used underlying Plone Event content types,
presented through a rather challenging UI based on XSLT date
arithmetic.  Since the Calendar tool is one of the lower priorities,
KARL3 will be very basic in its implementation: no Ajax, just ZPT
driven by Python-based DateTime arithmetic.

In fact, it is possible that the Calendar doesn't use the catalog, but
simply wakes up all of its children.  Usage shows that very few
communities have many clicks on the calendar tool, and fewer still
have a large number of events entries.

Offices
=======

TBD.

Syndication
===========

TBD.

Forums
======

TBD.

Reference Manuals
=================

TBD.
