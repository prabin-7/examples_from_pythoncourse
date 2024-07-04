colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet","purple"]
list_1 = []
for index,color in enumerate(colors):
    
    print(f'for {index} in colors we found {color}')
    my_tuple = (index,color)   #second mistake was writing 'colors' here 
    list_1.append(my_tuple)    # list_1 = yo gards bhayeko theyana 
                               #here the append fxn adds the tuple while /
                               #the extend fxn adds the elements as an individual element
                               #it generates list of tuples
print(list_1)