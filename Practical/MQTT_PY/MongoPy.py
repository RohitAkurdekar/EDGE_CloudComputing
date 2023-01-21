# Python code to illustrate
# inserting data in MongoDB
from pymongo import MongoClient
  
try:
    conn = MongoClient("192.168.77.205")
    print("Connected successfully!!!")
except:  
    print("Could not connect to MongoDB")
  
# database
db = conn.database
  
# Created or Switched to collection names: my_gfg_collection
collection = db.my_gfg_collection

# Insert Data
def send_data(data):
    collection.insert_one(data)
    print("Data inserted successfully...!!!")
  
# Printing the data inserted

def print_data():

    cursor = collection.find()
    for record in cursor:
        print(record)