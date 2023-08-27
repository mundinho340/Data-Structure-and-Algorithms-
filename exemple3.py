query =7
cards = [3,2,5,8]

def locate_number(card , queryy):
    position =0
    
    while True:
        if (card[position] == queryy):
            return position 
        
        position +=1
        
        if position == len(card):
            return -1
    
    
print(locate_number(cards, query))