import logging
import pymongo
import logging
import os
import json
from dotenv import load_dotenv
# avoid objectid error
from bson.json_util import dumps

# load .env
load_dotenv(".env")

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