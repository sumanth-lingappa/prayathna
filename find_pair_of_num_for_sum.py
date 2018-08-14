"""
Return pair of numbers from an array whose sum is the required number.
Eg. if array is [1,2,4,4] then the result pair is (4,4)
If no pair found, result "Not Found"


"""
REQ_SUM = 8
array = [1,2,4,4]

# case1 array given is sorted array
def findPair_sorted_recursive(array, req_sum):

    if array == []:
        print 'No pair found'
        return ()

    first = array[0]
    last = array[-1]
    # print 'first:last {}:{}'.format(first,last)


    if first+last == req_sum:
        pair = (first, last)
        print 'pair found {}'.format(pair)
        return pair

    if first+last < req_sum: findPair_sorted_recursive(array[1:], req_sum)
    else: findPair_sorted_recursive(array[:-2], req_sum)

def findPair_sorted_iterative(array, req_sum):
    low = 0
    high = len(array) - 1

    while low <= high:
        sum = array[low] + array[high]
        if sum == req_sum: return (array[low], array[high])
        elif sum < req_sum: low += 1
        else: high += 1
    print 'Not found'
    return ()



def findPair_unsorted(array, req_sum):
    """
    create a set that contains the complement of the numbers traversed so far and look for the rest of the
    array if the complement is present in the created set so far
    Eg. if array is [2,3,1,4,8] and sum is 7, then created set would be {5,4,6,3,-1}
    """
    def complement_of(n): return (req_sum - n)

    complementSet = set()

    for i in array:
        if complement_of(i) in complementSet: return (i, complement_of(i))
        complementSet.add(complement_of(i))
    print 'Not found'
    return ()


findPair_sorted_recursive(array, REQ_SUM)
print findPair_sorted_iterative(array, REQ_SUM)
print findPair_unsorted(array, REQ_SUM)

