import pennylane as qp
from pennylane import numpy as np

dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def apply_z_to_plus():
    """Write a circuit that applies PauliZ to the |+> state and returns
    the state.

    Returns:
        np.array[complex]: The state of the qubit after the operations.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # CREATE THE |+> STATE
    qp.H(wires=0)

    # APPLY PAULI Z
    qp.PauliZ(wires=0)

    # RETURN THE STATE
    return qp.state()


print(apply_z_to_plus())
