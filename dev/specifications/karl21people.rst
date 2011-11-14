========================================
KARL 2.1 People Directory Specifications
========================================

The People tab in KARL 2.1 needs to be reworked to remove OSI specific
code.  This specification intends to reuse the current functionality
of the People tab essentially removing some parts of the system.  The
new People tab should have the following features:

- When Staff look at the People tab, it will have 3 tabs inside of it:

  - Staff – Lists all users in the KarlStaff group (category_type =
    ‘entity’)

  - Affiliates – Lists all users in the KarlAffiliates group
    (category_type = ‘entity’)

  - All KARL – Lists all KARL users (i.e. both Staff and Affiliates)

- When an Affiliate clicks on the People tab, show only the All KARL
  subtab and only list users in the communities they are members of.
  Do not show any subtabs.

- Clicking on each tab in the people section will produce a tabular
  list of the people in the tab in alphabetical order similar to the
  current view when clicking on a department/entity

- The “Show Pictures” link should remain in place and functional

- The Search box in the people section will be removed in favor of
  using the live search box to find individual people

- The A-Z jump links will remain on each tabular and picture listing
  view of people

- The departmental information at the top of certain listings in KARL1
  will not be part of KARL2.1.
