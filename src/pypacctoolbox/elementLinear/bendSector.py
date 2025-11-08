from .elementLinearBase import elementLinearBase as _elementLinearBase
import sympy as _sympy
from sympy import sqrt as _sqrt
from sympy import cos as _cos
from sympy import sin as _sin
from sympy import cosh as _cosh
from sympy import sinh as _sinh

class bendSector(_elementLinearBase):

    def __init__(self, name='',
                 length=_sympy.Symbol('L'),
                 k0=_sympy.Symbol('k0'),
                 beta = _sympy.Symbol('beta'),
                 gamma= _sympy.Symbol('gamma')):
        _elementLinearBase.__init__(self, name, "quadrupole", length)
        self.beta = beta
        self.gamma = gamma
        self.k0 = k0
        self._relativistic_variables = [self._beta, self._gamma]
        self.matrix = self.makeMatrix(self.length, self.k0, self.beta, self.gamma)

    @property
    def k0(self):
        return self._k0

    @k0.setter
    def k0(self, k0):
        self._k0 = k0

    def makeMatrix(self, L, k0, beta, gamma):
        omega = k0

        return _sympy.Matrix([[       _cos(omega*L),             _sin(omega*L)/omega, 0, 0, 0,                               (1-_cos(omega*L))/(omega*beta)],
                              [-omega*_sin(omega*L),                   _cos(omega*L), 0, 0, 0,                                           _sin(omega*L)/beta],
                              [                   0,                               0, 1, L, 0,                                                            0],
                              [                   0,                               0, 0, 1, 0,                                                            0],
                              [  _sin(omega*L)/beta, -(1-_cos(omega*L))/(omega*beta), 0, 0, 1, L/beta**2/gamma**2-(omega*L-_sin(omega*L))/(omega * beta**2)],
                              [                   0,                               0, 0, 0, 0,                                                            1]])