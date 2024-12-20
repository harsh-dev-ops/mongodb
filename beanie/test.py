from pymongo.mongo_client import MongoClient
import os
# uri = "mongodb+srv://harshkushwah2011:IJvzgZH4z7IXhjtC@test-cluster.l563h.mongodb.net/?retryWrites=true&w=majority&appName=test-cluster"

def _mongo_url():
    root_user_name = os.getenv('MONGO_INITDB_ROOT_USERNAME')
    root_password = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
    host = os.getenv('MONGO_HOST')
    port = os.getenv('MONGO_PORT')
    init_database = os.getenv('MONGO_INITDB_DATABASE')
    url = f"mongodb://{root_user_name}:{root_password}@{host}:{port}/{init_database}?authSource=admin&retryWrites=true&w=majority"
    return url

uri = _mongo_url()
print(uri)

# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)