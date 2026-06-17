import pennylane as qp
from pennylane import numpy as np

n_shots = 10000
dev = qp.device("default.qubit", shots=n_shots)
np.random.seed(0)


@qp.qnode(dev)
def circuit():
    """
    This quantum function implements the 'bomb tester' for a live bomb using mid-circuit measurements
    and returns relevant statistics with qp.counts
    """

    qp.H(wires=0)  # 1st beam-splitter
    m_bomb = qp.measure(wires=0)  # measure and postselect
    qp.H(wires=0)  # 2nd beam-splitter
    m_det = qp.measure(wires=0)  # measure (detectors)
    return qp.counts(op=[m_bomb, m_det])  # collect counts for m_bomb and m_det

results = circuit()
print(results)
prob_suc = results["01"] / n_shots # favorable cases over total cases

print('the success probability is',prob_suc)

