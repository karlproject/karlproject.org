===============
Improved Search
===============

During the October 2010 meeting in NYC, we spoke to various user
groups and OSI about usability related to certain features.  Search,
particularly LiveSearch, was one of those features.  This note
documents some of the points mentioned and proposed improvements.

Backspace doesn't work
======================

This is simply a bug that needs to be fixed.  Pressing backspace
doesn't always re-issue the search in the way that it should.

Slow
====

One user didn't even know about the incremental search, because it was
regularly slow enough to not keep up with typing.

We should measure the server-side performance of LiveSearch and see
what percentage of requests are not be serviced within the window
needed to give the impression of quality autocomplete.  Then, we gauge
the effort to get within that window, and decide whether the cost is
reasonable.  An alternative: just give up on LiveSearch if we can't
credibly meet the time window.

Give Relevance to Staff
=======================

Much of the discussion was about using LiveSearch as an office
directory.  The particular challenge is that we can only show up to
five matches, and with prefix matching on many profile fields, it is
very hard to squeeze enough matches into that small a window.

As a start, staff doing a LiveSearch should see staff users as more
relevant than affiliates.  Ditto for advanced search.

Give Relevance to First Name and Last Name
==========================================

Prefixes (portions of words as they are typed) can match on portions
of words in many profile fields, including bio and department.

There was brief discussion about having the People matches in
LiveSearch only hit on First Name and Last Name.  This would address
the most common complaint ("It is showing me names that don't even
match what I type!")  However, it was felt that this, while very
effective in the dominant case, would be too draconian in the edge
cases.

Instead, we could start by just tuning the relevance to make matches
in those fields more relevant than matches elsewhere.

Ditto for advanced search.

Show Phone Extension
====================

Again, targeted at the use case of using LiveSearch as an office
directory.  We could have result rows show, floated right, the phone
extension of the staff person.  This would eliminate another click.

Change Behavior of Enter
========================

Typing a few letters and pressing enter takes the user to the advanced
search results for that series of letters.  Currently, we show the
results for that search without the astericks, meaning, a word search
and not a prefix search.  Clicking "Show All" in the LiveSearch
results, though, does a search with the astericks, meaning a prefix
search.

The decision of whether to prefix search or not comes down to quality
versus quantity.  Doing a prefix gives lots of results, but probably
not the one you were looking for in the first pagefull.

We could, like Google, do a "Did you mean" at the top to make
switching between the two more explicit.

Sticky Selection for Narrowing
==============================

LinkedIn's search has a drop-down menu for focusing the displayed
searches on People, Organizations, etc.  If we really wanted to target
the complaints of people using that box as an organizational search,
we could provide a drop-down menu like LinkedIn.  We could make the
results sticky, meaning we remembered their choice.

It was asserted that providing an option is of little use, since most
users won't try it but will still complain.  Another alternative is to
put a second search box at the top of each screen that is only for
people search.  Ugly, but explicit.

Contextual Summaries
====================

Not related to LiveSearch, but it was mentioned under the banner of
user experience that seeing some information about the results would
be helpful.  Most of the time we show nothing, not even a description.
Even better would be showing a contextual summary with the area around
the match, as they expect from modern search engines.

Drill-Down on Results
=====================

Also not about LiveSearch.  Once on search results, if we could do
some simple drill-down, very explicit, we could give a better
experience.  Specifically, narrowing results to profiles and perhaps
even type of profile (Staff, In My Office, In My Department, etc.)
