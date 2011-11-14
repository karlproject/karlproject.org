==============================
KARL 2 vs. KARL 3 Comparison
==============================

How does KARL3 compare to KARL2?  While the comparison isn't possible
in every aspect, many of the architectural features can be directly
stacked up, as shown below:

=====================	==============	===============
Item			KARL2		KARL3
===================== 	==============	===============
Programming language	Python		Python
Build system		buildout	buildout
Templating language	XSLT		ZPT (Chameleon)
Views	   		Skins, Fate, 	repoze.bfg functions
			ElementTree
Content type schemas	Archetypes,	Z3 Interfaces
			Z3 Interfaces
Content database	ZODB 3.7, ZEO	ZODB 3.8.1, 
			     	  	ZEO, BLOBs
Indexing		Xapian		ZCatalog
Object publisher	repoze.obob	repoze.bfg
App server		Zope 2.9, 	repoze.bfg,
    			repoze.plone,	WSGI
			WSGI
Content management	CMF, Plone	None
Ajax			MochiKit, XSLT	KSS, ExtJS
Forms			"Abused" AT, 	FormEncode,
			Fate, formlib	ZPT, lxml.html
Monitor			supervisor	supervisor
Editor			TinyMCE		TinyMCE
HTTP server		Apache, 	Apache (mod_wsgi)
     			CherryPy
Authentication		PAS (Zope),	PAS (repoze.who), 
			Postgresql	Postgresql
					SQLAlchemy
===================== 	==============	===============

