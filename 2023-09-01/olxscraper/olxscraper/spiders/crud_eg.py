import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["olxdb"]
collection = db["rentals"]
# create
# data = {
#     'property_url': 'https://www.example.com/property/1234',
#     'property_name': 'Example Property',
#     'property_id': '01234567890',
#     'price': {
#         'amount': '15000',
#         'currency': '₹',
#     },
#     'location': 'Example Location',
#     'property_type': 'Example Type',
#     'bathrooms': '5',
#     'bedrooms': '5',
# }
# response=collection.insert_one(dict(data))
# print(response)


# # ------------------------------------------------------------


# # read
# query = {"property_id":"01234567890"}
# results = collection.find(query)
# for document in results:
#     print(document)


# # --------------------------------------------------------


# # update
# filter_query = {"property_id":"01234567890"}
# update_data = {"$set": {"bedrooms": "10"}}
# result = collection.update_one(filter_query, update_data)
# print("Modified documents:", result.modified_count)


# # -------------------------------------------------------------------


# # delete
# delete_query = {"property_id":"01234567890"}
# result = collection.delete_one(delete_query)
# print("Deleted document count:", result.deleted_count)