dev = qp.device("default.qubit", wires=3)


@qp.qnode(dev)
def circuit():
    """
    Implements a circuit and returns the state
    """
    qp.Hadamard(wires=0)
    qp.CRY(np.pi / 4, wires=(0, 1))
    qp.CRX(np.pi / 3, wires=(1, 2))
    qp.Snapshot("very_important_state")
    qp.S(wires=1)
    qp.T(wires=2)
    qp.Toffoli(wires=(0, 1, 2))
    qp.Snapshot(measurement=qp.expval(qp.Z(0)))
    qp.SWAP(wires=(0, 2))
    return qp.state()


for key, val in qp.snapshots(circuit)().items(): print(key, val)
