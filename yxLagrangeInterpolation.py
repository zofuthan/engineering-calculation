def yxLagrangeInterpolation(x_y_dict=None,x=None):
    '''
    :param x_y_dict: like {0.40: 0.41075, 0.55: 0.57815,}
    :param x:  you set a x  
    :return: estimate y accoding to LagrangeInterpolation
    '''
    if x_y_dict==None or len(x_y_dict)==0:
        x_y = {0.40: 0.41075, 0.55: 0.57815, 0.65: 0.69675, 0.80: 0.88811, 0.90: 1.02652, 1.05: 1.25382}
    else:
        x_y = x_y_dict
    x_list = list(x_y.keys())
    y_list = list(x_y.values())
    N = len(x_y)
    if x==None:
        x = x_y[0]
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
    lagrange = 0
    for n in range(N):
        lagrange = lagrange + y_list[n] * Li_list[n]
    return lagrange

