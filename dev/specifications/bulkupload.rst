===========
Bulk Upload
===========

KARL users have long wished for a faster way to get many files from
their desktop into KARL.  Loading them one-at-a-time is quite
cumbersome.  The traditional alternatives required Flash or Java.

We propose to give power users an *optional* mechanism of uploading
files which, though impractical under IE, is still possible under
other browsers.  For some, the pain of uploading one-at-a-time is
higher than the pain of using a non-traditional browser.

Proposal
========

- Only consider this an *optional* extension of how KARL works.  Since
  it won't work in IE, we can't make this a front-and-center feature.

- Have an area in a folder view that implements the HTML5
  drag-and-drop specification for local files.

- Hook the uploading process to Javascript so we can control features
  in the upload process

Specification
=============

- Target Firefox 3.6 and possibly Safari and Chrome

- If you have the target browser, on View Folder you get a new menu
  action of "Upload"

- Clicking on this brings up an Upload Files form

- Allow tags and security settings to be applied to the group of files
  when uploaded

- Present some explanation and a big area that says "Drag and drop
  files into this box"

- When files are dropped, analyze them to see if any are too big for the policy

- If an upload fails, put a red message under the entry for that file

- If a new drag group comes in *after* all the files are uploaded,
  replace the drag box.  Otherwise, do not allow dropping until all
  existing files are uploaded.

- If possible, show mini-icons for file types such as PDF

- Provide a way to cancel a pending or in progress upload, as well as
  all uploads

Out of Scope
============

- Under this initial work, only folders will have this drag-and-drop
  file upload ability.

- Later, once we get more interest, we consider the right way to weave
  it more fully into the UI, possibly for other uses (blog
  attachments, wikipage authoring with images)

- IE might be supported using Google Gears, but that is likely a worse
  alternative than using Firefox
