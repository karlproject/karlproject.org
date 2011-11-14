from repoze.bfg.chameleon_zpt import render_template_to_response
from repoze.bfg.chameleon_zpt import get_template
from repoze.bfg.chameleon_zpt import render_template
from repoze.bfg.view import static

from baseform import BaseForm
from formencode import validators
from formencode import Invalid

static_view = static('templates/static')

# Define a form schema, make an instance
class MyAge(BaseForm):
    age = validators.Int(not_empty=True, max=200, default=93)
myage = MyAge


def my_view(context, request):
    layout = get_template('templates/layout.pt')
    form = myage()

    form_message = None

    if form.is_submitted(request):
        # We were submitted. Start by combining data from
        # request.params and form.defaults.
        fieldvalues = form.combine_dicts(form.defaults, request.params)

        # Now validate
        try:
            fieldvalues = form.to_python(fieldvalues)
            fielderrors = {}

            # Go ahead and do the work to add content, etc.
            form_message = "Saved the data."

        except Invalid, e:
            # Form data wasn't valid.
            fielderrors = e.error_dict

    else:
        # Set default values and no errors
        fieldvalues = form.defaults
        fielderrors = {}

    # Render the form and shove some default values in
    form_html = render_template(
        'templates/myform.pt',
        request=request,
        fielderrors=fielderrors,
        form_message=form_message,
        )
    rendered_form = form.merge(form_html, fieldvalues)

    return render_template_to_response(
        'templates/mytemplate.pt',
        request = request,
        layout=layout,
        form_html=rendered_form,
        elapsed=form.elapsed,
        )
