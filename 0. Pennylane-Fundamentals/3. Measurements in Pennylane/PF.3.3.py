
dev = qp.device("default.qubit", wires=2) # Define a two-qubit device here

@qp.qnode(dev)
def circuit():
    """
    This quantum function implements a Bell state and
    should return the probabilities for the PauliZ 
    observable on both qubits, using a single measurement
    """
    qp.H(wires=0)
    qp.CNOT(wires=[0,1])
    return qp.probs(op=qp.PauliZ(0)@qp.PauliZ(1)) # Add your measurement here