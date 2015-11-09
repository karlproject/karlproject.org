karl.peopledir
**************

Unreleased
----------

- ...

3.6 (2009-12-15)
----------------

- Updated sync_osi_staff to use refactored scripting helpers from core.

3.5 (2009-09-08
---------------

- Moved workflow over to repoze.workflow based system for script adds.

3.4 (2009-08-19)
----------------

- `LP #410442 <https://bugs.launchpad.net/karl3/+bug/410442>`_: trigger profile workflow when importing users.

3.3 (2009-08-04)
----------------

- Fix for `LP #399419 <https://bugs.launchpad.net/karl3/+bug/399419>`_: Change print and export csv view to use sort
  order from grid

- Changed the karl.peopledir package to use the new versioned static
  files view.

3.2.1 (2009-07-17)
------------------

- `LP #400743 <https://bugs.launchpad.net/karl3/+bug/400743>`_ - Fixed GSA sync

3.2 (2009-07-16)
----------------

- `LP #399336 <https://bugs.launchpad.net/karl3/+bug/399336>`_ - Provide OpenSearch view with full-text on OSI karl.peopledir

3.1 (2009-06-24)
----------------

- Moved profile change subscribers and the find_peopledirectory_catalog
  function to the KARL core.

- Updated ICatalogSearch registrations to match the KARL core.  (Stopped
  using multi-adaptation)

3.0 (2009-06-15)
----------------

- Just updated version number and tagging scheme.

osi-production-20090611 (2009-06-11)
------------------------------------

- No changes

osi-production-20090610 (2009-06-10)
------------------------------------

- Updated 'add_peopledir' subscriber to put minimal required keys into
  the faux WSGI environment.

- Fixed two sync issues:

  - Group delete was not working because it was adding the XML element
    object to the list instead of the group's title

  - Category Items were not removed from a profile if the category was
    no longer there

osi-production-20090608 (2009-06-08)
------------------------------------

- Switched to using a multi-adapter for footer (replaces hard-wired OSI
  branding).

osi-production-20090603 (2009-06-03)
------------------------------------

- No changes in this package.

osi-production-20090531 (2009-05-31)
------------------------------------

- Strip whitespace before checking for blank string in column value.

osi-production-20090528 (2009-05-28)
------------------------------------

- Initial version rolled out to replace KARL2.

