while True:
    if (get_ground_type() == Grounds.Turf):
        till()

    if can_harvest():
        harvest()
        trade(Items.Carrot_Seed)
        plant(Entities.Carrots)
    
    move(North)    
