import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Your code here
    col_mean = np.mean(data, axis=0, keepdims=True)
    col_std = np.std(data, axis=0, ddof=0, keepdims=True)
    col_min = np.min(data, axis=0, keepdims=True)
    col_max = np.max(data, axis=0, keepdims=True)

    standardized_data = np.round((data - col_mean) / col_std, 4).tolist()
    normalized_data = np.round((data-col_min) / (col_max - col_min), 4).tolist()

            
    return standardized_data, normalized_data