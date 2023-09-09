data = [20, 19 , 15 , 12, 8 , 4, 2, 0]
query = 8

def locate_cards(cards, query):
    for i in range(len(cards)):
        if cards[i] == query :
            print (cards[i])
                       
locate_cards(data, query)
            
