

def swap(array, x, y):
    array[x], array[y] = array[y], array[x]

def quicksort(array, left, right):
    if left >= right: return

    pivot = array[(left + right) / 2]
    index = partition(array, left, right, pivot)
    quicksort(array, left, index-1)
    quicksort(array, index , right)

def partition(array, left, right, pivot):
    print array, ' - ', pivot, left, right
    while left <= right:
        while array[left] < pivot: left += 1
        while array[right] > pivot: right -=1
        if left <= right:
            swap(array, left, right)
            left += 1
            right -= 1
    return left


input = [9,8,-7,6,-5,4,3,-2,1]
l = 0
r = len(input) - 1
quicksort(input, l, r) 
print input

