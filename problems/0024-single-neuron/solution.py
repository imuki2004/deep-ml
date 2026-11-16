import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    # Your code here
    preds = bias + np.array(features) @ np.array(weights)
    probabilities = 1 / (1+np.exp(-preds))
    mse = np.mean((labels-probabilities)**2)

    return probabilities, mse