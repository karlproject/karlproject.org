
Backlog, June 2009 Meeting
==========================

2 - Reporting
-------------

- Try to capture statistics across KARLs in the "cluster"

- Only solving the near-term requirements for the KARL cluster

- First cut uses simple tools

  - Export script dumps to CSV

  - Another script rsync's data to the reporting server

  - Another script loads CSV data into RDBMS

  - Reporting server has a UI for reports

- No ad-hoc reports

- Reporting service tracks trends over time


3 - Add warning....
-------------------

- Only applies to "Folder" in the FILES tool

- Simply add to the confirmation screen an extra red warning label
  that says: "Warning: This folder contains 999 subitems"

- Put the actual number only if this is a cheap operation

4 - Upgrade TinyMCE
--------------------------

- Fix MS Word paste bug


5 - Spell Check
----------------

- Multiple languages if possible, but not required

- Try to use the Google API if possible

- If not, implement a "Spellcheck service" in the cluster that handles
  all the KARLs at sixfeetup.com.  This spellcheck service runs
  outside of KARL, and there is a knob that points at the URL for it.

- Disable the Firefox built-in spellchecker

- Out-of-scope: no per-user or per-site dictionaries

- Only for rich-text fields


6 - Allow renaming a wiki page
------------------------------

- Make the title field editable, with help text explaining that titles
  shouldn't be changed too often

- On save, detect if the title changed

- If it did, open all the wiki pages, find places that referenced the
  old title, and correct their link text

- Later, if this proves to be a popular operation in big wikis that
  make this a performance problem, throw machinery at the problem

7 - Add a "Back to Wiki" link
-----------------------------

- First, write a content cleanup script to see if anybody manually put
  a reference to the URL that is the top of the wiki.  Provide a
  report for which wikis have the backlink.

- Put in the backlink breadcrumb thingy


8 - Send email alert option on blog comments
---------------------------------------------

- Problem

  - Edit Blog Entry has a field for sending alerts

  - People don't realize this is persistent and inherited

  - They think it applies only to this editing action

- Alerts will never go out on edits of any kind of resource.  Users
  will not be presented with the option to send an alert.

- When adding a new blog entry, the choice to send an alert will not
  apply to subsequent comments (or edits).  Thus, the sendalert value
  does not need to be saved.

- For blog comments via a browser, there will now be an alert option
  for sending or not sending an alert when adding a comment.

- For blog comments via email, always sends alerts.


11 - People OpenSearch
----------------------

- Challenge is that the results need to be displayed in a report that
  has extra columns, in the peopledir tabular view

- Thus, reports have to be filterable by text in addition other
  criteria

- This will be done in karl.peopledir first, then (much) later putting
  into KARL 3.x

12 - Drop-down widget from "site actions"
-----------------------------------------

- A pull-down menu that says "My Communities" with a droplet icon

- Needs to handle long community names

- Needs to handle overflow, people with lots of communities


XX - Include tags in search ranking
-----------------------------------

- Does NOT mean tags show up in search results

- Instead, treat tag text as having heigher weight, just as we did for
  title.

- Include tag count as a multiplier.

- Colossal problem: tagging means reindexing possibly large blobs


13 - Reformat network events portlet long titles
------------------------------------------------

- In all places where events are displayed in a portlet

  - Stop using two columns

  - Put date in front, wrap link text full left

  - If needed, increase spacing between portlet entries


14 - Automatic picture resizing
-------------------------------

- No user-driven cropping

- Keep aspect ratio

- Essentially, do the thing that Plone does

- Store both the original and the resized version

- The original is never displayed, it is kept in case KARL sets a new
  standard on profile photo dimensions


15 - Add Extension column to People Directory
---------------------------------------------

- Not for KARL core


16 - Advanced view 
--------------------

- File a bug saying only KarlAdmin sees the action and can get to the
  view

