def zero_y_axis():
    # If y pos is closer to max, go up
    # If closer to 0 go down
    if (get_pos_y() > (y_max()/2)):
        # above half
        while(get_pos_y() != 0):
            move(North)
    else:
        # below half
        while(get_pos_y() != 0):
            move(South)
    
def zero_x_axis():
    # If x pos is closer to max, go up
    # If closer to 0 go down
    if (get_pos_x() > (x_max()/2)):
        # above half
        while(get_pos_x() != 0):
            move(East)
    else:
        # below half
        while(get_pos_x() != 0):
            move(West)

def home():
    zero_y_axis()
    zero_x_axis()
    
home()