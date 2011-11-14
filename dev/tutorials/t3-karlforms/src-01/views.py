from repoze.bfg.chameleon_zpt import render_template_to_response
from repoze.bfg.chameleon_zpt import get_template
from repoze.bfg.chameleon_zpt import render_template
from repoze.bfg.view import static
from lxml.html import document_fromstring
from lxml.html import tostring
from time import time

static_view = static('templates/static')

def my_view(context, request):
    layout = get_template('templates/layout.pt')

    start = time()

    fielderror = formerror = None
    default_age = formfill_age = 40
    max_age = 200

    if request.POST.get('form.submitted', False):
        # Form was submitted, do some validation
        age = request.POST.get('age', False)
        if age is False or age == '':
            print 'Age is required'
            fielderror = 'Age is required'
        try:
            if int(age) > max_age:
                print '%s is over the max_age of %s' % (age, max_age)
                fielderror = 'Age must not be over %s' % age
            # Whether age is valid or not, shove it back into the form
            formfill_age = age
        except ValueError:
            print 'Age is not an integer'
            fielderror = 'Age must be an integer'
            formfill_age = age

    form_html = render_template(
        'templates/myform.pt',
        request=request,
        formerror=formerror,
        fielderror=fielderror,
        )

    # Merge in the value for the age, either from the default or from
    # what they typed in.
    form_tree = document_fromstring(form_html)
    form = form_tree.forms[0]
    form.fields['age'] = str(formfill_age)
    merged_form_html = tostring(form)

    elapsed = str(1 / (time() - start))[0:7]

    return render_template_to_response(
        'templates/mytemplate.pt',
        request = request,
        layout=layout,
        form_html=merged_form_html,
        elapsed=elapsed,
        )
