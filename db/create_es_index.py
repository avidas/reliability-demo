from elasticsearch import Elasticsearch

host = 'http://localhost:9200'
es = Elasticsearch([host])
es.indices.create(index='reliability')
