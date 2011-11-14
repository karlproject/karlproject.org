================
People Directory
================

.. note::

  The earlier (February 2009) proposal for this is at
  :ref:`people-tab-label`.

KARL 3.0 had a ``karl.peopledir`` add-on that implemented OSI's use
cases with an eye towards GSA.  This add-on was a tremendous help in
exploring new ideas for the People tab in KARL, as well as ideas with
potential across all of KARL.

KARL 3.1 plans to have a People application in the KARL3 core.  This
application will use OSI's ``karl.peopledir`` as a starting point for
refactoring functionality into the KARL3 core.

Status
======

#. The partners are deployed with the core People system.

#. The trunk has an improved People system that can be reviewed for
   use by OSI as a replacement for ``karl.peopledir``.

#. Or, OSI can continue overriding the builtin People system with
   ``karl.peopledir``.

#. We also have a generic alternative to the OSI-specific sync system
   for GSA.

People vs. ``karl.peopledir``
=============================

How does the in-core People system compare to the features and
implementation of ``karl.peopledir``?  This section analyzes the
differences as a way of converging the two, possibly by implementing
more of the features that are missing.

Architecture
------------

#. The in-core People directory does not use faceted index. This was
   our primary concern (mentioned elsewhere).  It instead achieves a
   dynamic category system using keywords.  Performance and
   scalability are signicantly more manageable.

#. The GSA sync has been refactored into a generic sync system that
   can work for other partners.  The design has been changed; the
   master system is completely read-only regarding KARL and does not
   keep track of a per-client completion queue.  Instead, KARL asks
   for any records changed since the last time it completed an update.

   This has greatly simplified the code and made it more reliable,
   while making it simpler to gateway a foreign system such as GSA.
   We also can use the sync on the staging (we're doing this now) or
   development system without a duplicate pseudo-GSA at OSI.

#. An generic XML format for the GSA sync was created.  This format is
   more terse than the existing GSA format, but we support the
   existing one via a KARL-side transformation.

#. The configuration of reports (the subtabs in people) is now down in
   a configuration file stored in version control for each KARL
   partner.  This replaces the TTW report builder, with pros and cons
   mentioned below.

Missing
-------

#. *End-user Filtering*.  End-users have a facility for taking one of
   the reports and further filtering them using an Ajax-oriented
   drill-down interface, along with showing more/fewer columns in the
   resulting report.

   Our hypothesis is that this feature is used by very few end users
   and isn't worth the performance hit (this is a very slow operation)
   and complexity/maintenance burden.  If there are data showing that
   this is used, we can propose and implement alternative.

#. *Content Administrator Report Building*.  ``karl.peopledir`` allows
   new reports to be defined using just a web browser.  This web-based
   report builder used Ajax and the faceted index to assemble new
   reports.  Ultimately, the idea was that end users would assemble
   and save their own reports.

   We contend that this is a maintenance burden.  Some portions of
   this never worked in IE.  The Javascript needed for this was quite
   advanced and the load put on the server for the drill-down was
   heavy.  Months after launch, anecdotal evidence suggests that the
   content administrators don't use this GUI but instead go directly
   to the developers.

   The in-core system allows configurable reports defined per KARL
   partner.  But the reports are managed along with the software.
   Later, if a web-based GUI is needed, we can put a front end on this
   system or allow each partner to edit the configuration file in
   Subversion themselves.

#. Jason added the OpenSearch support to ``karl.peopledir`` as a first
   step to better understanding who wanted it.  Tom wanted to reflect
   before committing to it in the core.  We'll need to make that
   decision.

GSA Sync
--------

We need to document the protocol for the GSA sync as well as the XML
format for the payload.  For OSI, though, we are very close to having
this already work based on a prototype Ajo did.

We need to chat with Ajo about some final changes to the sync strategy
in his prototype to match what we plan to offer other partners:

#. Eliminate the "loaddata" option with its limit parameter and its
   updating of timestamps on the master.  All syncronization requests
   from KARL should be stateless and read-only.  The master should
   never have to maintain state about the server.

#. When loading all users on the very first request, instead of
   sending a date far in the past, we propose to just allow omitting
   the date parameter.  Leaving out the parameter should signify no
   constraint on filtering records by last update.

#. Thus, the very first request from an empty KARL would issue the
   following read-only URL to GSA (hostname changed for obscurity)::

    https://gsaserver.company.org/gsasynctest/default.aspx

#. Then, a few minutes later, we would send::

    https://gsaserver.company.org/gsasynctest/default.aspx?timestamp=<timestamp>

Transition Strategy
===================

We propose to do this migration during the holiday season, while the
stakes are lower.

#. Finalize approval of the plan.

#. Work with Ajo to have a completed, final sync running automatically
   on the staging server.

#. Make sure that changes made in GSA get updated on the staging server.

#. Have Nat verify that, from the end user perspective, all reports
   are duplicated correctly.

#. When staging appears to function correctly, do the update at a time
   that is convenient for Ajo.

Questions
---------

#. Users might have bookmarked the existing ``/people/layouts/osi``
   scheme.  Should we preserve that jargon in the migration or use
   redirects?

#. We need to work with Ajo to simplify the way KARL and GSA swap
   "last modified" values for the report.

Requirements
============

#. Ships with KARL3 as part of the "core".

#. Maintained by all developers in the KARL3 team (OSI, Agendaless,
   Shane/Chris, Balazs, etc.).

