def traverse_column(function, max, moves=1, offset=1):
    # Ensure base position for looping with offset
    zero_y_axis()
    
    # Will move offfset quantity
    for i in range(0, offset):
        move(North)
    
    # Will perform a function call evey mvoes rows
    #for i in range(0, max):
    #    if not function():
    #        break
    #    for j in range(0,moves):
    #        move(North)
    
    # Move number of times specified by moves
    iterate = max
    while (iterate > 0):
        if not function():
            break
        for j in range(0, moves):
            move(North)
            iterate = iterate - 1
        