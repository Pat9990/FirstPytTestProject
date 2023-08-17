import pytest


def add_two_numbers(a,b):
    return a+b
@pytest.mark.math
def test_small_numbers():
    assert add_two_numbers(2,3) == 5, "Wrong result"