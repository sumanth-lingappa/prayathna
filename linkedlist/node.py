

class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data


def countNodes(head):
    count = 1
    while head.next is not None:
        count += 1
        head = head.next
    return count

def findMiddle(head):
    middle = head.data

