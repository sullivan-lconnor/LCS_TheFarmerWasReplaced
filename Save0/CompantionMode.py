#Initialize this in main as an event loop.  It will plant a grass then plant companions and harvest collissions forever

def companion_loop():
    info = get_companion()
    move_to(  list((info[1],info[2]))  )
    
    # REPLACE WITH DICTIONARY
    type = info[0]
    if type == Entities.Grass:
        plantByType(1)
    if type == Entities.Bush:
        plantByType(5)
    if type == Entities.Tree:
        plantByType(3)
    if type == Entities.Carrots:
        plantByType(2)
 
def spin_companion_mode():
    plantByType(1) # plant a grass
    while(1):
        companion_loop()

def smart_companion_mode():
    condition = num_items(Items.Carrot) < 10000
    if (num_items(Items.Carrot) < 10000):
        plantByType(1) # plant a grass
        while(num_items(Items.Carrot) < 10000):
            companion_loop()
            