from fastapi import FastAPI
from config.utils import connect_to_mongo, close_mongo_connection
from api.main import router as main_router

app = FastAPI()

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)
app.include_router(main_router, prefix="/api")