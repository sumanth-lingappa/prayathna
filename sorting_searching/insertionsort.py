


def insertionsort(array):
    for i in range(1, len(array)):
        value = array[i]
        j = i - 1
        while j >= 0 and value < array[j]:
            array[j+1] = array[j]
            array[j] = value
            j -= 1

input = [9,8,-7,6,-5,4,3,-2,1]
l = 0
r = len(input) - 1
insertionsort(input) 
print input
