.. _pilot-configuration-label:

===================
Pilot Configuration
===================

The "pilots" configured KARL2 in both expected and unexpected ways.
We need to identify the configuration points, propose an approach for
configuration, and get this implemented for KARL 3.1.

This document identifies two terms:

- *Configuration* refers to a change for a KARL site that was
   predicted by the software.  For example, KARL3 allows site
   administrators to add new offices and edit address information on
   existing offices.

- *Customization* refers to a change to the software itself, made
   through a consulting effort by a developer.  KARL3 allows most
   customization to be done without editing the actual source files,
   although the developer is responsible for merging future changes
   and bug fixes back into the customization.

In this specification, we start by surveying the configuration and
customization made by two pilots (E and O).  We then propose a
solution for how to do configuration.

.. note::

  The earlier (February 2009) proposal for this is at
  :ref:`site-configuration-spec-label`.

Existing KARL 3.0 Configuration
===============================

Here is a listing of all "knobs" that are possible in KARL3, no matter
whether they should be pilot-visible or basic system setup.

Directly in ``run.py``
----------------------

- *system_name*.  Pilot E wanted to make the name "KARL"
  parameterizable.  This variable defines the name of the system for
  various strings visible in the web and email UI.  Note that coverage
  for this is incomplete.

- *system_email_domain*.  The right-hand-side of the ``From:`` in
  emails that go out from KARL, as well as the email icon link on the
  Blog tool.

- *upload_limit*.  Set a limit on bytes that can be uploaded via a web
  form (and possibly, email.)  For migration, OSI chose to set this to
  zero (no limit), but indicated last week a desire to institute a
  limit.  (See note below on file upload limits.)

- *people_path*.  URL segment that should be used for various links to
  the people directory.

- *min_pw_length*.  Minimum password length.

- *admin_email*.  Email address used on ``From:`` messages and other
  places where contacting the Administrators is needed.

- *staff_change_password_url*.  This is an OSI-ism.  The clickpath for
  changing your password is different if you are KarlStaff vs. not
  KarlStaff (affiliate).

``configuration/office_data.py``
--------------------------------

This file contains bootstrapping information written into the ZODB
regarding office configuration.  All data is actually managed TTW.
This file exists primarily because there isn't a GenericSetup for
KARL.

.. note::

  We currently use KarlAdmin for intranet/office admin.  We probably
  need to invent a new core-supported group, so sites don't have to
  give these people uber powers.

- *List of forums*.  KarlAdmin can do this now TTW.  Forums can exist
  either at ``/offices/forums`` or in a particular intranet/office.
  There is a ``FORUMS`` community tool that provides an admin UI for
  adding and removing forums.  Also, there is an extra view that
  provides the recursive listing of forums, grouped by office.

- *Navmenu*.  The blob of HTML that is the left column in the
  intranet/office layout.  Administered for a particular
  intranet/office by editing the intranet/office (go to ``/offices``,
  choose the ``INTRANETS`` tool, and edit the intranet/office.)

- *Middle portlets*.  In the intranet/office layout, the middle column
  is the "voice of the organiztion".  Ideally this would be admin'd at
  the ``/offices`` level, to avoid duplicaton and extra work.
  However, we do this on each intranet/office, as we weren't convinced
  every "intranet" would want the same middle column.

- *Intranet/Office address*.  Done on the edit screen for the
  "intranet" (office).

- *Terms and conditions*.  A pointer to initial text for the piece of
  content (admin'd at the ``/offices/files`` level) that is displayed
  on Accept Invitation screens as a popup dialog.

- *Privacy statement*.  Ditto for the privacy statement.

``configuration/vocabularies``
------------------------------

The only useful content here is a mapping of country code to country
name.  This then (ridculously) gets assigned to ``site.vocabularies``
and from there, lots of fossils litter the site.  For example, there
is a helper method in ``karl.utils.find_vocabularies`` that abstracts
the abstraction. (gag)

``etc/osi-deploy.ini``
----------------------

- *Urchin*.  Per-site knobs for Google Analytics injection.

All other knobs in this file are low-level enough to not need customer
visibility.

File Upload Limits
------------------

In KARL2, largely through oversight, there was no limit placed on the
size of a file that could be uploaded.  Once community had a 250 Mb
file.

When this was discovered during migration, we decided at the time to
put in a configurable limit, but for the migration, don't enforce it.
We didn't want people to blame the migration for unusual errors.

Last week it was decided to put the limit back in place.  We'll do so
for KARL 3.1.

There are in fact 3 kinds of limits:

#. *In-KARL*.  The code itself can enforce a limit and provide a
   helpful error, for example, graceful form validation.  I believe
   the number chosen was 20 Megabytes.

#. *In-Apache*.  Rather than hand KARL a 1 GB file and watch it croak
   trying to give a nice error message, we can put a limit that Apache
   will enforce.  For example, 100 Megabytes.  People hitting this
   limit will see an error message, but it will look like Apache.

#. *In-Postfix*.  For email in, it probably makes sense to have the
   email server bounce emails that exceed a certain limit.  This
   provides a nicer error message than dropping it later.  Perhaps 20
   Megabytes for this as well.


KARL 2.1 Configuration and Customization
========================================

Pilot E
-------

- *Custom CSS file*.  Both pilots had customizations to CSS that
  loaded highest in the priority chain.

- *Logo information*. Provide different markup pointing at different
  logo information, both for the top left and bottom left logo
  positions. (LP #318022)

- *Forums per office*.  Can now be satisfied with KARL3 TTW options.

- *Office address information and left-hand navigation*.  Ditto.

- *URL and heading for RSS/Atom feed on offices home page*.  Ditto.

- *Removed events from right column on offices*. Ditto.

- *Formatting of left column*.  Ditto.

- Make sure the word KARL from ever appearing (LP #319744).  Discussed
  above.

- (Wish) Change private community to public community

- (Wish) Let site admins see the action to delete a community

- (Wish) More profile fields, e.g. Skype name


Pilot O
-------

- *Double logo at top and other places*.  Can be handled same as Pilot
  E above.

- *Hide Pilot S's profile fields*.  Can be done just as in KARL3, with
  a custom CSS that makes ``display:none`` for certain fields in
  certain cases.  Not ideal, but ideal can wait for after 3.1 and have
  a proper facility for configuring profile fields per "pilot".

- *Copyright text in footer*.  Pretty straightforward request.

- *T&C etc.* (LP #387234).  Change wording on "Terms and Conditions"
  to "Terms of Service", and hide field that requires accepting
  privacy policy.

- *Hide "Add to Outlook" link*.  This was for 2 reasons: (a) it was
  broken and (b) they use Notes instead of Outlook.  They would like
  to have such a link work, but might require other thinking.
  Minimum: ensure there is enough styling to disable it in an
  ``oxfam.css`` custom css file.

- (Wish) Make sure contact/legal/help pages and links are customizable
  on text and link location.  For example, a privacy statement
  maintained outside of KARL.

- (Wish) What does it mean to not have offices?  Should this be an
  optional install?  Does it break anything for a "staff" user to not
  have an office?  We should ensure that this works ok.

- (Wish) Allow an admin to convert an affiliate to staff.

- (Wish) Don't allow affiliates as moderators or to create communities

Other
------

- Handle the forgot password, change password OSI customization

- Certain fields not editable by staff

- Handle out-of-office loops


Out of Scope
============

#. We will consider the idea that multiple KARLs might run in on
   instance to *no longer* be part of the KARL3 roadmap.  Thus,
   persisting configuration in the ZODB site root is no longer a
   requirement/guideline.
