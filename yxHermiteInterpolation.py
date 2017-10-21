
x_list = [2, 2.5, 4]
y_list = [0.5, 0.4, 0.25]
dy_list = [-0.25, -0.16, -0.0625]
x = 3
"""
This function is designed acconding the Hermite Interpolation
    :param x: The value to be estimated ,f(x)
    :param x_list: The x value of the known point
    :param y_list: The y value of the known point
    :param dy_list:The f'(x) value of the known point
    :return: Hermite(x),A_list is a list of alfa coefficients, 
            B_list is a List of beta coefficients. 
"""

N = len(x_list)
Li_list = []
for n in range(N):
    s = 1
    b = 1
    for index, xi in enumerate(x_list):
        if n != index:
            s = s * (x - xi)
            b = b * (x_list[n] - xi)
    Li = s / b
    Li_list.append(Li)

Li_2_list = [ x*x for x in Li_list]

A_list = []
B_list = []

for n in range(N):
    sum = 0
    for index, xi in enumerate(x_list):
        if n != index:
            a = x_list[n] - xi
            sum  = sum + 1 / a
    a = (1- 2 * (x - x_list[n]) * sum) * (Li_2_list[n])
    A_list.append(a)

for n in range(N):
    b = (x - x_list[n]) * (Li_2_list[n])
    B_list.append(b)

Hermite = 0
for n in range(N):
    Hermite = Hermite + A_list[n] * y_list[n] + B_list[n] * dy_list[n]

print(Hermite,A_list,B_list)
