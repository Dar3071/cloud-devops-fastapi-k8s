import sys
import os
from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.exc import OperationalError
from sqlalchemy import text  # Import text function
from app.db import SessionLocal

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = FastAPI()

# Home Route
@app.get("/")
def read_root():
    return {"message": "FastAPI app homepage"} 

# Health Check Route
@app.get("/health")
def health_check():
    return {"status": "Health Check status OK"} 

@app.get("/db-check")
def db_check():
    try:
        db = SessionLocal()
        # Use the text() function to execute the query
        db.execute(text("SELECT 1"))
        return {"db_status": "connected"}
    except OperationalError:
        return {"db_status": "failed"}
    finally:
        db.close()





# Reset and start docker
# docker-compose down && docker-compose up --build


