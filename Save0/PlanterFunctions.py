
def do_hay():
    if can_harvest():
        harvest()
    plant(Entities.Grass)
    
def do_carrot():
    if can_harvest():
        harvest()
    trade(Items.Carrot_Seed)
    plant(Entities.Carrots)
    
def do_tree():
    if can_harvest():
        harvest()
    plant(Entities.Tree)
    
def do_pumpkin():
    trade(Items.Pumpkin_Seed)
    plant(Entities.Pumpkin)
    
def do_bush():
    if can_harvest():
        harvest()
    plant(Entities.Bush)