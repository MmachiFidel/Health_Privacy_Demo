import random
import math

def laplace_mechanism(value: float, sensitivity: float, epsilon: float) -> float:
    """A simple Laplace mechanism for demonstration.
    Not intended as a production-grade DP library.
    """
    if epsilon <= 0:
        raise ValueError("epsilon must be > 0")
    scale = sensitivity / epsilon
    # Sample from Laplace(0, scale)
    u = random.random() - 0.5
    return value - scale * math.copysign(1.0, u) * math.log(1 - 2 * abs(u))
