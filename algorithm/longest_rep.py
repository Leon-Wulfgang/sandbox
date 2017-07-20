# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.


def longest_repetition(int_array):

    max_ele = None
    max_len = 0
    cur_ele = None
    cur_len = 0

    for element in int_array:
        if cur_ele != element:
            cur_ele = element
            cur_len = 1
        else:
            cur_len += 1

        if cur_len > max_len:
            max_len = cur_len
            max_ele = cur_ele

    return max_ele


def longest_repetition2(int_array):
    cur_long = list()
    cur = list()
    pre = None
    for int_element in int_array:

        # same, rem
        if int_element == pre:
            cur.append(int_element)
        # diff,
        else:
            # print(cur, cur_long)
            pre = int_element

            if len(cur) > len(cur_long):
                cur_long = cur
            cur = list()
            cur.append(int_element)

    # last
    if len(cur) > len(cur_long):
        cur_long = cur

    if len(cur_long) > 0:
        return cur_long[0]
    else:
        return None




# For example,

print(longest_repetition([2, 2, 3, 3, 3]))

print(longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]))
# 3

print(longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']))
# b

print(longest_repetition([1,2,3,4,5]))
# 1

print(longest_repetition([]))
# None

