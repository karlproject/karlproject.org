from repoze.folder import Folder
from zope.interface import implements

from feedstool.models.interfaces import IFeedEntry

class FeedEntry(Folder):
    implements(IFeedEntry)
    title = None
    link = None
    id = None
    published = None
    updated = None
    summary = None
    content = None
    
    def __init__(self, title, link):

        super(FeedEntry, self).__init__()
        self.title = title
        self.link = link


