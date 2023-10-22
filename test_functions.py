import functions as f
import numpy as np
import math

def test_make_fittet_polynom_values_int():
    x = np.linspace(-10, 10, 20, dtype=int)
    a = 1
    b = 4
    c = -2
    d = 5
    e = 9
    coefficients = [a, b, c, d, e]
    y = f.make_fitted_polynom_values(x, coefficients)
    for i in range(len(x)):
        assert y[i] == a*x[i]**4+b*x[i]**3+c*x[i]**2+d*x[i]+e

def test_make_fittet_polynom_values_float():
    x = np.linspace(-10, 10, 30, dtype=float)
    a = 1.3
    b = 4.5
    c = -2.1
    d = 5.9
    e = 0.32
    coefficients = [a, b, c, d, e]
    y = f.make_fitted_polynom_values(x, coefficients)
    for i in range(len(x)):
        assert y[i] == a*x[i]**4+b*x[i]**3+c*x[i]**2+d*x[i]+e

def test_make_fittet_polynom_values_complex():
    x = np.linspace(-5-3j, 5+3j, 20, dtype=complex)
    a = 1.4+0.42j
    b = 4.0+0j
    c = -2.2+1.2j
    d = 0.6-4j
    e = 0+3j
    coefficients = [a, b, c, d, e]
    y = f.make_fitted_polynom_values(x, coefficients)
    for i in range(len(x)):
        assert y[i] == a*x[i]**4+b*x[i]**3+c*x[i]**2+d*x[i]+e

def test_make_fitted_sin_values_int():
    x = np.linspace(-10, 10, 20, dtype=int)
    a = 1
    b = 4
    c = -2
    d = 5
    y = f.make_fitted_sin_values(x, a, b, c, d)
    for i in range(len(x)):
        assert y[i] == a*math.sin(b*x[i]+c)+d

def test_make_fitted_sin_values_float():
    x = np.linspace(-10, 10, 30, dtype=float)
    a = 1.3
    b = 4.5
    c = -2.1
    d = 0.9
    y = f.make_fitted_sin_values(x, a, b, c, d)
    for i in range(len(x)):
        assert y[i] == a*math.sin(b*x[i]+c)+d

def test_make_fitted_sin_values_complex():
    x = np.linspace(-5, 5, 20, dtype=float)
    a = 1.4+0.42j
    b = 4.0
    c = -2.2
    d = 0.6-4j
    y = f.make_fitted_sin_values(x, a, b, c, d)
    for i in range(len(x)):
        assert y[i] == a*math.sin(b*x[i]+c)+d

def test_make_fitted_cos_values_int():
    x = np.linspace(-10, 10, 20, dtype=int)
    a = 1
    b = 4
    c = -2
    d = 5
    y = f.make_fitted_cos_values(x, a, b, c, d)
    for i in range(len(x)):
        assert y[i] == a*math.cos(b*x[i]+c)+d

def test_make_fitted_cos_values_float():
    x = np.linspace(-10, 10, 30, dtype=float)
    a = 1.3
    b = 4.5
    c = -2.1
    d = 0.9
    y = f.make_fitted_cos_values(x, a, b, c, d)
    for i in range(len(x)):
        assert y[i] == a*math.cos(b*x[i]+c)+d

def test_make_fitted_cos_values_complex():
    x = np.linspace(-5, 5, 20, dtype=float)
    a = 1.4+0.42j
    b = 4.0
    c = -2.2
    d = 0.6-4j
    y = f.make_fitted_cos_values(x, a, b, c, d)
    for i in range(len(x)):
        assert y[i] == a*math.cos(b*x[i]+c)+d