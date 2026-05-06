import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    
    error = np.mean((y_pred-y_true)**2)
    # return np.mean(error)
    # Write code here
    return error
    pass
