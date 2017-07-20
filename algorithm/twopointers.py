# remove -nth from LL
# 3 -> 4 -> 1 -> 6-> 2-> null


# node class
class Node(object):
    data = None
    nextNode = None

    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode


# print linkedlist
def printLL(head):
    curr = head
    while 1:
        print curr.data,
        if not curr.nextNode:
            break
        else:
            curr = curr.nextNode

# init LL
head = Node(3, Node(4, Node(1, Node(6, Node(2)))))
printLL(head)

# two pointers
ptrFirst = head
ptrSecond = head
# n th gap between 2 pointers
n = 2
# current iter count
i = 0
while 1:
    if not ptrSecond.nextNode:
        break
    else:
        ptrSecond = ptrSecond.nextNode
        i += 1
        if i > n:
            ptrFirst = ptrFirst.nextNode

print '\n', ptrFirst.data, ptrSecond.data
# remove -nth
ptrFirst.nextNode = ptrSecond
printLL(head)
