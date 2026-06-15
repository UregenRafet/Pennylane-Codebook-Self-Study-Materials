import pennylane as qp
from pennylane import numpy as np
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

def cost_function(params):
    """
    Computes the cost function given in the codercise, as a function of the
    parameters of circuit_as_function.
    Args:
    - params (np.ndarray): The parameters we pass to circuit_as_function
    Returns:
    - np.float: The cost function evaluated in params.
    """
    ################
    #YOUR CODE HERE#
    ################
    x = circuit_as_function(params)

    
    return  x**3 - 0.5 * (x**2) + x # Return the value of the cost function