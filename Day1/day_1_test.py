import math

Name_list = ["MH", "UP", "RJ", "DL", "HP"]


# Basic test cases examples.
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


def test_equality():
    assert 10 == 11


def test_rto():
    assert Name_list[0] == "MH"


def test_no_rto_spain():
    assert "Spain" not in Name_list
