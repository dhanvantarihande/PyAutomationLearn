import pytest


def sub(a, b):
    return a - b

@pytest.mark.positive
def test_sub_positive():
    assert sub(2, 3) == -1


@pytest.mark.negative
def test_sub_negative():
    assert sub(5, 3) != 4
