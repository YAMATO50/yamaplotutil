import fitfunctions as ff
import random

__testRuns = 10
__globalMin = -10
__globalMax = 10

def randFloat(min: float, max: float):
    return min + random.random() * (max - min)

def randInt(min: int, max: int):
    return random.randint(min, max)

def randComplex(min: float, max: float):
    real = randFloat(min, max)
    imag = randFloat(min, max)
    return complex(real, imag)

def test_fit_lin_int():
    for _ in range(__testRuns):
        m = randInt(__globalMin, __globalMax)
        b = randInt(__globalMin, __globalMax)
        x = randInt(__globalMin, __globalMax)
        assert ff.fit_lin(x, m, b) == m*x+b

def test_fit_lin_float():
    for _ in range(__testRuns):
        m = randFloat(__globalMin, __globalMax)
        b = randFloat(__globalMin, __globalMax)
        x = randFloat(__globalMin, __globalMax)
        assert ff.fit_lin(x, m, b) == m*x+b

def test_fit_lin_complex():
    for _ in range(__testRuns):
        m = randComplex(__globalMin, __globalMax)
        b = randComplex(__globalMin, __globalMax)
        x = randComplex(__globalMin, __globalMax)
        assert ff.fit_lin(x, m, b) == m*x+b

def test_fit_quad_int():
    for _ in range(__testRuns):
        a = randInt(__globalMin, __globalMax)
        b = randInt(__globalMin, __globalMax)
        c = randInt(__globalMin, __globalMax)
        x = randInt(__globalMin, __globalMax)
        assert ff.fit_quad(x, a, b, c) == a*x**2+b*x+c

def test_fit_quad_float():
    for _ in range(__testRuns):
        a = randFloat(__globalMin, __globalMax)
        b = randFloat(__globalMin, __globalMax)
        c = randFloat(__globalMin, __globalMax)
        x = randFloat(__globalMin, __globalMax)
        assert ff.fit_quad(x, a, b, c) == a*x**2+b*x+c

def test_fit_quad_complex():
    for _ in range(__testRuns):
        a = randComplex(__globalMin, __globalMax)
        b = randComplex(__globalMin, __globalMax)
        c = randComplex(__globalMin, __globalMax)
        x = randComplex(__globalMin, __globalMax)
        assert ff.fit_quad(x, a, b, c) == a*x**2+b*x+c
