from repoze.bfg.chameleon_zpt import render_template_to_response
from repoze.bfg.view import static
from repoze.bfg.chameleon_zpt import get_template

static_view = static('templates/static')

def list_feeds_view(context, request):
    layout = get_template('templates/layout.pt')

    return render_template_to_response(
        'templates/list_feeds.pt',
        request = request,
        layout=layout,
        page_title="List Feeds")
