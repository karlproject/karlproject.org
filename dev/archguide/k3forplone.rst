==============================
KARL3 for Plone Developers
==============================

Over its architectural history, KARL went from 100% Plone
out-of-the-box, to using Plone-the-framework, and finally to using a
subset of Plone/Zope technologies in a Python-oriented web framework.

This document explains the KARL3 architecture to a Plone developer.

Big Picture
===========

Plone is a content management system built on a technology stack that
includes Zope (application server) and Python (programming language).
As an end-user product, Plone contains a lot of architecture and
policy for its target.  If you aren't doing content management, then
using the needed technology of Plone, without the unneeded technology
and unwanted policy, is an attractive proposition.

KARL3 does just this.  A small, high-performance, and forward-looking
set of the technologies in the Plone stack form the architecture for
KARL.  These technologies have been re-organized in a Python-friendly
context called "Repoze", with the following characteristics:

#) Very familiar to Zope developers.

#) But very familiar to the (much larger) Python community.

#) Simplicity: *Pay only for what you eat*.

#) Speed: *go as fast as possible while still actually doing
   something*.

#) Documentation: *Useful, accurate, and updated*.

#) Collaboration: *Culture of using and promoting non-Zope stuff*.

Building KARL on a lighter architecture gives a number of critical
benefits:

- Fast, fast, fast.

- Agile, allowing new features by non-wizards.

- Combine the mature community of Zope with the huge community of
  Python.


Composition
=============

A Plone developer would classically start with all of Plone then add
to it.  This means Zope2, Zope3 (via Five), CMF, ZPT, DTML,
Archetypes, Zope 3 interfaces, workflow, 2 flavors of security, etc.
Instead of the monolith, we start with Repoze components and only pay
for what we eat:

#) The *model* provides data, both in the ZODB and a relational
   database (Postgresql via SQLAlchemy.)

#) The *catalog* provides indexing and searching of fielded and
   full-text data via repoze.catalog (a port of Zope's cataloging.)

#) Web pages are provided by *views*, which are simple Python
   functions.

#) Many views use *templates* to generate HTML.  ZPT is our templating
   language, albeit with the far-faster Chameleon implementation.

#) To handle *forms* we integrated :mod:`FormEncode` with ZPT, using a
   tiny (under 30 lines) integration step that leverages
   :mod:`lxml.html`.

#) Many other goodies from Python and Zope, as explained below.


Technology Soup
===============

A competent Plone developer is also a competent Zope developer, and
competent Zope developers will find much that is familiar in KARL3.
Here is a partial list:

- Zope transactions via repoze.tm

- Zope virtual hosting via repoze.vhm

- Zope3 interfaces, adapters, events, subscribers

- buildout

- ZPT

- ZODB, ZEO, blobs

- ZCatalog

- ZCML (or Grok-style decorators via martian)

- PAS

- Graph-based traversal, e.g. object publishing

- KSS

- Security

At the same time, a modern Zope developer is, hopefully, ready to
re-join the Python mainstream.  KARL3 is friendly towards Python web
developers as well:

- WSGI and middleware

- Paste

- WebOb
 
- Eggs

- FormEncode

- lxml.html

- mod_wsgi

- TinyMCE

- supervisor

- repoze.who
