# when using space is ok


def sort(array=[54, 26, 93, 17, 77, 31, 44, 55, 20]):
    # left of pivot, smaller
    less = []
    # pivot itself
    equal = []
    # right of pivot, greater
    greater = []

    # when array has only 1 element, return itself
    if len(array) > 1:
        # first ele as pivot
        pivot = array[0]

        # put small to less, pivot to pivot, greater to right
        for x in array:
            if x < pivot:
                less.append(x)
            if x > pivot:
                greater.append(x)

        # recursively sort left and right, combine with [pivot] as list
        return sort(less) + [pivot] + sort(greater)  # Just use the + operator to join lists

    # when array has only 1 element, return itself
    else:
        return array

print sort()