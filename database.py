from pymongo import MongoClient

MONGO_URI = "mongodb+srv://admin:<db_password>@cluster0.zfqotxw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client["mobile_app"]

user_collection = db["users"]
form_collection = db["forms"]
