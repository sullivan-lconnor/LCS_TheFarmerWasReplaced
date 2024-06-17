# This function will take an even
# Number of rows to initialize

# We will have a plant row function
 #The function shall plant a tree every other move
# The function will take as argument an offest
   
def produce_tree_col():
    traverse_column(make_tree, y_max(), 2, 0)
    move(East)
    traverse_column(make_tree, y_max(), 2, 1)
    move(East)
    
def make_tree():
    if (get_entity_type() != Entities.Tree):
        # Initializer
        plant(Entities.Tree)
        return True
    
    if can_harvest():
        # Cycle the item
        harvest()
        plant(Entities.Tree)
        return True
    # Nothing to Do
    return False