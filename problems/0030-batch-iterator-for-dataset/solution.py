import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    # Your code here
    n_samples = X.shape[0]
    batches = []
    for start in range(0, n_samples, batch_size):
        end = start + batch_size
        if y is not None:
            batches.append([X[start:end], y[start:end]])
        else:
            batches.append([X[start:end]])
    
    return batches
