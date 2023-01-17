from typing import Callable, Any, Optional
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

URL = os.environ.get('URL') 

client = MongoClient(URL)


# post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#   }
# db = client['test-database']

# post_id = db.insert(post)

# print(URL)
# # client = pymongo.MongoClient(<Atlas connection string>)




class MongoDb:
    """
    This class defines methods for connecting to the MongoDB client,
    loading data into the database, loading data from the database and
    closing the database connection
    """

    connect: Optional[MongoClient] = MongoClient(URL)

    async def start(self):
        """
        Connects to the MongoDB server
        """
        self.connect = MongoClient(URL)


    def get_collection(self):
        """This function gets a collection from mongo db database

        Args:
            self: instance of the class object
        """   
 
        db = self.connect['currency']
        collection = db['history']

        return collection


    def update_db(self, currency_info) -> None:
        """
        Sets the value for a key in the cache.
        Args:
            key (str): key
            value (str): value to save
            expire (int, optional): expire time (in seconds). Defaults to None.
        """

        collection = self.get_collection()
        collection.insert_one(currency_info)
        

    def retrieve_db(self) -> dict:
        """
        Gets the value for a key.
        Args:
            key (str): key
        Returns:
            str: value. Defaults to None if the key does not exist.
        """
        collection = self.get_collection()
        data = collection.find({})
        currencies = [x for x in data]
        for currency in currencies:
            del currency['_id']
        return currencies


    async def close(self) -> None:
        """Closes pool of connections"""
        await self.connect.close()

mongodb = MongoDb()



if __name__== "__main__":
    mongodb.start()
    data = mongodb.retrieve_db()
    # print([x for x in data])
    print(data)
    