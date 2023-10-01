array =[8, 4, 6,9, 3, 2,0,1]
list =[]
menor =0
i=0
left =0
right = len(array)

while i< len(array) :
    if menor >= array[i]:
        menor = array[i]
        list.append(menor)
    i+=1
print(list)