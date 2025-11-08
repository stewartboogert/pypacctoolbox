from .elementLinearBase import elementLinearBase as _elementLinearBase
import sympy as _sympy

class drift(_elementLinearBase):

    def __init__(self, name='',
                 length=_sympy.Symbol('L'),
                 beta = _sympy.Symbol('beta'),
                 gamma= _sympy.Symbol('gamma')):
        _elementLinearBase.__init__(self, name, "drift", length)
        self.beta = beta
        self.gamma = gamma
        self._relativistic_variables = [self._beta, self._gamma]
        self._matrix = self.makeMatrix(self.length, self.beta, self.gamma)

    def makeMatrix(self, L, beta, gamma):
        return _sympy.Matrix([[1, L, 0, 0, 0,                  0],
                              [0, 1, 0, 0, 0,                  0],
                              [0, 0, 1, L, 0,                  0],
                              [0, 0, 0, 1, 0,                  0],
                              [0, 0, 0, 0, 1, L/beta**2/gamma**2],
                              [0, 0, 0, 0, 0,                  1]])

