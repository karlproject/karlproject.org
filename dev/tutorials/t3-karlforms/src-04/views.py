from repoze.bfg.chameleon_zpt import render_template_to_response
from repoze.bfg.chameleon_zpt import get_template
from repoze.bfg.chameleon_zpt import render_template
from repoze.bfg.view import static

from baseform import BaseForm
from baseform import name
from baseform import age
from baseform import country
from baseform import vocabularies

from formencode import Invalid

static_view = static('templates/static')

# Define a form schema, make an instance
class MyInfo(BaseForm):
    name = name
    age = age
    country = country
myinfo = MyInfo

# Simulate editing exisiting model data
records = {
    '1': {'name': 'Rec 1', 'age': 27},
    '2': {'name': 'Rec 2', 'age': 94},
}

def my_view(context, request):
    layout = get_template('templates/layout.pt')
    formfields = get_template('templates/formfields.pt')
    form = myinfo()

    form_message = None
    rec_id = request.GET.get('id', None)

    if form.is_submitted(request):
        if rec_id is None:
            fieldvalues = form.combine_dicts(form.defaults, 
                                             request.POST)
        else:
            # Edit existing
            fieldvalues = form.combine_dicts(records[rec_id], 
                                             request.POST)

        # Now validate
        try:
            fieldvalues = form.to_python(fieldvalues)
            fielderrors = {}

            # Go ahead and do the work to add content, etc.
            form_message = "Saved the data."

        except Invalid, e:
            fielderrors = e.error_dict

    else:
        if rec_id is None:
            fieldvalues = form.defaults
        else:
            fieldvalues = records[rec_id]
        fielderrors = {}

    # Render the form and shove some default values in
    form_html = render_template(
        'templates/myform.pt',
        request=request,
        formfields=formfields,
        fielderrors=fielderrors,
        form_message=form_message,
        vocabularies=vocabularies,
        )
    rendered_form = form.merge(form_html, fieldvalues)

    return render_template_to_response(
        'templates/mytemplate.pt',
        request = request,
        layout=layout,
        form_html=rendered_form,
        elapsed=form.elapsed,
        )
