import random
import numpy as np
from prettytable import PrettyTable

x1_min = -10
x1_max = 50
x2_min = -20
x2_max = 60
x3_min = -20
x3_max = 5
x_av_max = x1_max + x2_max + x3_max / 3
x_av_min = x1_min + x2_min + x3_min / 3
y_max = int(200 + x_av_max)
y_min = int(200 + x_av_min)
m = 3

print("Кодоване значення X")
table1 = PrettyTable()
X11 = ("-1", "-1", "+1", "+1")
X22 = ["-1", "+1", "-1", "+1"]
X33 = ["-1", "+1", "+1", "-1"]
table1.add_column("№", (1, 2, 3, 4))
table1.add_column("X1", X11)
table1.add_column("X2", X22)
table1.add_column("X3", X33)
print(table1, "\n")

print("Матриця планування для m=3")
table2 = PrettyTable()
X1 = [x1_min, x1_min, x1_max, x1_max]
X2 = [x2_min, x2_max, x2_min, x2_max]
X3 = [x3_min, x3_max, x3_max, x3_min]
Y1 = [random.randrange(y_min, y_max, 1) for i in range(0, m + 1)]
Y2 = [random.randrange(y_min, y_max, 1) for i in range(0, m + 1)]
Y3 = [random.randrange(y_min, y_max, 1) for i in range(0, m + 1)]
table2.add_column("№", (1, 2, 3, 4))
table2.add_column("X1", X1)
table2.add_column("X2", X2)
table2.add_column("X3", X3)
table2.add_column("Y1", Y1)
table2.add_column("Y2", Y2)
table2.add_column("Y3", Y3)
print(table2, "\n")

print("Середнє значення функції відгуку за рядками ")
y1_av1 = (Y1[0] + Y2[0] + Y3[0]) / 3
y2_av2 = (Y1[1] + Y2[1] + Y3[1]) / 3
y3_av3 = (Y1[2] + Y2[2] + Y3[2]) / 3
y4_av4 = (Y1[3] + Y2[3] + Y3[3]) / 3

mx1 = sum(X1) / 4
mx2 = sum(X2) / 4
mx3 = sum(X3) / 4

my = (y1_av1 + y2_av2 + y3_av3 + y4_av4) / 4

a1 = (X1[0] * y1_av1 + X1[1] * y2_av2 + X1[2] * y3_av3 + X1[3] * y4_av4) / 4
a2 = (X2[0] * y1_av1 + X2[1] * y2_av2 + X2[2] * y3_av3 + X2[3] * y4_av4) / 4
a3 = (X3[0] * y1_av1 + X3[1] * y2_av2 + X3[2] * y3_av3 + X3[3] * y4_av4) / 4

a11 = (X1[0] * X1[0] + X1[1] * X1[1] + X1[2] * X1[2] + X1[3] * X1[3]) / 4
a22 = (X2[0] * X2[0] + X2[1] * X2[1] + X2[2] * X2[2] + X2[3] * X2[3]) / 4
a33 = (X3[0] * X3[0] + X3[1] * X3[1] + X3[2] * X3[2] + X3[3] * X3[3]) / 4
a12 = a21 = (X1[0] * X2[0] + X1[1] * X2[1] + X1[2] * X2[2] + X1[3] * X2[3]) / 4
a13 = a31 = (X1[0] * X3[0] + X1[1] * X3[1] + X1[2] * X3[2] + X1[3] * X3[3]) / 4
a23 = a32 = (X2[0] * X3[0] + X2[1] * X3[1] + X2[2] * X3[2] + X2[3] * X3[3]) / 4

b01 = np.array([[my, mx1, mx2, mx3], [a1, a11, a12, a13], [a2, a12, a22, a32], [a3, a13, a23, a33]])
b02 = np.array([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a32], [mx3, a13, a23, a33]])
b0 = np.linalg.det(b01) / np.linalg.det(b02)

b11 = np.array([[1, my, mx2, mx3], [mx1, a1, a12, a13], [mx2, a2, a22, a32], [mx3, a3, a23, a33]])
b12 = np.array([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a32], [mx3, a13, a23, a33]])
b1 = np.linalg.det(b11) / np.linalg.det(b12)

b21 = np.array([[1, mx1, my, mx3], [mx1, a11, a1, a13], [mx2, a12, a2, a32], [mx3, a13, a3, a33]])
b22 = np.array([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a32], [mx3, a13, a23, a33]])
b2 = np.linalg.det(b21) / np.linalg.det(b22)

b31 = np.array([[1, mx1, mx2, my], [mx1, a11, a12, a1], [mx2, a12, a22, a2], [mx3, a13, a23, a3]])
# b31 - визначник матриці, для якого ми замість 4 стовпця підставляємо стовпець вільних членів
b32 = np.array([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a32], [mx3, a13, a23, a33]])
# b32 - визначник матриці
b3 = np.linalg.det(b31) / np.linalg.det(b32)
"""
b3 - один з шуканих коефіцієнтів рівняння регресії, в даному випадку знаходиться методом Крамера шляхом
ділення коефіцієнта b31 на коефіцієнт b32
"""

