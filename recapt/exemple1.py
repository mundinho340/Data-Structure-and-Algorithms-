array = [9, 8, 6, 4, 3, 1]
query = 3


def location_number(cards, query) :
    left =0
    right = len(cards) -1
    while left <= right:
        mid = (left +right)// 2
        print(f"rigth=> {right} left=> {left} mid => {mid}" )
        if cards[mid] == query:
            return mid
        elif cards[mid]> query:
            left = mid +1
            
        else:
            right = mid-1
    return -1

print (location_number(array, query))