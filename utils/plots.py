import matplotlib.pyplot as plt
from ..braketMath import *
from .subutils.defaults import DEFAULT_HIST_PARAMS

def histogram(psi, states, measurments, kwargs=DEFAULT_HIST_PARAMS, view=False):
    if psi.type == 'bra':
        psi = psi.as_ket()
    for i, e in enumerate(states):
        if e.type == 'ket':
            states[i] = states[i].as_bra()

    kwargs = {**DEFAULT_HIST_PARAMS, **kwargs}

    p = [probability(x, psi) for x in states]

    fig = plt.figure()
    plt.bar(measurments, p)

    if kwargs['xlabel'] is not None:
        plt.xlabel(kwargs['xlabel'], fontsize=kwargs['xlabel_fontsize'])
    if kwargs['ylabel'] is not None:
        plt.ylabel(kwargs['ylabel'], fontsize=kwargs['ylabel_fontsize'])

    if kwargs['title'] is not None:
        plt.title(kwargs['title'], fontsize=kwargs['title_fontize'])

    if kwargs['xlim'] is not None:
        plt.xlim(kwargs['xlim'][0], kwargs['xlim'][1])

    if kwargs['ylim'] is not None:
        plt.ylim(kwargs['ylim'][0], kwargs['ylim'][1])

    if view is True:
        plt.show()
    else:
        return fig