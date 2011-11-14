==============================
Extra Profile Fields in KARL2
==============================

One of the pilot programs has requested a number of extra fields on
profiles.  This specification documents the agreement previously made,
then makes planning decisions based around this work.

Background
==========

One of the pilot programs has a specific need for 4 extra fields to be
on the profile:

1) Geography

2) Issues

3) Skills

4) Associated organizations

This information comes from a specification produced by them before
the process of considering KARL.

Analysis
========

Under this specification, those new fields would appear, possibly at
the bottom, of both the view profile and edit profile screens.  These
fields would appear for both staff and affiliate users.

When editing the fields, the following definitions are used:

#. Geography is a multiple-select drop-down list from a controlled
   vocabulary.

#. Issues is a multiple-select drop-down list from a controlled
   vocabulary.

#. Skills is a multiple-select drop-down list from a controlled
   vocabulary.

#. Associated organizations is a textarea, where each line contains a
   URL.  (Note: I'm not sure if this is what will ultimately be
   wanted, as you might want the name of the organization to appear in
   when viewing, rather than the URL.)

The information in each of these needs to become part of the
searchable text. Meaning, if "Advocacy" is a value selected for
Skills, then a search for Advocacy will result in a match on that
profile.  (Note that this doesn't come without a cost: it might
de-value other results that match on words in these standard
vocabularies.)

Once these values are provided on the edit profile screen, they should
appear on the view profile screen.  Multiple values will appear with
commas between the values.

Implementation
==============

To ease implementation costs and excessive work on the KARL2 codebase,
the specification proposes that all pilots get these four fields as
described herein.  That is, we are not making a facility in KARL2 that
allows per-pilot customization of the profile fields.

If it is necessary for some pilots to turn off some of the fields,
this can be done by editing the CSS file for each customer and setting
``display:none`` for those fields.  The hosting company would do this
as a customization charge and would be responsible for maintaining
those changes.

The values for the controlled vocabularies will appear in the
``src/karlfe/shared/siteconfig.xml``.  Same rules apply: if the
vocabulary values need to vary between pilot, they can make
arrangements with the hosting company for a customization.

Out of Scope
============

These extra profile fields have no effect on the system beyond the
points mentioned herein: they are listed on the View Profile screen,
editable on the Edit Profile screen, and contribute to the search
results.

As an example of an impact that is out of scope, the People tab will
not have any listings containing a column named Skills.

Beyond KARL2
============

This specification only covers a change for KARL 2.1.  It is
anticipated that KARL3 will provide a native facility that anticipates
this need.

