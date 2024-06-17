
## Makes robot move according to a linear function
def linear_pattern():
    while(1):
        x = x_pos()
        xis(x+1)
        
        y = y_pos()
        yis(y+1)
## Traverse all tiles and call a function columnwise
def vertical_traverse_all_action(function):
    for x in range(0,get_world_size()):
        for y in range(0,get_world_size()):
            move_to((x,y))
            function()
            
## Traverse all tiles and call a function rowwise
def horizontal_traverse_all_action(function):
    for y in range(0,get_world_size()):
        for x in range(0,get_world_size()):
            move_to((x,y))
            function()               

def traverse_2d_action(fucntion, dim_x, dim_y):
    x_pos = x_pos()
    y_pos = y_pos()
    for y in range(0, dim_y):
        for x in range(0, dim_x):
            function()
            move_to((x_pos+x, y_pos+y))
            
def traverse_2d_plant(pattern):
    dims = get_pattern_dim(pattern)
    x_pos = x_pos()
    y_pos = y_pos()
    for x in range(0, dims[0]):
        for y in range(0, dims[1]):
            move_to((x_pos+x, y_pos+y))
            plantByType(pattern[x][y])

def traverse_2d_harvest(pattern):
    dims = get_pattern_dim(pattern)
    x_pos = x_pos()
    y_pos = y_pos()
    for x in range(0, dims[0]):
        for y in range(0, dims[1]):
            move_to((x_pos+x, y_pos+y))
            plantByType(0)            
        