===============
Getting Started
===============

In this first step get the basics of a jQuery UI project in place.  We
will make a page that includes the standard jQuery UI calendar widget.

For this tutorial, we are using the `Google AJAX Libraries
 <http://code.google.com/apis/ajaxlibs/documentation/>`_ loader to get
 jQuery and jQuery UI into our project.  Loading from Google's content
 delivery network (CDN) improves performance and decreases the work of
 writing this tutorial.

HTML Page
=========

In :download:`demo.html <src/gettingstarted/demo.html>` we have some
basic markup for a page:

   .. literalinclude:: src/gettingstarted/demo.html
      :linenos:
      :language: html

#. *Line 5*. Include the Google script that lets us load common Ajax
   libraries.

#. *Lines 7-8*.  Load current versions of the jQuery and jQuery UI
   libraries.

#. *Lines 10-12*. Use the Google CDN to get the CSS for a particular
   jQuery UI theme (smoothness).

#. *Lines 13-14*.  Link to our custom CSS and JS.

JS
==

The :download:`demo.js <src/gettingstarted/demo.js>` has very little
in it:

   .. literalinclude:: src/gettingstarted/demo.js
      :linenos:
      :language: js

#. *Line 1*.  The traditional jQuery way to execute code safely when
   the page is loaded.

#. *Line 2*.  Turn an HTML node into a jQuery UI widget.

CSS
===

The CSS used in :download:`demo.css <src/gettingstarted/demo.css>` is
really just a placeholder:

   .. literalinclude:: src/gettingstarted/demo.css
      :linenos:
      :language: css

With these basics in place we can look the basics of writing our first
jQuery UI widget.  We will gradually build the widget into our
GridTable.

