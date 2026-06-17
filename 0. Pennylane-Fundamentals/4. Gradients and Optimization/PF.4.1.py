dev = qp.device("default.qubit", wires = 3)

@qp.qnode(dev)
def circuit_as_function(params):
    """
    Implements the circuit shown in the codercise statement.
    Args:
    - params (np.ndarray): [theta_0, theta_1, theta_2, theta_3]
    Returns:
    - (np.tensor): <Z0>
    """
    qp.RX(params[0], wires=0)
    qp.CNOT(wires=[0, 1])
    qp.CNOT(wires=[1, 2])
    qp.CNOT(wires=[2, 0])
    qp.RY(params[1], wires = 0)
    qp.RY(params[2], wires = 1)
    qp.RY(params[3], wires = 2)
    ####################
    ###YOUR CODE HERE###
    ####################

    return qp.expval(qp.PauliZ(0)) # Return the expectation value

angles = np.linspace(0, 4 * np.pi, 200)
output_values = np.array([circuit_as_function([0.5, t, 0.5, 0.5]) for t in angles])