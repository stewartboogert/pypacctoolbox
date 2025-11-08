from .elementLinearBase import elementLinearBase as _elementLinearBase
import sympy as _sympy
from sympy import sqrt as _sqrt
from sympy import cos as _cos
from sympy import sin as _sin
from sympy import cosh as _cosh
from sympy import sinh as _sinh

class quadrupoleThin(_elementLinearBase):

    def __init__(self, name='',
                 k1=_sympy.Symbol('k1'),
                 beta = _sympy.Symbol('beta'),
                 gamma= _sympy.Symbol('gamma')):
        _elementLinearBase.__init__(self, name, "quadrupole", 0)
        self.beta = beta
        self.gamma = gamma
        self.k1 = k1
        self._relativistic_variables = [self._beta, self._gamma]
        self.matrix = self.makeMatrix(self.k1, self.beta, self.gamma)

    @property
    def k1(self):
        return self._k1

    @k1.setter
    def k1(self, k1):
        self._k1 = k1

    def makeMatrix(self, k1, beta, gamma):
        if k1.is_negative :
            omega = _sqrt(-1)*_sqrt(k1)
        else :
            omega = _sqrt(k1)

        return _sympy.Matrix([[            1,  0,          0, 0, 0,                  0],
                              [    -omega**2,  1,          0, 0, 0,                  0],
                              [             0, 0,          1, 0, 0,                  0],
                              [             0, 0,   omega**2, 1, 0,                  0],
                              [             0, 0,          0, 0, 1,                  0],
                              [             0, 0,          0, 0, 0,                  1]])