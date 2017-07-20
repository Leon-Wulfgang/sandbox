# A polygon is a closed shape with three or more sides. For example, triangles are polygons.
# A polygon is non-degenerate if it has no overlapping sides (and no sides of zero length).

# You have sticks with positive integer lengths, . You want to create a polygon using all sticks.
# Because this is not always possible, you can cut one or more sticks into two smaller sticks
# (they do not necessarily need to be of integer length) and repeat the process of trying to
# create a polygon using all the sticks. Given the lengths of all sticks, find and print the
# minimum number of cuts necessary to make a non-degenerate polygon.


# plan:
# to achieve polygon: longest_edge < sum(other_edges)

i1 = "3"
i2 = "3 4 5"
i2 = "1 2 3"
i2 = "1 1 1 1 1 1 1 10"


# determine if a poly exist
def is_poly(arr):
    longest_edge = max(arr)

    if longest_edge < (sum(arr) - longest_edge):
        return True
    else:
        return False


# cut the longest edge to 2 edges and return the new array
def chop_longest_edge(arr):
    longest_edge = max(arr)
    arr.remove(longest_edge)
    cut_edge = [longest_edge / 2, longest_edge / 2]
    arr = arr + cut_edge
    return arr

# init input
a = map(float, i2.split())
n_cut = 0

while not is_poly(a):
    print '1:', a
    a = chop_longest_edge(a)
    n_cut += 1
    print '2:', a, n_cut

print n_cut





