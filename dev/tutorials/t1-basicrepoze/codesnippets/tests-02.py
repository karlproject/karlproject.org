    def test_add_feed_view(self):
        from feedstool.views import add_feed_view
        context = testing.DummyModel()
        request = testing.DummyRequest()
        renderer = testing.registerDummyRenderer('templates/add_feed.pt')
        response = add_feed_view(context, request)
        renderer.assert_(page_title='Add Feed')

    def test_add_feed_notsubmitted(self):
        from feedstool.views import add_feed_view
        context = testing.DummyModel()
        request = testing.DummyRequest()
        renderer = testing.registerDummyRenderer(
            'templates/add_feed.pt')
        response = add_feed_view(context, request)
        self.failIf(renderer.is_submitted)

    def test_add_feed_submitted_valid(self):
        from feedstool.views import add_feed_view
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
