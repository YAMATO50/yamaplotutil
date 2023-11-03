from yamaplotutil import dtypes
import math

def fit_lin(x: dtypes.numeric|dtypes.numericArray, m: dtypes.numeric, b: dtypes.numeric) -> dtypes.numeric|dtypes.numericArray:
    """This returns the result of m*x+b and can be used as a function for fitting
     
    numeric is int, float or complex; numericArray is list of numeric"""
    if type(x) == list:
        result = []
        for _x in x:
            result.append(m*_x+b)
        return result
    return m*x+b

def fit_quad(x: dtypes.numeric|dtypes.numericArray, a: dtypes.numeric, b: dtypes.numeric, c: dtypes.numeric) -> dtypes.numeric|dtypes.numericArray:
    """This returns the result of a*x²+b*x+c and can be used as a function for fitting
     
    numeric is int, float or complex; numericArray is list of numeric"""
    if type(x) == list:
        result = []
        for _x in x:
            result.append(a*_x**2+b*_x+c)
        return result
    return a*x**2+b*x+c

def fit_cube(x: dtypes.numeric|dtypes.numericArray, a: dtypes.numeric, b: dtypes.numeric, c: dtypes.numeric, d: dtypes.numeric) -> dtypes.numeric|dtypes.numericArray:
    """This returns the result of a*x³+b*x²+c*x+d and can be used as a function for fitting
     
    numeric is int, float or complex; numericArray is list of numeric"""
    if type(x) == list:
        result = []
        for _x in x:
            result.append(a*_x**3+b*_x**2+c*_x+d)
        return result
    return a*x**3+b*x**2+c*x+d

def fit_exp(x: dtypes.real|dtypes.realArray, a: dtypes.numeric, b: dtypes.real, c: dtypes.numeric) -> dtypes.real|dtypes.realArray:
    """This returns the result of a*e^(x*b)+c and can be used as a function for fitting
     
    numeric is int, float or complex; real is int or float; realArray is list of real"""
    if type(x) == list:
        result = []
        for _x in x:
           result.append(a*math.exp(_x*b)+c)
        return result 
    return a*math.exp(x*b)+c

def fit_ln(x: dtypes.real|dtypes.realArray, a: dtypes.numeric, b: dtypes.numeric) -> dtypes.real|dtypes.realArray:
    """This returns the result of a*ln(x)+b and can be used as a function for fitting
     
    numeric is int, float or complex; real is int or float; realArray is list of real"""
    if type(x) == list:
        result = []
        for _x in x:
            result.append(a*math.log(_x)+b)
        return result
    return a*math.log(x)+b

def fit_sin(x: dtypes.real|dtypes.realArray, a: dtypes.numeric, b: dtypes.real, c: dtypes.real, d: dtypes.numeric) -> dtypes.real|dtypes.realArray:
    """This returns the result of a*sin(b*x+c)+d and can be used as a function for fitting
     
    numeric is int, float or complex; real is int or float; realArray is list of real"""
    if type(x) == list:
        result = []
        for _x in x:
            result.append(a*math.sin(b*_x+c)+d)
        return result
    return a*math.sin(b*x+c)+d

def fit_cos(x: dtypes.real|dtypes.realArray, a: dtypes.numeric, b: dtypes.real, c: dtypes.real, d: dtypes.numeric) -> dtypes.real|dtypes.realArray:
    """This returns the result of a*cos(b*x+c)+d and can be used as a function for fitting
     
    numeric is int, float or complex; real is int or float; realArray is list of real"""
    if type(x) == list:
        result = []
        for _x in x:
            result.append(a*math.cos(b*_x+c)+d)
        return result
    return a*math.cos(b*x+c)+d