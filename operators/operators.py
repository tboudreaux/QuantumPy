from vectorpy import vector
import numpy as np


class goperator:
    def __init__(self, state_matrix, sym='P'):
        try:
            assert state_matrix.shape[0] == state_matrix.shape[1]
        except AssertionError as e:
            e.args += ('Error!', 'Non Square Operator State Matrix!')
            raise
        self.state_matrix = state_matrix
        self.sym = sym
        self.type = 'operator'
        self.shape = self.state_matrix.shape

    def get_eigens(self):
        return np.linalg.eigh(self.state_matrix)

    def hermetian_adjoint(self):
        return goperator(self.state_matrix.conj().T)

    def is_hermetian(self):
        return self.state_matrix.conjugate.T == self.state_matrix

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return goperator(self.state_matrix * other)
        if isinstance(other, goperator):
            try:
                assert self.state_matrix.shape[-1] == other.state_matrix.shape[0]
            except AssertionError as e:
                e.args += ('Error!', 'Inccorectly shaped Operator')
                raise
            return goperator(np.dot(self.state_matrix, other.state_matrix))

        from ..braket import ket
        if isinstance(other, ket):
            try:
                assert self.state_matrix.shape[-1] == other.psi.shape[0]
            except AssertionError as e:
                e.args += ('Error!', 'Inccorectly shaped ket')
                raise
            return ket(np.dot(self.state_matrix, other.psi),
                       sym=other.sym,eigenvalues=other.eigenvalues)

        from ..braket import bra
        if isinstance(other, bra):
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return goperator(self.state_matrix * other)
        if isinstance(other, goperator):
            try:
                assert other.shape[-1] == self.shape[0]
            except AssertionError as e:
                e.args += ('Error!', 'Inccorectly shaped Operator')
                raise
            return goperator(np.dot(other.state_matrix, self.state_matrix))

        from ..braket import ket
        if isinstance(other, ket):
            return NotImplemented

        from ..braket import bra
        if isinstance(other, bra):
            try:
                assert other.psi.shape[-1] == self.state_matrix.shape[0]
            except AssertionError as e:
                e.args += ('Error!', 'Inccorectly shaped bra')
                raise
            return bra(np.dot(other.psi, self.state_matrix),
                       sym=other.sym, eigenvalues=other.eigenvalues)

    def __pow__(self, other):
        if isinstance(other, goperator):
            return NotImplemented
        if isinstance(other, int):
            new_state_matrix = self.state_matrix
            for i in range(other - 1):
                new_state_matrix = np.dot(new_state_matrix, self.state_matrix)
            return goperator(new_state_matrix)

    def __add__(self, other):
        if isinstance(other, goperator) or other == 0:
            if other != 0:
                return goperator(self.state_matrix + other.state_matrix)
            else:
                return goperator(self.state_matrix)
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, goperator) or other == 0:
            if other != 0:
                return goperator(self.state_matrix + other.state_matrix)
            else:
                return goperator(self.state_matrix)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, goperator) or other == 0:
            if other != 0:
                return goperator(self.state_matrix - other.state_matrix)
            else:
                return goperator(self.state_matrix)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, goperator) or other == 0:
            if other != 0:
                return goperator(self.state_matrix - other.state_matrix)
            else:
                return goperator(self.state_matrix)
        else:
            return NotImplemented

    def __repr__(self):
        out = list()
        for p, i in enumerate(self.state_matrix):
            temp = list()
            for k, j in enumerate(i):
                if p == 0:
                    temp.append(str(j))
                else:
                    if k == 0:
                        string = '{0:>{1}}'.format(str(j), len(self.sym) + 2)
                    else:
                        string = '{}'.format(str(j))
                    temp.append(string)
            out.append(' '.join(temp))
        out = '\n'.join(out)
        out = '{}={}'.format(self.sym, out)
        return out

    def __eq__(self, other):
        if isinstance(other, goperator):
            if np.array_equal(self.state_matrix, other.state_matrix):
                return True
            else:
                return False
        else:
            return NotImplemented


