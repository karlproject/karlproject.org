from repoze.bfg.chameleon_zpt import render_template_to_response
from repoze.bfg.chameleon_zpt import get_template

def show_feed_view(context, request):
    layout = get_template('templates/layout.pt')

    return render_template_to_response(
        'templates/show_feed.pt',
        request=request,
        layout=layout,
        page_title = 'Show Feed ' + context.title,
        feed_url=context.url)
