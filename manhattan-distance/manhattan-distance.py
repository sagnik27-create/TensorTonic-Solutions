import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    x_arr = np.asarray(x)
    y_arr = np.asarray(y)
    dist1= float(np.sum(np.abs(x_arr-y_arr)))
    return dist1
    # Write code here
    pass