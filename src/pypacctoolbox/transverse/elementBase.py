import copy as _copy

class elementBase :

    def __init__(self):
        pass
    def __mul__(self, other):
        from .transfer import transfer_matrix
        t = transfer_matrix()
        t.m2x2 = self.m2x2 * other.m2x2
        return t

    def __neg__(self):
        from .transfer import transfer_matrix

        c = transfer_matrix()
        c.m2x2 = self.m2x2
        c.m2x2 = - c.m2x2
        return c


    def __pow__(self, exponent):
        from .transfer import transfer_matrix

        c = transfer_matrix()
        c.m2x2 = self.m2x2
        c.m2x2 = c.m2x2**exponent

        return c

    def __str__(self):
        return str(self.m2x2)


    def __repr__(self):
        return str(self)