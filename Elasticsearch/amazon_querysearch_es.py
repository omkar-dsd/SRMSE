from elasticsearch import Elasticsearch

es = Elasticsearch()

user_query = raw_input()

res = es.search(index = 'amazon-laptops', body = 
	{'query': {
		'match' : {
			'product' : user_query
		} 
	}
	})

# print("Got %d Hits:" % res['hits']['_source'])
print(res['hits'])
