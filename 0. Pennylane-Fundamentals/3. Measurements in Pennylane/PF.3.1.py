dev = qp.device("default.qubit", wires=2, shots=1) # Define a two-qubit device here

@qp.qnode(dev)
def circuit():
    """
    This quantum function implements the circuit shown above
    and should return a sample from all qubits
    """

    qp.H(wires=0)
    qp.CNOT(wires=[0,1])

    return qp.sample() # Add your measurement here

