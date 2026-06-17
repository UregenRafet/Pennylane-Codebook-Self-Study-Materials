import pennylane as qp
from pennylane import numpy as np

U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

def apply_u(state):
    """Apply a quantum operation.

    Args:
        state (np.array[complex]): A normalized quantum state vector.

    Returns:
        np.array[complex]: The output state after applying U.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    result = np.dot(U, state)

    # APPLY U TO THE INPUT STATE AND RETURN THE NEW STATE
    return result

state = np.array([0.8, 0.6])
print(apply_u(state))