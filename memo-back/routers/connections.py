from fastapi import APIRouter
from dotenv import load_dotenv
from db import db_connection as cons

# load .env
load_dotenv(".env")

router = APIRouter()

# routes
@router.get("/")
async def root_get():
    return {"message": "Hello World"}


@router.post("/")
async def root_post():
    return {"message": "Hello World, post"}


@router.get("/fetch_one")
async def fetch_one_data():
    return {"message": cons.database_connection.fetch_one()}


@router.get("/fetch_all")
async def fetch_all_data():
    return {"message": cons.database_connection.fetch_all()}


@router.get("/insert_one")
async def insert_one_data():
    return {"message": cons.database_connection.insert_one()}


@router.get("/insert_many")
async def insert_many_data():
    return {"message": cons.database_connection.insert_many()}