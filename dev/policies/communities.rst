=====================
Policies: Communities
=====================

Policies related to screens that have community functionality *outside*
of the core community tools (blog, etc.)

.. _list-communities-policies:

List Communities
================

This is the screen you get when you click on the Communities tab.

- Show a :ref:`screen-title-policies` of "Communities", actions box
  with "Add Community" if the :term:`Requesting User` is KarlStaff

- Under the screen title, show a :ref:`letter-box-policies` that
  filters the display by matching community titles starting with that
  letter.

- Give a listing of the first 20 communities meeting the current
  criteria (e.g. letter link).

- KarlStaff can see all public communities plus private communities
  which they are a member of

- KarlAffiliate can only see communities they are in

- The listing of each community should show:

  - The community title, as a hyperlink to the community, plus a privacy
    badge

  - The full textual description of the community, with no ellipsis

  - If the person is somehow not able to see any communities for the
    filtering, display a "No items for this community selection."

  - Optionally, show also the number of members in the community and the
    last update. These were in KARL1 but removed for performance
    reasons, making this feature desired, but not mandatory.

- Below the first 20 item batch of listings, a
  :ref:`pagination-box-policies` allows pagination

- If the :term:`Requesting User` is in any communities, display them in
  a right-floated "My Communities" box

  - Sorted list of communities

  - Each title is a hyperlink to the community


.. _add-community-policies:

Add Community
=============

A form for adding a community to KARL.

- Only KarlStaff should be able to get to this screen and post to this
  screen.

- Required fields get marked with a red box

- Fields

  - Title, required, input box

  - Tag box should appear just under the title to allow adding tags on
    the add community screen

  - Description, required, 100-word textarea

  - Overview, optional, editor

  - Is Private, radio, default to "public"

  - List of tools for the community

  - Submit and Cancel buttons.  Latter goes to
    :ref:`list-communities-policies`

- Successfully creating a community goes to
  :ref:`add-existing-users-policies`

- The description field shows up in search results

- Validation errors if:

  - Required fields are not supplied

  - Generated name/id matches something already in use

  - No tools are selected


.. _show-community-policies:

Show Community
==============

Display a home page for a community.

- If Overview is not the default "tool", then ``/communities/myplace``
  redirects to the chosen tool.

- If the community is private, say so with the privacy badge

- Show tabs for each of the tools the community was configured with

- Show a tagbox for tagging the community

- A TAGS portlet shows tags in the community, top five sorted in
  reverse order

- An ACTIVE PEOPLE portlet shows the most recently changed content
  that the requesting user is allowed to see

- A Recent Activity box on the overview shows the 20 most recently
  added/modified resources, sorted in reverse.  If more than 20, show
  a link to Recent Activity.

- Links to Members, Tags (for community tags), an RSS icon, and a
  search box for seaching within the community


.. _edit-community-policies:

Edit Community
==============

- Tag box should appear just under the title to allow adding tags on
  the edit community screen

- Changing the title does not change the ID in the URL

- An option to choose the default tool

- Make sure people don't accidentally remove a tool with content in
  it.  How to do this is an ongoing discussion.

.. _show-members-policies:

Show Members
============

- Members can get to this view in a private or public community.

- Non-members can get to this view in a public community but cannot
  get to this view in a private community.

- Removing a member's profile removes them from the listing.

- Removing moderator status from a member updates the moderator links
  and the coloring in the listing.

- Removing the moderator from the community removes them both from the
  listing and the moderators listing.

- Adding a department to someone's profile adds the department to this
  listing.

- Moderators should see an action box for `Manage`, `Add Existing`,
  and `Invite New`.

- Allowed users should see a submenu containing a toggle between Show
  Pictures and Hide Pictures.  Choosing one should: change the layout
  and hide the link for that menuitem.

.. _manage-members-policies:

Manage Members
==============

- Only moderators can see this screen

- Show the moderators, then the members, then the invitations

- For moderators, allow revoking their moderation or removing them
  from the community.

- For members, allow granting moderation or removing them from the
  community.

- For invitations, allow resending the invitation or removing the
  invitation.

- You cannot remove moderation or remove the moderator for the last
  moderator.

- Changes to the moderator list sends an email to all moderators,
  including the ones just un-moderated.

- A status message indicates that actions were taken.

- Submit goes back to the same screen, Cancel goes to Show Members.


.. _add-existing-users-policies:

Add Existing Users
==================

Get existing KARL users into your community.

- Only moderators can see this screen

- Send email including an optional HTML message.

- Skip people that are already in your community.

- Give a status message after saving showing the actions taken.


.. _invite-new-users-policies:

Invite New Users
================

Get new, non-KARL users into your community.

- Only moderators can see this screen

- Send email including an optional HTML message.

- Skip email addresses that are already in your community.

- Fail on things that don't look like email addresses.

- Give a status message after saving that showed how many invitations
  were sent.

- Create an invitation with a key that can't easily be guessed.


.. _accept-invitation-policies:

Accept Invitation
=================

- They see a view that doesn't have much "chrome" at all: no header,
  footer.

- Cannot choose a username that already exists

- Passwords must be 8 characters

- Confirm password must match Password

- List of countries comes from a "vocabulary"

- Languages and Departments should be a sequence

- "Terms and Conditions" and "Privacy Policy" should get their text
  from "configuration".  Both should give a friendly popup window.

- Only Anonymous can access this screen.  If you are logged in, flag a
  warning, but using the generic_layout.

- The invitation key should by pretty opaque, to help foil being
  re-used.

- The invitation URL should fit on one line in the email.  If it
  wraps, the link won't work in many email clients.

- Correctly processing the email logs someone in, delivers an email,
  then sends them to the :ref:`show-community-policies`.
