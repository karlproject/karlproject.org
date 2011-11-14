.. _forms-tutorial:

==========
KARL Forms
==========

As mentioned elsewhere, KARL3 has a minimalist approach.  Rather than
a megaframework, KARL3 attempts to be a microframework.  It does what
it should and no more, allowing extension and overriding to avoid
feature-itis and platform-itis.  It also strives to leverage Python
and other Python web libraries.

This philosophy applies to forms in KARL3.  If you're looking for
automajik generation of create/read/update/delete (CRUD) forms with
pluggable widgets and the like, you won't be interested in KARL.  If
you're looking for something with no surprises and good performance,
read on.

This tutorial explains the approach to forms in KARL3, then builds up
the forms system one chunk at a time.  That is, you'll see the actual
development of the KARL3 approach to forms.  We do so by documenting
all the common ways people want to use forms.

Objectives
==========

#. Explain the KARL3 forms system.

#. Gradually document the creation of the system.

#. Show the various "patterns" of web forms and how each is done in
   KARL3.

Sections
========

.. toctree::
   :maxdepth: 2

   background
   installation
   nomachinery
   baseclass
   formencode1
   formencode2
   refactorintomodels
   morevalidators
   notes
