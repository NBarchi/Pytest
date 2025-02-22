import pytest
from calculadora import suma, division, division1

@pytest.mark.parametrize("a,b,expected",  [
        (1,2,3),
        (-2,2,0),
        (-3,2,-1),

    ])
def test_suma(a,b,expected):
    assert suma(a,b) == expected

def test_suma():
    assert suma(1,2) == 3
    assert suma(-2,2) == 0
    assert suma(-3,2) == -1
    assert suma(0,0) == 0

def test_division():
    assert division(4,2) == 2
    with pytest.raises(ValueError):
        division(1,0)

def test_division1():
    assert division1(4,0) == "No se puede dividir por 0"

