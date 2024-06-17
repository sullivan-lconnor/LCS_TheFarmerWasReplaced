#Initialize this in the main event loop and it will grow and harvest whole pumpkins of 
#configurable size from the robots current position

def special_plant_pumpkin():
    # Returns true if we get to plant a pumpkin
    cur_pos_set_grid_info(4)
    if can_harvest():
        return False
    
    if get_entity_type() == Entities.Pumpkin:
        return True
    
    trade(Items.Pumpkin_Seed)
    plant(Entities.Pumpkin)
    return True

def recursive_pumpkin(visted_pumpkins):
    if len(visted_pumpkins) == 0:
        return
    
    locations_planted = list()
    for p in visted_pumpkins:
        move_to(p)
        if special_plant_pumpkin():
            locations_planted.append(p)
    recursive_pumpkin(locations_planted)

def plant_a_pumpkin_and_return_where(x_dim,y_dim):
    #plants a pumpkin in every square defined by the region
    # RETURNS: list of points we planted a pumpkin at
    locations_planted = list()
    starting_x = x_pos()
    starting_y = y_pos()
    for i in range(x_dim):
        for j in range(y_dim):
            target_pos = list ( (starting_x+i, starting_y+j) )
            move_to(target_pos)
            if special_plant_pumpkin():
                locations_planted.append(target_pos)
    return locations_planted

# def validate_pumpkin(visted_pumpinks, x_dim, y_dim):
#     if len(visted_pumpinks) == 0:
#         return
#     # check every square in defined region
#     # adds any squares that are not harvestable to a list and replant
#     # call validate_pumpkin again with list
#     starting_position = get_position()
#     validate_pumpkin(plant_a_pumpkin_and_return_where(x_dim,y_dim),x_dim,y_dim)

def spin_pumpkin_loop(x_dim, y_dim):
    # Check that we can in fact grow a pumpkin of the size from this square (check up and right)
    
    
    #EVENTUALLY NEED TO ADD CHECK IF WE CAN ACTUALLY FIT A PUMPKIN OF GIVEN SIZE ON WORLD
    #if not validate_pumpkin_spacing(x_dim, y_dim):
    #    return False
    while(1):
        move_to(list ( (0, 0) ))
        visted_pumpkins = plant_a_pumpkin_and_return_where(x_dim,y_dim)
        recursive_pumpkin(visted_pumpkins)
        harvest()

spin_pumpkin_loop(get_world_size(), get_world_size())