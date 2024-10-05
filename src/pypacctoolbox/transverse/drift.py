from sympy import Symbol as _Symbol
from sympy import Matrix as _Matrix

from .elementBase import elementBase as _elementBase
class drift(_elementBase):
    def __init__(self, d):
        super().__init__()

        if type(d) is str:
            d = _Symbol(d)

        self.m2x2  = _Matrix([[1, d],
                              [0, 1]])
