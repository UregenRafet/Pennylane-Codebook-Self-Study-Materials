import pennylane as qp
from pennylane import numpy as np

dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def many_rotations():
    """Implement the circuit depicted above and return the quantum state.

    Returns:
        np.array[complex]: The state of the qubit after the operations.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE CIRCUIT
    qp.Hadamard(wires=0)
    qp.S(wires=0)
    qp.adjoint(qp.T)(wires=0)
    qp.RZ(0.3, wires=0)
    qp.adjoint(qp.S)(wires=0)
    # RETURN THE STATE

    return qp.state()

print(many_rotations())