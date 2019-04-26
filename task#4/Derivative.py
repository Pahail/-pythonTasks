class Derivative:

    def setFunction(self, f):
        self._f = f

    def setStep(self, step):
        self._step = step


class DerivativeCenter(Derivative):

    def __init__(self):
        super().__init__()

    def __call__(self, x):
        f = self._f
        step = self._step
        return (f(x + step) - f(x - step)) / (2.0 * step)


class DerivativeRight(Derivative):
    def __init__(self):
        super().__init__()

    def __call__(self, x):
        f = self._f
        step = self._step
        return (f(x + step) - f(x)) / step


class DerivativeLeft(Derivative):
    def __init__(self):
        super().__init__()

    def __call__(self, x):
        f = self._f
        step = self._step
        return (f(x) - f(x - step)) / step


class Derivative4(Derivative):

    def __init__(self):
        super().__init__()

    def __call__(self, x):
        f = self._f
        step = self._step
        return 4.0/3 * (f(x + step) - f(x - step)) / (2 * step) - 1/3 * (f(x + 2 * step) - f(x - 2 * step)) / (4 * step)


class Derivative5(Derivative):

    def __init__(self):
        super().__init__()

    def __call__(self, x):
        f = self._f
        step = self._step
        return 1.5 * (f(x + step) - f(x - step)) / (2 * step) - 0.6 * (f(x + 2 * step) - f(x - 2 * step)) / (4 * step) + 0.1 * (f(x + 3 * step) - f(x - 3 * step)) / (6 * step)


class SecondDerivative(Derivative):
    def __init__(self):
        super().__init__()

    def __call__(self, x):
        f = self._f
        step = self._step
        return (f(x + step) - 2 * f(x) + f(x - step)) / (step ** 2)
