import numpy as np

def solve_circuit(EC:float, EJ:float, ng:int, N:int):
    """Returns the energy eigenstates"""
    n = np.linspace(-N, N, 2 * N + 1)
    diag = 4 * EC * (n - ng) ** 2
    H0 = np.zeros((2 * N + 1, 2 * N + 1))
    np.fill_diagonal(H0, diag)
    np.fill_diagonal(H0[:, 1:], -EJ / 2)
    np.fill_diagonal(H0[1:, :], -EJ / 2)

    energies, states = np.linalg.eigh(H0)
    return energies, states


