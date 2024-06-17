
## GETTERS ##
def x_max():
    return get_world_size()
    
def y_max():
    return get_world_size()
    
def max_hey():
    return y_max()
    
def max_wood():
    return y_max()
    
def max_carrot():
    return y_max()
    # Takes 1 hey
    # Takes 1 wood
    # We can not run out
    # Only make a 1 carrot for 3 wood and 3 hey
    #  a third of the least grown ingreedient (eventually this should be a function of yield and time)
    
    # A third max_hey
    #a = max_hey()
    #b = max_wood()
    #if (a < b):
    #    return a
    #else:
    #    return b
