=============
Plugin System
=============

KARL's business planning is going in two divergent directions.  We
need to remove all software differences between smaller KARLs and make
it very easy to create and support lots of KARLs.  At the same time,
the business plan calls for promotion of "KARL-the-platform" with
well-defined consulting value-add that can be done for KARLs.

This document proposes a plugin system to cover both cases.

Background
==========

In KARL1, the application was built specifically for OSI.  There was
no provision for KARL sites that weren't OSI, and thus the software
itself contained OSI-specific information (e.g. the list of offices in
the footer.)

In KARL2, we made the first changes to identify the places where the
information need customizing.

KARL3 was developed for the idea that there would be many KARLs.  The
supposition was that most customers would want the freedom to change
anything or add anything.  For this, KARL was implemented using an
idea called "customization packages".  That is, each KARL customer was
a software package which pulled in KARL, thus allowing anything to be
overridden.

In practice, however, we have dissuaded new KARL customers from
exercising that freedom due to the costs.  Once they start changing
the software, QA has to retest their site on each production update.
As we sometimes do updates several times a month, the costs pile up
quickly.

Additionally, each thing they override or add has to be kept in sync
with ongoing changes in the KARL software.  As an example, perhaps a
KARL partner wants a custom profile form, to collect more information
or present things differently.  Later, OSI has the development team
make a change to the way profiles work.  The KARL partner has to pay
the development team to update the customization to fit the changes in
the core of KARL.

Finally, these customization packages make operations for KARL extra
work.  Each KARL site is a different package of software and
installation of the KARL core software.  Everything is repeated, over
and over.  Each production update means visiting all the islands of
KARL and doing an update.  :doc:`multikarl` aims to change that, but
in a way that means the current customization model will be lost.

As such, the KARL3 model of allowing very broad power in customization
packages needs to be replaced.

Goals
=====

- Allow most KARLs to run the exact same versions of core software.

- Identify places where functionality can be added or overridden by
  specific, isolated consulting software.

- Permit KARLs that can avail themselves of custom,
  "KARL-the-platform" add-ons.

- Foster a market for consulting value-add and revenue.

Caveat
======

First, to be clear, this is a challenging problem.  It is impossible
to predict all the different kinds of new things customer might want,
and then find the common abstractions to give a single, manageable
plugin architecture.  Even if you can, you then have to get it right
the first time, because once plugins are developed, they need a stable
API.

Proposal
========

- A plugin is a managed package of software targeted at a pre-defined
  plugpoint in KARL.

- Plugins are software that is loaded for all KARL sites in an
  appserver, but perhaps enabled/disabled using an admin screen.
  Hence "managed" in the previous bullet.

- The plugin system for hosted KARL is a walled garden.  That is, only
  plugins developed or reviewed by the development/hosting team are
  installed.

- On each update of either the core KARL software or any one plugin,
  all features of KARL and each plugin are re-tested.  This means the
  plugin system is an expensive capability to have.  Since a plugin
  can impact all KARL sites (even if disabled), the QA cost is
  centrally borne.

Examples
========

- New tool.

- Extra properties on the profile aka aspects.

- Alternate editor.

- User manual.

- Navigation menu.

- Portlet.

- Widget.

- Wikiform.

- Types.

- Reports.

Specification
=============

- Each plugin is a separate Python package with extra metadata

- Testing.


- Walled garden.  If we change the core or the plugin architecture, we
  can also go change all the plugins.  Also, since the plugin is
  running in our instance, quality-wise, we can't just allow any code.
