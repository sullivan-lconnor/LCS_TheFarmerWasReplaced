
def metaPlant(toPlantFunc, info):
    # Set the grid_info
    # Call the plant function for type
    cur_pos_set_grid_info(info)
    toPlantFunc()
    
    
def plantByType(type):
    cur_pos_set_grid_info(type)
    if ((type == 0) and (can_harvest())):
        harvest()
    if type == 1:
        do_hay()
    if type == 2:
        do_carrot()
    if type == 3:
        do_tree()
    if type == 4:
        do_pumpkin()
    if type == 5:
        do_bush()