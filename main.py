from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# Read response.json and upload to MongoDB
import json
uri = "mongodb+srv://<username>:<password>@cluster0.9umowyn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    with open('response.json', 'r') as file:
        data = json.load(file)
    
    # Assuming we want to store this in a collection called 'companies'
    db = client['your_database_name']
    collection = db['companies']
    
    # Insert the data into the collection
    result = collection.insert_many(data)
    
    print(f"Inserted {len(result.inserted_ids)} documents into the collection.")

except Exception as e:
    print(e)