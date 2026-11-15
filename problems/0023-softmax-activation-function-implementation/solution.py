import math
import numpy as np

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    scores_adjusted = scores - np.max(scores)
    score_exps = np.exp(scores_adjusted)
    return score_exps / np.sum(score_exps)