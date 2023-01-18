"""
Test for the main page using fastapi.testclient.
"""

from fastapi.testclient import TestClient
from app import main




client = TestClient(main.app)
username = 'Johnny'
password = 'Done'



def test_currency_route():
    """Testing the currency endpoint and affirming the output
    """ 
    response = client.get("/currencies", auth= (username,password))
    assert response.status_code == 200
    data = response.json()
    all(len(code)==3 for code in data.values())


def test_history_route():
    """Testing the history endpoint and affirming the output
    """    
    response = client.get("/history", auth=(username, password))
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)





def test_convert_route_with_correct_input():
    """Testing the convert route when a right query is made
    """
    dict_keys = ['converted_amount', 'rate', 'metadata']    
    response = client.get("/convert?from_currency=gbp&to_currency=usd&amount=100", auth=(username, password))
    assert response.status_code == 200
    data = response.json()
    all(x in list(data.keys()) for x in dict_keys)
 


def test_convert_route_with_wrong_input():
    """Testing the convert route when a bad request is made
    """
    dict_keys = ['code', 'failure']  
    response = client.get("/convert?from_currency=gbp&to_currency=usd&amount=100")
    data = response.json()
    all(x in list(data.keys()) for x in dict_keys)


