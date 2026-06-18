import pennylane as qp
from pennylane import numpy as np

dev = qp.device("default.qubit", wires=1)

U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)


@qp.qnode(dev)
def apply_u():

    ##################
    # YOUR CODE HERE #
    ##################

    # USE QubitUnitary TO APPLY U TO THE QUBIT
    qp.QubitUnitary(U, wires=(0))

    # Return the state
    return qp.state()

