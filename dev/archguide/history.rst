==============================
History of KARL3 Architecture
==============================

KARL3 is a product of several iterations of architecture and the
lessons learned along the way.

Pre-KARL
==========

Before the KARL project was launched, OSI used Plone "out-of-the-box"
to do simple content management.  While largely successful, this usage
informed OSI's thinking process.  Primarily, they felt strongly that
the general-purpose Plone user experience, meant to cover a lot of
bases, was "too heavy".  Instead, they wanted a highly-custom user
experience, built for purpose, with control over every pixel.

KARL1
============

Since OSI was a heavy user of Windows technology internally, it was
natural for them to work with Enfold for a KARL that ran on Windows
and worked with Windows technologies (e.g. ActiveDirectory) where
appropriate.

Additionally, three key architectural decisions were made that had a
number of ramifications:

1) Enfold generally recommends not re-using the Plone ZPTs.  Since OSI
wanted complete control over the user experience, KARL planned to make
its own "screens" for all functionality.  As an attempt to do this in
a technology more familiar to a Windows shop (or other consultants),
XSLT was chosen for this.  In particular, XSLT transformations running
inside Enfold Proxy, outside of the Plone process.

2) It was felt that the scale of KARL required an alternative to
ZCatalog, with different features as well as performance.  Xapian was
chosen for indexing.

3) For the tagging features, the Tasty product was selected.  This was
a not-Plone application that used REST (via Ajax) as the tagging
system.

KARL2
================

For a number of business and technical reasons, the decision was made
to move off of Windows and onto a more general open source stack.
Additionally, since installation of KARL1 was a very challenging
process, creating a repeatable "buildout" was a high priority.

KARL2 didn't make many major changes to the architecture.  For
example, XSLT was still used, as was Xapian and Tasty.  However, KARL2
brought:

- WSGI application using repoze.plone

- Supervisor

- Postgresql for the Tasty database

- Export/import using generic setup

- buildout, with all sources and patches under version control

- ActiveDirectory replaced with Postgresql

- XSLT frontend written as WSGI middleware

