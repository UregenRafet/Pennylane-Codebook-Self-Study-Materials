def circuit(phi): # Write any arguments you need here
    """
    This quantum function implements the circuit shown above
    and returns the output quantum state
    """
    qp.Hadamard(wires=0)
    qp.X(wires=1)
    qp.CNOT(wires=[0, 1])
    qp.RY(phi, wires=1)####################
    ###YOUR CODE HERE###
    ####################

    return qp.state()