#. Fits in with the KARL3 project standards (testing, performance,
   architecture, bug filing, PM, etc.)

#. Plan around limited budget and schedule.

Jargon
======

- ``karl.peopledir`` is the add-on used by OSI in KARL 3.0.

- "People" is the name of the KARL3 component that will be the new
  people directory.  Similar to Tags, Profiles, Offices, etc.

- *Configuration* is the process of adapting "People" to a particular
  pilot or installation.  Quite possibly, this will be treated as
  software under version control, setup by an integrator.

- *Section* means one of many top-level ways to look at the
  directory. In ``karl.peopledir`` these are (for staff) "OSI",
  "Foundations", "Affiliates", "All KARL".

- *Report* is a listing of people in columns with certain extra
  options (filtering and pagination.)

- *GridTable* is the KARL3-core Ajax widget for showing paginated
  listings of content in a tabular fashion.

- *Table View*.  The report display type that uses the GridTable.

- *Picture View*.  The report display type that shows rows of 3
  "cards" containing pictures.

- *Column* is a piece of information shown in a GridTable.  Some
  columns are sortable, some aren't.

- *Field* is a piece of information stored on a profile,
   e.g. ``Department``.  Some fields are editable by users, some are
   not.  Some fields are used by People, some are not.

Must-Have Features
==================

#. *Configurable*.  There must be *some* scheme, even if it is via
   software overriding, to let one "pilot" have differences from
   another.  This scheme will overlap with
   :ref:`pilot-configuration-label`.

#. Define one ore more "Sections" as part of configuration.
   Definition should include order presented and what "role" (staff
   vs. affiliate) is allowed to see the section.

#. Each section can have an intermediate HTML page that organizes
   links to reports (e.g. "OSI" has groupings by department, etc.), or
   directly shows a report (e.g. "All KARL").

#. *Security*.  Obey specific security policies:

   - Some sections can be seen by staff, some by affiliates.  This
     setting should be "configurable".

   - Staff should see all users/profiles in a report's listing.

   - Affiliates only see profiles of people in a community that the
     requesting user is in.

#. *Filtering*.  Each report must provide filtering:

   - By first letter

#. *Columns*.  Just like Filters, there will be a defined set of
   profile attributes that can be displayed in the grid.  Some might
   be sortable, some might not.  The 3.1 pilots will help define this
   list.

#. *Pagination*.


Might-Have Features
===================

#. *Picture view*.  It isn't yet clear whether the pilots feel getting
   pictures uploaded is a success.  As such, this feature (which has a
   good bit of effort) might get de-prioritized if budget is limited.

#. *Organization addresses*.  OSI shows address information on some
   reports (e.g. Open Society Foundation for Albania).  It isn't clear
   whether the pilots want to maintain this extra information.

#. *Extra filters*.  We could provide filtering the results of a
   certain result in a number of ways:

   - Text box

   - A list of fields managed by the core, to be determined by the 3.1
     pilots.

#. *Handle text overflow*.

#. *Printable view*.

#. *Administrator-configurable metadata*.  OSI used a mechanism where
   administrators had a system (categories and facet indexing) to add
   extra fields and vocabularies for those fields.  We can discuss
   this during our 3.1 planning meeting in June.

#. *Administrator-configurable reports*.  OSI also had a mechanism
   where administrators could define reports at runtime.  We can
   discuss this during our 3.1 planning meeting in June.

#. *Custom profile fields*.  Both Eurasia and Oxfam were able to
   function with a shared set of profile fields.  If that is true,
   then we can defer the expensive work to allow each pilot to
   customize (add and remove) the fields on a profile and in People.

Out of Scope
============

#. *Download as CSV*.

#. Synchronizing with external applications or data.

