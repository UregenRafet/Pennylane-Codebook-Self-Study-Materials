dev = qp.device("default.qubit", wires = 2)

@qp.qnode(dev)
def phase_kickback(matrix):
    """Applies phase kickback to a single-qubit operator whose matrix is known
    Args:S
    - matrix (numpy.array): A 2x2 matrix
    Returns:
    - (numpy.array): The output state after applying phase kickback
    """
    qp.Hadamard(wires=0)
    qp.ControlledQubitUnitary(matrix, wires=[0, 1])
    qp.Hadamard(wires=0)
    ####################
    ###YOUR CODE HERE###
    ####################

    return qp.state()

matrix = np.array([[-0.69165024-0.50339329j,  0.28335369-0.43350413j],
    [ 0.1525734 -0.4949106j , -0.82910055-0.2106588j ]])

print("The state after phase kickback is: \n" , phase_kickback(matrix))