# I couldn't do :)

import pennylane as qml
from pennylane import numpy as np

n_shots = 10000
dev = qml.device("default.qubit", shots=n_shots)
np.random.seed(0)

@qml.qnode(dev)
def circuit():
    """
    This quantum function implements an improved version of ‘bomb tester’
    and returns relevant statistics with qml.counts
    """
    # copy and paste your previous code here
    # 1st beam-splitter
    qml.H(wires=0)
    m_bomb = qml.measure(wires=0, postselect=0) # measure and postselect
    # 2nd beam-splitter
    qml.H(wires=0)
    m_det = qml.measure(wires=0) # measure (detectors)
    # input four lines of code below
    qml.cond(m_det == 1, qml.H)(wires=0) # apply conditional operation
    qml.measure(wires=0)
    qml.H(wires=0)
    m_det_2 = qml.measure(wires=0) # measure (second set of detectors)

    return qml.counts(op=[m_bomb,m_det]),qml.counts(op=[m_det,m_det_2])

results = circuit() # array of two dictionaries
prob_suc_1 = results[0]["00"] / n_shots
prob_suc_2 = results[1]["10"] / n_shots
prob_suc = prob_suc_1 + prob_suc_2
print("The success probability is", prob_suc)