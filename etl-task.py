import requests, json
import './libs/Connection.py' as mgoConn

# Env Variables
host = 'localhost'
port = 27017

dbname = 'surveys'
collection = 'abcsurvey'

api = 'https://api.ona.io/api/v1/data/'
dataId = 185260

url = api + str(dataId)

## Create a new connection
conn = mgoConn.Connection(host, port)
conn.connect(dbname, collection)


## Get data from ONA through the API
req = requests.get(url)

print(req.headers)

if req.status_code != 200:
    print("GET request failed.")
    exit(1)

# Close the connection
req.close()


# Examine request
#print(req.headers)

data = req.content

data = json.loads(data)

#print(len(data))

#print(data[0])

tracker = 0

for doc in data:
    tracker += 1

    print(doc['_id'])

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

    print(newDoc)

    # Add to db
    conn.add(newDoc)

print("Total: ", tracker)
