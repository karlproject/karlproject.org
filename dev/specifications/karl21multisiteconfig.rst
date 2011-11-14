==============================================
KARL 2.1 Multisite Configuration Specification
==============================================

Since the main goal of KARL 2.1 is to launch the pilot program, KARL
2.1 needs to support running multiple instances on the same server
under different virtual hosted domains.  The research for KARL 2.1
needs to include this goal.  An initial check of the system indicates
the following tasks, but research may discover more:

- The email  to/from domain needs to be configurable.  This includes:

  - The imap/smtp server address and port

  - The links embedded in any outbound email addresses

  - The links to email the community in the front end UI

- Documentation on setting up an instance to run on different port
  numbers than the default

- Documentation on setting up KARL running through apache in a virtual
  host

- The string karl.soros.org should not exist anywhere in the KARL 2.1
  core code
