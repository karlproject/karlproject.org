======================
Offices as Communities
======================

Offices have long been a sore thumb in KARL.  This became excacerbated
when the pilots came on.  Not only did this highlight some of the
choices that OSI made for its needs, but it became clear that
different organizations would want different capabilities.

At the same time, during the rewrite for KARL3, the need for radically
different implementations of communities versus offices was revisited.
We have the opportunity to allow more sharing between the two, while
preserving the distinctions that justified the separation.



- allow modeling multiple kinds of hierarchy (offices in an
  organization, foundations in a network) inside a container

Existing Policies
=================

- KarlStaff is associated with a primary office.  Some people were in
  other offices, but that was more a reaction to a different need
  (being able to author shared content) that might be scratched better
  in other ways.

- KarlStaff can view any content in any office.

- Certain people are authors of certain kinds of content in an office.

- Anyone that is not KarlStaff has no knowledge of the existence of
  any office.

- KarlStaff sees a list of offices in the footer.  If the current URL
  is in one of the offices, that office is highlighted and displays
  the office information for that office.

- Each office has a left-hand navigation that is unique to that office
  and maintained (currently) manually.

- Office home page

  - The middle column is the same for all offices

  - The right column should be configurable for each office

Questions
==========

- how does this relate to groups, permissions, and "HOME"

- what is the future/better way of integrating RSS information for the
  middle column?

- What policies are wanted for which KarlStaff is allowed to see what
  office content?  Are there any resources in one office that aren't
  visibile to all KarlStaff?

Notes
=====

- Differences between file tool in community v. office

  - The "/files/" part of the URL

  - Difference in policy about who can create and edit

  - Offices can create "page"

- Attachments will be done as attachments, not as hierarchies in
  FILES.  We'll then make a UI to manage the attachments properly.

- The concep of "PRIVATE" might no longer be binary
