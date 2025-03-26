#
# list**mi
# diff(expr, var, mi)
#

import sympy as _sympy
import math as _math

class MultiIndex(list) :

    def __init__(self, index) :
        list.__init__(self,index)

    def __add__(self, other) :
        return MultiIndex([v1+v2 for v1, v2 in zip(self, other)])

    def diff(self, exprs, vars):
        pass

    def norm(self):
        vsum = 0

        for v in self:
            vsum += v

        return vsum

    def factorial(self):
        vprod = 1

        for v in self:
            vprod *=  _math.factorial(v)

        return vprod

    def binominal(self):
        pass

    def multinomial(self):
        pass

    def power(self, vars):

        pass

    def __eq__(self, other) :
        for v1,v2 in zip(self, other):
            if v1 != v2 :
                return False

        return True


    def __lt__(self, other) :
        for v1,v2 in zip(self, other):
            if v1 >= v2 :
                return False

        return True

    def __le__(self, other) :
        for v1,v2 in zip(self, other):
            if v1 > v2 :
                return False

        return True

    def __gt__(self, other):
        for v1,v2 in zip(self,other)
            if v1 <= v2 :
                return False

        return True