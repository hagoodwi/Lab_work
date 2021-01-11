#  Интерполяция таблично заданной функции

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  # Табличные значения
y = [5, 6, 8, 10, 12, 13, 12, 10, 8, 10, 8, 11, 7, 9, 11, 10, 9, 12, 11, 6]  # Табличные значения


def d1(a, b):  # Дифференциал 1-ой степени
	return (y[b] - y[a]) / (x[b] - x[a])


def d2(a, b, c):  # Дифференциал 2-ой степени
	return (d1(a, b) - d1(a, c)) / (x[b] - x[c])


def d3(a, b, c, d):  # Дифференциал 3-ой степени
	return (d2(a, b, c) - d2(a, b, d)) / (x[c] - x[d])


def d4(a, b, c, d, e):  # Дифференциал 4-ой степени
	return (d3(a, b, c, d) - d3(a, b, c, e)) / (x[d] - x[e])


def f(j, a):  # Функция, данная в задание 
	return y[a] + (j - x[a]) * (d1(a + 1, a) + (j - x[a + 1]) * (d2(a + 2, a + 1, a) +
		(j - x[a + 2]) * (d3(a + 3, a + 2, a + 1, a) + (j - x[a + 3]) * d4(a + 4, a + 3, a + 2, a + 1, a))))


ynew = []
xnew = []
i = 0
j = 1
while j <= 20:
	if j < 5:
		ynew.append(f(j, 0))
	elif j >= 17:
		ynew.append(f(j, 15))
	else:
		ynew.append(f(j, int(j) - 2))
	xnew.append(j)
	print('x =', j, ', y* = ', ynew[i])
	i += 1
	j += 0.25
plt.scatter(x, y, color='r', label='Исходные точки')
plt.plot(xnew, ynew)
plt.legend()
plt.show()