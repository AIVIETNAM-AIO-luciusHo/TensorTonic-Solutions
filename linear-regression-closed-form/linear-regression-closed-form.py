

def linear_regression_closed_form(X: list, y: list) -> list:
    #B1:change input to float
    X_arr=np.asarray(X,dtype=float)
    y_arr=np.asarray(y,dtype=float)
    #B2:calculate matrix GRAM 
    Xt=X_arr.T
    XtX=Xt@X_arr
    Xty=Xt@y_arr
    #B3:find w
    w=np.linalg.solve(XtX, Xty)
    #B4: return
    return w.tolist()
    