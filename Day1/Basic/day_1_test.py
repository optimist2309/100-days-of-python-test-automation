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
