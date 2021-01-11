
# Решение системы нелинейных уравнений методом Ньютона

import numpy as np


def f(x):  # Система уравнений, данная в задание
    F = np.zeros(3)
    F[0] = x[0] ** 5 - 2.1 * x[2] ** 2 - 3 * x[0] ** 2 * x[1] ** 4 - 17.9
    F[1] = x[1] ** 3 - 1.5 * x[0] ** 4 * x[1] - 0.3 * x[2] ** 3 + 22.7
    F[2] = x[0] * x[2] ** 2 - 6.5 * x[0] ** 2 * x[1] ** 2 + 24
    return F


def J(x):  # Матрица Якобиана, требующаяся для решения задания
    J = np.zeros((3, 3))
    J[0][0] = 5*x[0]**4 - 6*x[0]*x[1]**4
    J[0][1] = -12*x[0]**2*x[1]**3
    J[0][2] = -4.2*x[2]
    J[1][0] = -6*x[1]*x[0]**3
    J[1][1] = 3*x[1]**2 - 1.5*x[0]**4
    J[1][2] = -0.9*x[2]**2
    J[2][0] = x[2]**2 - 13*x[0]*x[1]**2
    J[2][1] = -13*x[1]*x[0]**2
    J[2][2] = 2*x[2]*x[0]
    return J


x = np.array([1, 1, 1])
x0 = x         # Начальный x
eps = 0.00001  # Погрешность
k = 1
while True:
    d = np.linalg.solve(J(x), -f(x))
    print(f"Итерация: {k}   x = {x[0]} y = {x[1]} z = {x[2]}")
    if np.linalg.norm(d) < eps:
        print(f"Начальные значения: x = {x0[0]} y = {x0[1]} z = {x0[2]}")
        print(f"Количество итераций: {k}")
        print(f"Решение: x = {x[0]} y = {x[1]} z = {x[2]}")
        break
    if k > 500:
        print("Решение не найдено!")
        break
    k += 1
    x = x + d