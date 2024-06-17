

def produce_pumpkin_cols(x_dim, y_dim):
    # We assume we are given enough rows
    # We will calculate the max pumpkins we can fit y_dim though
    max_pumpkins = floor_div(y_max(), y_dim)
    
    offset = 0
    for j in range(0, max_pumpkins):
        for i in range(0, x_dim):
            traverse_column(make_pumpkin, y_dim, 1, offset)
            move(East)
        offset = offset + y_dim
        
        for i in range(0, x_dim):
            # Reset
            move(West)
    
    for i in range(0, x_dim):
        # Allow us to leave pumpkin land
        move(East)
        
        
        
def make_pumpkin():
    if (get_entity_type() != Entities.Pumpkin):
        # Initilizer
        trade(Items.Pumpkin_Seed)
        plant(Entities.Pumpkin)
        return True
        
    if can_harvest():
        # Cycle the item
        harvest()
        trade(Items.Pumpkin_Seed)
        plant(Entities.Pumpkin)
        return True
        
    # Nothing to Do
    return False
    
    