============
Basic Repoze
============

This first tutorial helps new KARL3 developers get started on KARL3
development with :mod:`repoze.bfg`.  For the most part, this tutorial
gets us oriented on the development environment and paves the way for
further development of a "FEEDS" tool for KARL communities.

Like the other tutorials, we will progress through a series of steps
on the way to completion.

This tutorial does not use the KARL buildout or KARL itself.  Rather,
it stays in the environment of a Repoze and ZODB basic application.

Scenario
========

This series of tutorials explains the technologies of KARL3 (Zope,
WSGI, Repoze) through the development of a "FEEDS" tool for KARL3.
That is, a new tab that can appear on a community where external Atom
feeds can be subscribed to.

The scope of the FEED tool's features is fairly limited.  However, it
provides a good opportunity to cover many of the technologies in
KARL3.  Our tutorial should produce a tool with the following
features:

- A root object that can hold one or more feeds

- A facility to add a new feed and see it appear in the listing of
  known feeds

- View the contents of a feed

- Retrieve the remote Atom feed and process each feed entry into a
  persistent item in the folder for the feed

Objectives
==========

#. Make an environment for productive Repoze development.

#. Cover initial technologies in Repoze: virtualenv, Paster, ZODB, ZPT
   and macros, etc.

Sections
========

.. toctree::
	:maxdepth: 2

	preparation
	feedslayout
	formspersistence
