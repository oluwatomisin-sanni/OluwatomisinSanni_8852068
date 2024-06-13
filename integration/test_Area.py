import calculator
from math import pi


def test_rectangle():
    assert calculator.multiply(3.34, 5.33) == 17.8022

def test_Square():
    assert calculator.multiply (6,6) == 36

def test_circle():
     assert calculator.multiply(3.14159, (13**2)) == 530.229
