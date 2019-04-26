import numpy as m
import Derivative as der
import Integral as int


class Norm:

    def setA(self, a):
        self._aBound = a

    def setB(self, b):
        self._bBound = b

    def setStep(self, n = 10000):
        self._n = n
        self._h = (self._bBound - self._aBound) / n

    def getStep(self):
        return self._h

    def findMax(self, f):
        max = 0
        for i in m.linspace(self._aBound, self._bBound, self._n):
            if max < m.fabs(f.__call__(i)):
                max = m.fabs(f.__call__(i))
        return max

    def __call__(self, f):
        return self.findMax(f)

    def __str__(self):
        return 'В С[' + str(self._aBound) + ',' + str(self._bBound) + '] ->'


class Norm2(Norm):
    def __call__(self, f):
        d = der.Derivative5()
        d.setStep(self.getStep())
        d.setFunction(f)
        return self.findMax(f) + self.findMax(d)

    def __str__(self):
        return 'В С1[' + str(self._aBound) + ',' + str(self._bBound) + '] ->'


class Norm3(Norm):
    def __call__(self, f):
        d1 = der.Derivative5()
        d1.setStep(self.getStep())
        d1.setFunction(f)
        d2 = der.SecondDerivative()
        d2.setStep(self.getStep())
        d2.setFunction(f)
        return self.findMax(f) + self.findMax(d1) + self.findMax(d2)

    def __str__(self):
        return 'В С2[' + str(self._aBound) + ',' + str(self._bBound) + '] ->'


class ScalarMultiplication(Norm):

    def __call__(self, first, second):
        i = int.IntegralCenterRect()
        i.setStep(1000)
        i.setLeftBound(self._aBound)
        i.setFunction(lambda x: first(x) * second(x))
        return i(self._bBound)

    def __str__(self):
        return 'В Гильбертовом пространстве E[' + str(self._aBound) + ',' + str(self._bBound) + ']'


def __str__(self):
    return 'Гильбертово пространство[' + str(self._aBound) + ',' + str(self._bBound) + ']'