from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
 
@app.get("/")
def welcome():
    return {"message": "This is a simple API created using FastAPI"}
