dev = qp.device("default.qubit", wires = 3)

@qp.qnode(dev)
def prep_circuit(alpha, beta, gamma):
    """
    Prepares the state alpha|001> + beta|010> + gamma|100>.
    Args:
    alpha, beta, gamma (np.complex): The coefficients of the quantum state
    to prepare.
    Returns:
    (np.array): The quantum state
    """
    state = [0, alpha, beta, 0, gamma, 0, 0, 0]
    qp.StatePrep(state, wires=range(3), normalize=True)

    ####################
    ###YOUR CODE HERE###
    ####################
    
    return qp.state()

alpha, beta, gamma = 1/np.sqrt(3), 1/np.sqrt(3), 1/np.sqrt(3),

print("The prepared state is", prep_circuit(alpha, beta, gamma))
