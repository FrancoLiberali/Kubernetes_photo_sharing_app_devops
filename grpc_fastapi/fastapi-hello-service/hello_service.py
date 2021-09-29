#!/usr/bin/env python3

import uvicorn

from fastapi import FastAPI, HTTPException
from fastapi import Path

from enum import Enum

app = FastAPI()

@app.get("/hello", status_code=200)
def say_hello():
    return {'message': 'hello'}

class HelloTypes(str, Enum):
    familiar = "familiar"
    formal = "formal"

@app.get("/hello/{firstname}", status_code=200)
def say_hello(firstname: str, level: HelloTypes = HelloTypes.familiar):
    if level == HelloTypes.familiar:
        return {'message': f'Hello, {firstname}'}
    elif level == HelloTypes.formal:
        return {'message': f'Nice to meet you, {firstname}'}


if __name__ == "__main__":
    uvicorn.run(app, log_level="info")

