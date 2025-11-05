import sympy as _sympy

class elementLinearBase :

    def __init__(self, name='',
                 length=_sympy.Symbol('L'),):
        self.name = name
        self.length = length

