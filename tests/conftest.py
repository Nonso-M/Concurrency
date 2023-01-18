import pytest

dictionary = [{'iso': 'GBP', 'currency_name': 'British Pound', 'is_obsolete': False},
  {'iso': 'GEL', 'currency_name': 'Georgian Lari', 'is_obsolete': False},
  {'iso': 'GGP', 'currency_name': 'Guernsey Pound', 'is_obsolete': False},
  {'iso': 'GHS', 'currency_name': 'Ghanaian Cedi', 'is_obsolete': False},
  {'iso': 'GIP', 'currency_name': 'Gibraltar Pound', 'is_obsolete': False},
  {'iso': 'GMD', 'currency_name': 'Gambian Dalasi', 'is_obsolete': False},
  {'iso': 'GNF', 'currency_name': 'Guinean Franc', 'is_obsolete': False},
  {'iso': 'GTQ', 'currency_name': 'Guatemalan Quetzal', 'is_obsolete': False},
  {'iso': 'GYD', 'currency_name': 'Guyanese Dollar', 'is_obsolete': False},
  {'iso': 'HKD', 'currency_name': 'Hong Kong Dollar', 'is_obsolete': False},
  {'iso': 'HNL', 'currency_name': 'Honduran Lempira', 'is_obsolete': False},
  {'iso': 'HTG', 'currency_name': 'Haitian Gourde', 'is_obsolete': False},
  {'iso': 'HUF', 'currency_name': 'Hungarian Forint', 'is_obsolete': False},
  {'iso': 'IDR', 'currency_name': 'Indonesian Rupiah', 'is_obsolete': False},
  {'iso': 'ILS', 'currency_name': 'Israeli Shekel', 'is_obsolete': False},
  {'iso': 'IMP', 'currency_name': 'Isle of Man Pound', 'is_obsolete': False},
  {'iso': 'INR', 'currency_name': 'Indian Rupee', 'is_obsolete': False},
  {'iso': 'IQD', 'currency_name': 'Iraqi Dinar', 'is_obsolete': False},
  {'iso': 'IRR', 'currency_name': 'Iranian Rial', 'is_obsolete': False},
  {'iso': 'ISK', 'currency_name': 'Icelandic Krona', 'is_obsolete': False},
  {'iso': 'JEP', 'currency_name': 'Jersey Pound', 'is_obsolete': False},
  {'iso': 'JMD', 'currency_name': 'Jamaican Dollar', 'is_obsolete': False},
  {'iso': 'JOD', 'currency_name': 'Jordanian Dinar', 'is_obsolete': False},
  {'iso': 'JPY', 'currency_name': 'Japanese Yen', 'is_obsolete': False},
  {'iso': 'KES', 'currency_name': 'Kenyan Shilling', 'is_obsolete': False}]


dict1 = {'terms': 'http://www.xe.com/legal/dfs.php',
        'privacy': 'http://www.xe.com/privacy.php',
        'from': 'GBP',
        'amount': 100.0,
        'timestamp': '2023-01-16T00:00:00Z',
        'to': [{'quotecurrency': 'USD', 'mid': 122.248317431}]}

dict2= {'code': 7,
          'message': 'No USD29 found on 2023-01-17T19:00:48Z',
          'documentation_url': 'https://xecdapi.xe.com/docs/v1/'}


@pytest.fixture
def make_dict():

    return dictionary


@pytest.fixture
def make_dict2():

    return dict1

@pytest.fixture
def make_dict3():

    return dict2