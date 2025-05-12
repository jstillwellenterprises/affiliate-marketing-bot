from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient, errors
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    mongo_uri = os.getenv("MONGO_URI")
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    client.server_info()  # Force connection on startup
    db = client["affiliate"]
    collection = db["deals"]
    print("✅ Connected to MongoDB")
except errors.ServerSelectionTimeoutError as err:
    print("❌ MongoDB connection failed:", err)
    collection = None

@app.get("/")
def root():
    return {"status": "OK"}

@app.get("/deals")
def get_deals():
    if collection is None:
        return {"error": "Database connection failed"}
    return list(collection.find({}, {"_id": 0}))


