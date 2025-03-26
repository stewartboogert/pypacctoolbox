#
# list**mi
# diff(expr, var, mi)
#

import sympy as _sympy
import math as _math
import itertools as _itertools

class MultiIndex :

    def __init__(self, indices) :
        self.indices = indices

    def __add__(self, other) :
        return MultiIndex([v1+v2 for v1, v2 in zip(self.indices, other.indices)])

    def diff(self, exprs, vars):
        pass

    def norm(self):
        vsum = 0

        for v in self.indices:
            vsum += v

        return vsum

    def iterationCount(self):
        vcount = 1

        for v in self.indices:
            vcount = vcount*v

        return vcount

    def factorial(self):
        vprod = 1

        for v in self.indices:
            vprod *=  _math.factorial(v)

        return vprod

    def binominal(self):
        pass

    def multinomial(self):
        pass

    def power(self, vars):
        pass

    def __eq__(self, other) :
        for v1,v2 in zip(self.indices, other.indices):
            if v1 != v2 :
                return False

        return True


    def __lt__(self, other) :
        for v1,v2 in zip(self.indices, other.indices) :
            if v1 >= v2 :
                return False

        return True

    def __le__(self, other) :
        for v1,v2 in zip(self.indices, other.indices) :
            if v1 > v2 :
                return False

        return True

    def __gt__(self, other):
        for v1,v2 in zip(self.indices,other.indices) :
            if v1 <= v2 :
                return False

        return True

    def __repr__(self):
        return str(self.indices)

    def __iter__(self):
        # reset counter
        self._cntr = 0

        # make cartesian product
        ranges = []
        for i  in self.indices :
            ranges.append(range(0,i))


        self._cprod = [v for v in _itertools.product(*ranges)]

        return self

    def __next__(self) :

        if self._cntr == self.iterationCount():
            raise StopIteration

        mi = MultiIndex(list(self._cprod[self._cntr]))

        self._cntr += 1

        return mi




