# Query the position number of card using number reference
query =5
cards = [3,2,5,8]


def locate_number(card , queryy):
    for i in range (len(card)):
        if(card[i] == queryy):
            return i

print (locate_number(cards, query))