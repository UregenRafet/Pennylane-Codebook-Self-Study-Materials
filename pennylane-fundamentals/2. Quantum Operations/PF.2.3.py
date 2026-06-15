dev = qp.device("default.qubit", wires = 3)

@qp.qnode(dev)
def multi_qubit_gates(theta,phi):
    """
    Applies the circuit shown the figure above
    Args:
    theta, phi (float): parameters of the CRX and CRY gates, in that order.
    Returns:
    - (np.array): the quantum state
    """
    qp.Hadamard(wires=0)
    qp.CRY(phi, wires=[0, 1])
    qp.CRX(theta, wires=[1, 2])
    qp.S(wires=1)
    qp.T(wires=2)
    qp.Toffoli(wires=[0,1,2])
    qp.SWAP(wires=[0, 2])
    #####################
    ###YOUR CODE HERE####
    #####################

    return qp.state()

theta, phi = np.pi/3, np.pi/4
print("The output state is: \n", multi_qubit_gates(theta, phi))