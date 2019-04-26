import numpy as n


class Integral:

    def __init__(self):
        self._f = lambda x: 1
        self._steps = 10000
        self._leftBound = 0

    def setFunction(self, f):
        self._f = f

    def setStep(self, steps):
        self._steps = steps

    def setLeftBound(self, left):
        self._leftBound = left


class IntegralRightRect(Integral):

    def __init__(self):
        super().__init__()

    def __call__(self, x):
        f = self._f
        steps = self._steps
        a = self._leftBound
        b = x
        h = (b - a) / steps
        grid = n.linspace(a, b - h, steps)
        int = 0.0
        for d in grid:
            int += f(d + h)
        return h * int


class IntegralLeftRect(Integral):

    def __init__(self):
        super().__init__()

    def __call__(self, x):
        f = self._f
        steps = self._steps
        a = self._leftBound
        b = x
        h = (b - a) / steps
        grid = n.linspace(a, b - h, steps)
        int = 0.0
        for d in grid:
            int += f(d)
        return h * int


class IntegralCenterRect(Integral):

    def __init__(self):
        super().__init__()

    def __call__(self, x):
        f = self._f
        steps = self._steps
        a = self._leftBound
        b = x
        h = (b - a) / steps
        grid = n.linspace(a, b - h, steps)
        int = 0.0
        for d in grid:
            int += f(d + h / 2)
        return h * int


class IntegralTrapezium(Integral):

    def __init__(self):
        super().__init__()

    def __call__(self, x):
        f = self._f
        steps = self._steps
        a = self._leftBound
        b = x
        h = (b - a) / steps
        grid = n.linspace(a, b - 2*h, steps - 1)
        int = 0.0
        for d in grid:
            int += f(d + h)
        int += (f(a) + f(b))/2
        return h * int


class IntegralSimpson(Integral):

    def __init__(self):
        super().__init__()

    def _getCoef1(self, x):
        sigma = 0.0
        f = self._f
        steps = self._steps
        a = self._leftBound
        b = x
        h = (b - a) / steps
        m = int(steps / 2)
        for i in range(0, m - 1):
            sigma += f(a + h * (2 * i + 1))
        return sigma

    def _getCoef2(self, x):
        sigma = 0.0
        f = self._f
        steps = self._steps
        a = self._leftBound
        b = x
        h = (b - a) / steps
        m = int(steps / 2)
        for i in range(1, m - 1):
            sigma += f(a + h * (2 * i))
        return sigma

    def __call__(self, x):
        f = self._f
        steps = self._steps
        a = self._leftBound
        b = x
        h = (b - a) / steps
        int = f(a) + f(b) + 4 * self._getCoef1(b) + 2 * self._getCoef2(b)
        return h / 3 * int
