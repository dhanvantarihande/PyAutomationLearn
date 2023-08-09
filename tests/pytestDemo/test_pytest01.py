import pytest


def add(a, b):
    return a + b

# How to Test Function
# We Check expected Result and Actual Result
# We Put Some Data, Input Some Data and Verify
# This is What We Test the Function

@pytest.mark.positive
def test_add_positive():
    assert add(2, 3) == 5


@pytest.mark.negative
def test_add_negative():
    assert add(5, 3) != 5