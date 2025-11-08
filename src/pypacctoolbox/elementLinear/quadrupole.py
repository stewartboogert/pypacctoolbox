from .elementLinearBase import elementLinearBase as _elementLinearBase
import sympy as _sympy
from sympy import sqrt as _sqrt
from sympy import cos as _cos
from sympy import sin as _sin
from sympy import cosh as _cosh
from sympy import sinh as _sinh

class quadrupole(_elementLinearBase):

    def __init__(self, name='',
                 length=None,
                 k1=None,
                 beta = _sympy.Symbol('beta'),
                 gamma= _sympy.Symbol('gamma')):
        _elementLinearBase.__init__(self, name, "quadrupole", length)
        self.beta = beta
        self.gamma = gamma
        if not k1 :
            k1 = _sympy.Symbol(f'k1_{name}')
        self.k1 = k1
        self._relativistic_variables = [self._beta, self._gamma]
        self.matrix = self.makeMatrix(self.length, self.k1, self.beta, self.gamma)

    @property
    def k1(self):
        return self._k1

    @k1.setter
    def k1(self, k1):
        self._k1 = k1

    def makeMatrix(self, L, k1, beta, gamma):
        if k1.is_negative :
            omega = _sqrt(-1)*_sqrt(k1)
        else :
            omega = _sqrt(k1)

        return _sympy.Matrix([[       _cos(omega*L), _sin(omega*L)/omega,                     0,                    0, 0,                  0],
                              [-omega*_sin(omega*L),       _cos(omega*L),                     0,                    0, 0,                  0],
                              [                   0,                   0,        _cosh(omega*L), _sinh(omega*L)/omega, 0,                  0],
                              [                   0,                   0,  omega*_sinh(omega*L),       _cosh(omega*L), 0,                  0],
                              [                   0,                   0,                     0,                    0, 1, L/beta**2/gamma**2],
                              [                   0,                   0,                     0,                    0, 0,                  1]])