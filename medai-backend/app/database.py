from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient

# MongoDB connection string
MONGODB_URL = "mongodb://localhost:27017"
DATABASE_NAME = "medai"

# Create MongoDB client
client = AsyncIOMotorClient(MONGODB_URL)
db = client[DATABASE_NAME]

# Collections
forms_collection = db["forms"]
processed_forms_collection = db["processed_forms"]

# Synchronous client for operations that require it
sync_client = MongoClient(MONGODB_URL)
sync_db = sync_client[DATABASE_NAME]
