import pymongo, datetime
from pymongo import MongoClient

# Create a connection to MongoDB
class Connection:

    def __init__(self, host = 'localhost', port = 27017):
        try:
            self.client = MongoClient(host, port)
            print("Connection to MangoDB Succeeded")

        except:
            print("Connection to MangoDB Failed.")
            exit(1)

    # connect to targeted database
    def connect(self, dbname, collection):
        # get the list of existing db
        dbs = self.client.list_database_names()

        if len(dbs) > 0 and dbname in dbs:
            print("Using DB: ", dbname)

        else:
            print("Database not found, Creating new one ...")

        # select the targeted db
        self.db = self.client[dbname]

        # select the targeted collection
        self.selectDBCollection(collection)

    # Identify Target Collection
    def selectDBCollection(self, collection):
        dbCols = self.db.list_collection_names()

        if len(dbCols) > 0 and collection in dbCols:
            print("Using this collection: ", collection)
            self.collection = self.db[collection]

        else:
            print("collection not found. Creating a new collection ...")

            try:
                self.db.create_collection(collection)
                self.collection = self.db[collection]
                print("Completed: ", self.db.list_collection_names())

            except:
                print("Failed to create a new collection")

    # Find document by ID
    def find(self, id):
        return self.collection.count_documents({"fid": id})

    # Add new objects
    def add(self, doc):

        n = self.find(doc['fid'])

        print(n)

        if n == 0:
            doc['imported_on'] = datetime.datetime.utcnow()
            self.collection.insert_one(doc)
        elif n == 1:
            self.edit(doc)
        else:
            print("Error - duplicated doc with ID: ", doc['fid'])

    # Update existing document
    def edit(self, doc):
        # get existing object
        oldDoc = self.collection.find({'fid': doc['fid']})
        # update time tracker
        doc['imported_on'] = oldDoc[0].get('imported_on', datetime.datetime.utcnow())
        doc['updated_on'] = datetime.datetime.utcnow()
        # replace old object with new one
        self.collection.replace_one({'fid': doc['fid']}, doc)


# Eg: Instantiate the connection class
#conn = Connection()

#conn.connect('bk-test', 'demosurvey')

# conn.client.list_database_names()
# conn.db.list_collection_names()
# conn.client.list_database_names()




