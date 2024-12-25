""" from pymongo import MongoClient

# MongoDB bağlantısı
client = MongoClient("mongodb+srv://baydanemre:SP5PfDb5_PsM@complaint-cluster.ijzcq.mongodb.net/")
db = client["user_complaints"]
collection = db["complaints"]

# Koleksiyondaki tüm belgeleri sil
//collection.delete_many({})
print("Tüm veriler silindi.") """