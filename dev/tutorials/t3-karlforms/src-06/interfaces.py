
from zope.interface import Interface
from zope.interface import Attribute
from repoze.folder.interfaces import IFolder

class ISite(IFolder):
    pass

class IPerson(Interface):
    name = Attribute(u'The name of the person')
    age = Attribute(u'An integer representing the age')
