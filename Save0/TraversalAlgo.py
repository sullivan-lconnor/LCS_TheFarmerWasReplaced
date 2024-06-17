#####################################
# PRODUCE COLUMNS OF MATERIAL       #
#####################################
def produce_hey_col():
    traverse_column(make_hey,max_hey())
    move(East)
    
def produce_wood_col():
    traverse_column(make_wood,max_wood())
    move(East)
    
def produce_carrot_col():
    traverse_column(make_carrot,max_carrot())
    move(East)
    
    
    
    
##########################################
# Handle a single square of a given type #
##########################################
def make_hey():    
    if (get_entity_type() != Entities.Grass):
        # Initializer
        plant(Entities.Grass)
        return True
    
    if can_harvest():
        # Cycle the item
        harvest()
        plant(Entities.Grass)
        return True
    # Nothing to Do
    return False
    
def make_wood():
    if (get_entity_type() != Entities.Bush):
        # Initializer
        plant(Entities.Bush)
        return True
        
    if can_harvest():
        # Cycle the item
        harvest()
        plant(Entities.Bush)
        return True
    # Nothing to Do
    return False
    
def make_carrot():
    if (get_entity_type() != Entities.Carrots):
        # Initializer
        trade(Items.Carrot_Seed)
        plant(Entities.Carrots)
        return True
        
    if can_harvest():
        # Cycle the item
        harvest()
        trade(Items.Carrot_Seed)
        plant(Entities.Carrots)
        return True
    # Nothing to Do
    return False
#####################################

    