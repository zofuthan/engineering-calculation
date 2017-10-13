#!/usr/bin/python3 
class YxNewton(object):
    '''
    this class use Newton interpolation method
    first ac = YxNewton(x_y_dict)
    x_y_dict like {0.40: 0.41075, 0.55: 0.57815}
    then you can use y = ac.yxnewton(x) to predict new (x,y) point
    '''
    my_dict = {}
    N = 0
    my_dict_keys = []
    my_dict_values = []
    b_list = []
    cha_fen_list = []
    def __init__(self,x_y_dict):
        if x_y_dict == None or len(x_y_dict)==0:
            self.my_dict = {0.40: 0.41075, 0.55: 0.57815, 0.65: 0.69675, 0.80: 0.88811, 0.90: 1.02652, 1.05: 1.25382}
        else:
            self.my_dict = x_y_dict
        self.N = len(self.my_dict)
        self.my_dict_keys = list(self.my_dict.keys())
        self.my_dict_values = list(self.my_dict.values())
        for j in range(self.N):
            s_list = []
            for i in range(self.N + 1):
                s_list.append(0)
            self.b_list.append(s_list)

        for j in range(self.N):
            self.b_list[j][0] = self.my_dict_keys[j]

        for j in range(self.N):
            self.b_list[j][1] = self.my_dict_values[j]

        for j in range(2, self.N + 1):
            for i in range(1, self.N):
                if i > j - 2:
                    dy = self.b_list[i][j - 1] - self.b_list[i - 1][j - 1]
                    dx = self.b_list[i][0] - self.b_list[i - j + 1][0]
                    self.b_list[i][j] = round(dy / dx, 5)

        for i in range(0, self.N):
            for j in range(1, self.N + 1):
                if i == j - 1:
                    self.cha_fen_list.append(self.b_list[i][j])

    def show_big_list(self):
        '''
        show Newton divided difference table
        '''
        b_list = self.b_list
        for i in range(self.N):
            t = tuple(self.b_list[i])
            print("%.5f, %.5f, %.5f, %.5f, %.5f, %.5f, %.5f" % t)

    def newton_error(self,x=0):
        '''
        accoding your x
        retuen Newton interpolation error
        '''
        my_dict_keys = self.my_dict_keys
        cha_fen_list = self.cha_fen_list
        for i in my_dict_keys:
            if x != i:
                x = x * (x - i)
        x = x * cha_fen_list[-1]
        if x < 0:
            x = -x
        return x

    def yxnewton(self,x=0):
        cha_fen_list = self.cha_fen_list
        my_dict_keys = self.my_dict_keys
        my_dict_keys.remove(my_dict_keys[-1])
        newton = cha_fen_list[0]
        kuohao = x - my_dict_keys[0]
        for index, xi in enumerate(my_dict_keys[1:]):
            newton = newton + cha_fen_list[index + 1] * kuohao
            kuohao = kuohao * (x - xi)
        return newton

my_dict = {0.40:0.41075, 0.55:0.57815, 0.65:0.69675, 0.80:0.88811, 0.90:1.02652, 1.05:1.25382}
ac = YxNewton(my_dict)

print(ac.yxnewton(1.05))