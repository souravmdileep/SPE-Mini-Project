import math
import pytest
from app.calc import sqrt, factorial, ln, power, CalcError

def test_sqrt_ok():
    assert sqrt(9) == 3.0
    assert pytest.approx(sqrt(2), 1e-12) == math.sqrt(2)

def test_sqrt_negative():
    with pytest.raises(CalcError):
        sqrt(-1)

def test_factorial_basic():
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(5.0) == 120

def test_factorial_invalid():
    with pytest.raises(CalcError):
        factorial(-3)
    with pytest.raises(CalcError):
        factorial(3.5)

def test_ln_ok():
    assert pytest.approx(ln(1), 1e-12) == 0.0
    assert pytest.approx(ln(math.e), 1e-12) == 1.0

def test_ln_invalid():
    with pytest.raises(CalcError):
        ln(0)
    with pytest.raises(CalcError):
        ln(-10)

def test_power_ok():
    assert power(2, 10) == 1024.0
    assert power(9, 0.5) == 3.0
