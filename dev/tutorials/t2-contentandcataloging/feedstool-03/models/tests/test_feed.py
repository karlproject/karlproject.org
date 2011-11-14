import unittest

from zope.testing.cleanup import cleanUp

class FeedTests(unittest.TestCase):

    def setUp(self):
        cleanUp()

    def tearDown(self):
        cleanUp()

    def _getTargetClass(self):
        from feedstool.models.feed import Feed
        return Feed

    def _makeOne(self, title=u'title', url=u'url',):
        tc = self._getTargetClass()
        return tc(title, url)

    def test_class_conforms_to_IFeed(self):
        from zope.interface.verify import verifyClass
        from feedstool.models.interfaces import IFeed
        verifyClass(IFeed, self._getTargetClass())

    def test_instance_conforms_to_IFeed(self):
        from zope.interface.verify import verifyObject
        from feedstool.models.interfaces import IFeed
        verifyObject(IFeed, self._makeOne())
