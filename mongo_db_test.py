import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
load_dotenv()

uri = f"mongodb+srv://{os.environ.get('MONGO_DB_USERNAME')}:{os.environ.get('MONGO_DB_PASSWORD')}@cluster0.nlx3aur.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

client = MongoClient(uri)
collections = client['STRANGER']['PHISING']
df = pd.DataFrame(list(collections.find()))
print(df)