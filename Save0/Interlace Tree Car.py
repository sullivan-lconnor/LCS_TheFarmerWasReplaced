def produce_tree_car_interlace_col():
    traverse_column(make_tree_then_carrot, y_max(), 1, 0)
    move(East)
    traverse_column(make_tree_then_carrot, y_max(), 1, 1)
    move(East)
    
def make_tree_then_carrot():
    if (get_entity_type() != Entities.Tree and get_entity_type() != Entities.Carrots):
        # Initializer
        make_tree_then_carrot_opperation()
        return True
    
    if can_harvest():
        # Cycle the item
        if (get_entity_type() == Entities.Tree):
            harvest()    
            plant(Entities.Tree)
        if (get_entity_type() == Entities.Carrots):
            harvest()        
            trade(Items.Carrot_Seed)
            plant(Entities.Carrots)
        return True
    # Nothing to Do
    return False
    
def make_tree_then_carrot_opperation():
    plant(Entities.Tree)
    move(North)
    trade(Items.Carrot_Seed)
    plant(Entities.Carrots)
    