from .elementBase import elementBase as _elementBase
from sympy import cos as _cos
from sympy import sin as _sin

from sympy import Matrix as _Matrix
class transfer_matrix(_elementBase):
    def __init__(self, elements =[]):
        self.m2x2 = _Matrix([[1,0],[0,1]])

class cs_matrix(_elementBase):
    def __init__(self, c, s, cp, sp):
        self.m2x2 = _Matrix([[c,s],[cp,sp]])

class twiss_matrix():
    def __init__(self, beta0, alpha0, gamma0, mu):
        self.m2x2 = _Matrix([[_cos(mu) + alpha0*_sin(mu), beta0*_sin(mu)],
                             [-gamma0*_sin(mu), _cos(mu)-alpha0*sin(mu)]])
class beta_matrix(_elementBase):
    def __init__(self, beta, alpha, gamma):
        self.m2x2 = _Matrix([[beta, -alpha],[-alpha, gamma]])
class twiss_transform_matrix :
    def __init__(self, c,s, cp, sp):
        self.m2x2 = _Matrix([[c**2, -2*s*c, s**2],
                             [-c*cp, sp*cp + s*cp, -s*sp],
                             [cp**2, -2*sp*cp, sp**2]])
