.. _glossary:

============================
Glossary
============================

.. glossary::

  Former Staff
    A process in which an employee at a KARL organization 
    leaves and transitions according to a policy.
  GSA
    *Global Staff Administrator*, an in-house application 
    at OSI for managing information about staff users across 
    applications.
  GSA Sync
    Periodic batch job that pulls an XML export from GSA 
    (or some similiar system) and update user accounts and 
    profiles in KARL.  
  Feeds
    Timeline-oriented view of all changes across all KARL.
  Actions Box
    A ``WebOb`` request object.
  Requesting User
    The user account of the person making the current request.
  Hosting Organization
    The organization that is running a particular KARL deployment, such
    as OSI.
  Root URL
    The part of the URL above `/communites`. For example,
    `https://karl.soros.org`.
  Home URL
    The place a certain user gets sent when clicking on the logo, the
    HOME link, or visiting karl.soros.org/. Staff users go to their
    office, others go to the communities page.
  Root Community URL
    The abbreviated URL for a community, e.g. /communities/africa. This
    is either the community overview screen or the default tool if
    something else has been assigned.
  Static URL
    The URL that goes to the statically-served CSS, images, and
    JavaScript. In production, this uses a versioning and caching
    scheme.
  Site Admin
    A role that is configures the site and performs certain privileged
    operations.
  FormEncode
    A Python-oriented `library <http://formencode.org/index.html>`_ for
    form validation and generation.
  KarlAdministrator
    A role/group that has broad permissions across all of KARL site.
    For example, this role can add offices and forums.  Possibly
    implemented as a "moderator" of the OSI "community".
  KarlStaff
    A group/role that connotes people legally employed by the hosting 
    organization.
