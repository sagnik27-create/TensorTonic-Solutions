import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a_arr= np.asarray(a)
    b_arr= np.asarray(b)
    dot_product = np.dot(a_arr,b_arr)
    norm_a = float(np.linalg.norm(a_arr))
    norm_b = float(np.linalg.norm(b_arr))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(dot_product/(norm_a*norm_b))
    pass