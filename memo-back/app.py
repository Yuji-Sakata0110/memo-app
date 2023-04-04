
from fastapi import FastAPI
import pymongo
import logging
from dotenv import load_dotenv
import os
import json
# avoid objectid error
from bson.json_util import dumps


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


    def fetch_one():
        db_con = database_connection.con()
        document = db_con.find_one({"name": "yujis"})
        logging.info(document)
        return json.loads(dumps(document))


    def fetch_all():
        db_con = database_connection.con()
        # cursor type
        cursor = db_con.find()
        # cursor to list type
        documents = [document for document in cursor]
        logging.info(documents)
        return json.loads(dumps(documents))


    def insert_one():
        db_con = database_connection.con()
        with open('data/insert_data.json') as f:
            data: dict = json.load(f)
            try:
                db_con.insert_one(data)
                logging.debug(data)
                logging.info("inserted to database")
                return {"message": "insert success"}
            except:
                return {"message": "insert failed"}


    def insert_many():
        db_con = database_connection.con()
        with open('data/insert_many_data.json') as f:
            data: dict = json.load(f)
            try:
                db_con.insert_many(data)
                logging.debug(data)
                logging.info("inserted to database")
                return {"message": "insert many success"}
            except:
                return {"message": "insert many failed"}


# routes
@memo_back.get("/")
async def root_get():
    return {"message": "Hello World"}


@memo_back.post("/")
async def root_post():
    return {"message": "Hello World, post"}


@memo_back.get("/fetch_one")
async def fetch_one_data():
    return {"message": database_connection.fetch_one()}


@memo_back.get("/fetch_all")
async def fetch_all_data():
    return {"message": database_connection.fetch_all()}


@memo_back.get("/insert_one")
async def insert_one_data():
    return {"message": database_connection.insert_one()}


@memo_back.get("/insert_many")
async def insert_many_data():
    return {"message": database_connection.insert_many()}