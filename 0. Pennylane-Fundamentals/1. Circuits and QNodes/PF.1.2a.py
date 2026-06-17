def subcircuit_1(angle):

    ####################
    ###YOUR CODE HERE###
    qp.RX(angle, wires = 0)
    qp.PauliY(wires=1)
    ####################

    # No need to return anything

def subcircuit_2():

    ####################
    ###YOUR CODE HERE###
    ####################
    qp.Hadamard(wires=0)
    qp.CNOT(wires=[0, 1])
    # No need to return anything

dev = qp.device('default.qubit', wires = 2)

# Decorate this function to create a QNode
@qp.qnode(dev)
def full_circuit(theta, phi):

    ####################
    ###YOUR CODE HERE###
    ####################   
    subcircuit_1(theta)
    subcircuit_2()
    subcircuit_1(phi)
    return qp.state()
    

    # Return the quantum state