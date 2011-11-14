from repoze.bfg.chameleon_zpt import render_template_to_response
from repoze.bfg.chameleon_zpt import get_template
from repoze.bfg.chameleon_zpt import render_template
from repoze.bfg.view import static
from baseform import BaseForm

static_view = static('templates/static')

def my_view(context, request):
    layout = get_template('templates/layout.pt')
    form = BaseForm(request)

    fieldvalues = {'age': 40}  # Set a default age
    if form.is_submitted:
        fieldvalues, fielderrors = form.validate(fieldvalues)
    else:
        fielderrors = {'age': False}

    form_html = render_template(
        'templates/myform.pt',
        request=request,
        fielderrors=fielderrors,
        )
    rendered_form = form.render(form_html, fieldvalues)

    return render_template_to_response(
        'templates/mytemplate.pt',
        request = request,
        layout=layout,
        form_html=rendered_form,
        elapsed=form.elapsed,
        )
