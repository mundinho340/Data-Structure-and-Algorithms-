cards = [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
query =6

def test_location(cards, mid, query) :
    mid_number = cards[mid]
    print("mid: ", mid,", mid_number: ",mid_number)
    if mid_number == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return "left"
        else:
            return "found"  
    elif mid_number < query:
        return 'left'  
    else:
        return 'right'

def locate_card(cards, query):
    lo, hi = 0, len(cards) -1
    
    while lo <= hi:
        print ("lo: ", lo,", hi: ",hi)
        mid =(lo + hi) // 2
        result = test_location(cards, mid, query)
        
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid +1
    return -1


print(locate_card(cards, query))
