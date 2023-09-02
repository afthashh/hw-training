import scrapy
import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["olxdb"]
collection = db["rentals"]

class MySpider(scrapy.Spider):
    name = "new"

    start_urls = ['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723']

    def parse(self, response):
        yield from self.parse_listing(response)

    def parse_listing(self, response):
        properties = response.xpath('//li[contains(@class, "_1DNjI")]')
        for property in properties:
            relative_url = property.xpath('./a/@href').get()
            absolute_url = response.urljoin(relative_url)

            yield scrapy.Request(absolute_url, callback=self.parse_property)

    def parse_property(self, response):
        
        property_name = response.xpath('//h1[contains(@class, "_1hJph")]/text()').get()
        property_id = response.xpath('//div[contains(@class, "_1-oS0")]/strong/text()').re_first(r'\d+')
        breadcrumbs = response.xpath('//ol[contains(@class, "rui-2Pidb")]//li/a/text()').getall()
        price = response.xpath('//span[contains(@class, "T8y-z")]/text()').get().replace('₹','')
        image_url = response.xpath('//div[@class="_23Jeb"]/figure/img/@src').get()
        description = response.xpath('//div[@data-aut-id="itemDescriptionContent"]/p/text()').get()
        seller_name = response.xpath('//div[contains(@class, "eHFQs")]/text()').get()
        location = response.xpath('//span[contains(@class, "_1RkZP")]/text()').get()
        property_type = response.xpath('//span[contains(@class, "B6X7c")]/text()').get()
        bathrooms = response.xpath('//span[@data-aut-id="value_bathrooms"]/text()').get()
        bedrooms = response.xpath('//span[@data-aut-id="value_rooms"]/text()').get()

        data = {
            'property_url': response.url,
            'property_name': property_name,
            'property_id': property_id,
            'breadcrumbs': breadcrumbs,
            'price': {
                'amount': price,
                'currency': '₹',
            },
            'image_url': image_url,
            'description': description,
            'seller_name': seller_name,
            'location': location,
            'property_type': property_type,
            'bathrooms': bathrooms,
            'bedrooms': bedrooms,
        }

        self.save_to_mongodb(data)
        self.save_to_json(data)

    def save_to_json(self,data):
        filename = "output.json"
        # print(type(data))
        with open(filename, "a") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            file.write("\n")

    def save_to_mongodb(self, data):
        response=collection.insert_one(dict(data))
        print(response)





## CREATE
# new_property = {
#     'property_url': 'https://www.example.com/property/1234',
#     'property_name': 'Example Property',
#     'property_id': '1234567890',
#     'price': {
#         'amount': '1500',
#         'currency': '₹',
#     },
#     'location': 'Example Location',
#     'property_type': 'Example Type',
#     'bathrooms': '2',
#     'bedrooms': '3',
# }

# insert_result = collection.insert_one(new_property)
# if insert_result.inserted_id:
#     print(f"Property with ID {insert_result.inserted_id} created successfully.")
# else:
#     print("Failed to create the property.")



## READ
# property_id_to_read = "1616812515"  
# def read_from_mongodb(property_id):
#     result = collection.find_one({"property_id": property_id})
#     if result:
#         print("Read Data:")
#         print(result)
#     else:
#         print("Property not found in the database.")
# read_from_mongodb(property_id_to_read)



## UPDATE
# property_id_to_update = "1687330965"  
# updated_data = {
#     "price": {
#         "amount": "28,000", 
#         "currency": "₹"
#     },
#     "bedrooms": "4"  
# }
# def update_in_mongodb(property_id, updated_data):
#     result = collection.update_one({"property_id": property_id}, {"$set": updated_data})
#     if result.modified_count > 0:
#         print("Property updated successfully.")
#     else:
#         print("No matching property found for updating.")
# update_in_mongodb(property_id_to_update, updated_data)



## DELETE
# property_id_to_delete = "1687330965" 
# def delete_from_mongodb(property_id):
#     result = collection.delete_one({"property_id": property_id})
#     if result.deleted_count > 0:
#         print("Property deleted successfully.")
#     else:
#         print("No matching property found for deletion.")
# delete_from_mongodb(property_id_to_delete)

