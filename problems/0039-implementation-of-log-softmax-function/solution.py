import numpy as np

def log_softmax(scores: np.ndarray) -> np.ndarray:
    # Your code here
    scores_exp = np.exp(scores)
    
    return np.log(scores_exp/np.sum(scores_exp))