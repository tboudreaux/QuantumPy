from vectorpy import vector
import numpy as np


class ket():
    def __init__(self, state_matrix, sym='P', latex_sym=None, eigenvalues=None):
        if type(state_matrix) is list:
            state_matrix = np.array(state_matrix)
        if state_matrix.shape != 1:
            state_matrix = state_matrix.T
        self.psi = np.array(state_matrix)
        self.psi = self.psi.reshape(max(self.psi.shape), 1)
        self.sym = sym
        self.right_braket = '>'
        if latex_sym == None:
            self.latex_sym = sym
        else:
            self.latex_sym = latex_sym
        self.type = 'ket'

        if eigenvalues == None:
            self.eigenvalues = list()
            for i, _ in enumerate(self.psi):
                self.eigenvalues.append('a{}'.format(i))
        else:
            if not isinstance(eigenvalues, list):
                raise TypeError('Eignevalue declaritive argument must be of type list')
            else:
                bad_value = False
                for eigen in eigenvalues:
                    if not isinstance(eigen, str):
                        if not isinstance(eigen, int):
                            if not isinstance(eigen, float):
                                bad_value = True
                if bad_value:
                    raise ValueError('Elements of Eigenvalue declaritive list must'\
                                     'be of type string, integer, or float')
                else:
                    self.eigenvalues = eigenvalues

    def __mul__(self, other):
        if isinstance(other, ket):
            return NotImplemented
        if isinstance(other, int) or isinstance(other, float):
            out_state_matrix = other * self.psi
            return ket(out_state_matrix)
        if isinstance(other, bra):
            from ..operators import goperator
            return goperator(np.dot(self.psi, other.psi))
        return

    def __add__(self, other):
        if isinstance(other, bra):
            return NotImplemented
        if isinstance(other, int) or isinstance(other, float):
            return NotImplemented
        if isinstance(other, ket):
            new_matrix = list()
            for i, eigen in enumerate(self.eigenvalues):
                if eigen in other.eigenvalues:
                    selfamp = self.psi[i]
                    otheamp = other.psi[np.where(other.eigenvalues == eigen)]
                    print(otheamp)
                    print(selfamp)


    def as_bra(self):
        return bra(self.psi.conjugate(), sym=self.sym, eigenvalues=self.eigenvalues)

    def as_ket(self):
        return ket(self.psi, sym=self.sym, eigenvalues=self.eigenvalues)

    def normalized(self):
        return ket(self.psi/self.__abs__(), sym=self.sym, eigenvalues=self.eigenvalues)

    def __repr__(self):
        out = list()
        right = list()
        out.append(u'|{value}{braket}'.format(value = self.sym, braket = self.right_braket))
        for amp, e in zip(self.psi, self.eigenvalues):
            right.append(u'{value}|{eigen}{braket}'.format(value=amp[0], eigen=e, 
                                                           braket=self.right_braket))
        out.append(' + '.join(right))
        out = ' = '.join(out)
        return out

    def __abs__(self):
        ip = self.as_bra() * self
        return np.sqrt(ip)

    def to_latex(self, filename=None):
        out = list()
        right = list()
        build_ket = '{' + self.latex_sym + '}'
        out.append('\\ket{}'.format(build_ket))
        for i, e in enumerate(self.psi):
            build_ket = '{' + 'A_' + '{' + str(i) + '}' + '}'
            right.append('{value}\\ket{inner}'.format(value=e[0], inner=build_ket))
        out.append(' + '.join(right))
        out = ' = '.join(out)
        return out

    def __getitem__(self, key):
        if isinstance(key, slice):
            return NotImplemented
        if isinstance(key, int):
            if key < len(self.psi):
                return self.psi[key][0], self.eigenvalues[key]
            else:
                raise IndexError('Key out of range')
        else:
            raise TypeError('Non Integer Key Requested')

    def __len__(self):
        return self.psi.shape[0]



class bra():
    def __init__(self, state_matrix, sym='P', latex_sym=None, eigenvalues=None):
        self.psi = np.array(state_matrix)
        self.psi = self.psi.reshape(1, max(self.psi.shape))
        self.sym = sym
        self.left_braket = '<'
        if latex_sym == None:
            self.latex_sym = sym
        else:
            self.latex_sym = latex_sym
        self.type = 'bra'

        if eigenvalues == None:
            self.eigenvalues = list()
            for i, eigen in enumerate(self.psi):
                self.eigenvalues.append('a{}'.format(i))
        else:
            if not isinstance(eigenvalues, list):
                raise TypeError('Eignevalue declaritive argument must be of type list')
            else:
                bad_value = False
                for eigen in eigenvalues:
                    if not isinstance(eigen, str):
                        if not isinstance(eigen, int):
                            if not isinstance(eigen, float):
                                bad_value = True
                if bad_value:
                    raise ValueError('Elements of Eigenvalue declaritive list must'\
                                     'be of type string, integer, or float')
                else:
                    self.eigenvalues = eigenvalues

    def __mul__(self, other):
        if isinstance(other, ket):
            if set(other.eigenvalues) != set(self.eigenvalues):
                raise TypeError('State Vectors Do Not Share Eigenvalues')
            s = np.argsort(self.eigenvalues)
            spsi = np.array(self.psi[0])[s]
            opsi = np.array(other.psi)[s]
            return np.dot(spsi, opsi)[0]
        if isinstance(other, bra):
            return NotImplemented
        if isinstance(other, int) or isinstance(other, float):
            return bra(self.psi * other)
        from ..operators import goperator
        if isinstance(other, goperator):
            return NotImplemented

    def __abs__(self):
        return bra(self.psi/(np.sqrt(self.psi.conjugate() * self.psi)))

    def normalized(self):
        return self.__abs__()

    def as_ket(self):
        return ket(self.psi.conjugate())

    def as_bra(self):
        return bra(self.psi)

    def __repr__(self):
        out = list()
        right = list()
        out.append(u'{braket}{value}|'.format(value = self.sym, braket = self.left_braket))
        for amp, e in zip(self.psi[0], self.eigenvalues):
            right.append(u'{value1}{braket}{eigen}|'.format(value1=e, braket=self.left_braket,
                                                            eigen=e))
        out.append(' + '.join(right))
        out = ' = '.join(out)
        return out

    def to_latex(self, filename=None):
        out = list()
        right = list()
        build_ket = '{' + self.latex_sym + '}'
        out.append('\\bra{}'.format(build_ket))
        for i, e in enumerate(self.psi[0]):
            build_ket = '{' + 'A_' + '{' + str(i) + '}' + '}'
            right.append('{value}\\bra{inner}'.format(value=e, inner=build_ket))
        out.append(' + '.join(right))
        out = ' = '.join(out)
        return out

    def __getitem__(self, key):
        if isinstance(key, slice):
            return NotImplemented
        if isinstance(key, int):
            if key < len(self.psi[0]):
                return self.psi[0][key], self.eigenvalues[key]
            else:
                raise IndexError('Key out of range')
        else:
            raise TypeError('Non Integer Key Requested')

    def __len__(self):
        return self.psi.shape[1]