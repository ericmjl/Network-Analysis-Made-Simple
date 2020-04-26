import numpy as np

def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / len(data)
