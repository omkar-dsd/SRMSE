from datetime import datetime
from elasticsearch import Elasticsearch

#by default we connect to localhost:9200

es = Elasticsearch()

with open('/home/omkar/SRMSE/Scrapers/NasaScraper/spacymissions.json', 'r') as content_file:
    content = content_file.read()

es.index(index="nasa", doc_type="missions", id=1, body=("{" + "\"pikachu\"" + " : " + content + "}"))