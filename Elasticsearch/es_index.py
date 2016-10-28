#this code puts the document into the index of elasticsearch

from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

doc = {
	
	'author' : 'Rakmo',
	'text' : 'something cool',
	'timestamp' : datetime.now(),
}

res = es.index(index="text-index", doc_type='tweet', id=1, body = doc)
print(res['created'])