x_list = [2, 2.5, 4]
y_list = [0.5, 0.4, 0.25]
dy_list = [-0.25, -0.16, -0.0625]
x = 3

def yxHermite(x=x, x_list=x_list,y_list=y_list,dy_list=dy_list):
    """
    This function is designed acconding the Hermite Interpolation
    :param x: The value to be estimated ,f(x)
    :param x_list: The x value of the known point
    :param y_list: The y value of the known point
    :param dy_list:The f'(x) value of the known point
    :return: Hermite(x)
    """
    N = len(x_list)
    Hermite = 0
    for n in range(N):
        s = 1
        b_ = 1
        for index, xi in enumerate(x_list):
            if n != index:
                s = s * (x - xi)
                b_ = b_ * (x_list[n] - xi)
        Li = s / b_
        Li2 = Li * Li
        sum = 0
        for index, xi in enumerate(x_list):
            if n != index:
                a = x_list[n] - xi
                sum = sum + 1 / a
        a = (1 - 2 * (x - x_list[n]) * sum) * (Li2)
        b = (x - x_list[n]) * (Li2)
        Hermite = Hermite + a * y_list[n] + b * dy_list[n]
    return Hermite


print(yxHermite())