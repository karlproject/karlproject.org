==================
Distribution Lists
==================

OSI has a series of officially-sanctioned mailing lists.
Administering these in Exchange involves a set of tradeoffs that has
proven lacking.  Instead, we will provide a distribution list facility
tied to KARL, with email addresses that can act as message
distribution.

Goals
=====

- Easy for KARL Admins to create a new distribution list under
  "PEOPLE" and turn over control of distribution list maintenance to a
  particular staff member.

Background
==========

OSI has a few hundred mailing lists managed as part of Exchange.
Because they are in Exchange, it requires an Exchange admin to keep
these up-to-date, with the result that they are now out-of-date:

- People are incorrectly listed in the address book definitions for
  the distribution list

- Outdated, unused mailing lists still appear

As it turns out, KARL has proven to be the most accurate definition of
groupings (via PEOPLE.)  Since KARL has also proven to be reliable at
sending mail, the thought arose to use KARL as the facility for
distribution lists.

Proposal
========

1. A new tab on PEOPLE called "Distribution Lists".

2. This provides a listing of all defined distribution lists, with
   hyperlinks to visit a report page for each distribution list.

3. Clicking the Email icon opens Outlook with the To: address filled
   in for the distribution list (or multiple lists), similar to how we
   have an icon on the BLOG tool for email-in to a blog.

4. Provide this icon on existing report pages which have enabled
   "distribution list" support on their ``Edit`` screen.

5. The To: address is an email address for the distribution list.  See
   below for details.

6. Emails are not re-formatted in any way.

7. KarlAdmin creates the distribution list, then designates one or
   more moderators who add/edit/remove people from the distribution
   list.

Email Addresses
===============

Email addresses will be of the form::

  lists-name-of-list@karl.soros.org

Note that we are doing distribution list support for existing reports.
These might conflict with community names.  Thus, we reserve the right
to prefix ``lists-`` or something similar, or use some other solution
to this issue.

When someone sends an email to this list, each person receives an
email that says it is from the original person, exactly as if they
sent it directly.  The emails originate from the person's email
program via a ``mailto:`` link and have zero reformatting of the body
or subject.

Security
========

- "Distribution List" support is off by default, must be enabled by
  KarlAdmin.  (That's a proposal by me, to allow this to be used only
  by OSI at first.  Other solutions solicited.)

- Admins can add new distribution lists and assign moderators.

- Admins and Moderators can add/remove members on the distribution
  list.

- Admins can enable/disable distribution-list-ability on existing
  "organizational" reports.

- Admins and Moderators can enable/disable archiving (if we later
  choose to do archives.)

- Admins, Moderators, and Members can send emails to a distribution
  list.

- Staff can send email to organizational reports that are enabled for
  distribution-list-ability


Archives
========

Though not specifically requested, we had a discussion about whether
to archive emails in some cases.  For many cases, privacy of content
(and moreso, the impression of privacy as a default) is paramount.  In
other cases, using email as a low-barrier, lightweight way to hoover
in "knowledge" is very enticing.

How to square this circle?  Brainstorm different ways:

- A knob on list create/edit that turns on/off capture of or display
  of archives.

- Perhaps tie that to security, just like everything else.

- Maybe have one general purpose list, tied to an organizational
  report, that is a dumping ground for email-in.  Staff that with some
