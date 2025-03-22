from sympy import diff as _diff

class elementBase :

    def __init__(self,name):
        self.name = name
        self._hamiltonian = None
        self._canonical_variables = []
        self._canonical_momenta = []

    @property
    def hamiltonian(self):
        return self._hamiltonian

    @hamiltonian.setter
    def hamiltonian(self, hamiltonian):
        self._hamiltonian = hamiltonian

    @property
    def canonical_variables(self):
        return self._canonical_variables

    @canonical_variables.setter
    def canonical_variables(self, canonical_variables):
        self._canonical_variables = canonical_variables

    @property
    def canonical_momenta(self):
        return self._canonical_momenta

    @canonical_momenta.setter
    def canonical_momenta(self, canonical_momenta):
        self._canonical_momenta = canonical_momenta

    def equations_of_motion(self):
        v = self.canonical_variables
        p = self.canonical_momenta

        print(_diff(self.hamiltonian,v[0]))
        print(_diff(self.hamiltonian,v[1]))
        print(_diff(self.hamiltonian,v[2]))

        print(_diff(self.hamiltonian,p[0]))
        print(_diff(self.hamiltonian,p[1]))
        print(_diff(self.hamiltonian,p[2]))

