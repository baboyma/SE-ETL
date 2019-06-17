# SE-ETL: Python + MongoDB

This repo is a small ETL (Extract, Transform and Load) tool, mainly built in response to a task from WFP/VAM Data Science team.
The tool, built with Python and MongoDB, does 3 main tasks:
1. extracts survey data hosted on ONA Platform through an API
2. clean up the data
3. loads the data to a MongoDB Database

Note: the tool is set to run on a development environment (laptop) but you may update the hostname, port, database and collection names to point to external servers.

There are only 2 files in this repo:
1. Connection.py is a Class used to initiate the connection to a server/db and take care of some CRUD operations.
2. etl-taks.py loads the Connection class, reads data through an API, transfrom each document and hands them over to Connection class for the CRUD.


## Libraries

We used 3 Python Packages:

1. requests: used for make a GET call to ONA API end-point
2. json: used to convert the response into json format
3. PyMongo: used to interact with a local MongoDB server

```python
pip install requests
pip install json
pip install pymongo
```

## Execution

Before you run the script, make sure you've installed MongoDB on your machine and it's running as a service.
I am using MongoDB 4.0 on MacOS and you can find the documentation [here](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)

You may want to use your terminal to make sure that your MongoDB is working properly. [Here](https://docs.mongodb.com/manual/crud/) is a link to some basic CRUD operations.

Clone this repo and execute 
```python
python etl-task.py
```


Let me know how it works on your end. 
I am open to feedback. Thank you in advance.


