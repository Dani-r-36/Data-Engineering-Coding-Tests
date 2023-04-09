import pytest
from test_1 import is_log_line

def test_is_log():
    response = is_log_line("03/11/21 08:51:06 WARNING :.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.")
    assert response == True
    response = is_log_line("03/11/21 08:51:06 WARNING")
    assert response == False
    response = is_log_line("03/11/21 :.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.")
    assert response == False