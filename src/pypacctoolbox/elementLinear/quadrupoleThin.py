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
        self._beta = beta
        self._gamma = gamma
        self._k1 = k1
        self._relativistic_variables = [self._beta, self._gamma]
        self._matrix = self.makeMatrix(self._k1, self._beta, self._gamma)

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