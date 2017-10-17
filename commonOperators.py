from .operators import goperator
from numpy import sqrt
from numpy import array

# Spin 1/2 Systems
S2x = 0.5 * array([[0, 1], [1, 0]])
S2y = 0.5 * array([[0, -1j], [1j, 0]])
S2z = 0.5 * array([[1, 0], [0, -1]])

S2x = goperator(S2x, sym='S2x')
S2y = goperator(S2y, sym='S2y')
S2z = goperator(S2z, sym='S2z')

# Spin 1 systems
S3x = sqrt(2) * array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
S3y = sqrt(2) * array([[0, -1j, 0], [1j, 0, -1j], [0, 1j, 0]])
S3z = array([[1, 0, 0], [0, 0, 0], [0, 0, -1]])

S3x = goperator(S3x, sym='S3x')
S3y = goperator(S3y, sym='S3y')
S3z = goperator(S3z, sym='S3z')

# Dictionaries
SpinHalfOperators = {'X':S2x, 
                     'Y':S2y,
                     'Z':S2z}
SpinOneOperators = {'X':S3x,
                    'Y':S3y,
                    'Z':S3z} 