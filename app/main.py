# The entry point of the microservice.
# Define FastAPI route & runs the server

from fastapi import FastAPI
from services import process_conversion, ConversionRequest

app = FastAPI()


@app.post("/conversion")
async def convert_ingredients(request: ConversionRequest):
    return process_conversion(request)
