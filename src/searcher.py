from elasticsearch import Elasticsearch

###

# relevant info of index name and the field within index to be searched
# should be same as that used in the indexer.py
searchParams = {'indexName': 'tmp-index-raw-text', 'hostname': 'localhost', 'port': '9200', 'searchResLen': 1000,
                'searchField': 'rawText'}

# initialize elastic search with parameters defined above
es = Elasticsearch([{'host': searchParams['hostname'], 'port': searchParams['port']}])

# search query
searchQuery = 'university'

# search within indexed documents is performed with this line
res = es.search(index=searchParams['indexName'], body={'size': searchParams['searchResLen'],
                                                       'query': {'match': {searchParams['searchField']: searchQuery}}})

# print using search results obtained
# 'res' is a json object 
# within that fields res['hits']['hits'] contain most of the relevant info
# 'res' object can be explored to find out all the other info it contains
print("")
print('Search results for query \'' + searchQuery + '\':')
print('==========')
count = 0
for e in res['hits']['hits']:
    print('rank:', count, ', doc id:', e['_source']['id'], ', score:', e['_score'])
    print('doc content:', e['_source'][searchParams['searchField']][:200], '...')
    print('==========')
    count += 1