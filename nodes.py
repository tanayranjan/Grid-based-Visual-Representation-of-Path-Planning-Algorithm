from math import sqrt
import numpy as np
import pygame
class Nodes:
    def __init__(self, nodecolumn, noderow, screen_display):
        self.nodex = nodecolumn
        self.nodey = noderow
        self.s_display = screen_display
        self.array = np.zeros((40,30,7)) # 40 in the direction of X-axis, 30 in Y, dont do row and column logic
        for i in range(30):
            for j in range(40):
                self.array[j][i][0] = (i*40)+j
        for j in range (40):
            self.array[j][0][1] = 1
            self.array[j][29][1] = 1
        for i in range (30):
            self.array[0][i][1] = 1
            self.array[39][i][1] = 1
    
    def printdraw(self):
        for i in range(30):
            for j in range(40):
                if (self.array[j][i][1] == 0):
                    pygame.draw.rect(self.s_display, (255,255,255), ((20*j)+1,(20*i)+1,18,18))
                elif (self.array[j][i][1] == 1):
                    pygame.draw.rect(self.s_display, (0,0,0), ((20*j)+1,(20*i)+1,18,18))
                elif (self.array[j][i][1] == 3):
                    pygame.draw.rect(self.s_display, (0,255,0), ((20*j)+1,(20*i)+1,18,18))
                elif (self.array[j][i][1] == 2):
                    pygame.draw.rect(self.s_display, (255,0,255), ((20*j)+1,(20*i)+1,18,18))
                elif (self.array[j][i][1] == 4):
                    pygame.draw.rect(self.s_display, (0,255,255), ((20*j)+1,(20*i)+1,18,18))
                if (self.array[j][i][4] == 1):
                    pygame.draw.rect(self.s_display, (255,255,0), ((20*j)+1,(20*i)+1,18,18))
                elif (self.array[j][i][4] == 2):
                    pygame.draw.rect(self.s_display, (255,0,0), ((20*j)+1,(20*i)+1,18,18))

    def change_state_to (self, a, x, y):
        if (a == 'OBSTACLE'):
            self.array[x][y][1] = 1
        if (a == 'START'):
            self.array[x][y][4] = 1
        if (a == 'END'):
            self.array[x][y][4] = 2
        if (a == 'PATH'):
            self.array[x][y][1] = 2
        if (a == 'DISCOVERED'):
            self.array[x][y][1] = 3
        if (a == 'OPEN'):
            self.array[x][y][1] = 2

    def change_state_to1 (self, a, b):
        b = int(b)
        y = int(b/40)
        x = b%40
        if (a == 'OBSTACLE'):
            self.array[x][y][1] = 1
        if (a == 'START'):
            self.array[x][y][4] = 1
        if (a == 'END'):
            self.array[x][y][4] = 2
        if (a == 'DISCOVERED'):
            self.array[x][y][1] = 3
        if (a == 'PATH'):
            self.array[x][y][1] = 4
        if (a == 'OPEN'):
            self.array[x][y][1] = 2


    def obstacle_maker (self, x, y):
        for i in range(30):
            for j in range(40):
                if ((((20*j)+1)<=x)&(((20*j)+19)>=x))&((((20*i)+1)<=y)&(((20*i)+19)>=y)):
                    self.change_state_to ('OBSTACLE', j, i)

    def change_value (self, x, y, a, b):
        self.array[x][y][a] = b
    def change_value1 (self, a, b, c):
        a = int(a)
        i = int(a/40)
        j = a%40
        b = int(b)
        self.array[j][i][b] = c
    def state_value (self, x, y, b):
        return self.array[x][y][b]
    
    def get_neighbors (self, a, b=0, condi=0):
        i = int(a/40)
        j = a%40
        list1 = []
        if ((self.array[j][i+1][1] == condi) & (((i<29) & (j<39))& ((i>0) & (j>0)))):
            list1.append(self.array[j][i+1][0])
        if ((self.array[j][i-1][1] == condi) & (((i<29) & (j<39))& ((i>0) & (j>0)))):
            list1.append(self.array[j][i-1][0])
        if ((self.array[j-1][i][1] == condi) & (((i<29) & (j<39))& ((i>0) & (j>0)))):
            list1.append(self.array[j-1][i][0])
        if ((self.array[j+1][i][1] == condi) & (((i<29) & (j<39))& ((i>0) & (j>0)))):
            list1.append(self.array[j+1][i][0])
        if (b == 1):
            if ((self.array[j+1][i+1][1] == condi) & (((i<29) & (j<39))& ((i>0) & (j>0)))):
                list1.append(self.array[j+1][i+1][0])
            if ((self.array[j-1][i-1][1] == condi) & (((i<29) & (j<39))& ((i>0) & (j>0)))):
                list1.append(self.array[j-1][i-1][0])
            if ((self.array[j+1][i-1][1] == condi) & (((i<29) & (j<39))& ((i>0) & (j>0)))):
                list1.append(self.array[j+1][i-1][0])
            if ((self.array[j-1][i+1][1] == condi) & (((i<29) & (j<39))& ((i>0) & (j>0)))):
                list1.append(self.array[j-1][i+1][0])

        
        return list1

    def get_node_with_smallest_value (self, a, sus = 0):
        b = []
        c = 2001
        for i in range(30):
            for j in range(40):
                if ((c == self.array[j][i][a]) & (self.array[j][i][1] == sus)):
                    b.append(self.array[j][i][0])
                if ((c>self.array[j][i][a]) & (self.array[j][i][1] == sus)):
                    c = self.array[j][i][a]
                    b = []
                    b.append(self.array[j][i][0])
        return b
    def get_value (self, a, b):
        i = int(a/40)
        j = a%40
        return self.array[j][i][b]

    def set_start (self, x, y):
        sucess = 0
        for i in range(30):
            for j in range(40):
                if ((((20*j)+1)<=x)&(((20*j)+19)>=x))&((((20*i)+1)<=y)&(((20*i)+19)>=y)):
                    self.change_state_to ('START', j, i)
                    sucess = 1
                    g = (i*40)+j
                    print("start = ")
                    print(g)
        return sucess
        
    def set_end (self, x, y):
        sucess = 0
        for i in range(30):
            for j in range(40):
                if ((((20*j)+1)<=x)&(((20*j)+19)>=x))&((((20*i)+1)<=y)&(((20*i)+19)>=y)):
                    self.change_state_to ('END', j, i)
                    sucess = 1
                    g = (i*40)+j
                    print('end = ')
                    print(g)
        return sucess
    def check_for_end (self, a):
        y = int(a/40)
        x = a%40
        if (self.array[x][y][4] == 2):
            return True
        return False
    def end_finder (self):
        for i in range(30):
            for j in range(40):
                if (self.array[j][i][4] == 2):
                    return self.array[j][i][0]
    def start_finder (self):
        for i in range(30):
            for j in range(40):
                if (self.array[j][i][4] == 1):
                    return self.array[j][i][0]
    def get_coordinates (self, a):
        a = int(a)
        y = int(a/40)
        x = a%40
        return x, y

    def dist_bet (self, a, b):
        a = int(a)
        y = int(a/40)
        x = a%40
        b = int(b)
        i = int(a/40)
        j = a%40
        return sqrt((x-i)*(x-i))+((y-j)*(y-j))



        

        
        
