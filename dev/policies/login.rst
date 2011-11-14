===============
Policies: Login
===============

Policies related to logging in, logging out, recovering password,
changing password, etc.

.. _show-login-policies:

Show Login 
==========


- If you aren't logged in and go to the login screen directly, you get
  the login screen.

- If you aren't logged in and go to /communities, you get sent to the
  login screen with a message saying "Not logged in".

- If you are logged in and go to /communities/private (and you're not
  in that community), you will get an error screen clearly saying
  Forbidden.  You will still be on that URL and the proper HTTP status
  code (403) will be returned.

- If you are on the login screen and provide a bad username/password
  combo, the error message will say "Bad username or password".

- Provide a "Remember me on this computer" checkbox the sets cookies
  that span sessions.

- The link "I forgot my password" should go to the password recovery
  screen.

- When sent to this screen as the result of an authorization error,
  logging in should then send you back to the screen you were
  attempting to go to.

- Otherwise, logging in should send you to your "default" screen.  For
  "staff", this is your office home page.  Otherwise, it is the
  communities screen.

- If you are an affiliate with only one community, you get sent there
  on login (if there is no came_from).

- The logout link should go to the login screen with a status message
  saying "You are logged out".

