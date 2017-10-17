from .braket import ket
import numpy as np

# Spin 1/2 States
X2u = [1/np.sqrt(2), 1/np.sqrt(2)]
X2u = ket(X2u, eigenvalues=['+', '-'])

X2d = [1/np.sqrt(2), -1/np.sqrt(2)]
X2d = ket(X2d, eigenvalues=['+', '-'])

Y2u = [1/np.sqrt(2), 1j/np.sqrt(2)]
Y2u = ket(Y2u, eigenvalues=['+', '-'])

Y2d = [1/np.sqrt(2), -1j/np.sqrt(2)]
Y2d = ket(Y2d, eigenvalues=['+', '-'])

Z2u = [1, 0]
Z2u = ket(Z2u, eigenvalues=['+', '-'])

Z2d = [0, 1]
Z2d = ket(Z2d, eigenvalues=['+', '-'])

# Spin 1 States
X31 = [1/2, 1/np.sqrt(2), 1/2]
X31 = ket(X31, eigenvalues=['+1', '0', '-1'])

X30 = [1/np.sqrt(2), 0, -1/np.sqrt(2)]
X30 = ket(X30, eigenvalues=['+1', '0', '-1'])

X3i2 = [1/2, -1/np.sqrt(2), 1/2]
X3i2 = ket(X3i2, eigenvalues=['+1', '0', '-1'])

Y31 = [1/2, 1j/np.sqrt(2), -1/2]
Y31 = ket(Y31, eigenvalues=['+1', '0', '-1'])

Y30 = [1/np.sqrt(2), 0, 1/np.sqrt(2)]
Y30 = ket(Y30, eigenvalues=['+1', '0', '-1'])

Y3i2 = [1/2, -1j/np.sqrt(2), -1/2]
Y3i2 = ket(Y3i2, eigenvalues=['+1', '0', '-1'])

Z31 = [1, 0, 0]
Z31 = ket(Z31, eigenvalues=['+1', '0', '-1'])

Z30 = [0, 1, 0]
Z30 = ket(Z30, eigenvalues=['+1', '0', '-1'])

Z3i2 = [0, 0, 1]
Z3i2 = ket(Z3i2, eigenvalues=['+1', '0', '-1'])

# Dictionary of Spins
SpinHalfVectors = {'X':[X2u, X2d], 
                   'Y':[Y2u, Y2d],
                   'Z':[Z2u, Z2d]}
SpinOneVectors = {'X':[X31, X30, X3i2],
                  'Y':[Y31, Y30, Y3i2],
                  'Z':[Z31, Z30, Z3i2]}