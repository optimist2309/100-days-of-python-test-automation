import sys

import pytest


# Custom Marker examples.
# How to run custom marker - pytest -m <marker-name>.


@pytest.mark.smoke_test_cases
def test_smoke_1():
    assert 10 == '10'


@pytest.mark.smoke
def test_smoke_2():
    assert 10 == 10


@pytest.mark.smoke
def test_smoke_3():
    assert 10 != 20


@pytest.mark.smoke
@pytest.mark.regression
def test_reg_smoke():
    assert 100 != 20


# Built-in Marker Examples
'''Skipping test functions :- The simplest way to skip a test function is to mark it with the skip decorator which 
may be passed an optional reason. '''


@pytest.mark.skip(reason="Feature has not implemented yet so skipping this test case")
def test_eol():
    assert 123 == 123333


# Skipping test cases on some conditions.
@pytest.mark.skipif(sys.version_info > (2, 7), reason="requires Python  2.7+")
def test_runs_on_python_grt_2_7():
    assert sys.version_info > (2, 7)


# Mark test functions as expected to fail.
@pytest.mark.xfail(reason="Bug has not fixed yet so failing this test")
def test_bug_4301():
    assert 'browser' == 'chrome'


# Parametrizing test functions.
# The builtin pytest.mark.parametrize decorator enables parametrization of arguments for a test function.
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("number", [1, 2, 3, 0, 42])
def test_foo(number):
    assert number > 0


def text_contain_word(word: str, text: str):
    """Find whether the text contains a particular word"""

    return word in text


test = [
    ('There is a duck in this text', True),
    ('There is nothing here', False)
]


@pytest.mark.parametrize('sample, expected', test)
def test_text_contain_word(sample, expected):
    word = 'duck'

    assert text_contain_word(word, sample) == expected
