import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    input = np.array(list).reshape(3, 3)
    calculations = {
        'mean': [np.mean(input, axis = 0).tolist(), np.mean(input, axis = 1).tolist(), np.mean(input).tolist()],
        'variance': [np.var(input, axis = 0).tolist(), np.var(input, axis = 1).tolist(), np.var(input).tolist()],
        'standard deviation': [np.std(input, axis = 0).tolist(), np.std(input, axis = 1).tolist(), np.std(input).tolist()],
        'max': [np.max(input, 0).tolist(), np.max(input, 1).tolist(), np.max(input).tolist()],
        'min': [np.min(input, 0).tolist(), np.min(input, 1).tolist(), np.min(input).tolist()],
        'sum': [np.sum(input, axis = 0).tolist(), np.sum(input, axis = 1).tolist(), np.sum(input).tolist()]
    }
    return calculations