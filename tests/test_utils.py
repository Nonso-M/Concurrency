from app.utils import request
import pytest




def test_extract_value_from_dict(make_dict2):
    """Test the function for parsing the dictionary to check its functionality
    """
    dict_keys = ['converted_amount', 'rate', 'metadata']
    dir_dict = request.parse_data(make_dict2)
    assert type(dir_dict) == dict
    #assert the all the keys in the dict are what is expected on the endpoint
    all(x in list(dir_dict.keys()) for x in dict_keys)


def test_extract_value_when_dict_empty(make_dict3):
    """Tests when an invalid dict is passe into the function

    Args:
        make_dict3 (_type_): Pytest fixture
    """    
    dict_keys = ['code', 'failure']
    dir_dict = request.parse_data(make_dict3)
    assert type(dir_dict) == dict
    
    #assert the all the keys in the dict are what is expected on the endpoint
    all(x in list(dir_dict.keys()) for x in dict_keys)

