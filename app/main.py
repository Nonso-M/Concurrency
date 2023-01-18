from utils import request
from fastapi import FastAPI, Depends
from cache import mongodb
from models.models import Convert, History, Error
from typing import Union
from security.authentication import get_current_username



description = """
            This is a currency conversion API that converts from on denomination to
            another 
            There three major endpoints in this application
            ### Currency
            This endpoint lists all **available currencies** that are not obsolete.

            ### Convert
            * In this endpoint you willl be able to convert from one currency to another.
            * You will provide the **from_currency**, **to_currency** and **amount** parameters

            ### History
            This endpoints retrieves all previous requests to the API.
            """


app = FastAPI(
    title="Currency Converter",
    description=description,
    version="0.0.1",
    contact={
        "name": "Nonso",
        "url": "https://www.linkedin.com/in/nonso-muolokwu/",
        "email": "muolokwunonso@gmail.com",
    },
)

@app.on_event("startup")
async def startup_event():
    """Code to run during startup (Initialize connection to the mongodb server)"""
    # Start pool of connections to the Redis cache
    await mongodb.mongodb.start()



@app.get("/")
async def root(username: str = Depends(get_current_username)):
    return {"message": "Welcome to my Currency Converter!"}



@app.get("/currencies/", tags = ["currency"])
async def get_currencies(username: str = Depends(get_current_username)):    
    data = await request.parse_currency_data()
    return data



@app.get("/convert", response_model= Union[Convert, Error], tags = ["Convert"])
async def converter(from_currency: str, to_currency: str, amount: float,
                        username: str = Depends(get_current_username)):
    data = await request.convert_currency(from_currency, to_currency, amount)
    if 'rate' in data.keys():
      mongodb.mongodb.update_db(dict(data))
    return data



@app.get("/history", response_model= History, tags= ["history"] )
async def converter(username: str = Depends(get_current_username)):
    data= mongodb.mongodb.retrieve_db()
    return data



@app.on_event("shutdown")
async def shutdown_event():
    """Code to run during shutdown"""
    await mongodb.mongodb.close()

