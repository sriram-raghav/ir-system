# Information Retrieval System
Indexes large amounts of text files to then search with a query. (Can be modified easily modified to work with raw JSON objects)

## Requirements
Install ElasticSearch for Python, can be installed using pip:
```
pip install elasticsearch
```
Run Elasticsearch locally, instructions can be found at the following link:
```
https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-install.html
```
## Usage
Edit the dataPath variable in indexer.py to specify the name of directory containing text files
```
dataPath = 'file-name/'
```
Edit the searchQuery variable in searcher.py to specify the search query
```
searchQuery = 'your query'
```
## License
[MIT](LICENSE)

