import unittest

from zope.testing.cleanup import cleanUp

class SiteTests(unittest.TestCase):

    def setUp(self):
        cleanUp()

    def tearDown(self):
        cleanUp()

    def _getTargetClass(self):
        from feedstool.models.site import Site
        return Site

    def _makeOne(self):
        tc = self._getTargetClass()
        return tc()

    def test_class_conforms_to_IFeedsContainer(self):
        from zope.interface.verify import verifyClass
        from feedstool.models.interfaces import IFeedsContainer
        verifyClass(IFeedsContainer, self._getTargetClass())

    def test_instance_conforms_to_IFeedsContainer(self):
        from zope.interface.verify import verifyObject
        from feedstool.models.interfaces import IFeedsContainer
        verifyObject(IFeedsContainer, self._makeOne())