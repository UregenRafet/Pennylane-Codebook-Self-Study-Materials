import pennylane as qp
from pennylane import numpy as np

# Here are the vector representations of |0> and |1>, for convenience
ket_0 = np.array([1, 0])
ket_1 = np.array([0, 1])


def normalize_state(alpha, beta):
    """Compute a normalized quantum state given arbitrary amplitudes.

    Args:
        alpha (complex): The amplitude associated with the |0> state.
        beta (complex): The amplitude associated with the |1> state.

    Returns:
        np.array[complex]: A vector (numpy array) with 2 elements that represents
        a normalized quantum state.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    norm = np.abs(alpha) ** 2 + np.abs(beta) ** 2
    alpha_prime = alpha / np.sqrt(norm)
    beta_prime = beta / np.sqrt(norm)

    # RETURN A VECTOR
    return alpha_prime * ket_0 + beta_prime * ket_1

print(normalize_state(1+2j, 2+2j))
