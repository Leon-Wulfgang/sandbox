# each child has to know all children of its parent's sibling

class Node(object):
    def __init__(self, name, children=[], right=None):
        self.name = name
        self.children = children
        self.right = right

    def __str__(self):
        return 'Name:%s Children: %s  Right: %s' % (self.name, self.children, self.right)

n6 = Node('n6')
n5 = Node('n5')
n4 = Node('n4')

n3 = Node('n3', [n6])
n2 = Node('n2')
n1 = Node('n1', [n4, n5])

n0 = Node('n0', [n1, n2, n3])


def get_siblings(child, siblings, parent_siblings):
    no_self_siblings = []

    # exclude self
    for s in siblings:
        if s != child:
            no_self_siblings.append(s)

    # get child of parent's sibling
    for parent_sibling in parent_siblings:
        for child in parent_sibling.children:
            no_self_siblings.append(child)

    return no_self_siblings

# get the right of the node
def get_right(n, siblings):

    #print('\n', n)
    #for s in siblings:
        #print(s)
    #print('\n')

    right = None

    for i in range(len(siblings)-1):
        print(n.name, siblings[i].name)
        n.right = siblings[i+1]
        #if n == siblings[i]:
            #print(n, siblings[i])
            #right = siblings[i+1]

    #if siblings:
        #return siblings[0]
    #else:
        #return None
    return right

# node and its siblings
def mark_right(n, siblings=[]):

    # not bottom
    if n.children:
        # apply to each child
        for child in n.children:
            # with child's exclusive siblings
            mark_right(child, get_siblings(child, n.children, siblings))

            if siblings:
                n.right = siblings[0]

            print('\n')
            print(n.name)
            for s in siblings:
                print(s.name)
            print('\n')
    else:
        #n.right = get_right(n, siblings)
        print('\n')
        print(n.name)
        for s in siblings:
            print(s.name)
        print('\n')
        return

# root has no siblings
mark_right(n0)


print(n0, '\n', n1, '\n', n2, '\n', n3, '\n', n4, '\n', n5, '\n', n6)
