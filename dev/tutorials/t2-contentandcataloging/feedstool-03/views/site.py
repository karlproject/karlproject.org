from repoze.bfg.chameleon_zpt import render_template_to_response
from repoze.bfg.chameleon_zpt import get_template

from webob.exc import HTTPFound
from repoze.bfg.url import model_url
from repoze.bfg.view import static

from repoze.lemonade.content import create_content
from feedstool.models.interfaces import IFeed

import itertools
from repoze.bfg.traversal import find_model
from repoze.bfg.traversal import find_root

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


def catalog_search(context, searchterm):

    catalog = getattr(find_root(context), 'catalog', False)
    if catalog is False:
        # We are testing from the unit test, so just return an empty
        # list. Long term we'd make a DummyCatalog in the unit test to
        # mimic the semantics of an actual catalog.
        return []
    batch_start = 0
    limit = 100
    query = {'texts': searchterm}
    num, iter = catalog.search(**query)

    info = []
    for docid in itertools.islice(iter, batch_start, limit):
        path = catalog.document_map.address_for_docid(docid)
        instance = find_model(context, path)

        info.append(instance)

    return info


def search_view(context, request):
    layout = get_template('templates/layout.pt')

    # Get the search results, pick them apart into a list of dicts
    searchterm = request.params.get('searchterm', False)

    results = []
    for result in catalog_search(context, searchterm):
        results.append({
                'title': result.title,
                'model_url': model_url(result, request),
                })
    
    return render_template_to_response(
        'templates/search.pt',
        request=request,
        layout=layout,
        page_title="Search Results for " + searchterm,
        results=results)

def add_feed_view(context, request):

    layout = get_template('templates/layout.pt')

    is_submitted = request.POST.get('form.submitted', False)
    if is_submitted is not False:
        title = request.POST['title']
        url = request.POST['url']
        feed = create_content(IFeed, title, url)

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
