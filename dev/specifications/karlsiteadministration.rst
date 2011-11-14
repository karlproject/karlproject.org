========================
KARL Site Administration
========================

In KARL1 and KARL2, we had a series of facilities for administering
"configuration" information in KARL.  This proposal documents some of
these facilities and proposes and implementation in KARL3.

This proposal is motivated by discussions about "groupings" in KARL,
such as department, and how this maps into browsing the people
directory.

Summary
=======

- KARL3 will allow an ad-hoc group to be setup for security purposes,
  similar to the one known case where this has happened.

- KARL3 will allow Department address information to be shown when
  displaying people in a Department.  (Other facets beside Department,
  e.g. Language Spoken, can be done in the same way.)

- When the "Enhanced Communities Home Page" enhancement is approved
  after KARL 3.0, we will provide a way to list different kinds of
  communities, to enhance discoverability.

- Other enhancements that weren't present in KARL2 can be scheduled as
  part of the KARL enhancement process.


Background
==========

We need to provide a richer experience for navigating information
about People in KARL3.  We also need a way for administrators to
manage certain configuration information, a role held in KARL1 by AD
and in KARL2 by Global Site Administrator (GSA).

These goals are evaluated under the following givens:

1) The people directory effort is aimed for the KARL 3.0 timeframe.

2) Its only purpose is to serve needs inside KARL, not to serve other
organizational (e.g. HR Administration) requirements.

3) To keep the budget and schedule for delivering the non-people part
of KARL, it is expected that development outside of the People package
will be under 20-40 hours, whether by Agendaless or Balazs or OSI.

4) More specifically, the one part that is needed in the core is the
ability to do efficient searches based on department or some other
known-in-advance "facet".

5) Faceted navigation, stored searches, and the other features that
aren't present in KARL 3.0 will be done as part of the People package.
The core isn't expected to provide these services.

In KARL1, we had configuration information in several places.  The
Plone UI was used to upload a navigation menu.  Office addresses were
in an XML file in the frontend.  Other organizational information was
embedded directly into the XSLT.  Some groupings of information were
put into AD.

Also, in KARL1, we only had two "types" of groups: community and
office.  We were able to mimic other groups, as discussed below in use
cases below under "HR Folder".

In KARL2, some of this got consolidated.  Most configuration
information stored as content got moved to an XML file in Subversion.
AD was replaced with GSA.

In KARL3, we have a number of things at play:

- We are moving from 2 kinds of security groups to one.  That is,
  offices are now communities, albeit with a custom browsing
  experience.

- In the People directory, we would like some enhanced groupings.  For
  example, we would like to provide a list of known Departments, then
  show people in a certain Department.

- We can't expect customers to edit an XML configuration file stored
  in Subversion to do configuration.  We should keep the idea of
  administrator-oriented configuration, but provide an easier facility
  to manage the configuration.

Existing Use Cases
===================

The following are use cases that exist in KARL2.  As such, these
*must* be present, as opposed to new use cases that must be treated as
enhancements.

HR Folder
---------

In KARL1, we had an "HR Policies" folder in the intranet.  This was
like all the other folders, except it had a different list of people
that could edit and a different list that could view.  Meaning, a
custom security group.

This was not implemented in KARL per se, but instead, used systems
lower in the stack.  First, an entity was created in ActiveDirectory
called `HRDepartment`.  Usernames were then added into that entity,
thus defining a group.

Next, the synchnonization script was taught to mirror that entity into
a Zope-based "group".  Zope has a concept of ad-hoc groupings of
people.  Finally, the Zope Management Interface (ZMI) was used to give
that group certain security permissions on the intranet folder.

This was the only case of a custom security grouping in KARL, and this
ad-hoc solution worked.  Note that there was *no* concept of
"department".  Anybody from any department could be put into the
`HRDepartment` group.

In KARL2, this was done somewhat more seamlessly using GSA.  Instead
of going to a group and adding people, you could go to a person and
edit their Department field.  Behind the scenes, one or more groups
were updated, making it fundamentally the same as KARL1.

Offices
-------

KARL1 treated offices and communities as very different fish.  They
were different content types with different security concepts.  They
also relied on some (occassionally) fishy concepts of a "staff" role
and knowing what office someone was in.

Browse People by Communications Department
------------------------------------------

In KARL1 you could go to the People tab and find a link to list people
in the Communications department.  For some of the other links
(e.g. Open Society Foundation for Albania), you would see the people
in that entity, along with information about the entity (address,
phone, etc.)

The existence of "Communications Department" as an entity that should
be linked to was very much hardcoded (in the XSLT).  The other
information, though, was somewhat more coherently available:

- You could issue a query and get the people in the Communications
  Department because each person's profile was indexed by department.

- The information about Albania was available in the frontend.

However, the system never treated Department as a "group" from a
security perspective.

Vocabularies
------------

We had some drop-down menus that needed a constrained set of choices.
For example, the country you reside in shouldn't be a free text field.
You should choose from a set list.

We implemented this in KARL2 as part of configuration, meaning, this
went in an XML file on disk.

New Use Cases
=============

The following use cases are under discussion in this proposal, though
might be scheduled for implementation in different releases.

