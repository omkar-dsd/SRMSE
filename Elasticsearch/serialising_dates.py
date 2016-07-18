from datetime import datetime
from elasticsearch import Elasticsearch

#by default we connect to localhost:9200

es = Elasticsearch()

es.index(index="my-index", doc_type="test-type", id=42, body={"any":"data","timestamp":datetime.now()})