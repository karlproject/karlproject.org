Full-text Indexing in KARL3
===========================

Adapter-based Text Extraction
-----------------------------

Each content object in KARL can be adapted to extract the text provided
to the text index.  The adapter API is specified in
:class:`karl.models.interfaces.ITextIndexData`:  each such adapter called
with no additional arguments, and is expected to return a string representing
the searchable text of its context.

A trivial implementation which returned only the title of its context
might look like:

.. code-block:: python

   class TitleOnlySearchableText(object):

       def __init__(self, context):
           self.context = context

       def __call__(self):
           return self.context.title


Tuning Full-text Search Results
-------------------------------

The relevance of a particular document with respect to a given query term
depends on the weight assigned to the occurences of the term in the document's
searchable text.  By default, this weight is computed using the number of
occurences of the term.

:func:`karl.content.models.adapters.makeFlexibleTextData` is a
"factory-factory", which defines full-text search adapters using
parameterized weighting for different fields.  The same adapter defined as a
class above could be defined using the factory-factory as follows:

.. code-block:: python

   from karl.content.models.adapters import makeFlexibleTextData

   TitleOnlySearchableText = makeFlexibleTextData([('title', 1, None)])

The argument passed to the factory-factory is an ordered list of tuples,
each of the form ``(extractor, weight, cleaner)``.

- The ``extractor`` element is either a string, naming the attribute to be
  used, or a callable, which will be passed the context, and must return a
  string.

- The ``weight`` element is an integer, representing the number of times the
  extracted string will be repeated in the searchable text.

- The ``cleaner`` element must be either None, or else a callable taking a
  string and returning a "cleaned" version of the string.

Example:  Providing a Fallback
++++++++++++++++++++++++++++++

To define an adapter which can be used across a number of different content
types, we might provide an extractor function which tried different
attributes:

.. code-block:: python

   from karl.content.models.adapters import makeFlexibleTextData

   def _find_headline_or_title(context):
       result = getattr(context, 'headline', None)
       if result is None:
           result = getattr(context, 'title', '')
       return result

   HeadlineOrTitleTextData = makeFlexibleTextData(
                                [(_find_headline_or_title, 1, None)])


Example:  Cleaning HTML
+++++++++++++++++++++++

Assume that we have a "news story" content object which has a
``blurb`` element, containing HTML, in addition to a plain text ``headline``.
We might define the adapter for such objects using the `_html_cleaner`
utility function defined in :mod:`karl.content.models.adapters`:

.. code-block:: python

   from karl.content.models.adapters import makeFlexibleTextData
   from karl.content.models.adapters import _html_cleaner

   HeadlineBlurbTextData = makeFlexibleTextData([('headline', 1, None),
                                                 ('blurb', 1, _html_cleaner),
                                                ])

To weight terms found in the headline three times more strongly than those
found in the blurb:

.. code-block:: python

   HeadlineBlurbTextData = makeFlexibleTextData([('headline', 3, None),
                                                 ('blurb', 1, _html_cleaner),
                                                ])

Example:  Indexing Blob Data
++++++++++++++++++++++++++++

Some KARL content keeps a portion of its indexable data in "blob" files
on the filesystem.  To index such data, we can use another utility function,
`_extract_file_data`, defined in :mod:`karl.content.models.adapters`:

.. code-block:: python

   from karl.content.models.adapters import makeFlexibleTextData
   from karl.content.models.adapters import _extract_file_data

   HeadlineBlurbTextData = makeFlexibleTextData([('title', 4, None),
                                                 (_extract_file_data, 1, None),
                                                ])
