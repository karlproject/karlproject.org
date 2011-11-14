.. _site-configuration-spec-label:

================================
Site Configuration Specification
================================


In KARL2, configuration of the site is spread over many places inside
and outside of the system. Moreover, parts that should be configurable
are instead hard-wired.

This specification documents the KARL3 system for managing
specification. With this, different :term:`Hosting Organization` gets a
central console for their configuration activities.

Background
==========

There is quite a bit of configuration information used to get a KARL
site running. Some of this information is "server configuration" (port
number, number of thread, log level, etc.) However, there is also some
configuration that is part of the business requirements (list of
offices, address for each office, location of RSS feeds, etc.) We will
refer to this information as *site configuration*.

In KARL1, this site configuration was spread across different facilities
and was hard to locate and setup. Some was done TTW, some done in a
config.py file in the BE, some done in an XML file in the FE, some done
in Python code, and some even done hardwired in the code.

KARL2 attempted to reduce this somewhat, but also introduced INI files
as a possible source for configuration.

More importantly, the KARL2 cycle began the concept of "Hosted KARL",
where non-OSI :term:`Hosting Organization` folks might be running a
KARL. Thus, providing a coherent story for Site Configuration is even
more valuable in KARL3.

Requirements
============

- Balance the needs of a developer sandbox sometimes clash with the
  needs of building a deployable site. The former wants dummy data.

- Balance the desire to make configuration data part of the software,
  and thus placed under version control, versus part of the content.

- Ensure that site configuration migrates easily between updates to the
  software or building on a new machine.

- Must be ZEO friendly.

- Allow configuration by customer's :term:`Site Admin` without direct
  access to the login shell on the server.

- Like other information in the system, allow an export and import.

Configuration Data
==================

The following are some of the pieces of information that need to be
configurable.

#. Name for :term:`Hosting Organization`.

#. Upload and scale a logo.

#. Rich text for the Help, Contact, and Legal screens.

#. Rich text for the copyright line.

#. URL for the feeds in the network column of the office home pages.

#. Admin screen for managing KarlStaff accounts TTW.

#. Hostname and login information for IMAP and SMTP servers.

#. Initial supports for some reports providing analytics.

3.0 Work
========

- Write a separate application that administers the configuration data.

- Use `repoze.who` to integrate authentication for that application into
  the KARL authentication scheme.

- Leverage the Ajax framework (e.g. KSS/ExtJS) to maximum effect. For
  example, presume that the :term:`Site Admin` uses a browser that does
  JS, and don't provide a non-JS fallback.

- This app will talk directly to SQL for the user part, perhaps using an
  ORM. This means that we need a way to signal KARL when user data needs
  to be re-indexed.

- This app will talk directly to ZEO for all non-user data. We'll have
  an instance of a persistent class, non-catalogable, at the root of the
  ZODB.

- All this will be hidden from the view layer by a helper class that
  knows where the data is and makes it available for relevant templates.

- Allow a developer sandbox to run a "start_over" that fills in sample
  data.

- Rely on standard dump/repload for the user data and the ZODB data to
  survive a rebuild.

- Changing the id of a vocabulary item won't go fix existing data.  We
  thus should disallow changing the identifiers until we're ready to
  discuss doing work needed to do cleanup.

Further Work
============

Questions
=========

- The list of offices is problematic. Adding a new office is easy. But
  should we allow renaming or deleting an existing office?

- Should we revisit how forums are associated with an office? We
  certainly shouldn't use "name in the ID" conventions.

- 
