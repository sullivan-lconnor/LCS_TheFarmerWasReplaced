def x_pos():
    return position[0]
def y_pos():
    return position[1]

def xis(x):
    position[0] = x%get_world_size()
    go_to_x()
    
def yis(y):
    position[1] = y%get_world_size()
    go_to_y()

    
# TO OPTIMIZE    
def go_to_x():
    while (get_pos_x() < x_pos()):
        inc_x_()
    while (get_pos_x() > x_pos()):
        dec_x_()
def go_to_y():
    while (get_pos_y() < y_pos()):
        inc_y_()  
    while (get_pos_y() > y_pos()):
        dec_y_()    
        
#def go_to_x():
#    while (get_pos_x() != x_pos()):
#        inc_x_()
#def go_to_y():
#    while (get_pos_y() != y_pos()):
#        inc_y_() 
# END OPTIMIZE

def move_to(x,y):
    xis(x)
    yis(y)
    
def move_to(coord):
    # coord (tuple) : (x,y)
    if len(coord) !=2:
        return
    xis(coord[0])
    yis(coord[1])