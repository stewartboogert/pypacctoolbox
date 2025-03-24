from sympy import diff as _diff
from sympy import Wild as _Wild
from sympy import sqrt as _sqrt

class elementBase :

    def __init__(self,name):
        self.name = name
        self._hamiltonian = None
        self._canonical_coords = []
        self._canonical_momenta = []
        self._relativistic_variables = []

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

    @property
    def relativistic_variables(self):
        return self._relativistic_variables

    @relativistic_variables.setter
    def relativistic_variables(self, relativistic_variables):
        self._relativistic_variables = relativistic_variables

    def equations_of_motion(self):
        v = self.canonical_coords
        p = self.canonical_momenta

        return [_diff(self.hamiltonian,v[0]),
                _diff(self.hamiltonian,v[1]),
                _diff(self.hamiltonian,v[2]),
                _diff(self.hamiltonian,p[0]),
                _diff(self.hamiltonian,p[1]),
                _diff(self.hamiltonian,p[2])]

    def taylor_coefficient(self, var1,  order1,var2, order2):
        h = self.hamiltonian

        x, y, z, p_x, p_y, delta = self.canonical_variables
        beta0, gamma0 = self.relativistic_variables

        h_deriv = h.diff(var1, order1).diff(var2, order2)
        h_zero  = h_deriv.subs({x: 0, p_x: 0, y: 0, p_y: 0, z: 0, delta: 0})
        h_simp  = h_zero.subs({gamma0:1/_sqrt(1-beta0**2)}).simplify()

        return h_simp


    def approximate_hamiltonian(self, order=2):
        v = self.canonical_variables


        for i in range(0,len(v)) :
            for j in range(0,len(v)) :
                for o1 in range(j, order+1):
                    for o2 in range(0, order) :
                        print(v[i],v[j],o1,o2,self.taylor_coefficient(v[i],o1,v[j],o2))



