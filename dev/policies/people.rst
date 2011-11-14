================
Policies: People
================

Policies that apply to the screens that appear either under the People
tab, the Community People views, or the profiles.

.. _change-password-policies:

Change Password
===============

- Screencast at http://www.karlproject.org/screencasts/ChangePassword.mov

- You get to this from Edit Profile

- There is a paragraph of text at the top of Edit Profile

- This paragraph is different if you are staff vs. affiliate

Staff
---------

- The edit profile paragraph should read::

    OSI users have their basic employee information managed
    centrally. If you notice something wrong, please send an email to
    karladmin@list.soros.org. If would you like to change your
    password, please click Change Password.

- The emai address is hopefully parameterized.  Later, we'll probably
  parameterize the OSI part.

- The link to "change password" navigates you out of the system to
  OSI's in-house system (GSA).

- The link to Change Password should be setup as part of the site
  configuration

- See src/osi/osi/run.py for "forgot_password_url" (something in the
  next set of screens we need to do)

- The external system will collect the changed staff password and POST
  back to the view as admin

Affiliate
---------------

- The paragraph in Edit Profile says::

    KARL affiliates can use the following form to edit their profile
    information. If you would like to delete your KARL account and
    remove yourself from all communities, click this delete account
    link and say "yes" to the confirmation window. If would you like
    to change your password, please click Change Password.

- "delete account" is a hyperlink that will be implemented in another
  screen.

- Clicking on the change password link goes to Change Password

- This uses the generic layout (unlike KARL2), same as Edit Profile

- Make it be somewhat like a KARL3 form.  Let me know if you'd like me
  to do the form work.

- An introductory paragraph saying::

    Please enter a valid password below and click on Submit
    button. Password must be at least 8 characters long. If you need
    additional help please email the _Site Administrator_.

- The ``Site Administrator`` is a hyperlink with an href of
  ``mailto:karladmin@karl.soros.org``.

- If possible, make that email a parameter set in ``run.py``

- Fields

  - Current password (required).  Prevents people from walking up to a
    logged-in user and changing their password.

  - New password (required.)  Must be 8 characters.  Steal this and
    the confirm from the accept invitation view/form.

  - Confirm password (required).  Use a chained_validator to make sure
    it matches the first.  (Again, steal from accept invitation.)

- The "Cancel" goes back to View Profile.

- Submit, if successful, should:

  - Go back to View Profile

  - With a ``?status_message=Password%20changed``

  - Send a confirmation email

Change Password Confirmation Mail
---------------------------------

- From "KARL Admin <karladmin@karl.soros.org>" 

- Subject "KARL Password Change Notification"

- To "Firstname Lastname <email>"

- Body::

    Your Username for KARL is: <username> and your new 
    Password is: <password.


.. _forgot-password-policies:

Forgot Password
===============

- Screencast at http://www.karlproject.org/screencasts/ForgotPassword.mov

- You get here by clicking "I forgot my password" on the login screen.

- It is shown in the same "anonymous" layout as the login screen

- You collect the email address on a form with help text as shown in
  the screencast.

- Cancel goes back to the login screen

- On submit, validate that the email address is known.  Use the index
  we have for looking that up. Give a form validation error if the
  email address isn't known.

- This should be a self-posting form, because the next step in the
  process is a fork:

  - Use the email to grab the profile, then use that to grab the user

  - If the user is KarlStaff *and* ``run.py`` has defined a
    ``forgot_password_url``:

    - Issue a redirect to ``forgot_password_url`` along with
      ``?txtEmail=`` plus the email address

    - This will hand over processing of staff password recovery to
      their existing system (GSA)

  - Otherwise, it is an affiliate *or* the site running this KARL3
    doesn't have an existing system

  - Either redirect to another view, or handle the next step (Password
    Recovery Confirmation) in this view


.. _forgot-password-confirmation-policies:

Password Recovery Confirmation
==============================

- Part of the screencast at
  http://www.karlproject.org/screencasts/ForgotPassword.mov

- Anonymous "layout"

- Display a message similar to the text in the screencast

  - "An email has been sent to <username> with password reset
    instructions".

  - Etc.

- Send an email:

  - From "KARL Admin <karladmin@karl.soros.org>" 

  - Subject "KARL password reset request"

  - To "Firstname Lastname <email>"

  - Body::

      Please go to the following url to reset the password for your 
      KARL account.  https://karl.soros.org/passwordreset.html?key=49a95d4bb7fa5558083bfbcf7b96e9e0

- How that key matches up to identification, or even if it is some
  other approach, is up for discussion.  Is this a CMF-ism?


.. password-reset-policies:

Password Reset
==============

- Part of the screencast at
  http://www.karlproject.org/screencasts/ForgotPassword.mov

- You arrive here by clicking on the link in the email

- Shown as in the screencast

- Fields

  - Username (required)

  - New password and re-enter password same as other screens (8
    characters, must match, use chained_validators, etc.)

- Cancel goes to login screen

- Submit shows validation errors if fail

- If succeed, set new password, log them in, and redirect them to
  their home_path.

- Tack on a ``?status_message=Password%20reset`` to the URL to get a
  message displayed.
