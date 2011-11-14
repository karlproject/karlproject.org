==============================
Notify Former Staff Moderators
==============================

Let moderators know when someone leaves OSI.

.. note::

  This specification presumes the implementation of "Remove Former
  Staff from Communities".  That is, we wouldn't send out an email if
  the person wasn't actually removed.

Product Backlog Description
===========================

As a moderator of a community, I receive an email notification when a
member of my community was automatically removed because they are no
longer staff.  The email contains a link to re-add the user to the
community if the user is still active.

Specification
=============

#. The admin_edit_profile.html view will gain a new form field.  This
   will be a radio box that says::

     Email Moderators on Former Staff

     [X] No action
     [ ] Remove user from all communities and notify moderators
     [ ] Remove user from all communities, without notifying 
         moderators

#. It is a validation error to select options two or three if the
   KarlStaff group is still selected.

#. This field appears just below the group assignments.

#. If this is checked *and* the status of the user changed from having
   KarlStaff to no longer having KarlStaff, then an email is sent.

#. The email goes to all the moderators of all the communities that
   the person is a member of.  However, no moderator will receive
   multiple emails.  Make a unique list of moderators and only send
   them one email.

#. This same email is sent in the case that a user's KarlStaff was
   removed via a GSA sync.

#. The email has the following text::

     From: [normal KARL from address]
     Subject: Notice that [person name] is now former staff

     You are a moderator of one or more KARL communities in which
     [person name] was a member.  This person recently changed from
     OSI Staff to former staff status.  No action is required by you
     unless you would like re-add [person name] to your community.  To
     add [person name] click here [link to re-add].
