from utils import request
from fastapi import FastAPI


app = FastAPI()



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
    return data








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
