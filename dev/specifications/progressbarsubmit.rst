=================================
Progress Bar Submit Specification
=================================

In KARL2, we had a progress bar at the bottom of forms, such as add
community. This was introduced because, since KARL was so slow, people
were clicking submit multiple times. We wanted to both:

a. Let people know something was happening.

b. Prevent multiple clicks on submit.


Proposal
========

- Make KARL so fast that it never takes much time to add/edit something.

- Remove the code that has the progress bar.

- When the submit is clicked, make sure the form submit is disabled.

- Consider using ExtJS widgets, e.g.
  http://extjs.com/deploy/dev/examples/message-box/msg-box.html, to go
  into a modal dialog box mode.