More Facets for Browsing People
-------------------------------

The facility for browsing people needs to provide a few more "facets"
(aka entities, aka groupings).  Some of these facets, e.g. Department,
might have extra information to display when you visit that facet
(just as Albania did.)  Each KARL site (e.g. OSI, Synergos) should be
able to add and remove Department values, along with the extra
information.

The ability to dynamically create new facets is complete R&D and thus
is listed under "out of scope" below.

List Communities by Facets
----------------------------

The proposed enhancement to the Communities home page didn't make the
schedule for KARL3 (files tool and dashboard beat it out.)  Thus, this
use case won't affect KARL3 planning.

People want to discover communities to participate in.  We need a
better communities home page that lists communities by different
criteria.  Analysis was provided for this before the December meeting,
listing the ways OSI identified that it wanted to list communities.

It is possible that communities might have, in addition to other
properties, a "type" that helps in this future organization work.


Proposal
========

The proposed solutions for these use cases are listed in subheadings
below.  Each adheres to the following desired objectives:

- Continue striving toward the goal of preventing the KARL core
  software and security model from being wired into organizational
  structure.

- Don't conflate two different things.  Collaboration in a community
  is different than administers configuring a site.  Different
  audiences with different goals.  We should avoid creating a
  community each time we need a grouping of people.  Instead,
  communities should be created when people need to collaborate on
  content.

- Continue treating the information previousy managed as
  configuration, as configuration.  Just make the management easier by
  providing a web-based UI.

- Stick to the least risky implementation of the use cases, as well as
  the least expensive. Respect the hard-earned wisdom we have bitterly
  accumulated over the years in KARL regarding broad scope.

We propose a KARL Site Adminstrator tool that takes the common
activities for configuring KARL and provides a web-based front-end:

- The KSA tool is for configuration, not content.

- It isn't super-easy lowest-common-denominator, as it is used
  infrequently by advanced users.

- It isn't a separate application.  It runs as part of the KARL
  application, and thus is written using Repoze.

- It is, though, a separate package that can be "plugged into" KARL.

- The KSA is solely about a finite set of configuration directives.
  It is decoupled from the KARL implementation to the extent possible.

- KARL Adminstrators, though, have the impression that it is part of
  KARL.

KARL3 HR Folder
---------------

Susan, a KARL Administrator at ICTJ, visits `karl.ictj.org/ksa` and
logs into the KARL Site Administrator tool.  They click on `Ad-hoc
Groups` and read the introduction that explains the screens.  Here
they can add/edit/remove ad-hoc groups.

An ad-hoc group is simply: A security group that isn't a community.

Susan clicks "add" and types `hrdepartment` as the identifier of the
group.  She also types `HR Department` as the title.  She then uses
some facilities to add users into that group.  (For example, a query
on users matching a facet.)

Later Susan might want to remove someone from that group.  She visits
the KSA, clicks on `Ad-Hoc Groups`, and chooses `HR Department` from
the list.  This allows her to remove one or more people.

Once this ad-hoc group is created, it can be used in the security
setting on a community or a resource in a community.  Bob has a File
that he would like to share only with people in HR.  He goes to a
folder in the ICTJ Staff community (office) and clicks `Add Folder`.
In the security field, he limits the Viewers by browsing the known
groups (communities and ad-hoc) and choosing `HR Department`.

Open Questions:

- What happens to content when you delete an ad-hoc group?

- What happens to a community or ad-hoc group when you delete a user?
  (Same issue for KARL1)

Browse People by Communications Department
------------------------------------------

Susan is told that a new Department was created at ICTJ called "Newest
Department".  She goes to `karl.ictj.org/ksa` and clicks on
`Departments`.  Here she sees a list of all known Departments.

She clicks `add department` and fills in the information about a
department.  This is a custom form that edits information stored in
the ZODB.  Whether this is an instance of a Department class, or
whether it just edits some string of XML representing all departments
(or all configuration) can be decoupled from the discussion.

She then clicks "Users" to add some newly-hired user accounts for
people in Newest Department.  For these new users, she edits the
Department value on the profile in the manner she would for an
existing department.

By editing the data on the profile, she updated the queries that drive
the People directory tab.  Thus, reporting on people in KARL is
nothing more than a traditional reporting application, driven
completely by the Profile (instead of trying to extend the security
model to allow reporting.)

Vocabularies
------------

Susan clicks on `Vocabularies`, chooses one of the known vocabularies,
edits, etc.  No facility to add a new vocabulary, as nothing in the
software could use it.

Out of Scope
=============

#. *Dynamic profile fields*.  This is a very hard problem, and our
   long experience as core developers of existing systems (Zope, CMF,
   Plone) has exposed us to the pitfalls and hidden surprises.  It
   *can* be done, and *is* useful, but is too risky to add to the
   gameplan so late in the 3.0 process.

#. *Group types*.  The use cases above catalog the known needs.  These
   needs can be met by simpler, cheaper, and less risky means than
   growing "richness" in the security model.  We have a long and
   dismal history with monkeying around with security in KARL.

#. *Non-KARL*.  Functionality and changes will only be considered for
   things that manifest themselves in KARL.  Non-KARL needs are not in
   scope.
