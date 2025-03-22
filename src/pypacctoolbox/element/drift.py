from .elementBase import elementBase as _elementBase
import sympy as _sympy
from sympy import sqrt as _sqrt

class Drift(_elementBase) :
    def __init__(self, name,length) :
        _elementBase.__init__(self,name)
        self._length = length

        # create canonical symbols
        x, px, y, py, z, delta = _sympy.symbols('x,p_x,y,p_y,z,delta')
        beta0 = _sympy.Symbol('beta0')
        gamma0 = _sympy.Symbol("gamma0")

        # set canonical varibales
        self.canonical_coords = [x, y, z]
        self.canonical_momenta   = [px, py, delta]

        # set relativistic factors
        self.relativistic_variables = [beta0, gamma0]

        # element hamiltonian
        self.hamiltonian = delta/beta0 - _sqrt((delta + 1/beta0)**2 - px**2 - py**2 - 1/(beta0*gamma0)**2)

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        if type(length) is float :
            if length < 0 :
                raise ValueError("length cannot be negative")
        self._length = length