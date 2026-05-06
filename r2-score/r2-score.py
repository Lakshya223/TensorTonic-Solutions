import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    if np.array_equal(y_true, y_pred):
        return 1.0 
    sse = np.sum((y_true-y_pred)**2.0)
    tss = np.sum((y_true-np.mean(y_true))**2.0)
    if tss == 0:
        return 0.0
    r_square = 1.0-(sse/tss)
    return r_square
    pass