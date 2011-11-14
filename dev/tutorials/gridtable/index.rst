.. _gridtable-tutorial:

=============================
Dynamic Grids Using GridTable
=============================

Modern web systems use Ajax to enhance the user experience.  Tabular
"grids" of dynamically-loaded data are a popular example.  KARL3 uses
jQuery and the jQuery UI widget framework as its Ajax foundation, with
a "GridTable" component that covers these needs.

The GridTable used by KARL is a derivative of the preliminary `jQuery
UI GridTable <http://jqueryui.pbworks.com/GridTable>`_.

This tutorial documents the GridTable by gradually writing a "User
Manager" application for KARL3.  In fact, the tutorial is used to
document the writing of the GridTable widget itself.  Piece by piece,
we add more functionality to the widget.

Audience
========

#. The `jQuery UI community <http://jqueryui.com>`_ as our ultimate
   goal is to present this work to them for inclusion per their
   `GridTable proposal <http://jqueryui.pbworks.com/GridTable>`_.

#. KARL developers that want to present batched data using the
   GridTable.


Objectives
==========

#. Get started with a static jQuery and jQuery UI project.

#. Illustrate how to introduce a GridTable into a real-world
   application.

#. Document the functionality and implementation of the widget itself.

Sections
========

.. toctree::
   :maxdepth: 2

   background
   gettingstarted
   firstplugin
   todoandnotes
