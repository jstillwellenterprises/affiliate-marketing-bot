from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import os

app = FastAPI()

# Allow requests from frontend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # NOTE: Lock this down in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection using environment variable
mongo_uri = os.getenv("MONGO_URI")  # Set this in Render
client = MongoClient(mongo_uri)
db = client["affiliate"]  # your database name
collection = db["deals"]  # your collection with scraped items

@app.get("/")
def read_root():
    return {"message": "Affiliate backend is live!"}

@app.get("/deals")
def get_deals():
    # Return all documents, hide MongoDB _id
    return list(collection.find({}, {"_id": 0}))

