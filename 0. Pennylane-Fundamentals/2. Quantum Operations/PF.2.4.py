dev = qp.device("default.qubit", wires = 3)

@qp.qnode(dev)
def ctrl_circuit(theta,phi):
    """Implements the circuit shown in the Codercise statement
    Args:
        theta (float): Rotation angle for RX
        phi (float): Rotation angle for RY
    Returns:
        (numpy.array): The output state of the QNode
    """
    qp.RY(phi, wires=0)
    qp.Hadamard(wires=1)
    qp.RX(theta, wires=2)
    qp.ctrl(qp.S, control=(0), control_values=(1))(wires=1)
    qp.ctrl(qp.T, control=(1), control_values=(0))(wires=2)
    qp.ctrl(qp.Hadamard, control=(2), control_values=(1))(wires=0)
    ####################
    ###YOUR CODE HERE###
    ####################
    
    return qp.state()