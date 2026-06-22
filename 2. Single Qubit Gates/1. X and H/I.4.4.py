import pennylane as qp
from pennylane import numpy as np

##################
# YOUR CODE HERE #
##################

# CREATE A DEVICE
dev = qp.device("default.qubit", wires=1)

@qp.qnode(dev)
def apply_hxh(state):
    if state==1:
        qp.PauliX(wires=0)
    qp.H(wires=0)
    qp.PauliX(wires=0)
    qp.H(wires=0)
    return qp.state()
# CREATE A QNODE CALLED apply_hxh THAT APPLIES THE CIRCUIT ABOVE

# Print your results
print(apply_hxh(0))
print(apply_hxh(1))
