import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    # Your code here
    # features = len(vectors)
    # covariance_matrix = [features*[]]
    # feature_count = 0

    # for i in range(features):
    #     for j in range(features):
    #         if i == j:
    #             covariance_matrix[i][j] = np.var(vectors[feature_count])
    #             feature_count += 1
    #         else:
    #             covariance_matrix[i][j] = 
    return np.cov(vectors)
