import sys
sys.path.insert(1, './../')
from test_3 import sum_current_time, sum_current_time_remove
import pytest



def test_ex():
    response = sum_current_time('01:02:03')
    assert response == 6
    response = sum_current_time('11:20:03')
    assert response == 34
    response = sum_current_time('00:00:00')
    assert response == 0
    response = sum_current_time('20:02:43')
    assert response == 65

def test_ex_remove():
    response = sum_current_time_remove('01:02:03')
    assert response == 6
    response = sum_current_time_remove('11:20:03')
    assert response == 7
    response = sum_current_time_remove('00:00:00')
    assert response == 0
    response = sum_current_time_remove('20:02:43')
    assert response == 11


def test_wrong_format():
    response = sum_current_time('01 02 03')
    assert response == "wrong format"
    response = sum_current_time('01:02')
    assert response == "wrong format"

def test_wrong_format_remove():
    response = sum_current_time_remove('01 02 03')
    assert response == "wrong format"
    response = sum_current_time_remove('01:02')
    assert response == "wrong format"