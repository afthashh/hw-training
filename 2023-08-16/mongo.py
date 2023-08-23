from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['mydb']

collection = db['students']

document = {"name": "John", "age": 30}
result = collection.insert_one(document)
print("Inserted ID:", result.inserted_id)

documents = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 28}
]
result = collection.insert_many(documents)
print("Inserted IDs:", result.inserted_ids)

all_documents = collection.find()
for doc in all_documents:
    print(doc)

# query = {"Name": "Tom"}  
# update = {"$set": {"age": 25}}  
# collection.update_one(query, update)
# print(doc)

# collection.delete_one({"name": "John"})