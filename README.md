# Information Retrieval System
Indexes large amounts of text files to then search with a query. (Can be modified easily modified to work with raw JSON objects)

## Requirements
Install ElasticSearch for Python, can be installed using pip:
```
pip install elasticsearch
```
Elasticsearch setup instructions can be found at the following link:
```
https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-install.html
```
## Usage
Edit the host variable in indexer.py to specify the ip of the server (localhost by default)
```
host = 'host-ip/localhost'
```
Edit the dataPath variable in indexer.py to specify the name of directory containing text files
```
dataPath = 'file-name/'
```
Edit the searchQuery variable in searcher.py to specify the search query
```
searchQuery = 'your query'
```
After running Elasticsearch locally, run indexer.py first, to create "successfullyIndexedIdList.txt", then edit the query in searcher.py and run.
## License
[MIT](LICENSE)

