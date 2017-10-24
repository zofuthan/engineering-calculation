'''
If you want to get more information, you can read
http://www.cnblogs.com/xpvincent/archive/2013/01/26/2878092.html
'''
my_dict = {0.40: 0.41075, 0.55: 0.57815, 0.65: 0.69675, 0.80: 0.88811, 0.90: 1.02652, 1.05: 1.25382}
N = 6
x = 0.596

def show_matrix(matrix, N):
    for n in range(N):
        print(matrix[n])

def yx_three_sline_interpolation(x_y_dict, N, x):
    """
    :param x_y_dict: x and y vaules ,like this:{0.40: 0.41075, 0.55: 0.57815,}
    :param N: the number of x,
    :param x: x is in f(x) that you want to predict
    :return:f(x)
    """
    x_list = list(x_y_dict.keys())
    y_list = list(x_y_dict.values())
    N = N
    x = x

    #Initializing h, the number of h is N-1
    h_list = [0 for x in range(N - 1)]
    for i in range(0, N - 1):
        h_list[i] = x_list[i + 1] - x_list[i]

    #initializing e, the number of e is N-2, so I set e[0] and e[N-1] to be 0
    # This is based on natural interpolation conditions
    # You can use other values as needed
    e_list = [0 for x in range(N)]
    e_list[0] = 0
    e_list[N - 1] = 0
    for i in range(1, N - 1):
        e_list[i] = 6 * ((y_list[i + 1] - y_list[i]) / h_list[i] - (y_list[i] - y_list[i - 1]) / h_list[i - 1])

    # initializing N*N matrix
    # This is based on natural interpolation conditions
    # You can use other values as needed
    data_matrix = [[0] * (N) for x in range(N)]
    data_matrix[0][0] = 1
    data_matrix[N - 1][N - 1] = 1
    for i in range(1, N - 1):
        data_matrix[i][i] = 2 * (h_list[i - 1] + h_list[i])
        data_matrix[i][i - 1] = h_list[i - 1]
        data_matrix[i][i + 1] = h_list[i]

    #use Thomas Algorithm to handle tridiagonal matrices
    for i in range(N):
        if i == 0:
            data_matrix[i][i + 1] = data_matrix[i][i + 1] / data_matrix[i][i]
            e_list[i] = e_list[i] / data_matrix[i][i]
        elif i != (N - 1):
            data_matrix[i][i + 1] = data_matrix[i][i + 1] / (
            data_matrix[i][i] - data_matrix[i - 1][i - 1] * data_matrix[i - 1][i])
            e_list[i] = (e_list[i] - e_list[i - 1] * data_matrix[i - 1][i]) / (
            data_matrix[i][i] - data_matrix[i - 1][i - 1] * data_matrix[i - 1][i])
            data_matrix[i][i - 1] = 1
        else:
            e_list[i] = (e_list[i] - e_list[i - 1] * data_matrix[i - 1][i]) / (
            data_matrix[i][i] - data_matrix[i - 1][i - 1] * data_matrix[i - 1][i])
            data_matrix[i][i - 1] = 1

    #The solution of the three diagonal matrix is m_list
    m_list = [0 for x in range(N)]
    m_list[N - 1] = e_list[N - 1]
    for i in range(N - 2, -1, -1):
        m_list[i] = e_list[i] - data_matrix[i][i + 1] * m_list[i + 1]

    #Calculation of coefficients of three spline interpolation functions:a, b, c, d
    #the number of a is N-1, the same as b, c, d
    #we can get N-1 functions
    a_list = [0 for x in range(N - 1)]
    b_list = [0 for x in range(N - 1)]
    c_list = [0 for x in range(N - 1)]
    d_list = [0 for x in range(N - 1)]
    for i in range(N - 1):
        a_list[i] = y_list[i]
        b_list[i] = ((y_list[i + 1] - y_list[i]) / h_list[i]) - \
                    (h_list[i] * m_list[i] / 2) - ((m_list[i + 1] - m_list[i]) * h_list[i] / 6)
        c_list[i] = m_list[i] / 2
        d_list[i] = (m_list[i + 1] - m_list[i]) / (6 * h_list[i])

    out_a_b_c_d_list = list(zip(a_list, b_list, c_list, d_list))

    #calculate f(x) when x>x[0] and x<x[N-1]
    if x >= x_list[0] and x <= x_list[N - 1]:
        for n in range(N - 1):
            if x >= x_list[n] and x <= x_list[n + 1]:
                a_b_c_d = out_a_b_c_d_list[n]
                a, b, c, d = a_b_c_d[0], a_b_c_d[1], a_b_c_d[2], a_b_c_d[3]
                f_x = a + b * (x - x_list[n]) + c * ((x - x_list[n]) ** 2) + (d * (x - x_list[n]) ** 3)
                return f_x
    else:
        return None



'''
from three_spline_interpolation import yx_three_sline_interpolation

import matplotlib.pyplot as plt
import math
import random
x_list = []
x_2_list = []
y_a_list = []
y_b_list = []
y_three_sline_interpolation = []
for i in range(30):
    x_list.append(i)
    y_a_list.append(math.sin(i))

for j in range(0, 1000):
    x_2_list.append(random.uniform(0,30))
    x_2_list.sort()

y_c_list = [math.sin(x) for x in x_2_list]
x_y_dict = dict(list(zip(x_list, y_a_list)))

for x in x_list:
    f_x = yx_three_sline_interpolation(x_y_dict,30,x)
    y_three_sline_interpolation.append(f_x)

plt.plot(x_2_list, y_c_list,color='r')
plt.plot(x_list, y_three_sline_interpolation, color='b')
plt.show()

'''