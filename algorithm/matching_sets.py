# The first line contains a single integer, .
# The second line contains space-separated integers describing the respective values of set .
# The third line contains space-separated integers describing the respective values of set .
# Output Format
# Print a single integer denoting the minimum number of operations required to make set equal to set ;
# if no number of operations will ever make the two sets equal, print instead.

n = 3
x = [1, 2, 1, 2, 3, 3]
y = [-1, 4, 4, -1, 3, 3]

""" above is for input outside hackerRank editor """

sumx = sum(x)
sumy = sum(y)


if sumx != sumy:
    print -1
    exit()

# determine if they have the same sum
# print sumx, sumy

### removing dups in both arrays increased time-complexity by O(n), which is critical for large arrays, and caused time-out for test case#12
# remove elements exist in both
# ynew = []
# for e in y:
# if e in x:
# x.remove(e)
# else:
# ynew.append(e)
# y = ynew
# print x
# print y

x.sort()
y.sort()

# print x
# print y

""" cutting arrays in half caused bias on odd number of element arrays """
# x = x[0:len(x)/2]
# y = y[0:len(y)/2]

i = 0
# operation counts
c = 0
while i < len(x):

    ### calculating diffs significantly optimized the performance, passed all test cases
    # if diff exist
    if x[i] != y[i]:
        # diff in value between x[i] and y[i]
        diff_value = abs(x[i] - y[i])
        x[i] = y[i]
        c += diff_value

        # xi == yi increment i
    else:
        i += 1

# print x
# print y
print c / 2
