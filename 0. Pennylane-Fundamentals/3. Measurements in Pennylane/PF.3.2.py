
dev = qp.device("default.qubit", wires=2) # Define a two-qubit device here

A = np.array([[1, 0], [0, -1]])
op_a = qp.Hermitian(A, wires=[0])
@qp.qnode(dev)
def circuit():
    """
    This quantum function implements a Bell state and
    should return the expectation value the observable
    corresponding to the matrix A applied to the first qubit
    """
    qp.H(wires=0)
    qp.CNOT(wires=[0,1])
    return qp.expval(op=op_a) # Add your measurement here