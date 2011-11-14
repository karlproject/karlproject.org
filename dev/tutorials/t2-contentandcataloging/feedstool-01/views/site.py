from repoze.bfg.chameleon_zpt import render_template_to_response
from repoze.bfg.chameleon_zpt import get_template

from webob.exc import HTTPFound
from repoze.bfg.url import model_url
from repoze.bfg.view import static

from feedstool.models.feed import Feed

static_view = static('templates/static')

def list_feeds_view(context, request):
    layout = get_template('templates/layout.pt')

    feeds = []
    for feed in context.values():
        feeds.append({
                'title': feed.title,
                'model_url': model_url(feed, request),
                })

    return render_template_to_response(
        'templates/list_feeds.pt',
        request=request,
        layout=layout,
        page_title="List Feeds",
        feeds=feeds)

def add_feed_view(context, request):

    layout = get_template('templates/layout.pt')

    is_submitted = request.POST.get('form.submitted', False)
    if is_submitted is not False:
        title = request.POST['title']
        url = request.POST['url']
        feed = Feed(title, url)

        name = title.replace(' ', '-').lower()
        context[name] = feed

        return HTTPFound(location=model_url(feed, request))

    # Form was not submitted, return the page

    return render_template_to_response(
        'templates/add_feed.pt',
        request=request,
        layout=layout,
        page_title='Add Feed',
        is_submitted=is_submitted)
