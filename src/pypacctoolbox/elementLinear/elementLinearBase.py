import sympy as _sympy

from sympy import Matrix as _Matrix

class elementLinearBase :

    def __init__(self,
                 name='',
                 type='base',
                 length=0):
        self._name = name
        self._type = type
        self._length = length

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, name):
        self._type = type

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    @property
    def matrix(self):
        try :
            return self._matrix
        except :
            return _Matrix([[1,0,0,0,0,0],
                            [0,1,0,0,0,0],
                            [0,0,1,0,0,0],
                            [0,0,0,1,0,0],
                            [0,0,0,0,1,0],
                            [0,0,0,0,0,1]])

    @matrix.setter
    def matrix(self, matrix):
        self._matrix = matrix

    @property
    def matrixXYZ(self):
        return self.matrix

    @property
    def matrixX(self):
        return self.matrix[0:2,0:2]

    @property
    def matrixY(self):
        return self.matrix[2:4,2:4]

    @property
    def matrixXY(self):
        return self.matrix[0:4,0:4]

    @property
    def matrixZ(self):
        return self.matrix[4:6,4:6]

    @property
    def matrixXZ(self):
        z = _sympy.Matrix([[0,0],[0,0]])
        mx = self.matrixX
        mz = self.matrixZ

        blocks = [[mx,z],[z,mz]]

        return _sympy.BlockMatrix(blocks).as_explicit()

    def __mul__(self, other):
        from .line import line as line

        l = line()
        l._matrix = self.matrixXYZ * other.matrixXYZ
        l._length = self.length + other.length

        return l

    def __str__(self):
        return self.name + " " + self.type + " " + str(self.length)

    def __repr__(self):
        return self.name + " " + self.type + " " + str(self.length)
