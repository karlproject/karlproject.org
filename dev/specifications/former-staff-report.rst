===================
Former Staff Report
===================

Find out which existing users are already "former staff" in which
communities.

Product Backlog Description
===========================

As a developer, I can run a script that accepts a csv file file
containing usernames and the date they became former staff.  The
script outputs csv showing the username, communities (one row per
community), and last activity date for the user in each community they
are members of.

Motivation
==========

In the initial phase of the Former Staff effort, we'll simply be
handling usage going forward.  We still have, though, years of "former
staff" sitting in KARL, members of communities without the moderators
knowing the person is no longer an OSI employee.

Thus, we need a report that shows us all the accumulated former staff
that needs pruning.

Specification
=============

#. Console script that can be given usernames and returns information.

#. The usernames come from GSA, which knows which now-KarlAffiliates
   originated as KarlStaff.

#. The output is CSV.
