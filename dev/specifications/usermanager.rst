============
User Manager
============

Jason provided a quick application to allow editing of staff (and
other) data, similar in spirit to GSA.  We need something in the core
performing the necessary functions.

The current decision is to have User Manager functionality woven into
regular screens of KARL.  Admins will see extra options.

Must-Have Features
==================

#. *Add/edit/delete users*.

#. *Add/edit user's groups*.  This also allows converting from
   affiliate to staff.


Might-Have Features
===================

#. *Staff vs. Affiliate reports*.

#. *Upload/download CSV*.

#. *Bulk email a message*.

#. *Bulk operations*.

#. *Add/edit/delete ad-hoc groups*.

#. Extra profile fields with constrained vocabularies

Out of Scope
============

#. *Sync*.  We won't provide an architecture or scripts for
   integrating with an internal user management system
   (e.g. ActiveDirectory or GSA).  Instead, we'll treat that as custom
   consulting for each pilot.

Implementation
==============

We will weave the necessary use cases into the KARL UI itself.  There
will not be a separate application that provides user management.
Instead, admins will find one or more users to manage by using the
facilities in the People Directory.  When viewing a profile, there
will be extra options for administration of users.

This will include the ability to add a new user.
