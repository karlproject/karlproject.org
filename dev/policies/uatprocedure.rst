=============
UAT Procedure
=============

As KARL3 is developed, we provide a test site where OSI evaluates
deliverables and reports bugs.  This process is called "UAT": User
Acceptance Testing.

This document explains the process and provides details (URLs,
usernames and passwords, bug reporting procedures) for conducting UAT.

Summary
=======

- Review UAT and report bugs at https://bugs.launchpad.net/karl3

- Go to evaluation test site at http://carlos.agendaless.com/demo

- Usernames and passwords are staff1:staff1, staff2:staff2,
  affiliate1:affiliate1, affiliate2:affiliate2, etc.

Big Picture
===========

The KARL3 project is scheduled into units called "milestones".  A
milestone is usually around a week long and contains a number of
"screens" (Login screen, List Communities screen, etc.) that are
scheduled for completion and evaluation.

Each of these screens have a scorecard that measures success.  The
scorecard is called the "UAT" (user acceptance test) and lists all the
business rules for that screen.  The set of UATs for a milestone is
the definition of the milestone itself and the success criteria.

.. note::

  The buck stops with Nat on approving updates to the scorecard and
  flagging the scorecard as "Confirmed".  He will consolidate OSI's
  internal discussions and be the liason for testing.

To manage and report on this UAT process, we create "bug reports" in
Launchpad for each UAT in a milestone.  They are denoted as a UAT by
using the "uat" tag on the bug report.  Further, we use a tag as the
screen identifier to know which screen the UAT is associated with.
This system of cross-referencing via tags is how we layer project
management atop Launchpad's (rather limited) PM facilities.

Details about each of these UAT bug reports in Launchpad:

- The UAT bug is assigned a milestone that schedules that screen's
  evaluation to a milestone.

- The UAT bug has two tags: one for "uat" that makes it a UAT bug
  report, and onther for the screen id (e.g. "show-login").

- The screen id helps see what existing bugs are open for that screen.

- The body of the issue points to a page in the docs with all the
  business rules.

- The UAT bug is assigned to OSI and owned by them.  The status of the
  UAT bug reflects percent completion of evaluation:

  o Mark its status as "Confirmed" to say that Nat and Paul agree on
  the scorecard.

  o "In Progress" says evaluation has started.

  o "Fix Committed" when all bugs have been reported.

  o "Fix Released" when OSI confirms all bugs are closed.  (Note: We
  might never get around to this step, it's a lot of extra work for
  OSI to confirm bug closing.)

- To discuss the scorecard's business rules, use comments on the UAT
  issue.  This keeps an historical record of the discussion and the
  decisions regarding the scorecard.  Again, this is the
  **authoritative** specification, trumping all emails, phone calls,
  and hearsay.

.. note::

  Use bookmarks and multiple tabs to avoid re-opening the same screens
  repeatedly.  For example, do an advanced search of all the uat's in
  M3 and bookmark that (with a friendlier bookmark title.)  Bookmark
  the advanced bug report URL, etc.

Reporting Bugs
==============

As you progress through the items in the UAT "scorecard" and find a
problem, report a bug.  Simple tip: bookmark the URL for adding an
advanced bug.

Filing a bug is relatively simple:

- First, see if there is an existing bug for that screen.  To do so,
  revisit the Launchpad screen showing the bug list and look in the
  ``Tags`` portlet on right.  There you can find the screen identifier
  (e.g. ``show-login``) for the screen you are testing.  Open that in
  a new tab or window.

- Click "Report a bug" and click on the ``Advanced reporting options``
  link.

- Provide a *useful* sentence in the summary.  Not "Problems on
  login".  Remember, people will be scanning listings of these bug
  reports.  Don't make them click to read the bug report for basic
  understanding.

- In ``Tags``, it is critical to put the correct screen identifier
  (e.g. ``show-login``) for the screen.  This needs to match the tag
  on the UAT bug you are working on.

- In some cases, you should attach a screenshot to explain a problem.

- Skip the ``This is a security vulnerability`` part.

- Click ``Submit Bug Report``.

On the next screen you have the option to do additional categorizing
by clicking on the icon to the left of ``New`` under ``Status``.  The
icon looks like an "eject" button.

- Leave Status alone

- Grade the Importance using the criteria discussed below under "The
  Hidden Value of Importance".

- Choose a Milestone related to the milestone you are doing UAT on.

- Assign the bug to ``paul-agendaless`` for triage.

- Leave the comment empty unless you need to explain an Importance
  higher than medium.

Testing Details
================

- The test site is at ``http://carlos.agendaless.com/demo``

- The first load of a screen after a server restart is slow.  Each
  request thereafter should be zippy.

- All content is temporary, we frequently delete all the data.

- Your KARL2 login won't work

- Test accounts are provided for different roles:

  - staff and affiliate roles, with password same as username

  - staff1:staff1 is username and password of one account

  - Ditto for staff2:staff2, staff3:staff3, affiliate1:affiliate1,
    affiliate2:affiliate2


The Hidden Value of Importance
==============================

Grade inflation is the bane of project management.  Every new thing
marked as "High" simply lowers the importance of everything else
marked as high.  In particular, the tendency to judge the item
currently under discussion as more urgent than yesterday's urgent
thing will be met with skepticism.

Thus, Nat and Paul have agreed on a tough-love grading system:

- By default, everything is medium.  This should be around 60% of the
  bugs.

- If you could possibly go into production without a fix, mark it Low.
  This should be around 30%.

- Items that aren't in KARL2 should be Wishlist.

- Things that are truly critical to the success of the project should
  be High.  This should be around 10% and represent "massive
  investment to secure victory," aka the Powell Doctrine.

- Critical means "everything by everybody stops, the entire project
  stops, until this thing is resolved".  It should rarely be used and
  indicates true, flat-out, stop-the-presses panic in the streets and
  mass hysteria.

When tempted to over-grade, the answer is simple: Don't.  You may
think you are increasing the chance that it will get done, but you're
really just decreasing the chance other stuff will get done.

