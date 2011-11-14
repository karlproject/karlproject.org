==================
KARL3 Architecture
==================

Overview of proposed/implemented architecture decisions for KARL3.

Versioning
===========

- No plans to do a "framework". Most likely built directly into the
  content resources.

Forms
=====

We currently use :term:`FormEncode` and `repoze.monty`.

mod_wsgi
==========

- KARL2 has Apache <-> FE http <-> BE http

- Ditto for tagging, going to TG

- We propose running under Apache, in daemon mode

- We specifically hope to allow clean process restart with no dropped
  requests

Tagging
=============

- IIOBTree

- Community tags are treated as another user.  Tagging a resource in a
  community updates the community user for that community.

Miscellaneous
=================

- KARL3 should restart in under 5 seconds, with initial page load in
  under 200% the time of second page load

- BLOB support, with the indexer able to talk directly to the blob
  (means single machine or NFS limitation on deployment)

