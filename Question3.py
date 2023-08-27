
def locate_number(card, query):
    #create the variable set value 0
    position =0
    # Set up a loop for repetition
    while True:
        if card[position] == query:
            return position
        
        position+=1
        
        if position == len(card):
             #Number not found , return -1
            return -1

        
    