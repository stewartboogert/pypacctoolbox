from .drift import Drift as _Drift
import sympy as _sympy
from sympy import sqrt as _sqrt

class Quadrupole(_Drift) :
    def __init__(self,name, length, k1):
        _Drift.__init__(self, name, length)
        self._k1 = k1

        # create canonical symbols
        x, px, y, py, z, delta = _sympy.symbols('x,p_x,y,p_y,z,delta')
        beta0 = _sympy.Symbol('beta0')
        gamma0 = _sympy.Symbol("gamma0")

        # set canonical varibales
        self.canonical_coords = [x, y, z]
        self.canonical_momenta = [px, py, delta]

        # set relativistic factors
        self.relativistic_variables = [beta0, gamma0]

        # element hamiltonian
        self.hamiltonian = self.hamiltonian + self.k1 * (x**2 - y**2)/2

    @property
    def k1(self):
        return self._k1

    @k1.setter
    def length(self, k1):
        self._k1= k1