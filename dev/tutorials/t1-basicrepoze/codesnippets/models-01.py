from repoze.folder.interfaces import IFolder
from zope.interface import implements
from repoze.folder import Folder

class IFeedsContainer(IFolder):
    pass

class Site(Folder):
    implements(IFeedsContainer)

def appmaker(zodb_root):
    if not 'app_root' in zodb_root:
        app_root = Site()
        zodb_root['app_root'] = app_root
        import transaction
        transaction.commit()
    return zodb_root['app_root']
