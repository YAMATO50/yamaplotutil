from yamaplotutil import fitfunctions as ff
import random
import math

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

def test_fit_lin_int_list():
    for _ in range(__testRuns):
        m = randInt(__globalMin, __globalMax)
        b = randInt(__globalMin, __globalMax)
        x = [randInt(__globalMin, __globalMax), randInt(__globalMin, __globalMax)]
        result = ff.fit_lin(x, m, b)
        assert len(result) == len(x)
        for i in range(len(x)):
            assert result[i] == m*x[i]+b


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

def test_fit_quad_int_list():
    for _ in range(__testRuns):
        a = randInt(__globalMin, __globalMax)
        b = randInt(__globalMin, __globalMax)
        c = randInt(__globalMin, __globalMax)
        x = [randInt(__globalMin, __globalMax), randInt(__globalMin, __globalMax)]
        result = ff.fit_quad(x, a, b, c)
        assert len(result) == len(x)
        for i in range(len(x)):
            assert result[i] == a*x[i]**2+b*x[i]+c

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

def test_fit_cube_int():
    for _ in range(__testRuns):
        a = randInt(__globalMin, __globalMax)
        b = randInt(__globalMin, __globalMax)
        c = randInt(__globalMin, __globalMax)
        d = randInt(__globalMin, __globalMax)
        x = randInt(__globalMin, __globalMax)
        assert ff.fit_cube(x, a, b, c, d) == a*x**3+b*x**2+c*x+d

def test_fit_cube_int_list():
    for _ in range(__testRuns):
        a = randInt(__globalMin, __globalMax)
        b = randInt(__globalMin, __globalMax)
        c = randInt(__globalMin, __globalMax)
        d = randInt(__globalMin, __globalMax)
        x = [randInt(__globalMin, __globalMax), randInt(__globalMin, __globalMax)]
        result = ff.fit_cube(x, a, b, c, d)
        assert len(result) == len(x)
        for i in range(len(x)):
            assert result[i] == a*x[i]**3+b*x[i]**2+c*x[i]+d

def test_fit_cube_float():
    for _ in range(__testRuns):
        a = randFloat(__globalMin, __globalMax)
        b = randFloat(__globalMin, __globalMax)
        c = randFloat(__globalMin, __globalMax)
        d = randFloat(__globalMin, __globalMax)
        x = randFloat(__globalMin, __globalMax)
        assert ff.fit_cube(x, a, b, c, d) == a*x**3+b*x**2+c*x+d

def test_fit_cube_complex():
    for _ in range(__testRuns):
        a = randComplex(__globalMin, __globalMax)
        b = randComplex(__globalMin, __globalMax)
        c = randComplex(__globalMin, __globalMax)
        d = randComplex(__globalMin, __globalMax)
        x = randComplex(__globalMin, __globalMax)
        assert ff.fit_cube(x, a, b, c, d) == a*x**3+b*x**2+c*x+d

def test_fit_exp_int():
    for _ in range(__testRuns):
        a = randInt(__globalMin, __globalMax)
        b = randInt(__globalMin, __globalMax)
        c = randInt(__globalMin, __globalMax)
        x = randInt(__globalMin, __globalMax)
        assert ff.fit_exp(x, a, b, c) == a*math.exp(x*b)+c

def test_fit_exp_int_list():
    for _ in range(__testRuns):
        a = randInt(__globalMin, __globalMax)
        b = randInt(__globalMin, __globalMax)
        c = randInt(__globalMin, __globalMax)
        x = [randInt(__globalMin, __globalMax), randInt(__globalMin, __globalMax)]
        result = ff.fit_exp(x, a, b, c)
        assert len(result) == len(x)
        for i in range(len(x)):
            assert result[i] == a*math.exp(x[i]*b)+c

def test_fit_exp_float():
    for _ in range(__testRuns):
        a = randFloat(__globalMin, __globalMax)
        b = randFloat(__globalMin, __globalMax)
        c = randFloat(__globalMin, __globalMax)
        x = randFloat(__globalMin, __globalMax)
        assert ff.fit_exp(x, a, b, c) == a*math.exp(x*b)+c

def test_fit_exp_complex():
    for _ in range(__testRuns):
        a = randComplex(__globalMin, __globalMax)
        b = randFloat(__globalMin, __globalMax)
        c = randComplex(__globalMin, __globalMax)
        x = randFloat(__globalMin, __globalMax)
        assert ff.fit_exp(x, a, b, c) == a*math.exp(x*b)+c

def test_fit_ln_int():
    for _ in range(__testRuns):
        a = randInt(__globalMin, __globalMax)
        b = randInt(__globalMin, __globalMax)
        x = randInt(1, __globalMax)
        assert ff.fit_ln(x, a, b) == a*math.log(x)+b

