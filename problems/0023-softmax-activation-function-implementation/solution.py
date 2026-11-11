import math
import numpy as np

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    scores_shifted = scores - np.max(scores)
    exp_x = np.exp(scores_shifted)
    return exp_x / np.sum(exp_x)