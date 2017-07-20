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


# get smaller siblings
def get_siblings(node, all_siblings):
    idx_node = all_siblings.index(node)
    return all_siblings[idx_node+1:]


# node and its siblings
def mark_right(n, siblings=[]):
    print(n.name)
    for s in siblings:
        print('s:', s.name)

    if siblings:
        n.right = siblings[0]

    if n.children:
        for child in n.children:
            mark_right(child, get_siblings(child, n.children))

    else:
        return

# root has no siblings
mark_right(n0)


print(n0, '\n', n1, '\n', n2, '\n', n3, '\n', n4, '\n', n5, '\n', n6)
