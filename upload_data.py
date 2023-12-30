from pymongo.mongo_client import MongoClient
import pandas as pd
import json
# uniform resource identifier 
uri = "mongodb+srv://aladdin:ankit@cluster0.t8afsoj.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)

#create database nameand collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME="waferfault" 

#read the data as dataframe 
df=pd.read_csv("D:\MLproject\sensor_project\notebooks\wafer_23012020_041211.csv")

# convert the data into json 
json_recorder=json.load(df.T.to_json)

#now dump the data into the database 
client[DATABASE_NAME][COLLECTION_NAME]=json_recorder

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)