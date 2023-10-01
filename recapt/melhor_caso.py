array = [1, 2, 3,6, 7, 8, 9]
max =0
i=0

while True:
    print(max)
    if(array[i]> max):
        max = array[i]
    i+=1
    if(i>= len(array)) or array[i]<= max:
        break
    