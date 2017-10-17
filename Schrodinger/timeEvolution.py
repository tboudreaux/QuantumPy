from ..braket import ket
from ..operators import goperator
from numpy import exp


def spin_to_energy(psi):
    return NotImplemented


def evolve(t, psi, ev):
    if len(psi) != len(ev):
        raise IndexError('Length of State Vector and Eigen Values do not match')
    else:
        elements = list()
        for amp, eigen in zip(psi, ev):
            f = lambda t: amp * exp(-1j * eigen * t)
            elements.append(lambda t:)