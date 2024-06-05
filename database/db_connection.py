
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# URI to connect to mongodb free server
uri = "mongodb+srv://cosentinosantiago92:ZVIxJad2oGIFQ2sz@timetracker.60srdxz.mongodb.net/?retryWrites=true&w=majority&appName=TimeTracker"

# Create a new client and connect to the server
client = MongoClient() # This connects to localhost
# client = MongoClient(uri, server_api=ServerApi('1')) # This connects to Mongo DB Atlas Server


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)