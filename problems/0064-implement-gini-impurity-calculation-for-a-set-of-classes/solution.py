
import numpy as np

def gini_impurity(y):
    """
    Calculate Gini Impurity for a list of class labels.

    :param y: List of class labels
    :return: Gini Impurity rounded to three decimal places
    """
    labels = set(y)
    total = 0
    
    for l in labels:
        pi = np.sum(np.array(y) == l) / len(y)
        total+=pi**2
    
    val = 1 - total
    return round(val,3)