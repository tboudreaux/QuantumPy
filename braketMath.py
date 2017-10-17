from numpy import sqrt

def amplitude(bra, ket):
    return bra * ket


def probability(bra, ket):
    amp = amplitude(bra, ket)
    return (amp.conjugate() * amp).real


def vexpectation_value(psi, states, measurments):
    if psi.type == 'bra':
        psi = psi.as_ket()
    for i, e in enumerate(states):
        if e.type == 'ket':
            states[i] = states[i].as_bra()
    ev = sum([probability(x, psi) * y for x, y in zip(states, measurments)])
    return ev

def mexpectation_value(psi, state):
    return psi.as_bra() * state * psi.as_ket()

def standard_deviation(psi, state):
    one = psi.as_bra() * state * state * psi.as_ket()
    two = mexpectation_value(psi, state)**2
    return sqrt(one - two)

def commutator(stateA, stateB):
    from .operators import goperator
    if not isinstance(stateA, goperator) or not isinstance(stateB, goperator):
        raise TypeError('Arguments must be Operators')
    if not stateA.shape == stateB.shape:
        raise ValueError('Shapes of Operators must be equal')
    else:
        return stateA * stateB - stateB * stateA