# Import required python packages & modules
import requests, json
import Connection as mgoConn

## Env Variables

# MongoDB hostname: we are using 'localhost as default'
host = 'localhost'
# MongoDB Port: we are using the default port
port = 27017

# MongoDB Database name
dbname = 'surveys'
# MongoDB Collection name
collection = 'abcsurvey'


# Online WFP/VAM data resources
api = 'https://api.ona.io/api/v1/data/'
dataId = 185260

url = api + str(dataId)

## Create a new connection
conn = mgoConn.Connection(host, port)
conn.connect(dbname, collection)


## Get data from ONA through the API
req = requests.get(url)

# Check the status of the request
if req.status_code != 200:
    print("GET request failed.")
    exit(1)

# Close the request
req.close()


# Examine request
#print(req.headers)

# Get the content of the request's response
data = req.content
# Convert the response as collection of JSON objects (dictionaries)
data = json.loads(data)


# Tracker for the document being process
tracker = 0

""" This will loop through the data (array)
and transform each document into a simplified version
before loading each of them into MongoDB Collection"""
for doc in data:
    tracker += 1

    newDoc = {
        'fid': doc.get('_id'),
        'age': doc.get('age', ''),
        'continent': doc.get('Continent', ''),
        'jm_haircut': doc.get('JM_haircut', ''),
        'borrow_food': doc.get('borrow_food', ''),
        'attachments': doc.get('_attachments', ''),
        'location': doc.get('_geolocation', ''),
        'avoid_eating': doc.get('avoid_eating', ''),
        'arif_moustache': doc.get('Arif_moustache', ''),
        'type_of_moustache': doc.get('type_of_moustache', ''),
        'less_preferred_food': doc.get('less_preferred_food', ''),
        'submission_datetime': doc.get('_submission_time', ''),
        'submitted_by': doc.get('_submitted_by', ''),
        'imported_on': '',
        'updated_on': ''
    }

    print(tracker)

    # Add to db
    conn.add(newDoc)


print("Total: ", tracker)
