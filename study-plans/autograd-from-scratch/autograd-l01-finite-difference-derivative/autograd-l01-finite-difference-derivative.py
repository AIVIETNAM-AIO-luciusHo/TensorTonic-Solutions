import numpy as np

def finite_difference_derivative(coefficients, x, h):
    def eval_poly(t):
        return sum(c * (t**k) for k, c in enumerate(coefficients))
    
    fx = eval_poly(x)
    fx_h = eval_poly(x + h)
    slope = (fx_h - fx) / h
    return fx, fx_h, slope