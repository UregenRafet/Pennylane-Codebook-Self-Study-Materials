import pennylane as qp
from pennylane import numpy as np

dev = qp.device("default.qubit", wires = 2)

@qp.qnode(dev, diff_method = "parameter-shift", max_diff = 2)
def circuit_for_hessian(params):
    """
    Implements the circuit shown in the codercise statement
    Args:
    - params (np.ndarray): [theta_0, theta_1, theta_2, theta_3]
    Returns:
    - np.tensor: <Z0xZ1>
    """

    ####################
    ###YOUR CODE HERE###
    ####################
    qp.RY(params[0], wires=0)
    qp.IsingXX(params[1], wires=[0, 1])
    qp.RX(params[2], wires=0)
    qp.RX(params[3], wires=1)

    return qp.expval(qp.Z(0)@qp.Z(1)) # Return the expectation value required

test_params = np.array([0.1,0.2,0.3,0.4], requires_grad = True)
# Don't change test_params! 

hessian = qp.jacobian(qp.jacobian(circuit_for_hessian))(test_params) # Compute the Hessian
print("The hessian of the circuit is: \n", hessian)
