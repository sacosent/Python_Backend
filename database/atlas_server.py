
### MongoDB client ###
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

#-------------- Base de datos remota MongoDB Atlas (https://mongodb.com) --------------#
username = quote_plus('sacosent')
password = quote_plus('hFzrMd23rD6gxonc')
cluster = 'timetracker.ulzcznb.mongodb.net'
appname = 'TimeTracker'
retrywrites = 'true'
w = 'majority'
authSource = 'admin'
authMechanism = '<authMechanism>'
# URI to connect to mongodb free server
uri = 'mongodb+srv://' + username + ':' + password + '@' + cluster + '/?retryWrites=' + retrywrites + '&w=' + w + '&appName=' + appname

dbclient = MongoClient(uri).timetracker_db
result = dbclient["<dbName"]["<collName>"].find()

# uri = 'mongodb+srv://' + username + ':' + password + '@' + cluster + '/?authSource=' + authSource + '&authMechanism=' + authMechanism
# dbclient = MongoClient(uri, server_api= ServerApi('1')) # This connects to Mongo DB Atlas Server
## dbclient = MongoClient("mongodb+srv://<user>:<password>@<url>/?retryWrites=true&w=majority").test

# Send a ping to confirm a successful connection
""" try:
    dbclient.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
"""