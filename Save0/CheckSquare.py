

# def check_region_has_type(pattern, position, type, x_dim, y_dim):
#     ## Checks to see if we can build the pattern from the current square
#     ## RETURNS: True if pattern fits from this tile up and right    
#     for i in range(0,x_dim):
#         for j in range(0,y_dim):
#             if (get_grid_info(position[0]+i, position[1]+j) != pattern[i][j] and get_grid_info(position[0]+i, position[1]+j) != 0):
#                 return False
#     return True
     
     

 def check_region_has_type(pattern, position, type, x_dim, y_dim):
     ## Checks to see if we can build the pattern from the current square
     ## RETURNS: True if pattern fits from this tile up and right  
     
     # Check if region bounds exceed farm
     if (position[0]+x_dim >= get_world_size()):
         return False
     if (position[1]+y_dim >= get_world_size()):
         return False
     
     # Check to see if the pattern is valid in the grid      
     for i in range(0,x_dim):
         for j in range(0,y_dim):
             if (get_grid_info(position[0]+i, position[1]+j) != 0):
                 return False
     return True