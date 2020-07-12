"""

1. Execute following query and store it as data.json

        GET village/_search
        {
          "size": 0,
          "query": {
            "bool": {
              "filter": [
                {
                  "terms": {
                    "region_id": [
                      1,
                      4593
                    ]
                  }
                }
              ]
            }
          },
          "aggs": {
            "villages": {
              "top_hits": {
                  "_source": {
                      "includes": [
                          "id",
                          "name",
                          "full_address"
                      ]
                  },
                  "size": 10000
            }
          }
          }
        }

2. Manually fix all strings with triple-"
3. Run this script


"""

import json

with open('data.json', 'r') as elastic_data:
    raw_data = elastic_data.read()
document = json.loads(raw_data)

with open('output.csv', 'tw') as csv_data:
    csv_data.write('id;name;full_address\r\n')
    for hit in document['aggregations']['villages']['hits']['hits']:
        csv_data.write('{};{};{}\r\n'.format(
            hit['_source']['id'],
            hit['_source']['name'],
            hit['_source']['full_address'],
        ))
