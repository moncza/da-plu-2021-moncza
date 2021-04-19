from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello world!"}

@app.api_route(path="/method", methods=["GET", "POST", "DELETE", "PUT", "OPTIONS"])
def read_request(request: Request):
    return {"method": request.method}

class Patient(BaseModel):
    name: str
    surename: str

app.counter: int = 0
app.storage: Dict[int, Patient] = {}

@app.post("/register")
def show_data(patient: Patient):
    resp = {"id": app.counter,
            "patient": Patient}
    app.storage[app.counter] = patient
    app.counter += 1
    return resp


