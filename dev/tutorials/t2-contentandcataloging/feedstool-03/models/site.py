
from repoze.folder import Folder
from zope.interface import implements

from feedstool.models.interfaces import IFeedsContainer

from repoze.catalog.catalog import Catalog
from repoze.catalog.indexes.text import CatalogTextIndex
from repoze.catalog.indexes.keyword import CatalogKeywordIndex
from repoze.catalog.document import DocumentMap
from zope.interface.declarations import Declaration
from zope.interface import providedBy


def get_interfaces(object, default):
    # we unwind all derived and immediate interfaces using spec.flattened()
    # (providedBy would just give us the immediate interfaces)
    provided_by = list(providedBy(object))
    spec = Declaration(provided_by)
    ifaces = list(spec.flattened())
    return ifaces

def get_textrepr(object, default):
    return getattr(object, 'title', default)


class Site(Folder):
    implements(IFeedsContainer)

    def __init__(self):
        super(Site, self).__init__()
        self.catalog = sc = Catalog()
        sc['interfaces'] = CatalogKeywordIndex(get_interfaces)
        sc['texts'] = CatalogTextIndex(get_textrepr)
        sc.document_map = DocumentMap()

def appmaker(zodb_root):
    if not 'app_root' in zodb_root:
        app_root = Site()
        zodb_root['app_root'] = app_root
        import transaction
        transaction.commit()
    return zodb_root['app_root']
