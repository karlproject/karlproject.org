import unittest

from zope.testing.cleanup import cleanUp
from repoze.bfg import testing

class SiteModelTests(unittest.TestCase):

    def setUp(self):
        """ cleanUp() is required to clear out the application registry
        between tests (done in setUp for good measure too)
        """
        cleanUp()
        
    def tearDown(self):
        """ cleanUp() is required to clear out the application registry
        between tests
        """
        cleanUp()

    def _getTargetClass(self):
        from t3.models import Site
        return Site

    def _makeOne(self):
        tc = self._getTargetClass()
        return tc()

    def test_class_conforms_to_ISite(self):
        from zope.interface.verify import verifyClass
        from t3.models import ISite
        verifyClass(ISite, self._getTargetClass())

    def test_instance_conforms_to_IFeed(self):
        from zope.interface.verify import verifyObject
        from t3.models import ISite
        verifyObject(ISite, self._makeOne())


class PersonModelTests(unittest.TestCase):

    def setUp(self):
        """ cleanUp() is required to clear out the application registry
        between tests (done in setUp for good measure too)
        """
        cleanUp()
        
    def tearDown(self):
        """ cleanUp() is required to clear out the application registry
        between tests
        """
        cleanUp()

    def _getTargetClass(self):
        from t3.models import Person
        return Person

    def _makeOne(self, name=u'Dummy', age=30, country=u'FR'):
        tc = self._getTargetClass()
        return tc(name, age, country)

    def test_class_conforms_to_IPerson(self):
        from zope.interface.verify import verifyClass
        from t3.models import IPerson
        verifyClass(IPerson, self._getTargetClass())

    def test_instance_conforms_to_IFeed(self):
        from zope.interface.verify import verifyObject
        from t3.models import IPerson
        verifyObject(IPerson, self._makeOne())

class ViewTests(unittest.TestCase):

    """ These tests are unit tests for the view.  They test the
    functionality of *only* the view.  They register and use dummy
    implementations of repoze.bfg functionality to allow you to avoid
    testing 'too much'"""

    def setUp(self):
        """ cleanUp() is required to clear out the application registry
        between tests (done in setUp for good measure too)
        """
        cleanUp()
        
    def tearDown(self):
        """ cleanUp() is required to clear out the application registry
        between tests
        """
        cleanUp()

    def test_list_people(self):
        from t3.views import list_people_view
        context = testing.DummyModel()
        request = testing.DummyRequest()
        renderer = testing.registerDummyRenderer('templates/list_people.pt')
        response = list_people_view(context, request)
        self.assert_(hasattr(renderer, 'layout'))

    def test_add_person(self):
        from t3.views import add_person_view
        context = testing.DummyModel()
        request = testing.DummyRequest()
        renderer = testing.registerDummyRenderer('templates/add_person.pt')
        response = add_person_view(context, request)
        self.assert_(hasattr(renderer, 'layout'))

    def test_show_person(self):
        from t3.views import show_person_view
        context = DummyPerson()
        request = testing.DummyRequest()
        renderer = testing.registerDummyRenderer('templates/show_person.pt')
        response = show_person_view(context, request)
        self.assert_(hasattr(renderer, 'layout'))

    def test_edit_person(self):
        from t3.views import edit_person_view
        context = DummyPerson()
        request = testing.DummyRequest()
        renderer = testing.registerDummyRenderer('templates/edit_person.pt')
        response = edit_person_view(context, request)
        self.assert_(hasattr(renderer, 'layout'))



class ViewIntegrationTests(unittest.TestCase):
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
        import t3
        import zope.configuration.xmlconfig
        zope.configuration.xmlconfig.file('configure.zcml',
                                          package=t3)

    def tearDown(self):
        """ Clear out the application registry """
        cleanUp()

    def test_list_people_view(self):
        from t3.views import list_people_view
        context = testing.DummyModel()
        request = testing.DummyRequest()
        result = list_people_view(context, request)
        self.assertEqual(result.status, '200 OK')
        body = result.app_iter[0]
        self.failUnless('KARL3 Forms' in body)
        self.assertEqual(len(result.headerlist), 2)
        self.assertEqual(result.headerlist[0],
                         ('Content-Type', 'text/html; charset=UTF-8'))
        self.assertEqual(result.headerlist[1], ('Content-Length',
                                                str(len(body))))

    def test_add_person_view(self):
        from t3.views import add_person_view
        context = testing.DummyModel()
        request = testing.DummyRequest()
        result = add_person_view(context, request)
        self.assertEqual(result.status, '200 OK')
        body = result.app_iter[0]
        self.failUnless('KARL3 Forms' in body)
        self.assertEqual(len(result.headerlist), 2)
        self.assertEqual(result.headerlist[0],
                         ('Content-Type', 'text/html; charset=UTF-8'))
        self.assertEqual(result.headerlist[1], ('Content-Length',
                                                str(len(body))))

    def test_show_person_view(self):
        from t3.views import show_person_view
        context = DummyPerson()
        request = testing.DummyRequest()
        result = show_person_view(context, request)
        self.assertEqual(result.status, '200 OK')
        body = result.app_iter[0]
        self.failUnless('KARL3 Forms' in body)
        self.assertEqual(len(result.headerlist), 2)
        self.assertEqual(result.headerlist[0],
                         ('Content-Type', 'text/html; charset=UTF-8'))
        self.assertEqual(result.headerlist[1], ('Content-Length',
                                                str(len(body))))

    def test_edit_person_view(self):
        from t3.views import edit_person_view
        context = DummyPerson()
        request = testing.DummyRequest()
        result = edit_person_view(context, request)
        self.assertEqual(result.status, '200 OK')
        body = result.app_iter[0]
        self.failUnless('KARL3 Forms' in body)
        self.assertEqual(len(result.headerlist), 2)
        self.assertEqual(result.headerlist[0],
                         ('Content-Type', 'text/html; charset=UTF-8'))
        self.assertEqual(result.headerlist[1], ('Content-Length',
                                                str(len(body))))

class DummyPerson(testing.DummyModel):

    name = u'Dummy Name'
    age = 23
    country = u'FR'
