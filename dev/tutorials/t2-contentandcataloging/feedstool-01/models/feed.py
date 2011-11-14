
from repoze.folder import Folder
from zope.interface import implements

from feedstool.models.interfaces import IFeed

class Feed(Folder):
    implements(IFeed)
    persist_entries = True
    fetch_enclosures = False
    subtitle = None
    etag = None
    last_modified = None
    id = None
    updated = None

    def __init__(self, title, url):

        super(Feed, self).__init__()
        self.title = unicode(title)
        self.url = unicode(url)
