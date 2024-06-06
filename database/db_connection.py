
### MongoDB client ###
from pymongo import MongoClient, server_api

# Create a new client and connect to the server
dbclient = MongoClient() # This connects to localhost

#-------------- Base de datos remota MongoDB Atlas (https://mongodb.com) --------------#
## URI to connect to mongodb free server
# uri = "mongodb+srv://cosentinosantiago92:ZVIxJad2oGIFQ2sz@timetracker.60srdxz.mongodb.net/?retryWrites=true&w=majority&appName=TimeTracker"
# dbclient = MongoClient(uri, server_api=server_api('1')) # This connects to Mongo DB Atlas Server
## dbclient = MongoClient("mongodb+srv://<user>:<password>@<url>/?retryWrites=true&w=majority").test

# Send a ping to confirm a successful connection
""" try:
    dbclient.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
"""