def subcircuit_1(angle, wire_list):
    """
    Implements the first subcircuit as a function of the RX gate angle
    and the list of wires wire_list on which the gates are applied
    """
    ####################
    ###YOUR CODE HERE###
    ####################
    qp.RX(angle, wires = wire_list[0])
    qp.PauliY(wires=wire_list[1])

def subcircuit_2(wire_list):
    """
    Implements the second subcircuit as a function of the list of wires 
    wire_list on which the gates are applied
    """

    ####################
    ###YOUR CODE HERE###
    ####################
    qp.Hadamard(wires=wire_list[0])
    qp.CNOT(wires=wire_list)

dev = qp.device("default.qubit", wires = [0,1])

@qp.qnode(dev)
def full_circuit(theta, phi):
    """
    Builds the full quantum circuit given the input parameters
    """

    ####################
    ###YOUR CODE HERE###
    ####################
    subcircuit_1(theta, [0, 1])
    subcircuit_2([0, 1])
    subcircuit_1(phi, [1, 0])
    return qp.state()

    return qp.state()
