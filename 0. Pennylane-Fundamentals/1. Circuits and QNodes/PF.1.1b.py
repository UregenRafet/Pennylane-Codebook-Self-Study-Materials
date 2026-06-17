dev_qubit = qp.device("default.qubit", wires=["alice", "bob"])# Define the device here
dev_mixed = qp.device("default.mixed", wires=2) # Define the device here

@qp.qnode(dev_qubit) # Choose the device you want
def example_circuit(theta):
    
    qp.RX(theta, wires = "alice" ) # Complete with wires in the device
    qp.CNOT(wires = ["alice", "bob"] ) # Complete with wires in the device
    
    return qp.state()

print(example_circuit(0.3))