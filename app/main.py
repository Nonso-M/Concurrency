from utils import request
from fastapi import FastAPI
from cache import mongodb
from models import models




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
    """Code to run during startup"""
    # Start pool of connections to the Redis cache
    await mongodb.mongodb.start()



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/currencies/")
async def get_currencies():
    data = await request.parse_data1()
    return data
    

@app.get("/convert" )
async def converter(from_currency: str, to_currency: str, amount: float):
    data = await request.convert_currency(from_currency, to_currency, amount)
    mongodb.mongodb.update_db(dict(data))
    return data

@app.get("/history" )
async def converter(limit:str):
    data= mongodb.mongodb.retrieve_db()
    return data

    

@app.on_event("shutdown")
async def shutdown_event():
    """Code to run during shutdown"""
    await mongodb.mongodb.close()


# load_dotenv()
# URL = os.environ.get('URL') 
# client = pymongo.MongoClient(URL)


# post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#   }
# db = client['test-database']

# post_id = db.insert(post)

# print(URL)
# # client = pymongo.MongoClient(<Atlas connection string>)
