import numpy as np
import time
from math import *

def Astar_init(object1):
    for i in range(1200):
        object1.change_value1(i, 2, 200000)
    u = object1.start_finder()
    u = int(u)
    object1.change_state_to1('OPEN', u) # Putting Start Node in Open List
    object1.change_value1(u, 2, 0)
    object1.change_value1(u, 3, 0)
    
    return hcost_calculator(object1)
    
def hcost_calculator (object1):
    e = object1.end_finder()
    e = int(e)
    x, y = object1.get_coordinates(e)
    for n in range(1200):
        j, i = object1.get_coordinates(n)
        temp1 = int(sqrt(((x-j)*(x-j)) + ((y-i)*(y-i))))
        object1.change_value1(n, 5, temp1)
    return update_fcost(object1)
def update_fcost(object1):
    for n in range(1200):
        object1.change_value1(n, 3, (object1.get_value(n, 5) + object1.get_value(n, 2)))
    return object1    

def Astar (object1):
    fu = object1.get_node_with_smallest_value(3, 2)
    for u in fu:
        u = int(u)
        if (object1.check_for_end(u)):
            return object1, 3
        else:
            list1 = object1.get_neighbors(u, 1)
            for something in list1:
                something = int(something)
                if object1.get_value(something, 1) == 3:
                    continue
                elif ((object1.get_value(something, 1) != 2) | (object1.get_value(something, 2)>(object1.get_value(u, 2) + object1.dist_bet(something, u)))):
                    g_cost = object1.get_value(u, 2) + object1.dist_bet(something, u)
                    object1.change_value1(something, 2, g_cost)
                    object1.change_value1(something, 6, u)
                    object1.change_value1(something, 1, 2)
        object1.change_state_to1('DISCOVERED', u)
    time.sleep(0.001)
    return update_fcost(object1), 2


def path_finder (object1):
    end1 = object1.end_finder()
    
    start1 = object1.start_finder()
    u = end1
    while (u != start1):
        object1.change_state_to1('PATH', int(u))
        tel = object1.get_value(int(u), 3)
        u = tel
    return object1
