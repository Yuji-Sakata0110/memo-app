
from fastapi import FastAPI
from routers import connections
import logging
import os
from dotenv import load_dotenv

# load .env
load_dotenv(".env")

# fastapi app register
memo_back = FastAPI()

# router import from submodules
memo_back.include_router(connections.router)

# logger setting
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler(os.environ.get("LOG_FOLDER")),
        logging.StreamHandler()
    ]
)