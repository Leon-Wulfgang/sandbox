"""
Code
public class Node
{
    public Node[] Children;
    public Node Right;
}
Question
Each node represents an element of a tree and specifies a list of immediate children.
The 'Children' property lists all children (in order) but the 'Right' property is set to null.
Suppose you are given the root of a fully populated tree (i.e. a Node called RootNode).
Write code to set the 'Right' property so that each node is linked to its right sibling.
"""
# each child has to know all children of its parent's sibling
# recursively apply to each node with its righter siblings and its parent's siblings' children


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

root = Node('n0', [n1, n2, n3])


# get siblings to the right of current node
def get_siblings(node, all_siblings=[], parent_siblings=[]):

    # slice righter siblings
    idx_node = all_siblings.index(node)
    righter_siblings = all_siblings[idx_node+1:]

    # add cousins to righter siblings
    for uncle in parent_siblings:
        for cousin in uncle.children:
            righter_siblings.append(cousin)
    return righter_siblings


# node and its siblings
def mark_right(n, siblings=[]):

    # mark right for those have siblings to the first sibling
    if siblings:
        n.right = siblings[0]

    # apply for each of the children with their righter siblings
    if n.children:
        for child in n.children:
            mark_right(child, get_siblings(child, n.children, siblings))

    # bottom layer
    else:
        return


# main
mark_right(root)


print(root.name, root.right, '\n')
print(n1.name, n1.right, '\n')
print(n2.name, n2.right, '\n')
print(n3.name, n3.right, '\n')
print(n4.name, n4.right, '\n')
print(n5.name, n5.right, '\n')
print(n6.name, n6.right,)

