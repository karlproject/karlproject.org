======================
GSA Sync Specification
======================

OSI manages information about staff users across applications using an
in-house application called :term:`GSA`.  KARL has a periodic batch
process called :term:`GSA Sync` which pulls XML from GSA and updates
KARL.  This document specifies aspects of the protocol format.

Former Staff
============

When GSA makes a user "former staff", the next sync will contain a
sync item for that user (since it was modified since the previous
sync.)  The fact that the user is no longer staff, but instead is
"former staff", is connoted by the *absence* of the ``KarlStaff``
group as part of the XML.

Active Users
============

As part of :term:`Former Staff` process, OSI can make a user account
inactive.  This is connoted by an XML fragment such as:

.. code-block:: xml

  <inactive>1</inactive>

Unless that exact spelling is in the XML, the user is considered
active.  For example, *all* of the following mean the user is
*active*:

.. code-block:: xml

   <inactive>true</inactive>
   <inactive/>

The absence of ``<inactive>`` also implies the user is active.

.. _note:

  A user can *NOT* go from active to inactive to active etc. This is a
  one-way operation in the current implementation.

Incremental Sync
================

The batch job for GSA runs periodically, making a URL containing the
datetime of the most recent successful sync.  GSA then returns all
records that have been modified since that time.  If the sync
completes successfully, GSA Sync records the datetime of completion
and uses it for the next request.

To mimic a "full" sync, just choose a time very far in the past or
omit the parameter from the URL.
