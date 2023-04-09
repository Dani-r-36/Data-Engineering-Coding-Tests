import sys
sys.path.insert(1, './../')
from test_2 import open_csv, api_data
import pytest


def test_raise_open_csv():
    with pytest.raises(Exception, match = "Invaild location for CSV") as err:
        response = open_csv()

def test_api_data():
    response= api_data("z")
    assert "Invalid postcode" in response
    response= api_data("")
    assert "Invalid postcode" in response