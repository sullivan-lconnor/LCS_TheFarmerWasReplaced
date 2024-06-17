def visit_all_and_do(function):
    for i in range(0, x_max()):
        move(North)
        for j in range(0, y_max()):
            function()
            move(East)
            
def something():
    pass
visit_all_and_do(something)