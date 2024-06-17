#################################################################
# CONFIGURATION VARIABLES                                       #
#################################################################

grid_info = list()
position = list((0,0))

hey = list(( ( 1, 1 ), ( 1, 1 ) ))

carrot_tree = list(( ( 2, 3 ), ( 3, 2 ) ))

pumpkin = list(( ( 4, 4, 4 ), ( 4, 4, 4 ), (4, 4, 4) ))



# GRID CONFIGURATION CONVENTIONS
# 0 : empty
# 1 : hay
# 2 : carrot
# 3 : tree
# 4 : pumpkin
    
#################################################################
# CONFIGURATION VARIABLE Getters                                #
#################################################################
def get_position():
    return position

def get_hey():
    return hey

def get_carrot_tree():
    return carrot_tree  

def get_pumpkin():
    return pumpkin

def set_grid_info(x, y, info):
    grid_info[x%get_world_size()][y%get_world_size()] = info

def get_grid_info(x,y):
    return grid_info[x][y]
    
def initialize_grid_info():
    for i in range(0,get_world_size()):
        row_list = list()
        for j in range(0,get_world_size()):
            row_list.append(0)
        grid_info.append(row_list)
     
#################################################################
# Minimal Control Functions                                     #
#################################################################   
    
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

#################################################################
# THE SACRID CALL TO MAIN                                       #
################################################################# 

def main():
    initialize_grid_info()
    initialize_0()
    while(1):
        smart_companion_mode()
        smart_pumpkin_loop()
    # do_patterns()
    # spin_companion_mode()
    # spin_pumpkin_loop(get_world_size()-1, get_world_size()-1)
    
main()