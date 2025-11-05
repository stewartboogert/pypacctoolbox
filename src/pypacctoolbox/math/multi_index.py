#
# list**mi
# diff(expr, var, mi)
#
import math
import sympy as _sympy
import math as _math
import itertools as _itertools

class MultiIndex :

    def __init__(self, indices) :
        self.indices = indices

    def __add__(self, other) :
        return MultiIndex([v1+v2 for v1, v2 in zip(self.indices, other.indices)])

    def __sub__(self, other) :
        return MultiIndex([v1-v2 for v1, v2 in zip(self.indices, other.indices)])

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

    @staticmethod
    def binominal(alpha, beta):
        return alpha.factorial()/(beta.factorial()*(alpha-beta).factorial())

    def multinomial(self, k):
        return math.fabs(k)/self.factorial()

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

    @staticmethod
    def power(vars, multi_index):
        result = 1

        for v, i in zip(vars, multi_index.indices) :
            result *= v**i

        return result

    @staticmethod
    def diff(to_diff, vars, multi_index):
        for v, i in zip(vars, multi_index.indices) :
            to_diff = to_diff.diff(v,i)

        return to_diff

    @staticmethod
    def taylor(to_taylor, vars, order = 2, multi_index = None):
        taylor_series = 0

        if not multi_index :
            multi_index = MultiIndex(len(vars)*[order+1])

        for alpha in multi_index :
            # print(alpha, MultiIndex.diff(to_taylor, vars, alpha))
            if alpha.norm() < order :
                taylor_series += MultiIndex.diff(to_taylor, vars, alpha).subs(zip(vars, len(vars)*[0]))* \
                                 MultiIndex.power(vars,alpha)/alpha.factorial()

        return taylor_series

