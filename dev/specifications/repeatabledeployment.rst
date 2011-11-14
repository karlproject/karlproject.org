Toward Repeatable Deployment of KARL3 Sites
===========================================

Current Status
--------------

We currently manage KARL-the-software in Subversion, using tags made
during (mostly weekly) release cycles to label the version released.
At time of writing, for instance, the latest release of the :mod:`karl`
package is ``3.30``, made during the release cycle on 2010-05-06.

The release cycle includes the following steps:

1. In the sandbox on the developer's machine, run all unit and functional
   tests.
   
2. Check / update the ``CHANGES.txt`` file.

3. Make a Subversion tag from the ``karl`` trunk.

Next, for each deployed customer:

1. In the developer's sandbox for the customer's "buildout" (including
   the customer's "customization package"), update the ``svn:externals``
   to pull in the tagged version of the ``karl`` package.  Re-run the
   buildout and the tests.

2. Commit changes to the buildout trunk.

Then, for each deployed customer's KARL3 site, update the staging instance:

1. On the staging box, update the SVN checkout to the "tip" of the trunk,
   reconciling any uncommitted changes.  There should normally be no such
   changes.  This step pulls in the new version of the ``karl`` package
   via the updated ``svn:externals``.

2. On the staging box, run the buildout "in-place".

3. Stop the staging database service (``bin/supervisorctl shutdown``).

4. Copy the customer's production database into the staging instance.

5. Restart the staging database service (``bin/supervisord``).

6. Run any "evolve" scripts to update the database.

7. Restart Apache.

8. Check that the site has come back up by logging in via the browser,
   checking for errors in the ``Admin`` application, etc.

9. Verify bug reports alleged to be closed by the ``karl`` changelog,
   closing them as ``fix released``.

10. Tag the customer's "buildout" with an appropriate tag.

Finally, for each customer's KARL3 site, update the production instance:

1. On the production box, verify that there are no uncommitted changes
   to ``etc-deploy``.  Compare and reconcile the ``etc-deploy`` SVN history
   to that of ``etc-staging``.

2. On the production box, ``svn switch`` the customer's "buildout" checkout
   to the tag made above, reconciling any uncommitted changes.  There should
   normally be no such changes.  This step pulls in the new version of the
   ``karl`` package via the updated ``svn:externals``.

3. On the production box, run the buildout "in-place".

4. Back up the production database.

5. Stop the production database service (``bin/supervisorctl shutdown``).

6. Run any "evolve" scripts to update the production database.

.. note::
   If the evolve step is known or expected to be impossible to run
   while users update the site, e.g. due to ``ConflictErrors``, put the
   production site into "maintenance mode" during this step.

7. Restart the production database service (``bin/supervisord``).

8. Restart Apache.

9. Check that the site has come back up by logging in via the browser,
   checking for errors in the ``Admin`` application, etc.


Issues and Risks
----------------

A number of problems and risks are built into the current process:

- There are a *lot* of manual steps here, most of which have to be done
  remotely and on boxes which have very high availability requirements,
  especially compared to developer sandboxes.

- We are not releasing source distributions of the ``karl`` package,
  but relying only on Subversion's tagging feature.  Leaving the
  checked-out versions in the staging or production environments subtly
  encourages making local, "quick fix" changes, and then committing them
  later.  Likewise, we do not do as good a job of release management as
  if we were packaging the software for use outside the current hosting
  environment.

- The customer buildouts are also purely based on Subversion, and have even
  less release management done:  e.g., they have no changelogs, and the
  step of making tags after testing on staging seems to be sometimes
  elided (there are fewer tags than in ``karl``).

- Updating Subversion checkouts "in-place" under a live production server
  might cause unexpected changes to the running server:  this scenario is
  perhaps unlikely given our current model for view / template registration.

- Running the buildout "in-place" while the production server is running
  can cause the server to crash (e.g., if buildout decides to rebuild
  the ``libxml2`` or ``libxslt`` shared libraries).

- Running the buildout "in-place" leaves us without a fall-back option
  if something goes wrong:  the environment cannot be changed "atomically".
  Even if the process completes successfully, it doesn't allow for rolling
  back to a prior version of the environment if some bug is discovered
  during testing.

- Bundling the ZEO server inside the same buildout as the application
  subjects it to many more frequent "update" cycles than necessary.  In
  addition, it makes doing centralized admin / backup of the various customer
  databases harder than necessary.

- The buildout currently uses an "accretive" index, containing every version
  of every package ever used to build any version of KARL3.  In addtion,
  the ``buildout.cfg`` does not "pin" any specific versions of packages.
  In combination, this means that no run of the buildout is "repeatable",
  except in cases where the index is known not to have changed.  For
  instance, once any new version of a package is released to the index,
  it is impossible for a developer to recreate exactly the software currently
  used in the production or staging environments.

- Running "evolve" scripts is currently very time consuming, and frequently
  causes conflict errors with human users, requiring downtime to get the
  script to complete.  In many cases, these conflicts are due to having
  the udpated content objects be reindexed in *all* indexes, even though
  only one attribute has been changed.


Proposed Changes
----------------


Improve ``karl`` Release Management
+++++++++++++++++++++++++++++++++++

Move from the current "accretive" index to creating "versioned" indexes
as part of making a release of ``karl``, releasing the ``karl`` package
itself as an egg into the corresponding index.  These indexes will ensure
that the software environment remains repeatable, even if new packages are
added to the "development" version.  As an exemplar, see:

    http://download.zope.org/Zope2/index/2.12.4/

Use `compoze <http://svn.repoze.org/compoze>`_ to manage these
versioned indexes against the common "pool" directory, which can remain
"accretive".


Improve Customer Software Release Management
++++++++++++++++++++++++++++++++++++++++++++

Begin doing normal release management of each customer's "customization"
package, noting the versions of ``karl`` and any other packages which are
not its dependencies.

This change may require maintaining a set of versioned indexes for each
customer.


Avoid "In-Place" Upgrades
+++++++++++++++++++++++++

Rather than updating on-disk software in place, or re-running a buildout,
treat each deployment as a new installation into a versioned subdirectory.
Use symlinks to make the switchover from version ``N-1`` to version ``N``
as atomic as possible.

.. note::
   The requirement to build ``libxml2`` and ``libxslt`` (and event ``lxml``)
   within the buildout adds significantly to the overhead of doing the
   build.  Consider using either the system libraries or shared copies of
   these dependencies in production.


Split the ZEO Server apart from the Application
+++++++++++++++++++++++++++++++++++++++++++++++

Changes to the underlying ZODB software used to run ZEO happen at a much
slower pace than changes to the application (on the order of once a year
rather than once or twice a month).  Centralizing the database server
processes for all application instances on a single box should make doing
maintenance and backups simpler, and removes the database from the set of
things which might be inadvertently "touched" during an upgrade.

Splitting the storage server out from the deployed application should also
ease experimenting with a solution like
`relstorage <http://pypi.python.org/pypi/RelStorage>`_.


Automate On-Demand Backup / Restore / Evolve
++++++++++++++++++++++++++++++++++++++++++++

Evolve scripts should *never* run against "live" data, nor even against
the only copy of the "live" data.  Instead, we should be following a procedure
something like:

- Take a full backup of the production database, including blobs.
- Put the production site into "read-only" mode
- Take an incremental backup of the production database.
- Restore into a new copy of the database.
- Run the evolve scripts on the restored copy.
- Restart the database server instance against the updated copy.
- Bring the application back online in "writable" mode.

This process should be as automated as possible.


Automate Rollout of Customer Software
+++++++++++++++++++++++++++++++++++++

Ideally, the developer doing the updates and tests of a customer's
customization package or configuration should be able to tag changes, push
the source distribution to the index, and then run a script which automates
laying down the updated software configuration on the staging server.


Write Smarter Evolve Scripts
++++++++++++++++++++++++++++

Rather and relying on the default, event-based catalog operations triggered
by subscribers to "modified" events for the content, each evolve script should
arrange to re-index content in only the indexes relevant to the changes it
makes.
