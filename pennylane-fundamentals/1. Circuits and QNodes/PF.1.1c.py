dev = qp.device("default.qubit", wires=2) # Define the device

circuit_qnode = qp.QNode(circuit, dev) # Assign a QNode to circuit"

print(circuit_qnode(0.3))
