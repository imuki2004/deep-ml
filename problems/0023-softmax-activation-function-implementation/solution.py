import math
import numpy as np

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    scores_adj = scores - np.max(scores)
    scores_exp = np.exp(scores_adj)
    return scores_exp / sum(scores_exp)