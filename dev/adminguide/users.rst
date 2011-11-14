===============
User Management
===============


In KARL3, user management is built directly into the KARL application.
Existing facilities (LiveSearch, People Directory, etc.) are used to
locate users.  If you are logged in as an administrator, you see extra
information that lets you manage the users.

This document reviews the following capabilities:

- Adding a user

- Changing profile information on a user

- Putting a user in more "groups"

- Changing a user's password

- Home path

Also, an :download:`audio/video "screencast" is available
<screencast1.mov>` that demonstrates many of these administrative
actions.  The screencast is in QuickTime format.

.. note::

  There isn't currently an option to delete a user.  This is due to
  the extra policy decisions regarding what to do with content created
  by the user.  If the goal is to prevent someone from logging in, the
  easiest course is to change their password without telling them the
  new password.

Adding a User
=============

The process of adding a new user to KARL is relatively simple: visit
the ``PEOPLE`` tab and click on the action to add a new user.  More
detail as follows:

#. Log in using an account that has UserAdmin or Admin privileges.

#. Click on the ``PEOPLE`` link near the top right.

#. Click on the action (in the green box) which says ``Add User``.

#. Fill in the details as appropriate.  If the new user is intended to
   be "Staff", choose ``KarlStaff`` under ``Group Memberships``.


Editing Existing User and Profile
=================================

Users that have been granted ``KarlUserAdmin`` rights are able to edit
the profiles of existing users:

#. You start by locating the profile you want to edit using any of the
   navigation schemes in KARL (LiveSearch, the ``PEOPLE`` directory,
   etc.)

#. The ``Edit`` action (in the green action box) leads to
   ``admin_edit_profile.html``.  This is the administrative screen for
   editing a profile, which contains extra options.

#. This screen allows editing all the same profile values the user
   sees.


Putting a User In More Groups
=============================

How can one convert an "affiliate" user into a "staff" user, or vice
versa?  How can a user be given ``KarlUserAdmin`` or ``KarlAdmin``
rights?

#. Follow the instructions above to edit the profile.

#. In the ``Group Membership`` section, select ``KarlStaff`` to make
   the user a staff user.  De-select it to make them an affiliate user.

#. The same is true for the other groups.


Change a User's Password
========================

The procedure above for editing a profile also allows changing a
user's password.  Provide the new value in the ``Reset Password`` and
``Confirm Reset Password`` fields.

Home Path
=========

The "home path" controls the URL that users are sent to when they
login, or click on ``HOME`` in the top menu, or visit the URL at the
root of the KARL site.  In each of these cases, a user is redirected
to the location at the "home path".

In most cases, leave this blank to allow system policy to do its job.
For example, affiliates are sent to the ``/communities`` path.
