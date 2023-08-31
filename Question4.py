card =[6, 5, 4, 3, 2, 1, 0]
def locate_card(cards, query):
    lo, hi =0, len(cards) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]

        print('lo: ', lo, ", hi: ",hi, " mid:", mid,",  mid_number: ", mid_number)
        
        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid -1 
        elif mid_number > query:
            lo = mid + 1
        
print (locate_card(card, 2))