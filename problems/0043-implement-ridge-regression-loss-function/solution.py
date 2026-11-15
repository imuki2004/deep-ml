import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
    # Your code here
    error = y_true - X @ w
    loss = np.mean(error**2) + alpha * np.sum(w**2)
    return loss
    
