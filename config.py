import pymongo
import certifi

con_str = "mongodb+srv://hetheallemand:heep123@cluster0.ly7cdc8.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("goodies")