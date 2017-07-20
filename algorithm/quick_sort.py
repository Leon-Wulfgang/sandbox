# divide n conquer
# 1 first element pivot point
# 2 partition:  < pivot to left, > pivot to right
# 3 recursive on left of pivot and right of pivot


# recursive on left and right
def recursive_left_right(arr, first, last):
    if first > last:
        pass

    # divide current arr to left and right, return split point
    split = partition(arr, first, last)
    print 'final=', arr
    print 'split=', split, arr[split]

    # left
    recursive_left_right(arr, first, split-1)
    # right
    recursive_left_right(arr, split+1, last)


# < pivot to left, > pivot to right
def partition(arr, first, last):
    print 'partition:', arr, 'first:', first, 'last:', last

    # first as pivot
    pivot = arr[first]
    print 'pivot:', pivot

    # left start from pivot + 1
    left = first+1
    # right start from last
    right = last

    # start swaps
    while True:
        # when right cross left
        # swap pivot and right to end
        if right <= left:
            print 'left:', left, arr[left], 'right:', right, arr[right]
            arr[first], arr[right] = arr[right], arr[first]
            print 'part-done:', arr
            break

        else:# otherwise, find left> and right< then swap
            # find a element > pivot from left, left cannot cross right
            while True:
                if arr[left] > pivot:
                    print 'found left>pivot:', left, arr[left]
                    break
                else:
                    if left >= right:
                        break
                    left += 1

            # find a element > pivot from right , right can cross left
            while True:
                if arr[right] < pivot:
                    print 'fount right<pivot:', right, arr[right]
                    break
                else:
                    if right < left:
                        break
                    right -= 1

            # swap left and right if left not crossing right
            if right < left:
                continue
            arr[left], arr[right] = arr[right], arr[left]
            print arr

    return right

# unsorted
a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print 'original=', a

# init recursive on whole arr
recursive_left_right(a, 0, len(a)-1)

