# You're having a cookie party tonight! You're expecting guests and you've already made cookies.
# You want to distribute all the cookies evenly between your guests in such a way that each
# guest receives the same number of whole cookies. If there are not enough cookies to give everyone the same amount,
# you must make some number of additional cookies.
# Given and , find and print the minimum number of additional cookies you must make
# so that everybody receives the same number of cookies.

n = 3
c = 2

n = 3
c = 5

# print c/n

# less than 1 per person
if c/n == 0:
    a = n - c
# more than 1 per person
else:
    # remainder
    if c % n == 0:
        a = 0
    else:
        i = c/n
        a = (i+1) * n - c

print a
