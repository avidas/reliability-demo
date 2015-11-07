from elasticsearch import Elasticsearch

mappingJson = {
  "behave":{
    "_timestamp":{
      "enabled":True,
      "path": "date"
    },
  "properties":{
    "date":{
        "type": "date"
      },
      "duration":{
        "type": "string"
      },
      "feature":{
        "type": "string",
        "index":"not_analyzed"
      },
      "scenario":{
        "type": "string",
        "index":"not_analyzed"
      },
      "scenario_status":{
        "type": "string",
        "index":"not_analyzed"
      },
      "environment":{
        "type": "string",
        "index":"not_analyzed"
      },
    "step":{
        "type":"string",
        "index":"not_analyzed"
      },
      "step_number":{
        "type":"integer"
      },
      "status":{
        "type":"string"
      }
        }
    }
}

host = 'http://localhost:9200'
es = Elasticsearch([host])

result=es.indices.put_mapping(doc_type='behave', body=mappingJson, index=['reliability'])
print(result)
