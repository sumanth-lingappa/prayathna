'''
6->3->4->2->1
'''

import node

nodeA = node.Node(6) #head
nodeB = node.Node(3)
nodeC = node.Node(4)
nodeD = node.Node(2)
nodeE = node.Node(1)


nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

numberOfNodes = node.countNodes(nodeA)

print "Number of nodes is {}".format(numberOfNodes)