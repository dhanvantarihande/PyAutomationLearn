# Exception
# try and except

import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Can't divide by Zero")
    return a / b


def test_divide_raise_error():
    with pytest.raises(ValueError) as e:
        divide(10,0)
    assert "Can't divide by Zero" in str(e.value)