import pennylane as qp
from pennylane import numpy as np

dev = qp.device("default.qubit", wires = 3)

@qp.qnode(dev)
def embedding_and_circuit(features, params):
    """
    A QNode that depends on trainable and non-trainable parameters
    Args:
    - features (np.ndarray): Non-trainable parameters in the AngleEmbedding routine
    - params (np.ndarray): Trainable parameters for the rest of the circuit
    Returns:
    - (np.tensor): <Z0>
    """

    ####################
    ###YOUR CODE HERE###
    ####################
    qp.AngleEmbedding(features=features, wires= [0, 1, 2])
    qp.CNOT(wires=[0, 1])
    qp.CNOT(wires=[1, 2])
    qp.CNOT(wires=[2, 0])
    qp.RY(params[0], wires=0)
    qp.RY(params[1], wires=1)
    qp.RY(params[2], wires=2)
    
    return qp.expval(qp.PauliZ(0))

features = np.array([0.3,0.4,0.6], requires_grad = False)
params = np.array([0.4,0.7,0.9], requires_grad = True)
print("The gradient of the circuit is:", qp.jacobian(embedding_and_circuit)(features, params))
