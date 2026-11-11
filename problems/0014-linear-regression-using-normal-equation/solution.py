import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Your code here, make sure to round
    res = []
    for coef in np.linalg.lstsq(X,y)[0]:
        res.append(round(coef,4))
    return res