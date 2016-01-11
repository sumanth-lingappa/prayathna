def findStep(sequence):
    first = sequence[0]
    second = sequence[1]
    third = sequence[2]

    step = min(abs(second - first), abs(third - second))

    if (second - first) < 0:
        step = -1 * step

    return step

def findMissing(seq):
    step = findStep(seq)
    start = 0
    end = len(seq) - 1
    middle = (end - start)/2
    missing = -1

    while start <= end:
        middle = start + (end - start)/2
        expected = seq[0] + step * middle
        if expected == seq[middle]:
            start = middle + 1
        else:
            end = middle - 1
            missing = expected

    # if no missing is found, then the missing element is the next item in the sequence
    if missing == -1:
        missing = seq[-1] + step
    return missing

if __name__ == '__main__':
    print findMissing([-5, 0, 5, 10, 15])

