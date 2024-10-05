import numpy as _np
import sympy as _sp
from sympy import Matrix as _Matrix
from sympy import Symbol as _Symbol

from .elementBase import elementBase as _elementBase

class thick_quad(_elementBase):
    def __init__(self):
        pass


class thin_quad(_elementBase):
    def __init__(self, f):
        if type(f) is str:
            f = _Symbol(f)

        self.m2x2  = _Matrix([[1, 0],
                              [1. / f, 1]])

