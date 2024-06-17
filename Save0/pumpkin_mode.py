#Initialize this in the main event loop and it will grow and harvest whole pumpkins of 
#configurable size from the robots current position



def pumpkin_loop(x_dim, y_dim):
    pass

def validate_pumpkin(x_dim, y_dim):
    #returns true if a pumpkin can be grown up and to the right from current position, false otherwise
    
    pass

def special_plant_pumpkin():
    # Returns true if we get to plant a pumpkin
    cur_pos_set_grid_info(4)
    if can_harvest():
        return False
    else:
        trade(Items.Pumpkin_Seed)
        plant(Entities.Pumpkin)
        return True

def plant_a_pumpkin_and_return_where(x_dim,y_dim):
    #plants a pumpkin in every square defined by the region
    # RETURNS: list of points we planted a pumpkin at
    starting_x = x_pos()
    starting_y = y_pos()
    locations_planted = list()
    for i in range(x_dim):
        for j in range(y_dim):
            if special_plant_pumpkin():
                locations_planted.append(get_position())
            xis(starting_x+i)
            yis(starting_y+j)

    xis(starting_x)
    yis(starting_y)
    return locations_planted

def validate_pumpkin(visted_pumpinks, x_dim, y_dim):
    if len(visted_pumpinks == 0):
        return
    # check every square in defined region
    # adds any squares that are not harvestable to a list and replant
    # call validate_pumpkin again with list
    starting_position = get_position()
    validate_pumpkin(plant_a_pumpkin_and_return_where(x_dim,y_dim))

def spin_pumpkin_loop(x_dim, y_dim):
    # Check that we can in fact grow a pumpkin of the size from this square (check up and right)
    if not validate_pumpkin(x_dim, y_dim):
        return False
    while(1):
        visted_pumpkins = plant_a_pumpkin_and_return_where(x_dim,y_dim)
        validate_pumpkin(visted_pumpinks, x_dim, y_dim)
        harvest()
        