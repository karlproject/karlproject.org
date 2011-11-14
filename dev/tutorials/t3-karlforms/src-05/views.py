from repoze.bfg.chameleon_zpt import render_template_to_response
from repoze.bfg.chameleon_zpt import get_template
from repoze.bfg.chameleon_zpt import render_template
from repoze.bfg.view import static
from webob.exc import HTTPFound
from repoze.bfg.url import model_url

from baseform import BaseForm
from baseform import name
from baseform import age
from baseform import country
from baseform import vocabularies

from t3.models import Person
from formencode import Invalid

from random import randrange

static_view = static('templates/static')

# Define a form schema, make an instance
class MyInfo(BaseForm):
    name = name
    age = age
    country = country
myinfo = MyInfo

def list_people_view(context, request):

    layout = get_template('templates/layout.pt')

    return render_template_to_response(
        'templates/list_people.pt',
        context = context,
        request = request,
        page_title='List People',
        layout=layout,
        )

def add_person_view(context, request):

    layout = get_template('templates/layout.pt')

    formfields = get_template('templates/formfields.pt')
    form = myinfo()

    if form.is_submitted(request):
        fieldvalues = form.combine_dicts(form.defaults, request.POST)
        # Now validate
        try:
            fv = fieldvalues = form.to_python(fieldvalues)
            fielderrors = {}

            # Go ahead and do the work to add content, etc.
            person = Person(fv['name'], fv['age'], fv['country'])
            __name__ = str(randrange(0, 99999))
            context[__name__] = person
            return HTTPFound(location=model_url(person, request))

        except Invalid, e:
            fielderrors = e.error_dict

    else:
        fieldvalues = form.defaults
        fielderrors = {}

    # Render the form and shove some default values in
    form_html = render_template(
        'templates/myform.pt',
        context = context,
        request=request,
        formfields=formfields,
        fielderrors=fielderrors,
        vocabularies=vocabularies,
        )
    rendered_form = form.merge(form_html, fieldvalues)

    return render_template_to_response(
        'templates/add_person.pt',
        context=context,
        request = request,
        page_title='Add Person',
        layout=layout,
        form_html=rendered_form,
        elapsed=form.elapsed,
        )

def show_person_view(context, request):

    layout = get_template('templates/layout.pt')

    return render_template_to_response(
        'templates/show_person.pt',
        context = context,
        request = request,
        page_title='Show Person',
        layout=layout,
        )

def edit_person_view(context, request):

    layout = get_template('templates/layout.pt')

    formfields = get_template('templates/formfields.pt')
    form = myinfo()

    if form.is_submitted(request):
        fieldvalues = form.combine_dicts(context.__dict__, request.POST)

        # Now validate
        try:
            fieldvalues = form.to_python(fieldvalues)
            fielderrors = {}

            # Go ahead and do the work to update content, etc.
            context.name = fieldvalues['name']
            context.age = fieldvalues['age']
            context.country = fieldvalues['country']
            return HTTPFound(location=model_url(context, request))

        except Invalid, e:
            fielderrors = e.error_dict

    else:
        fieldvalues = context.__dict__
        fielderrors = {}

    # Render the form and shove some default values in
    form_html = render_template(
        'templates/myform.pt',
        request=request,
        formfields=formfields,
        fielderrors=fielderrors,
        vocabularies=vocabularies,
        )
    rendered_form = form.merge(form_html, fieldvalues)

    return render_template_to_response(
        'templates/edit_person.pt',
        context = context,
        request = request,
        page_title='Edit %s' % context.name,
        layout=layout,
        form_html=rendered_form,
        elapsed=form.elapsed,
        )

