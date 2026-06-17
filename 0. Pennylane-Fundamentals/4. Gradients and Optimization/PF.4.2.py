dev = qp.device("default.qubit", wires = 4)

@qp.qnode(dev)
def strong_entangler(weights):
    """
    Applies Strongly Entangling Layers to the default initial state
    Args:
    - weights (np.ndarray): The weights argument for qp.StronglyEntanglingLayers
    Returns:
    - (np.tensor): <Z0>
    """
    qp.StronglyEntanglingLayers(weights, wires=range(4))
    ####################
    ###YOUR CODE HERE###
    ####################
    
    return qp.expval(qp.PauliZ(0))
shape = qp.StronglyEntanglingLayers.shape(n_layers=2, n_wires=4)
rng = np.random.default_rng(12345)
test_weights = rng.random(size=shape) # Write some valid weights here.

print("The output of your circuit with these weights is: ", strong_entangler(test_weights))
