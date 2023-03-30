
from fastapi import FastAPI
import pymongo
import logging
from dotenv import load_dotenv
import os

# load .env
load_dotenv(".env")
# fastapi app register
memo_back = FastAPI()

# logger setting
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler(os.environ.get("LOG_FOLDER")),
        logging.StreamHandler()
    ]
)

# database connection class
class database_connection():
    def con():
        try:
            client = pymongo.MongoClient(os.environ.get("MONGODB_URL"))
            logging.info("database connected")
            db = client["memo-db"]
            collection = db["memo"]
            return collection
        except:
            message = "connection error. Please check database connection."
            logging.error(message)
            return {"message": message}

    def find_one():
        db_con = database_connection.con()
        document = db_con.find_one()
        return document

    def find_all():
        db_con = database_connection.con()
        # cursor type
        cursor = db_con.find()
        # cursor to list type
        documents = [document for document in cursor]
        logging.info(documents)
        return documents


# routes
@memo_back.get("/")
async def root_get():
    return {"message": "Hello World"}

@memo_back.post("/")
async def root_post():
    return {"message": "Hello World, post"}

@memo_back.get("/feach_one")
async def feach_one_data():
    return {"message": database_connection.find_one()}

@memo_back.get("/feach_all")
async def feach_all_data():
    return {"message": database_connection.find_all()}