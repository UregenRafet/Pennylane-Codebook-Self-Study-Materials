dev = qp.device("default.qubit", wires = 2)

@qp.qnode(dev)
def single_qubit_gates(theta, phi):
    """
    Implements the quantum circuit shown in the statement
    Args:
    - theta, phi (float): The arguments for the RX and RZ gates, respectively
    Returns:
    - (np.array): The output quantum state.
    
    """
    qp.Hadamard(wires=0)
    qp.Hadamard(wires=1)
    qp.T(wires=0)
    qp.S(wires=1)
    qp.RX(theta, wires=0)
    qp.RZ(phi, wires=1)

    ####################
    ###YOUR CODE HERE###
    ####################
    
    return qp.state()

theta, phi = np.pi/3, np.pi/4
print("The output state of the circuit is: ", single_qubit_gates(theta, phi))