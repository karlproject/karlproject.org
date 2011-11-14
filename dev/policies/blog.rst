==============
Policies: Blog
==============

UI policies for the Blog tool in a community.


.. _show-blog-policies:

Show Blog
=========

- For all screens inside the blog tool, the bottom portlet on the
  right is the :ref:`blog-archive-portlet-policies` rather than the
  :ref:`active-people-portlet-policies`.

- If you are a member of the community, you will see one action: Add
  Blog Entry

- Nobody else sees any actions

- List most recent 20 blog entries, sorted in reverse descending order
  on date "posted" (which means creation date)

- Only show blog entries someone is allowed to see

- Each blog entry should show: 

  - Blog entry title as link to that blog entry, with the privacy
    badge

  - A "long-format" date

  - The "description" of the blog entry, conforming to the rules for
    :ref:`description-extraction-policies`.

  - The full name of the poster, as a hyperlink to the profile

  - If there are no comments, a link saying "Add a Comment" that goes
    to the blogentry/#addcomment URL.

  - If there is one comment, say "1 Comment" as a hyperlink to the
    blogentry#comments block.  If there are multiple comments, say "3
    Comments" with the same hyperlink.

- The "pagination box" simply displays ``Earlier posts >>`` or ``Later
  posts <<`` as needed.  No counts or anything.

- Put the RSS/Atom icon at the bottom to allow subscribing to an Atom
  feed for that tool

- Put the mail icon which has a
  ``mailto:communityid+blog@systemdomain`` as the hyperlink.

- A horizontal ruled line between entries


.. _add-blogentry-policies:

Add Blog Entry
==============

- Fields

  - Title (required)

  - Text field

  - Attachments

  - Tag box to allow tagging during adding

  - Is Private

  - Send alert

- Handle international character sets in title and text


- The first "block" in the text becomes the "description" per the
  :ref:`description-extraction-policies`.

- Attachments allows one or more files to be attached to a blog entry.
  You can remove an attachment from the add blogentry form before
  submitting.

- The attached files are stored inside the blog entry and are deleted
  if the blog entry is deleted.

- The content of an attached file is indexed (using same rules as a
  File object).  Matching on a word in the attachment shows a
  searchresult that goes to View Attachment.  The attachment has a
  "title" that matches the resource it is attached to and that is the
  title that shows up in searchresults.

- The "Is Private" field obeys the policies in
  :ref:`is-private-field-policies`.

- The "Send alert" field obeys the policies in
  :ref:`send-alert-field-policies`.

- Total upload size capped at 5 Mb (which is a configurable setting).
  Exceeding that results in an error message.

- Words in either title or text show up in LiveSearch and search
  results in accordance with security rules

- Generates an email alert using the alert policies

- Updates the "ACTIVE PEOPLE" portlet and recent items box

- A validation failure (namely, failing to provide a Title)

- Providing a blog entry Title that matches an existing blog entry
  results in a existing-1 URL.

- After successful post, you are sent to the View Blog Entry view for
  the new blog entry.

- Blog entries show up in LiveSearch in the Posts grouping, under the
  terms of the security policy.

- Attached piece of content title should be the file name.  Getting to
  the content should have bread crumbs associating it with a
  community, blog post, etc.  See :ref:`view-attachment-policies` for
  more details.

- Since upload size is customizable, we want to test at 5 MB and 10
  MB.

.. _email-blogentry-policies:

Email Blog Entry
================

- Blog entries can be created by sending an email to
  communityid+blog@systemname

- They can also be created by email to communityid@systemname (since
  the blog tool is configured as the default tool.)

- The title comes from the email subject

- The email address of the sender maps to the creator of the blog
  entry

- Only email addresses matching someone in the community result in
  creation of blog entry

- The body of the email is converted using Markdown text->email
  conventions

- Email attachments become blog entry attachments.  The email is
  bounced if the attachments are greater than the upload limit
  setting.

- Spam, out of office vactions messages, etc. are all enforced in the
  mail server, not in KARL.  (More work might be done after the basic
  port is completed.)


.. _blogentry-alert-policies:

Blog Entry Alert
================

- Adding or editing a blog entry sends an email alert in accordance
  with the :ref:`sending-alert-policies`

- The "from" address looks like: ``Some Person | System Name
  <community-name+blog-entryiuid@system.email>``

- The "to" address looks like::

    Community name <community@karl.soros.org>

- The "reply to" looks like::

    community name <whatever uid convention>

  This is important because users need to know they are responding to
  community, not the sender of the message.

.. note::

   If we run into users who need to whitelist a stable address for
   mail originating from KARL, then the 'Reply-To:' header will allow
   us to get mail-in replies directed to the correct address.

- The subject matches the generic policies

- The HTML body (there is no text-only version) contains:

  - "A new [Blog Entry] has been posted by Person Name in the
    Community Title community", where [Blog Entry] is a hyperlink to
    the blog entry.

  - A line of dashes

  - The literal text::

    --- Reply ABOVE THIS LINE to post a comment

    We use this to remove the quoted text when saving replies per
    :ref:`email-text-scrubbing-policies`

  - The text body of the email

  - Another short line of dashes then the footer, per the generic
    policies

  - Hyperlinks to each of the file attachments, if any