def test_fit_ln_int_list():
    for _ in range(__testRuns):
        a = randInt(__globalMin, __globalMax)
        b = randInt(__globalMin, __globalMax)
        x = [randInt(1, __globalMax), randInt(1, __globalMax)]
        result = ff.fit_ln(x, a, b)
        assert len(result) == len(x)
        for i in range(len(x)):
            assert result[i] == a*math.log(x[i])+b

def test_fit_ln_float():
    for _ in range(__testRuns):
        a = randFloat(__globalMin, __globalMax)
        b = randFloat(__globalMin, __globalMax)
        x = randFloat(0.001, __globalMax)
        assert ff.fit_ln(x, a, b) == a*math.log(x)+b

def test_fit_ln_complex():
    for _ in range(__testRuns):
        a = randComplex(__globalMin, __globalMax)
        b = randComplex(__globalMin, __globalMax)
        x = randFloat(0.001, __globalMax)
        assert ff.fit_ln(x, a, b) == a*math.log(x)+b

def test_fit_sin_int():
    for _ in range(__testRuns):
        a = randInt(__globalMin, __globalMax)
        b = randInt(__globalMin, __globalMax)
        c = randInt(__globalMin, __globalMax)
        d = randInt(__globalMin, __globalMax)
        x = randInt(__globalMin, __globalMax)
        assert ff.fit_sin(x, a, b, c, d) == a*math.sin(b*x+c)+d

def test_fit_sin_int_list():
    for _ in range(__testRuns):
        a = randInt(__globalMin, __globalMax)
        b = randInt(__globalMin, __globalMax)
        c = randInt(__globalMin, __globalMax)
        d = randInt(__globalMin, __globalMax)
        x = [randInt(__globalMin, __globalMax), randInt(__globalMin, __globalMax)]
        result = ff.fit_sin(x, a, b, c, d)
        assert len(result) == len(x)
        for i in range(len(x)):
            assert result[i] == a*math.sin(b*x[i]+c)+d

def test_fit_sin_float():
    for _ in range(__testRuns):
        a = randFloat(__globalMin, __globalMax)
        b = randFloat(__globalMin, __globalMax)
        c = randFloat(__globalMin, __globalMax)
        d = randFloat(__globalMin, __globalMax)
        x = randFloat(__globalMin, __globalMax)
        assert ff.fit_sin(x, a, b, c, d) == a*math.sin(b*x+c)+d

def test_fit_sin_complex():
    for _ in range(__testRuns):
        a = randComplex(__globalMin, __globalMax)
        b = randFloat(__globalMin, __globalMax)
        c = randFloat(__globalMin, __globalMax)
        d = randComplex(__globalMin, __globalMax)
        x = randFloat(__globalMin, __globalMax)
        assert ff.fit_sin(x, a, b, c, d) == a*math.sin(b*x+c)+d

def test_fit_cos_int():
    for _ in range(__testRuns):
        a = randInt(__globalMin, __globalMax)
        b = randInt(__globalMin, __globalMax)
        c = randInt(__globalMin, __globalMax)
        d = randInt(__globalMin, __globalMax)
        x = randInt(__globalMin, __globalMax)
        assert ff.fit_cos(x, a, b, c, d) == a*math.cos(b*x+c)+d

def test_fit_cos_int_list():
    for _ in range(__testRuns):
        a = randInt(__globalMin, __globalMax)
        b = randInt(__globalMin, __globalMax)
        c = randInt(__globalMin, __globalMax)
        d = randInt(__globalMin, __globalMax)
        x = [randInt(__globalMin, __globalMax), randInt(__globalMin, __globalMax)]
        result = ff.fit_cos(x, a, b, c, d)
        assert len(result) == len(x)
        for i in range(len(x)):
            assert result[i] == a*math.cos(b*x[i]+c)+d

def test_fit_cos_float():
    for _ in range(__testRuns):
        a = randFloat(__globalMin, __globalMax)
        b = randFloat(__globalMin, __globalMax)
        c = randFloat(__globalMin, __globalMax)
        d = randFloat(__globalMin, __globalMax)
        x = randFloat(__globalMin, __globalMax)
        assert ff.fit_cos(x, a, b, c, d) == a*math.cos(b*x+c)+d

def test_fit_cos_complex():
    for _ in range(__testRuns):
        a = randComplex(__globalMin, __globalMax)
        b = randFloat(__globalMin, __globalMax)
        c = randFloat(__globalMin, __globalMax)
        d = randComplex(__globalMin, __globalMax)
        x = randFloat(__globalMin, __globalMax)
        assert ff.fit_cos(x, a, b, c, d) == a*math.cos(b*x+c)+d