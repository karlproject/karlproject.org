import unittest

from zope.testing.cleanup import cleanUp
from repoze.bfg import testing

class SiteViewTests(unittest.TestCase):

    """ These tests are unit tests for the view.  They test the
    functionality of *only* the view.  They register and use dummy
    implementations of repoze.bfg functionality to allow you to avoid
    testing 'too much'"""

    def setUp(self):
        """ cleanUp() is required to clear out the application registry
        between tests (done in setUp for good measure too)
        """
        cleanUp()
        import feedstool
        import zope.configuration.xmlconfig
        zope.configuration.xmlconfig.file('configure.zcml',
                                          package=feedstool)
        
    def tearDown(self):
        """ cleanUp() is required to clear out the application registry
        between tests
        """
        cleanUp()

    def test_list_feeds_view(self):
        from feedstool.views.site import list_feeds_view
        context = testing.DummyModel()
        request = testing.DummyRequest()
        renderer = testing.registerDummyRenderer('templates/list_feeds.pt')
        response = list_feeds_view(context, request)
        renderer.assert_(page_title='List Feeds')

    def test_add_feed_view(self):
        from feedstool.views.site import add_feed_view
        context = testing.DummyModel()
        request = testing.DummyRequest()
        renderer = testing.registerDummyRenderer('templates/add_feed.pt')
        response = add_feed_view(context, request)
        renderer.assert_(page_title='Add Feed')

    def test_add_feed_notsubmitted(self):
        from feedstool.views.site import add_feed_view
        context = testing.DummyModel()
        request = testing.DummyRequest()
        renderer = testing.registerDummyRenderer(
            'templates/add_feed.pt')
        response = add_feed_view(context, request)
        self.failIf(renderer.is_submitted)

    def test_add_feed_submitted_valid(self):
        from feedstool.views.site import add_feed_view
        context = testing.DummyModel()
        request = testing.DummyRequest(
            params={
                'form.submitted':True,
                'title':'Some Title',
                'url': 'someurl',
                }
            )
        renderer = testing.registerDummyRenderer(
            'templates/add_feed.pt')
        response = add_feed_view(context, request)
        self.assertEqual(response.location, 
                         'http://example.com/some-title/')

    def test_search_view(self):
        from feedstool.views.site import search_view
        context = testing.DummyModel()
        request = testing.DummyRequest(
            params={
                'searchterm': 'someword',
                }
            )
        renderer = testing.registerDummyRenderer('templates/search.pt')
        response = search_view(context, request)
        renderer.assert_(page_title='Search Results for someword')



class SiteViewIntegrationTests(unittest.TestCase):
    """ These tests are integration tests for the view.  These test
    the functionality the view *and* its integration with the rest of
    the repoze.bfg framework.  They cause the entire environment to be
    set up and torn down as if your application was running 'for
    real'.  This is a heavy-hammer way of making sure that your tests
    have enough context to run properly, and it tests your view's
    integration with the rest of BFG.  You should not use this style
    of test to perform 'true' unit testing as tests will run faster
    and will be easier to write if you use the testing facilities
    provided by bfg and only the registrations you need, as in the
    above ViewTests.
    """
    def setUp(self):
        """ This sets up the application registry with the
        registrations your application declares in its configure.zcml
        (including dependent registrations for repoze.bfg itself).
        """
        cleanUp()
        import feedstool
        import zope.configuration.xmlconfig
        zope.configuration.xmlconfig.file('configure.zcml',
                                          package=feedstool)

    def tearDown(self):
        """ Clear out the application registry """
        cleanUp()

    def test_list_feeds_view(self):
        from feedstool.views.site import list_feeds_view
        context = testing.DummyModel()
        request = testing.DummyRequest()
        result = list_feeds_view(context, request)
        self.assertEqual(result.status, '200 OK')
        body = result.app_iter[0]
        self.failUnless('Welcome to' in body)
        self.assertEqual(len(result.headerlist), 2)
        self.assertEqual(result.headerlist[0],
                         ('content-type', 'text/html; charset=UTF-8'))
        self.assertEqual(result.headerlist[1], ('Content-Length',
                                                str(len(body))))

