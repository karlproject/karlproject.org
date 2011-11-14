===============================
M3 Community Security Test Plan
===============================

Getting the security policies correct for community security is very
important.  This document outlines a test plan for trying each
combination of each policy.


Test Plan Overview
==================

- Seeing staff1 means, performa action.  Ditto for staff2, affiliate1,
  etc.

- LS means see if the community or view is visible to that user in
  LiveSearch.

- SR means see if the community or view is visible to that user in
  search results.

- CP means see if that community or view is visible to that user on
  the communities page.

- MC means see if that community or view is visible to that user in
  the My Communities portlet of the communities page.

- URLBAR means you can type the community or view

Test 3.1
===============

- Login as staff1, logout, login as staff2, logout, login as
  affiliate1, logout, login as affiliate2.

Test 3.2
===========

- As staff1, create a community with title 'M3T2 Test 2'.  Confirm
  staff1 can see it in LS (search for "M3T2"), SR (search for "M3T2"),
  CP, MC, and URLBAR.

- As staff2, confirm you can see M3T2 in LS, SR, CP, and URLBAR.  You
  should not see it in MC.

- As affiliate1, confirm that you can NOT see M3T2 in LS, SR, CP,
  URLBAR, or MC.

* Ensure affiliate1 does not see add community action on Show
  Communities view, or can navigate to /communities/add_community.html
  view.

Test 3.3
=============

- As staff1, create a PRIVATE community with title 'M3T3 Test 3'.
  Confirm that staff1 can see it in LS, SR, CP, MC, and URLBAR.

- Confirm that neither staff2 nor affiliate1 can see M3T3 in LS, SR,
  CP, MC, and URLBAR.

Test 3.4
================

- As staff1, make a private community 'M3T4 Test 4'.  Ensure staff1
  can see M3T4 in LS, SR, CP, MC, and URLBAR.

- Ensure neither staff2 can see M3T4 in LS, SR, CP, MC, nor URLBAR.

Test 3.5 
===========

- As staff1, make a 'M3T5 Test 5' community.  Ensure staff1 can see
  M3T5 in LS, SR, CP, MC, and URLBAR.

- Ensure staff2 sees M3T5 in LS, SR, CP, and URLBAR, but not MC.

- Ensure affiliate1 can NOT see M3T5 in LS, SR, CP, MC, and URLBAR.

- As staff1, add staff2 as a member of M3T5.  Ensure staff2 appears on
  the Members and Manage Members screens.  Ensure staff2 receives an
  email message.

- As staff2, ensure M3T5 is in MC.

- As staff1, add affiliate1 as a member of M3T5.  Ensure affiliate1
  appears on Members and Manage Members screens.  Ensure affiliate2
  receives an email message.

- As affiliate1, ensure M3T5 is in LS, SR, CP, MC, and URLBAR.

- As staff1, remove affiliate1 from the M3T5 community.

- As affiliate1, ensure that affiliate1 receives an email message.
  Ensure that M3T5 does not appear in LS, SR, CP, MC, or URLBAR.

Test 3.6
============

- As staff1, make a public community 'M3T6 Test 6'.  Ensure staff1 can
  see M3T6 in LS, SR, CP, MC, and URLBAR.

- Ensure staff2 sees M3T6 in LS, SR, CP, and URLBAR, but not in MC.

- Ensure affiliate1 cannot see M3T6 in LS, SR, CP, MC, and URLBAR.

- As staff1, make M3T6 private.  Ensure staff1 can see M3T6 in LS, SR,
  CP, MC, and URLBAR.

- Ensure neither staff2 nor affiliate1 can see M3T6 in LS, SR, CP, MC,
  and URLBAR.

Test 3.7
============

- As staff1, make a community 'M3T7 Test 7'.

- Add staff2 and affiliate1 as members.

- As all 3 users, confirm that M3T7 appears in MC.

- As staff1, visit the '/delete.html' URL on the community.  Confirm
  the deletion.

- Ensure that M3T7 does NOT appear in MC for staff1, staff2, and
  affiliate1.

Test 3.8
===============

- As staff1, make a community 'M3T8 Test 8'.

- Add staff2 and affiliate1 as members of M3T8.  Ensure both receive
  email messages.

- As staff1, make staff2 a moderator.  Ensure that staff1 and staff2
  receives an email message.

- As staff2, remove affiliate1 as a member.  Ensure affiliate1
  receives an email message.

- Attempt to remove staff1 and staff2 from the community.  Should get
  an error screen.

- Attempt to remove moderation from staff1 and staff2.  Should get an
  error screen.

- As staff1, remove moderation from staff1.  Confirm that staff1 is no
  longer a moderator be visiting Members and seeing if the actions box
  appears.  As staff1, try to navigate to the URL for managing
  members, ensure it fails.  Ensure that staff1 and staff2 received
  email messages.

- As staff2, confirm that Manage Members has no checkboxes for
  removing staff2's moderator or membership.

Test 3.9
============

- As staff1 make a 'M3T9 Test 9' community.

- As staff1, go to Members then Invite New.  Paste an email address
  for invitee1 (not yet a user), as well as the email addresses for
  staff2 and affiliate2.  Confirm an error that staff2 and affiliate2
  are already users of the system.

- As staff1, remove staff2 and affiliate2.  Paste in a malformed email
  address, such as zzz.  Confirm another error message.

- As staff1, change the textbox to only have invitee1 and submit.
  Confirm that the email address appears in Manage Members.  Use the
  checkbox to remove the invitation.  Confirm that invitee1 received
  an email.

- As staff1, re-visit Invite New and re-submit invitee1 as a user.

- Read the new email and paste the URL into a browser window that IS
  logged in.  Confirm that you cannot accept an invitation when logged
  in.

- Log out, then paste the invitation URL again.  Leave out some
  required fields and submit.  Confirm error messages.  Use staff1 as
  a username, confirm that the username exists.  Use a username with a
  space, confirm the error message.  Try passwords that don't match,
  and passwords that aren't long enough.  Confirm errors.

- Provide correct information for invitee1.  Submit.  Get teleported
  to the new community, already logged in.  Confirm receipt of an
  email.

- As invitee1, confirm that M3T9 appears in LS, SR, CP, MC, or URLBAR.

- As invitee1, confirm that M3T8 does NOT appear in LS, SR, CP, MC, or
  URLBAR.

