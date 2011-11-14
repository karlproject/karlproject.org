=====
Forms
=====

Although KARL3 started down the path of using ToscaWidget's
:mod:`tw.forms` (which uses :mod:`FormEncode` internally), we later
switched to a very simple form "system" focused on:

- FormEncode for validation

- ZPT for "widgets" and error display

- :mod:`lxml.html` for shoving values into forms

To see more on the motivation, read :ref:`forms-tutorial-background`
for the goals and anti-goals.

  .. note::

    That tutorial is still basically correct in its philosophy, but
    out of date on specifics.  For example, our approach currently
    allows instances of KarlForms to have state.

The Basics
==========

KarlForms are really quite simple, though verbose, per its goals to be
an anti-framework:

- *A view handles most of the work*.  Especially, the view keeps the
  model, the form, and the request data at arm's length from each
  other.

- *The view is verbose*.  The flow of control through the form
  processing is explicit and easy to figure out by reading.  Decisions
  aren't made behind the scenes: you make them, allowing you to opt in
  or out.


- *ZPT does most of the UI*.  You make your form and form elements
   with ZPT.  You can elect to have macros for all cases, some cases,
   or no cases.

- *FormEncode does validation*.  When a form is submitted, you can
   validate the data and provide information for the ZPT about errors.

- *lxml.html does form filling*.  If your form has data (default
   values from a "schema", existing model data on a edit form,
   transient POST data due to a validation error), you need to merge
   this into the form.  lxml.html is good at this.

The View
========

It is relatively easy to read an example
(e.g. ``src/karl.content/karl/content/views/blog.py``) and see forms
in action, but here's a high-level view:

  .. code-block:: python
    :linenos:

    class AddBlogEntryForm(baseforms.BaseForm):
        title = baseforms.title
        text = baseforms.text
        tags = baseforms.tags
        sendalert = baseforms.sendalert

    def add_blogentry_view(context, request):

        fieldwidgets = get_template(templates_formfields_path)
        form = AddBlogEntryForm(request.POST, submit='form.submitted', 
                                    cancel='form.cancel')

        if form.cancel in form.formdata:
            return HTTPFound(location=model_url(context, request))

        if form.submit in form.formdata:
            try:
                state = baseforms.AppState(tagslist=['t1','t2'])
                converted = form.to_python(form.fieldvalues, state)
                form.is_valid = True
		# Valid post, do some work and redirect away

                return HTTPFound(location=location)

            except Invalid, e:
                fielderrors = e.error_dict
                form.is_valid = False
        else:
            fielderrors = {}

        page_title = 'Add Blog Entry'
        api = TemplateAPI(context, request, page_title)

        # Render the form and shove some default values in
        form_html = render_template(
            'templates/form_add_blogentry.pt',
            post_url=request.url,
            formfields=fieldwidgets,
            fielderrors=fielderrors,
            )
        form.rendered_form = form.merge(form_html, form.fieldvalues)

        return render_template_to_response(
            'templates/addedit_blogentry.pt',
            api=api,
            form=form,
            )

#. *(Lines 1)*.  Make a "schema" for form validation using
   ``BaseForm``, which is a FormEncode Schema plus a couple of
   helpers.

#. *(Lines 2-5)*.  Put 4 validators on the form.  In this case, we are
   re-using some validators that are configured for the rest of the
   project to re-use.

#. *(Line 9)*.  In many cases we use the same formfield over and
   over, with the same label, help text, and layout.  We can load a
   sheet of ZPT macros to avoid repetition across a project.  (Note: a
   field is an instance of a "widget", to use jargon from other
   systems.)

#. *(Line 10)*.  Make an instance of our form.  Hand it the form data
   and point our KarlForm at the HTML name attributes for the submit
   and cancel buttons.

#. *(Lines 13-14)*.  Bail out early if the cancel button was clicked.

#. *(Line 16)*.  Detect that the form was submitted and start form
   validation.

#. *(Line 17, Line 25)*.  Wrap a ``try/except`` around FormEncode
   validators raising a validation error.

#. *(Line 18)*.  FormEncode has a protocol for how model state from
   the application (not the form data) gets into the validators.  Pass
   in keyword value pairs for model data needed for validation.

#. *(Line 19)*. Get FormEncode to convert the form data into your
   datastructures per the validators.

#. *(Line 20)*. If we make it hear, the form was valid.  Say so, to
   allow unit tests to have data we can check for each branch in the
   form processing.

#. *(Line 23)*.  Here's where we would take the converted form data
   and jam it onto our model objects, or send emails, or whatever
   actions are needed.

#. *(Lines 26-27)*.  Store the reason why the form validation failed,
   for use in the ZPT.  Also, let the unit test know, quite
   explicitly, that the form is invalid.

#. *(Line 28)*.  The form wasn't submitted.  This is actually the
   dominant code path.  We make sure that it is fast.

#. *(Lines 35-40)*.  The ZPT for the form is in its own file.  Load it
   and hand the ZPT some data needed to render.  For example, if you
   have a select box for choosing country, you probably need to pass
   in a list of countries.  All normal ZPT stuff, optimized for the
   fastest/simplest cases.

#. *(Line 41)*.  The one frameworky place.  Call a helper that merges
   the form HTML from the previous step with the form data based on
   different form processing paths.

   This helper is "optimized" to detect when it has no work to do.
   Rather than parsing the form HTML into an lxml.html tree, it just
   returns the htmlstring.

#. *(Lines 43-47)*.  The normal conclusion to a view in KARL: render
   the template.



