dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def apply_rx_pi(state):
    """Apply an RX gate with an angle of \pi to a particular basis state.

    Args:
        state (int): Either 0 or 1. If 1, initialize the qubit to state |1>
            before applying other operations.

    Returns:
        np.array[complex]: The state of the qubit after the operations.
    """
    if state == 1:
        qp.PauliX(wires=0)

    ##################
    # YOUR CODE HERE #
    ##################
    qp.RX(np.pi, wires=0)

    # APPLY RX(pi) AND RETURN THE STATE

    return qp.state()


print(apply_rx_pi(0))
print(apply_rx_pi(1))
