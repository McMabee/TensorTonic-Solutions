import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    x = np.asarray(x, dtype=float)
    match x:
        case list():
            return [1/(1 + np.exp(-item)) for item in x]
        case _:
            return 1/(1 + np.exp(-x))