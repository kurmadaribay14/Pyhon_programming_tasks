def func(array1,array2):
    array3=range(7)
    for i in range(len(array1)):
        array3[i]=array1[i]
    for i in range(len(array2)):
        array3[len(array2)+i]=array2[i]
    return array3
a=["Hello","world","calc"]
b=[3,"+",5]
print func(a,b)
