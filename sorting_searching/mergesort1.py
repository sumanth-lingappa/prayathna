

def merge(larray, rarray):
    result = []
    i, j = 0, 0
    while i < len(larray) and j < len(rarray):
        if larray[i] < rarray[j]:
            result.append(larray[i])
            i += 1
        else:
            result.append(rarray[i])
            j += 1

    while i < len(larray):
        result.append(larray[i])
        i += 1

    while j < len(rarray):
        result.append(rarray[j])
        j += 1

    return result


def mergesort(array):
    if len(array) < 2: 
        return array[:]
    else:
        mid = len(array)//2
        left = mergesort(array[:mid])
        right = mergesort(array[mid:])
        return merge(left, right)

input = [9,8,-7,6,-5,4,3,-2,1]
l = 0
r = len(input) - 1
print mergesort(input) 
print input

