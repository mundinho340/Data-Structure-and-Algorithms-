card =[]
def locate_number (cards, query):
    position = 0
    
    while position < len(cards):
        if cards[position] == query:
            return 1
            position +=1
    return -1
        
print (locate_number(card, 4))