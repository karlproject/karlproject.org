
from repoze.bfg.traversal import find_root
from repoze.bfg.traversal import model_path

def index_content(object, event):
    catalog = getattr(find_root(object), 'catalog', None)
    path = model_path(object)
    docid = catalog.document_map.add(path)
    catalog.index_doc(docid, object)

