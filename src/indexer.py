import os
from elasticsearch import Elasticsearch


# function to add a text document to the index
# doc is a json object (dictionary) containing info about doc
def addToIndex(doc, indexName, docType, es):
    try:
        dId = doc['id']
        res = es.index(index=indexName, doc_type=docType, id=dId, body=doc, request_timeout=1000)
        return True
    except Exception as e:
        print('Failed to index: ' + doc['docId'])
        print(e.info)
        return False


###

dataPath = 'sample-text-data/'  # documents path
dataFileExt = 'txt'  # documents file name extensions
indexName = 'tmp-index-raw-text'  # name of the new index to be created
docType = 'doc-raw-text'  # some description of the doc content type
host = 'localhost'  # can be replaced with ip address (such as '9.1.1.1') of the machine running elasticsearch server.
port = '9200'  # port

# initialize elastic search object
es = Elasticsearch([{'host': host, 'port': port}])

# get list of file names that contain docs to be indexed in directory 'dataPath' and with file extensions 'dataFileExt'
fileIdLst = [f.split('.')[0].strip() for f in os.listdir(dataPath) if
             (os.path.isfile(os.path.join(dataPath, f)) and f.split('.')[-1] == dataFileExt)]
print(str(len(fileIdLst)) + ' docs to be indexed.')

count = 0
successCount = 0
failLst = []
failCount = 0
indexedIdLst = []
for fId in fileIdLst:
    doc = {'id': fId, 'rawText': open(os.path.join(dataPath, fId + '.' + dataFileExt), encoding="utf8").read()}
    successFlag = addToIndex(doc, indexName, docType, es)
    if successFlag:
        indexedIdLst.append(doc['id'])
        successCount += 1
    else:
        failLst.append(doc['id'])
        failCount += 1
    count += 1
    if count % 10000 == 0:
        print(str(successCount) + ' / ' + str(count) + ' - indexed successfully')
        es.indices.flush(index=indexName)

print('SuccessCount:', successCount)
print('FailCount:', failCount)
print('FailLst:', failLst)
print('Total ' + str(successCount) + ' successfully indexed out of ' + str(count))

with open('successfullyIndexedIdList.txt', 'w') as fop:
    for indexedId in indexedIdLst:
        fop.write("%s\n" % indexedId)
    fop.close()
print('List of successfully indexed id list are stored in file \'successfullyIndexedIdList.txt\'')