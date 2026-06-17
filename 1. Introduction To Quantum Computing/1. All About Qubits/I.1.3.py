import pennylane as qp
from pennylane import numpy as np

def measure_state(state, num_meas):
    """Simulate a quantum measurement process.

    Args:
        state (np.array[complex]): A normalized qubit state vector.
        num_meas (int): The number of measurements to take

    Returns:
        np.array[int]: A set of num_meas samples, 0 or 1, chosen according to the probability
        distribution defined by the input state.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    # COMPUTE THE MEASUREMENT OUTCOME PROBABILITIES
    p_1 = np.abs(state[0]) ** 2
    p_2 = np.abs(state[1]) ** 2
    print(f"p_1:{p_1}, p_2:{p_2}")
    rng = np.random.default_rng()
    result = rng.choice(2, num_meas, p=[p_1, p_2])
    # wire_count = np.log2(len(state))
    # dev = qp.device("default.qubit", shots=num_meas)
    # @qp.qnode(dev)
    # def circuit(state, wires):
    #     qp.StatePrep(state=state, wires=wires)
    #     return qp.sample()
    
    # RETURN A LIST OF SAMPLE MEASUREMENT OUTCOMES

    # return circuit(state, wire_count)
    return result

state = np.array([0.8, 0.6])
print(measure_state(state, 10))
