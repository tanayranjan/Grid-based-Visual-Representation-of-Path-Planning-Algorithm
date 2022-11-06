import numpy as np
import time
import random
def Dijkstra_init (object1):
    for i in range(30):
        for j in range(40):
            if ((object1.state_value(j, i, 1) == 0) & ((object1.state_value(j, i, 4) == 0) | (object1.state_value(j, i, 4) == 2))):
                object1.change_value(j,i,2,2000)
    return object1
#            object1.change_value(j,i,3,0)

def Dijkstra (object1):
    fu = object1.get_node_with_smallest_value(2)
    random.shuffle(fu)
    for u in fu:
        u = int(u)
        object1.change_state_to1 ('DISCOVERED', u)
        list1 = object1.get_neighbors(u)
        for i in list1:
            alt = object1.get_value(u, 2) + 1
            if alt < object1.get_value(int(i), 2):
                object1.change_value1(i, 2, alt)
                object1.change_value1(i, 3, u)
        if (object1.check_for_end(u)):
            return object1, 3
        time.sleep(0.0005)
    return object1, 2

def path_finder (object1):
    end1 = object1.end_finder()
    
    start1 = object1.start_finder()
    u = end1
    while (u != start1):
        object1.change_state_to1('PATH', int(u))
        tel = object1.get_value(int(u), 3)
        u = tel
    return object1
    



    
