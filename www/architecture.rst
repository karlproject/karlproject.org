Architecture and Technologies
*****************************

The software stack in KARL reflects :doc:`history <background>` as a 
`Plone <http://www.plone.org/>`_ application, as well as the backgrounds of 
the team involved throughout development.

At a high level, the technology stack as of KARL 3.0 uses:

* **\*nix**. Linux, FreeBSD, and other flavors of Unix such as OS X are in use
  by the KARL developers. Linux is used for the current hosting of KARL3
  for OSI.
* **Python**. The `Python <http://python.org>`_ programming language is
  used for the implementation of KARL.
* **BFG**. Although much of the web framework used by KARL comes from a number
  of popular Python tools, `BFG <http://bfg.repoze.org>`_ is the web
  microframework that glues the application together.
* **ZODB object database**. Content is stored and searched using the object
  database from the `Zope <http://zope.org>`_ project, also used by Plone.

More detail is available on `dev.karlproject.org <http://dev.karlproject.org>`_ in 
the `architecture guide <http://dev.karlproject.org/devguide/architecture.html>`_.

Technologies
============

In development and deployment, KARL 3.0 uses a number of technologies from two
basic backgrounds: Python and Zope. KARL itself has very little "framework" or
architecture, which was certainly a design goal (KARL isn't a platform, it is
an end-user application.)

Python Technologies
-------------------

This group of technologies are used beyond the Zope/Plone/KARL community and
should be familiar to people familiar with basic Python web development.

* **WSGI** for generic Python web applications.
* **WebOb** for handling web requests and responses in a standard API.
* **Paste** to wire together application configurations in a simple,
  declarative format.
* **virtualenv** to give each deployment a reproducible, isolated Python
  environment.
* **Eggs** as the package distribution facility.
* **repoze.who** for generic authentication and goup handling.
* **Supervisor** to manage server processes.
* **TinyMCE** as a widely-used (beyond Python) browser-based editor.
* **jQuery and jQuery UI** as a widely-used (beyond Python) JavaScript
  framework for Ajax.
* **mod_wsgi** as one deployment choice for running KARL directly inside
  Apache.
* **nose** for a unit testing framework.
* **Twill** to give functional testing of web requests.

Zope Technologies
-----------------

Reflecting the project's background in Plone and Zope, a number of
battle-tested technologies were used from the world of Zope.

* **Interfaces** as a "type" system for objects and behavior.
* **Adapters** to provide pluggable customization points.
* **Utilities** to provide pluggable services across the system.
* **Traversal** to represent hierarchies in URLs as containment in the object
  system.
* **Views** to interact with web requests and return a response.
* **Events** to provide uniform actions on certain kinds of operations.
* **Security** as a very rich architecture for access control, including
  filtering of search results and other queries.
* **ZODB** (including ZEO, middleware transactions, and blobs) to store,
  retrieve, index, and query schemaless objects.
* **ZPT** as the templating language, via the Chameleon implementation.
* **Catalog** as an indexing and searching facility.
* **PAS** to manage information about users and groups.
* **ZCML** to allow customization points by different deployments of KARL.
* **buildout** to give repeatable, reliable installation and ongoing updating
  of the software.
