

    
    
    
  # Take in some pattern Type
    
  # Find a valid minimum emptry space in grid to build pattern
    
  # Produce Pattern
def get_pattern_dim(pattern):
    # assign x_dim
    x_dim = len(pattern)
    
    # assigning y_dim handling 1x1 case
    if x_dim == 1:
        y_dim = 1
    else:
        y_dim = len(pattern[0])
        
    return list( (x_dim, y_dim) )
    
def find_valid_space_for_pattern(pattern):
    ## Returns position of bottom right corner where pattern fits    
    pattern_dim = get_pattern_dim(pattern)
    p_x_dim = pattern_dim[0]
    p_y_dim = pattern_dim[1]
    for y in range(0,get_world_size()):
        for x in range(0,get_world_size()):
            if check_region_has_type(pattern, list((x,y)), 0, p_x_dim, p_y_dim):
                return list((x,y))
    return list(())
    
def plant_pattern(pattern):
    ## Attempts to find a place to plant the pattern, if can True else False
    plant_at = find_valid_space_for_pattern(pattern)
    if len(plant_at) == 0:
        traverse_2d_harvest(pattern)
    move_to(plant_at)
    traverse_2d_plant(pattern)   
    
def do_patterns():
    while(1):
        plant_pattern(get_carrot_tree())
        plant_pattern(get_hey())  
        plant_pattern(get_pumpkin())
            
    
#################################################################
# Hay                                       #
#################################################################   
  