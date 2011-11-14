""" update_feeds [OPTIONS] 

Iterate through each Feed in the FeedContainer, download each Atom
feed, and make new FeedEntry objects.

Options
=======

--config (-c)            Path to ini file (defaults to $CWD/FeedsTool.ini)

--dry-run (-d)           Don't actually commit the transaction

"""

import getopt
import sys
import os
import transaction

from paste.deploy import loadapp
from repoze.bfg.registry import registry_manager
import feedparser
from feedstool.models.interfaces import IFeedEntry

from repoze.lemonade.content import create_content

def log_debug(msg):
    pass

def update(site):

    fmt = "Feed %s failed to parse because %s on line %s"

    for feed in site.values():
        print "Processing", feed.title, "at", feed.url
        d = feedparser.parse(feed.url)

        import pdb;pdb.set_trace()

        if d.bozo==1:
            exc = d.bozo_exception()
            msg = fmt % (feed.url, exc.getMessage(), exc.getLineNumber())
            log_debug(msg % msg)

        # XXX Store etag and last-modified to conserve bandwidth and
        # not get banned from some feeds. 
        feed_title = d.feed.title
        feed_subtitle = d.feed.subtitle
        feed_etag = d.etag
        feed_id = d.feed.id
        feed_updated = d.feed.updated
        for entry in d['entries']:
            title = entry.title
            link = entry.link
            id = entry.id
            published = entry.published
            updated = entry.updated
            summary = entry.summary
            content = entry.content[0]['value']
            fe = create_content(
                IFeedEntry, title, summary
                )
            name = id

    return

def usage(self, message=None, rc=1):
    print __doc__
    if message is not None:
        print message
        print
    sys.exit(rc)

def main(argv=sys.argv):
    name, argv = argv[0], argv[1:]

    try:
        opts, args = getopt.getopt(argv, 'c:dh?',
                                         ['config=',
                                          'dry-run',
                                          'help'
                                         ])
    except getopt.GetoptError, e:
        usage(e)

    config = None
    dry_run = False

    for k, v in opts:
        if k in ('-c', '--config'):
            config = v
        if k in ('-d', '--dry-run'):
            dry_run = True
        elif k in ('-h', '-?', '--help'):
            usage(rc=2)
        
    if config is None:
        # we assume that the console script lives in the 'bin' dir of a
        # sandbox or buildout, and that the .ini file lives in the 'etc'
        # directory of the sandbox or buildout
        me = sys.argv[0]
        me = os.path.abspath(me)
        sandbox = os.path.dirname(os.path.dirname(os.path.dirname(me)))
        #config = os.path.join(sandbox, 'etc', 'osi.ini')
        config = os.path.join(sandbox, 'FeedsTool.ini')

    config = os.path.abspath(os.path.normpath(config))

    app = loadapp('config:%s' % config, name='zodb')
    environ = {}
    registry_manager.set(app.registry)
    root = app.root_policy(environ)
    update(root)
    if dry_run:
        transaction.abort()
    else:
        transaction.commit()

if __name__ == '__main__':
    main()
