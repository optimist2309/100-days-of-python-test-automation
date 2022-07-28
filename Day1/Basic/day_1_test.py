import math


# Basic test cases examples.
def test_1():
    assert 2309 == 2309


def test_2():
    assert 23 != 2131


def test_sqrt():
    assert math.sqrt(49) == 7


city_list = ["UP", "MP", "TN", "MH", "RJ"]
def test_name():
    assert "DL" not in city_list


# Assertions about expected exceptions.
# In order to write assertions about raised exceptions, you can use pytest.raises() as a context manager like this.
def whatever():
    return 9/0
def test_whatever():
    with pytest.raises(ZeroDivisionError):
        whatever()
