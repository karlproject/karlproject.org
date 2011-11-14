from zope.interface import implements
from repoze.folder import Folder

from t3.interfaces import ISite
from t3.interfaces import IPerson

class Site(Folder):
    implements(ISite)

class Person(Folder):
    implements(IPerson)

    def __init__(self, name, age, country=None):
        Folder.__init__(self)
        self.name = unicode(name)
        self.age = age
        if country is not None:
            self.country = unicode(country)

def appmaker(zodb_root):
    if not 'app_root' in zodb_root:
        app_root = Site()
        zodb_root['app_root'] = app_root
        import transaction
        transaction.commit()
    return zodb_root['app_root']
