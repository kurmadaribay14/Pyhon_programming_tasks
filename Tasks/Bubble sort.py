def bubbleSort(numsList):
    size = len(numsList)
    for i in range(0, size):
        j = size - 1
        while j > i :
            if numsList[j] < numsList[j - 1]:
                swap(numsList, j, j - 1)
            j = j - 1
print bubbleSort(j)
