
def merge_halves(array, left, right, mid):
    print array, left, right, mid
    left_array = array[0:mid]
    right_array = array[mid+1:right]

    nL = len(left_array)
    nR = len(right_array)

    i, j, k = 0, 0, 0

    while i < nL and j < nR:
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            k += 1
            i += 1
        else:
            array[k] = right_array[j]
            k += 1
            j += 1

        while i < nL:
            array[k] = left_array[i]
            k += 1
            i += 1

        while j < nR:
            array[k] = right_array[j]
            k += 1
            j += 1


def mergesort(array, left, right):
    if left >= right: return

    n = len(array)
    mid = (left+right)/2
    
    mergesort(array, left, mid)
    mergesort(array, mid+1, right)
    merge_halves(array, left, right, mid)




input = [9,8,-7,6,-5,4,3,-2,1]
l = 0
r = len(input) - 1
mergesort(input, l, r) 
print input
