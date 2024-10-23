import pytest
from src.calculator import divide, subtract, suma


def test_suma():
    assert suma(14, 90) == 104


def test_subtract():
    assert subtract(14, 90) == -76


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
