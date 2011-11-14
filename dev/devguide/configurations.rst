===================
KARL Configurations
===================

KARL3 was designed to promote configurations of KARL for each
organization that uses it.  With this approach, the configuration of
KARL is the entry point for ``paster serve``.  The configuration pulls
in each of the main KARL packages, but allows extending and overriding
any built-in behavior.

Stated differently, instead of having KARL be the entry point that
loads configurations, the configuration is the entry point which pulls
in any parts of KARL.

By default the ``src/osi`` package is the entry point for running
KARL.  Each organization will have a different package that has
customizations and extensions.

We now drive the installation with the osi package.  It dicates the
etc ini file that gets started, name of the zodb, etc.  More
importantly, its configure.zcml loads everything else, and thus, you
can override/add views, adapters, add subscribers, etc. in this
package.  Menuitems are driven by adapters and "position", so this
works also.