print("y1_av1=" + str(round(b0 + b1 * X1[0] + b2 * X2[0] + b3 * X3[0], 2)) + "=" + str(round(y1_av1, 2)))
print("y2_av2=" + str(round(b0 + b1 * X1[1] + b2 * X2[1] + b3 * X3[1], 2)) + "=" + str(round(y2_av2, 2)))
print("y3_av3=" + str(round(b0 + b1 * X1[2] + b2 * X2[2] + b3 * X3[2], 2)) + "=" + str(round(y3_av3, 2)))
print("y4_av4=" + str(round(b0 + b1 * X1[3] + b2 * X2[3] + b3 * X3[3], 2)) + "=" + str(round(y4_av4, 2)))
if round(b0 + b1 * X1[0] + b2 * X2[0] + b3 * X3[0], 2) == round(y1_av1, 2) and round(
        b0 + b1 * X1[1] + b2 * X2[1] + b3 * X3[1], 2) == round(y2_av2, 2) and round(
        b0 + b1 * X1[2] + b2 * X2[2] + b3 * X3[2], 2) == round(y3_av3, 2) and round(
        b0 + b1 * X1[3] + b2 * X2[3] + b3 * X3[3], 2) == round(y4_av4, 2):
    print("Значення співпадають")
else:
    print("Значення не співпадають")

print("Дисперсія за рядками")
d1 = ((Y1[0] - y1_av1) ** 2 + (Y2[0] - y2_av2) ** 2 + (Y3[0] - y3_av3) ** 2) / 3
d2 = ((Y1[1] - y1_av1) ** 2 + (Y2[1] - y2_av2) ** 2 + (Y3[1] - y3_av3) ** 2) / 3
d3 = ((Y1[2] - y1_av1) ** 2 + (Y2[2] - y2_av2) ** 2 + (Y3[2] - y3_av3) ** 2) / 3
d4 = ((Y1[3] - y1_av1) ** 2 + (Y2[3] - y2_av2) ** 2 + (Y3[3] - y3_av3) ** 2) / 3
print("d1=", round(d1, 2), "d2=", round(d2, 2), "d3=", round(d3, 2), "d4=", round(d4, 2), "\n")

d_couple = [d1, d2, d3, d4]

print("Критерій Кохрена")
Gp = max(d_couple) / sum(d_couple)
f1 = m - 1
f2 = N = 4
Gt = 0.7679
if Gp < Gt:
    print("Gp < Gt -> Дисперсія однорідна\n")
else:
    print("Дисперсія  неоднорідна\n")
print("Критерій Стьюдента")
sb = sum(d_couple) / N
ssbs = sb / N * m
sbs = ssbs ** 0.5

beta0 = (y1_av1 * 1 + y2_av2 * 1 + y3_av3 * 1 + y4_av4 * 1) / 4
beta1 = (y1_av1 * (-1) + y2_av2 * (-1) + y3_av3 * 1 + y4_av4 * 1) / 4
beta2 = (y1_av1 * (-1) + y2_av2 * 1 + y3_av3 * (-1) + y4_av4 * 1) / 4
beta3 = (y1_av1 * (-1) + y2_av2 * 1 + y3_av3 * 1 + y4_av4 * (-1)) / 4

t0 = abs(beta0) / sbs
t1 = abs(beta1) / sbs
t2 = abs(beta2) / sbs
t3 = abs(beta3) / sbs

f3 = f1 * f2
ttabl = 2.306
print("f3 = f1*f2, з таблиці tтабл = 2.306")
if (t0 < ttabl):
    print("t0<ttabl, b0 не значимий")
    b0 = 0
if (t1 < ttabl):
    print("t1<ttabl, b1 не значимий")
    b1 = 0
if (t2 < ttabl):
    print("t2<ttabl, b2 не значимий")
    b2 = 0
if (t3 < ttabl):
    print("t3<ttabl, b3 не значимий\n")
    b3 = 0

yy1 = b0 + b1 * x1_min + b2 * x2_min + b3 * x3_min
yy2 = b0 + b1 * x1_min + b2 * x2_max + b3 * x3_max
yy3 = b0 + b1 * x1_max + b2 * x2_min + b3 * x3_max
yy4 = b0 + b1 * x1_max + b2 * x2_max + b3 * x3_min
print("Критерій Фішера")
d = 2
print(d, "значимих коефіцієнта")
f4 = N - d
sad = ((yy1 - y1_av1) ** 2 + (yy2 - y2_av2) ** 2 + (yy3 - y3_av3) ** 2 + (yy4 - y4_av4) ** 2) * (m / (N - d))
Fp = sad / sb
print("d1=", round(d1, 2), "d2=", round(d2, 2), "d3=", round(d3, 2), "d4=", round(d4, 2), "d5=", round(sb, 2))
print("Fp=", round(Fp, 2))
print('Ft беремо з таблиці 8 рядок 2 стовпець Ft = 4.5')
Ft = 4.5
if Fp > Ft:
    print("Fp=", round(Fp, 2), ">Ft", Ft, "Рівняння неадекватне оригіналу")
else:
    print("Fp=", round(Fp, 2), "<Ft", Ft, "Рівняння адекватне оригіналу")
