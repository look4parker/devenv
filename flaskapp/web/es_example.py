import requests
import json
from elasticsearch import Elasticsearch

#connect to our cluster
def load_es_starwars_names():
    es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
    request = requests.get('http://elasticsearch:9200')
    i = 1
    while request.status_code == 200:
        request =  requests.get('http://swapi.co/api/people/'+ str(i))
        es.index(index='sw', doc_type='people', id=i, body=json.loads(request.content))
        i=i+1

def get_starwars_name(index):
    es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
    return es.get(index='sw', doc_type='people', id=index)

if __name__ == "__main__":
    load_es_starwars_names
