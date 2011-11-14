=========
MultiKARL
=========

Easier deployment of multiple tiers at different service levels.

Goals
=====

- TTW creation of new KARL sites

- Much lower ongoing costs for small-to-medium KARL sites

- Mechanism for upselling people from the :doc:`freekarl` into their
  own site.

Background
==========

As part of the KARL Sustainability Plan project, business plan and
marketing discussions have focused in on the need to quickly and
cheaply deploy lower-cost KARL sites (small-medium sized.)  During
this discussion there was analysis of the cost numbers of far for the
current operations: where are the costs for launching and maintaining
a KARL site.

In particular, the consensus has been that the imperative is to drive
the support costs way down. Getting a KARL going should be a TTW
("through-the-web", browser-based) operation rather than a system
administrator option.  It should be possible to get started with KARL
cheaply.

Then after that, caring for a KARL and upgrading a KARL needs to be
significantly cheaper.  It takes quite a bit at the moment to maintain
separate KARLs.

Two initiatives sprung from this:

- :doc:`freekarl` for allowing a low service level at no cost, for
  people to evaluate it and start spending money when making a
  commitment.

- :doc:`multikarl` to allow small and medium sized KARLs to be
  provisioned via a browser.

It is critical to be able to upsell people to a higher tier as their
level of organizational commitment deepens.  Thus we have companion
issues regarding user and content migration between sites:

- :doc:`identitymanagement` between FreeKARL and the various KARL
  sites.

- :doc:`exportimport` covers the need for KARL content to be dumped
  out of a MultiKARL in case of upsell to Large KARL.

Proposal
========

- Change the architecture of KARL to have KARL sites in the database
  under a common ``KarlRoot``.

- This ``KarlRoot`` allows system administrators to add/edit/archive
  KARL sites for new customers, as well as the FreeKARL site

- Content in each KARL is only visible to that KARL

Specification
=============

- A new KARL can be created using a web form.

- Many (if not all) current site configuration options can be
  administered via a browser.  Over time, expose more to configuration
  (e.g. workflows.)

- Many (if not all) site customizations currently being done in
  customization packages can be done via a browser.  For example,
  logo.

- Ability to upsell people from FreeKARL through various for-fee KARLs

- Base level offering has URL scheme that is shared,
  e.g. ``https://sites.karlnetwork.org/mykarl``.  

- For-fee option to put custom URL on the site,
  e.g. ``https://karl.my.org/``.

- Simple plugin system for add-ons.  See :doc:`pluginsystem` for
  detail.

- Sane approach to logging.  Need to allow SFU to see everything but
  KarlAdmin to only see their logging.

Implementation
==============

- Still all one big WSGI app.  Only the highest pricing tier can break
  off into their own database/process/server.

- Database root object is a ``KarlRoot`` containing multiple
  ``KarlSite`` objects.

- Custom router which isolates each ``KarlSite`` from a model
  perspective from the others.

- Configuration UI on the ``KarlRoot`` which lets an administrator
  add, edit, archive/delete KARL sites.

- Open question about partitioning of configuration information.  Some
  needs to be beyond the scope of the customer's ``KarlAdmin`` rights,
  such as usage limits.

- Each ``KarlSite`` might or might not be some special ZODB machinery,
  e.g. mount point or subtree, or something special for RelStorage.

- Lower-price tiers will not get a custom URL, they will be something
  like ``https://sites.karlproject.org/my-org/``.  Others might get
  some kind of wildcard DNS (``https://my-org.karlproject.org/``) or
  user-controlled domain (``https://karl.my-org.com/``).  To be
  determined.  No matter what, try as much as possible to avoid
  sysadmin intervention (restarting Apache, for example) in the
  provisioning of these sites.

- Each KARL retains control over its own set of users, except for the
  sysadmin users that exist at the ``KarlRoot`` level.  But as noted
  in :doc:`identitymanagement` we're going to need a way to have
  cross-KARL identity/authentication (though not authorization).

- Logging is in a specially-mounted RelStorage.  Log entries get
  smarter than current (to allow sorting, pagination, filtering) and
  security-aware (so KarlSysAdmin at the root can see anything.)

Phase One
=========

- Proof-of-concept running at SFU

- Depends on RelStorage

- KarlRoot with users that are KarlSysAdmin

- Add/edit/delete sites via a form

Phase Two
=========

- Production-ready but on limited basis

- Email-in works correctly

- Move configuration knobs into an admin screen and eliminate
  customization packages


Phase Three
===========

- Handle upsell for custom domain name

- Resource limits

- Cover some of the FreeKARL need by making it easy for Nat/Evan to
  make a crippled KARL site.



Phase Four
==========

- Handle upsell for export/import to a dedicated KARL

- Handle upsell by an KarlRoot admin option that converts a KarlSite
  to a bigger KARL.

- Make logging work


Phase Five
==========

- The complete vision for try-apply-buy.  Improve the admin screens
  and process of getting started to have a positive initial
  impression.

Phase 99
========

- Cross-site profiles and identities

