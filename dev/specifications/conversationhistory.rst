

Backlog ID: 18 (Est 8 hours)

Problem
===========

Bob adds a blog entry that generates an alert.  People start replying,
creating comments, and Sue makes a proposal regarding the topic being
discussed.  Steve agrees and emails a blog comment saying "Sounds
good."

The email alert only says "Sounds good".  For any other context,
people have to go back to the blog entry and read the discussion.
Some KARL users, though, communicate with KARL primarily via email and
this is less helpful.

We need the blog comment alerts to contain more information about the
discussion.

Constraints
=============

- Since Outlook/Exchange doesn't implement standards for "in reply
  to", we have never been able to support threading.  Thus, we can't
  know whether an incoming email is a reply to a particular comment or
  the original blog entry.  This means we can't show in the
  conversation history the particular item a comment was commenting
  on.

Specification
==============

- Has no effect on alert email text for original blog entry

- All extra information is provided below the "reply to" separator

- Show the full text, author information, and date of the original
  blog entry, as well as the same for the most recent 3 blog comments.

- If more than 3 comments exist, show a note that X comments are not
  shown in the email with a link to view all comments

- Order the comments in descending order followed by the notice that X
  comments are not shown (if needed) then by the original blog entry
  text
