from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

# Connect to http://127.0.0.1:8000/docs to get the wragger doc

@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return {'data':'This is all!'}