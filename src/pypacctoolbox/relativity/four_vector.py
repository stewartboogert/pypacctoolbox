class FourVector :
    def __init__(self, v0, v1, v2, v3):
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def norm(self):
        return self.v0*self.v0 - self.v1*self.v1 - self.v2*self.v2 - self.v3*self.v3


    def __add__(self, other):
        return FourVector(
            self.v0 + other.v0,
            self.v1 + other.v1,
            self.v2 + other.v2,
            self.v3 + other.v3
        )

    def __sub__(self, other):
        return FourVector(
            self.v0 - other.v0,
            self.v1 - other.v1,
            self.v2 - other.v2,
            self.v3 - other.v3
        )

    def __mul__(self, other):
        return self.v0 * other.v0 - self.v1 * other.v1 - self.v2 * other.v2 - self.v3 * other.v3
