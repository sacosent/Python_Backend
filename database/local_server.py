
### MongoDB client ###
from pymongo import MongoClient

# Create a new client and connect to the server
dbclient = MongoClient().local # This connects to localhost
