import logging

import azure.functions as func

from azure.functions import Context
from azure.functions import AsgiMiddleware
from fastapi import FastAPI
import nest_asyncio

nest_asyncio.apply()
app = FastAPI()

@app.get("/api/hello")
def read_root():
    return {"message": "deploy from github actions"}

def main(req: func.HttpRequest, context: Context) -> func.HttpResponse:
    return AsgiMiddleware(app).handle(req, context)
