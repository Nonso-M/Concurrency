import aiohttp
import asyncio
import os
import datetime
from dotenv import load_dotenv

load_dotenv()


# account_id = 'ehealth4everyone667749809'
# api_key = '1bn8ip05ghk76prqdq97guu35e'

account_id = os.environ.get('ACCOUNT_ID')
api_key= os.environ.get('API_KEY')


def parse_data(dictionary:dict)->dict:
    """ Take in a dictionary and parses it as specified in the pydantic model
    Args:
        dictionary (dict): Dictionary to be passed
    Returns:
        dict: parsed dictionary
    """  
    check = dictionary.get('to', 0)
    if check== 0:
        return { "code": "Failure",
                "message": "Invalid conversion strings"
                                                             }

    else:
        rate = round(dictionary['to'][0]['mid'] / dictionary['amount'], 2)
        conv_amount =  round(dictionary['to'][0]['mid'],2)
        from_currency = dictionary['from']
        to_currency = dictionary['to'][0]['quotecurrency']
        
        data = {
                    "converted_amount": conv_amount,
                    "rate": rate,
                    "metadata": {
                    "time_of_conversion": dictionary['timestamp'],
                    "from_currency": from_currency,
                    "to_currency": to_currency
                    }}
        return data




async def parse_data1()->dict:
    """ Take in a dictionary and parses it as specified in the pydantic model
    Args:
        dictionary (dict): Dictionary to be passed
    Returns:
        dict: parsed dictionary
    """  
    url = 'https://xecdapi.xe.com/v1/currencies/'
    print(url)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, auth=aiohttp.BasicAuth(account_id, api_key)) as response:
                dictionary = await response.json()

                return {data['currency_name']:data['iso'] for data in dictionary['currencies'] 
                            if data['is_obsolete'] ==False }


    except Exception as e:
        print(e)
        return {"Error": "The is is a network cnnection issue"}


async def convert_currency( to_currency:str, from_currency:str, amount:float)->dict:
    """This function converts from one currency to another when given their names and amount

    Args:
        from_currency (str): Currency you are converting from
        to_currency (str): Currency you are converting to
        amount (float): Aountyou want to convert

    Returns:
        dict: a dictionary that contains several keys and values about
                details of the conversion
    """   
    base_url = 'https://xecdapi.xe.com/v1/convert_from/' 
    query_string = f'?to={to_currency}&from={from_currency}&amount={amount}'
    full_url = base_url + query_string
    print(full_url)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(full_url, auth=aiohttp.BasicAuth(account_id, api_key)) as response:

                dictionary = await response.json()
                data = parse_data(dictionary)
                return data


    except Exception as e:
        print(e)
        return {"Error": "The is is a network cnnection issue"}



        
      


       



if __name__ == "__main__":
    print(asyncio.run(convert_currency('usd', 'gbp', 100)))