.. _show-blogentry-policies:

Show Blog Entry
===============

- Show the :ref:`screen-title-policies`

- Also show the creator's name as link to profile and the *modified*
  date/time in long format

- List the attachments by filename with an icon and a hyperlink

- If you are the creator, you see the Edit and Delete actions

- Display whether email alerts are turned on for the blog entry

- Show the tagbox for the blog entry

- Show the text content, if any

- If there are no comments yet:

  - Show the Add Comment box, which has the heading, help text,
    editor, attachments field, and submit/cancel button

  - Anybody that is allowed to see the blog entry is allowed to
    comment, whether they are in the community or not

- If there are comments, show the comments listing:

  - A "Comments" heading with an "Add Comment" jumplink floated right

  - The profile picture, link to profile for the commentor, date
    comment was last modified, and body of the comment

  - A menuitem floated right that says "quote".  Clicking this: jumps
    to the #addcomment box and puts the text of comment into the add
    comment box at the cursor position, styled as a reply.

  - If you are the creator of the comment (or a KARL administrator),
    show "edit" and "delete" links on the comment

  - If there are attachments to the comment, list them horizontally
    under the text as icon then filename as hyperlink.  For each,
    provide a permalink to the View File screen for that attachment.

- New comments are indexed and show up in search results with the
  title of the blog entry they commented on and a URL that goes to
  viewing the comment by itself.

- Typing text into the Add Comment box and clicking ``submit`` saves
  the comment, returning to the current screen with the comment added
  and a message in the :ref:`status-box-policies`.

- Words in the text of a blog comment show up in search results.  In
  LiveSearch, the comment shows up in the "Posts" grouping with a
  title of the original blog entry and a URL that goes to the comment
  itself.

- The first "block" in the text becomes the "description" per the
  :ref:`description-extraction-policies`.

.. _blogcomment-alert-policies:

Blog Comment Alert
==================

- Commenting on a blog entry, either with a web browser or by replying
  to an email, generates an alert email

- The email alert is sent in accordance with the
  :ref:`sending-alert-policies`

- The "from", "to", and "reply to" is the same as a
  :ref:`blogentry-alert-policies` (meaning, the name of the commentor
  etc.)

- The "subject" is::

  [Community Title] Re: Blog entry title

- The HTML body (no text-only version) has:

  - A first line that has "A new [Blog Comment]" instead of "A new
    [Blog Entry]"

  - Everything else matches :ref:`blogentry-alert-policies`



.. _edit-blogentry-policies:

Edit Blog Entry
===============

- Only the creator of the blog entry (or an administrator) can edit a
  blog entry.  Other community members (including moderators) are not
  allowed to edit someone's blog entry.

- You can attach more attachments when editing, but not alter the
  existing list of attachments.


.. _delete-blogentry-policies:

Delete Blog Entry
==================

- Deletion is the same as all :ref:`delete-resource-policies`.


.. _email-blogcomment-policies:

Email Blog Comment
==================

- An email to africa-project+blog+5131343@karl.soros.org generates a
  blog comment on the appropriate blog entry

- When replying to an email containing a blog entry or another
  comment, the emailer might choose to quote existing text.  Use the
  same code KARL2 uses to ellide the quoted parts, per Jonathan and
  Jason.

- Other policies follow :ref:`email-blogentry-policies`


.. _show-blogcomment-policies:

Show Blog Comment
=================

- Follows the policies of :ref:`screen-title-policies` with a screen
  title set to the title of the original blog entry.

- If you were the creator of the blog entry, you also see actions of
  Edit and Delete

- There is a backlink to the original blog entry.

- Attachments are listed the same as in
  :ref:`show-blogentry-policies`.

- Show the same "byline" (posted by author on date) as
  :ref:`show-blogentry-policies`.


.. _edit-blogcomment-policies:

Edit Blog Comment
=================

- Changes to the title or text reflect in search results

- An edit also shows a new "Posted" with the date/time of the
  modification.


.. _delete-blogcomment-policies:

Delete Blog Comment
===================

- Deletion is the same as all :ref:`delete-resource-policies`.


.. _view-attachment-policies:

View Attachment
===============

- An attachment is actually the same as a CommunityFile, just not
  inside a CommunityFolder in the FILES tool.

- The attachment URLs in the show blog entry and show blog comment
  screens go directly to downloading the file.  Thus, also provide a
  URL to get to the View File screen via a ``#`` that serves as a
  permalink hyperlink.

- The creator of the attachment also see Edit and Delete actions on
  the attachment.

- Attached piece of content title should be the file name.  Getting to
  the content should have bread crumbs associating it with a
  community, blog post, etc.


.. _edit-attachment-policies:

Edit Attachment
===============

- Editing the attachment allows changing the file that is stored in
  the attachment.

- Doing so triggers no alerts or updates to the modification time of
  the blog entry or blog comment.  However, the index is updated for
  search results.


.. _delete-attachment-policies:

Delete Attachment
=================

- Deletion is the same as all :ref:`delete-resource-policies`.


.. _atom-blog-policies:

Atom Feed for Blog
==================

- Provide the 20 most recent blog entries and comments following the
  general :ref:`atom-feed-policies`.
