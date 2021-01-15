import os
import pymongo

if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDb"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is Connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB:%s" % e)


# new_records = [{
#         "fname": "terri",
#         "lname": "pratchet",
#         "dob": "28/04/1948",
#         "hair_color": "not much"
#     },
#     {
#         "fname": "george",
#         "lname": "r r martin",
#         "dob": "20/09/1948",
#         "hair_color": "white"
#     }]

# coll.insert(new_record)
# coll.insert_many(new_records)
conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
# documents = coll.find({"lname": "lennon"})

# coll.remove({"fname": "george"})
coll.update_one({"fname": "terri"}, {"$set": {"hair_color": "white"}})
documents = coll.find()

for doc in documents:
    print(doc)





