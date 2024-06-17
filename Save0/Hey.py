while True:
    if (get_ground_type() == Grounds.Soil):
        till()
        
    
    if can_harvest():
        harvest()

    move(North)