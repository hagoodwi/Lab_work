
# Программа для решение нелинейного уравнения методом Ньютона

from sympy import cos, sin, cosh, sinh


def f(x):  # Функция, указанная в задании
    return float(cos(x) * cosh(x) - 1)


def df(x):  # Производная функции
    return float(cos(x)*sinh(x) - sin(x)*cosh(x))


def newton(x, eps):  # Функция Ньютона для решения задания
    f_value = f(x)
    iteration = 0
    while abs(f_value) > eps and iteration < 200:
        x = x - f_value/df(x)
        f_value = f(x)
        iteration += 1
        print(f'итерация №{iteration}   x = {x}')
    if iteration >= 200:
        iteration = -1
    return x, iteration


x0 = 7.5     # Начальный x
eps = 0.001  # Погрешность
print(f'Начальный x = {x0}')
x, iteration = newton(x0, eps)
if iteration == -1:
    print('Нет решения!')
else:
    print(f'Ответ: x = {x}')