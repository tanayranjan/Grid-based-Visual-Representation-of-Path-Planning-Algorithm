import pygame
from pygame.constants import K_RETURN
import nodes
import dijkstra
import astar

pygame.init()
screen = pygame.display.set_mode((800,600))
disp1 = nodes.Nodes(40,30,screen)

current_mode = 0
running = True
processing = 0

start_flag = 0
end_flag = 0
phase_mode = 0


def main():
    global current_mode
    global running
    global processing
    global phase_mode

    while (running):
        disp1.printdraw()
        pygame.display.update()
        current_mode, processing, running, phase_mode = event_scanner(current_mode, processing, running, phase_mode)
        if phase_mode == 0: 
            current_mode, processing = phase1(current_mode, processing) 
        if phase_mode == 1:
            phase_mode = phase2()
            phase_mode = 2
        if phase_mode == 2:
            phase3()
        if phase_mode == 3:
            phase4()
         

def event_scanner (current_mode, processing, running, phase_mode):
    global screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_RETURN:
                if phase_mode == 0:
                    phase_mode = 1
                else:
                    running = False
        if phase_mode == 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    current_mode = 1
                if event.key == pygame.K_s:
                    current_mode = 2
                if event.key == pygame.K_e:
                    current_mode = 3
            if event.type == pygame.KEYUP:
                current_mode = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                processing = 1
            if event.type == pygame.MOUSEBUTTONUP:
                processing = 0     
    return current_mode, processing, running, phase_mode

            
            
def processor(c_m, x, y):
    global start_flag, end_flag
    global start_node_existance
    if (c_m == 1):
        disp1.obstacle_maker(x, y)
    if (c_m == 2 and start_flag == 0):
        start_flag = disp1.set_start(x, y)
    if (c_m == 3 and end_flag == 0):
        end_flag = disp1.set_end(x, y)

def phase1 (current_mode, processing):
    
    if processing == 1:
        
        x, y = pygame.mouse.get_pos()
        processor(current_mode, x, y)   
    return current_mode, processing 

def phase2 ():
    global disp1
    disp1 = dijkstra.Dijkstra_init(disp1)
    # disp1 = astar.Astar_init(disp1)
    return 2
def phase3 ():
    global phase_mode
    global disp1
    disp1 , phase_mode = dijkstra.Dijkstra(disp1)
    # disp1 , phase_mode = astar.Astar(disp1)

def phase4 ():
    global disp1
    # disp1 = astar.path_finder(disp1)
    disp1 = dijkstra.path_finder(disp1)
    global phase_mode
    phase_mode = 4
    
    
    
        

if __name__ == '__main__' :   
    try:
        main()
    except KeyboardInterrupt:
        pass