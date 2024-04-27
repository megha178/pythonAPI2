'''
author:Megha

# tc1 verify status code,headers
tc2 verify the body id
tc3 verify json shcema is valid
'''
import pytest


@pytest.mark.run(order=1)
def test_crete_booking_tc1():
    assert True == True


@pytest.mark.run(order=2)
def test_crete_booking_tc2():
    assert True == False


@pytest.mark.run(order=3)
def test_crete_booking_tc3():
    assert True == True
