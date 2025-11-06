from .elementLinearBase import elementLinearBase as _elementLinearBase

from sympy import Symbol as _Symbol

class line(_elementLinearBase):

    def __init__(self, name='temp'):
        _elementLinearBase.__init__(self, name, "line", _Symbol("temp"))
        self._nameCountDict = {}
        self._elements = []

    @property
    def nameCountDict(self):
        return self._nameCountDict

    @nameCountDict.setter
    def nameCountDict(self, nameCountDict):
        self._nameCountDict = nameCountDict

    @property
    def elements(self):
        return self._elements;

    @elements.setter
    def elements(self, elements):
        self._elements = elements

    def append(self,e):
        # append length
        if len(self.elements) == 0:
            self.length = e.length
        else :
            self.length += e.length

        # count the name
        if e.name in self.nameCountDict:
            self.nameCountDict[e.name] += 1
        else :
            self.nameCountDict[e.name] = 1

        # append matrix calculation
        if not self.matrix :
            self.matrix = e.matrix
        else :
            self.matrix = self.matrix * e.matrix

        self.elements.append(e)

    def reverse(self):
        self.elements.reverse(self)

        # recompute matrix

    def __add__(self, other):
        l = line()
        l.elements = self.elements + other.elements

        # merge name count dicts
        for k in self.nameCountDict:
            l.nameCountDict[k] = self.nameCountDict[k]

        for k in other.nameCountDict:
            if k in l.nameCountDict:
                l.nameCountDict[k] += other.nameCountDict[k]
            else:
                l.nameCountDict[k] = other.nameCountDict[k]

        # merge lengths
        l.length = self.length + other.length

        return l

    def __getitem__(self,i):
        return self.elements[i]

    def __repr__(self):
        s = ""
        for e in self.elements:
            s += e.__repr__() + "\n"

        return s