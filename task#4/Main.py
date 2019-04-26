import Norma as norm
import math as m


listOfFunctions = [lambda x: 5.0 / (2 + 3 * (x**2)),
                   lambda x: 2.0 / (5 + m.cos(x)),
                   lambda x: (3 + 4 * (x**2)) ** (1.0 / 3),
                   lambda x: 2 / m.sqrt(m.pi) * m.exp(-(x**2))]

listOfLegend = ['5/(2 + 3x^2)',
                '2/(5 + cos(x))',
                '(3 + 4x^2)^(-1/3)',
                '2/sqrt(Pi) * exp(-x^2)']

listOfNorma = [norm.Norm(), norm.Norm2(), norm.Norm3()]


print("Нормы функций")
for n in listOfNorma:
    n.setA(0)
    n.setB(2)
    n.setStep()
for f, t in zip(listOfFunctions, listOfLegend):
    for n in listOfNorma:
        print('\t', t, n, n(f))


print("\nРасстояния между функциями")
for f1, t1 in zip(listOfFunctions, listOfLegend):
    for f2, t2 in zip(listOfFunctions, listOfLegend):
        for n in listOfNorma:
            if f1 != f2:
                print('\tРасстояние между', t1, ' и ', t2, ' ', n, n(lambda x: f1(x) - f2(x)))


i = norm.ScalarMultiplication()
i.setA(0)
i.setB(2)
i.setStep()
print("\nВсевозможные скалярные произведения функциями в E[0,2]")
for f1, t1 in zip(listOfFunctions, listOfLegend):
    for f2, t2 in zip(listOfFunctions, listOfLegend):
        if f1 != f2:
            print('\tПроизведение', t1, ' на ', t2, ' равно ', i(f1, f2))


print("\nУглы между функциями", i )
for f1, t1 in zip(listOfFunctions, listOfLegend):
    for f2, t2 in zip(listOfFunctions, listOfLegend):
        if f1 != f2:
            print('\tУгол между', t1, ' и ', t2, ' равнен ', i(f1, f2) / (m.sqrt(i(f1, f1)) * m.sqrt(i(f2, f2))))
