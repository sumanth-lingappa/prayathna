

def binary_search(array, n):
    mid = len(array)/2

    if len(array):
        if array[mid] == n: 
            print 'Found {} at index {}'.format(n, mid)
            return
    
        if array[mid] < n: binary_search(array[mid+1:], n)
        else: binary_search(array[:mid-1], n)
    else:
        print 'Not found'
    

input_array = [1,3,5,7,9,11,33,67,89]

binary_search(input_array, 10)
