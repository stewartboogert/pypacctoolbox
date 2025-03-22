from sympy import diff as _diff

class elementBase :

    def __init__(self,name):
        self.name = name
        self._hamiltonian = None
        self._canonical_coords = []
        self._canonical_momenta = []

    @property
    def hamiltonian(self):
        return self._hamiltonian

    @hamiltonian.setter
    def hamiltonian(self, hamiltonian):
        self._hamiltonian = hamiltonian

    @property
    def canonical_coords(self):
        return self._canonical_coords

    @canonical_coords.setter
    def canonical_coords(self, canonical_coords):
        self._canonical_coords = canonical_coords

    @property
    def canonical_momenta(self):
        return self._canonical_momenta

    @canonical_momenta.setter
    def canonical_momenta(self, canonical_momenta):
        self._canonical_momenta = canonical_momenta

    @property
    def canonical_variables(self):
        return self.canonical_coords + self.canonical_momenta

    @canonical_variables.setter
    def canonical_variables(self, canonical_variables):
        self.canonical_coords = canonical_variables[0:3]
        self.canonical_momenta = canonical_variables[3:6]

    def equations_of_motion(self):
        v = self.canonical_coords
        p = self.canonical_momenta

        return [_diff(self.hamiltonian,v[0]),
                _diff(self.hamiltonian,v[1]),
                _diff(self.hamiltonian,v[2]),
                _diff(self.hamiltonian,p[0]),
                _diff(self.hamiltonian,p[1]),
                _diff(self.hamiltonian,p[2])]

