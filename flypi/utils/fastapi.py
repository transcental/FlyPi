from fastapi import FastAPI

from flypi.couriers.asendia import Asendia

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/asendia/{tracking_number}")
async def asendia(tracking_number: str):
    data = await Asendia.fetch(tracking_number)
    return data
