import math

class CalcError(ValueError):
    pass

def sqrt(x: float) -> float:
    try:
        x = float(x)
    except Exception as e:
        raise CalcError("sqrt: x must be a number") from e
    if x < 0:
        raise CalcError("sqrt: undefined for negative numbers")
    return math.sqrt(x)

def factorial(x) -> int:
    try:
        fx = float(x)
    except Exception as e:
        raise CalcError("factorial: x must be numeric") from e
    if not fx.is_integer():
        raise CalcError("factorial: only defined for whole numbers")
    n = int(fx)
    if n < 0:
        raise CalcError("factorial: negative not allowed")
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def ln(x: float) -> float:
    try:
        x = float(x)
    except Exception as e:
        raise CalcError("ln: x must be a number") from e
    if x <= 0:
        raise CalcError("ln: x must be > 0")
    return math.log(x)

def power(x: float, b: float) -> float:
    try:
        return float(x) ** float(b)
    except Exception as e:
        raise CalcError("power: x and b must be numbers") from e
