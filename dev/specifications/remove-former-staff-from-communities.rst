====================================
Remove Former Staff From Communities
====================================

When a user transitions to "former staff", remove them from
communities.

Product Backlog Description
===========================

As an administrator working in KARL directly or in an external system
sync'ing users with KARL (i.e. GSA), when I remove the KarlStaff role
on a user, the user is automatically removed from all their
communities.

Specification
=============

#. (Web) A user profile is edited by an administrator as described in
   :ref:`notify-former-staff-moderators` and the option to remove them
   from communities is triggered.

#. (GSA) Alternatively, a record in GSA sync indicates that a user
   that previously had the KarlStaff group, no longer does.

#. Find all the communities that person is a member/moderator in and
   remove them from the membership of the community.

#. Clean up any alert preferences as appropriate.

Questions
=========

#. What if the former staff user is the sole moderator of a community?
   Should we prevent the action from taking place in the web version
   of this story?  What do we do with the GSA background process,
   which doesn't have a user sitting in front of it to send an error
   to?
