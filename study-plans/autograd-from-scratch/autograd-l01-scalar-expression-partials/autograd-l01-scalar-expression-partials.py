import numpy as np

def scalar_expression_partials(a, b, c, h):
    """
    Returns: the expression value and its three numerical partial derivatives
    """
    def  function_d(a,b,c):
        return a*b+c 
    d0=function_d(a,b,c)
    da=(function_d(a+h,b,c)-d0)/h
    db=(function_d(a,b+h,c)-d0)/h
    dc=(function_d(a,b,c+h)-d0)/h


    return d0,da,db,dc