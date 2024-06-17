
def main():
    while(True):
        # Col 1 allocation
        produce_hey_col()


        # Col 2 3 4 5 allocations
        #produce_tree_col()
        produce_tree_car_interlace_col()
        produce_tree_car_interlace_col()
        
        # col 6, 7 allocation
        #produce_carrot_col()
        produce_pumpkin_cols(2,2)
                
        # col 8
        produce_hey_col()
        

        
clear()
initialize()
main()