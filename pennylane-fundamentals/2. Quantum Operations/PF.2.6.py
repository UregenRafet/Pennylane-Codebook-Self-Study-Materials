dev = qp.device("default.qubit")

def do(k):

    qp.StatePrep([1,k], wires = [0], normalize = True)

def apply(theta):

    qp.IsingXX(theta, wires = [1,2])

@qp.qnode(dev)
def do_apply_undo(k,theta):
    """
    Applies V, controlled-U, and the inverse of V
    Args: 
    - k, theta: The parameters for do and apply (V and U) respectively
    Returns:
    - (np.array): The output state of the routine
    """
    do(k)
    qp.ctrl(apply, control=[0], control_values=[1])(theta)
    qp.adjoint(do)(k)
    ####################
    ###YOUR CODE HERE###
    ####################

    return qp.state()

k, theta = 0.5, 0.8

print("The output state is: \n", do_apply_undo(k, theta))