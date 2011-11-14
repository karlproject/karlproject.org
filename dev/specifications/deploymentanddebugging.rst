========================
Deployment and Debugging
========================

In KARL1 (and to a degree, KARL2), when something went wrong, we had
obscure outages and there wasn't much available for debugging.  KARL3
will already be vastly better, in that enormous chunks of troublesome
C/C++ code will be removed, along with the multiple process
architecture.

Still, there is room for discussing improvements in how KARL can be
deployed, maintained, and debugged.

Notes
=====

- Nice error page that covers any possible condition

- Autolance for as much as possible

- Easy way to switch to a configuration that collects massive amounts
  of postmortem droppings

- Emails for tracebacks and crashes, sent to osi-dev

- Documented scripts for fast backups and restores, as well as
  reindex.  Note that blob support helps.

- Put catalog in a different ZODB.

- Make either a deployment buildout, or a different etc for the
  deployment.

- Turn off Chameleon reload sniffer

- Consider returning to separate hostname for static resources, for
  parallelization of HTTP requests

- Look at Scotch for recording WSGI requests in production and doing
  playback in staging

- Automating the pack process in a cron job

mod_wsgi
========

- Exit after N requests

- Stack/recursion limits

- Speed up restart with preimport (so a daemon child doesn't get
  requests until after some amount of work is done)

- Make it easy to fire up a parallel modwsgi in debug mode that
  doesn't interfere with public requests, perhaps read-only ZODB
  connection
