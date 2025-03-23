import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

posts_database_obj = client['Posts']
students_database_obj = client['Students']

all_databases = client.list_database_names()
print(all_databases)


