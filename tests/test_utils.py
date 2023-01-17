from app.utils import request
import pytest




def test_extract_old_nhmis_data(make_dict):
    """Test the function for parsing the dictionary to check its functionality
    """
    dir_dict = request.parse_data(make_dict)
    assert type(dir_dict) == dict
    #assert the values of the dictionary al have lenght of three e.g USD, GBP
    all(len(code)==3 for code in dir_dict.values())

