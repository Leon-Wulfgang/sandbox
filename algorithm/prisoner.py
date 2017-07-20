# https://www.hackerrank.com/challenges/save-the-prisoner
# A jail has prisoners, and each prisoner has a unique id number, ,
# ranging from to . There are sweets that must be distributed to the prisoners.
# The jailer decides the fairest way to do this is by sitting the prisoners down in a circle (ordered by ascending ),
# and then, starting with some random , distribute one candy at a time to each sequentially numbered prisoner until
# all candies are distributed. For example, if the jailer picks prisoner , then his distribution order would be
# until all sweets are distributed.
# But wait theres a catch the very last sweet is poisoned! Can you find and print the ID number of the last
# prisoner to receive a sweet so he can be warned?

# test cases
t = 1

# num of prisoners
n = 5

# num of candies
m = 2

# start prisoner id
s = 1

# draft
# 1 2 3 4 5
# 1
# 1 2=5+1 5%2 = 1 1+1 = 2
#   2
#   1 2@3  5%2 = 1  1+2=3

for _ in range(0, t):
    n = 5
    m = 2
    s = 1

    # if start from 1, id of last m
    start_one = m
    print 'start from one:', start_one

    # start from s, remove 1 from s
    start_s = start_one + s - 1
    print 'start from s:', start_s

    # go around
    # Consider the test case: 499999999 999999997 2
    # Here the output should be 499999999. So when we consider (s+m-1)%n; we get 999999998%499999999 which is zero.
    # There is a chance of getting zero when we use (s+m-1). To avoid zero as our answer (as we use 1-based indexing
    # here) we should use (s+m-2)%n +1 because even if (s+m-2) is zero, we still get index 1 as the output which is
    # the requirement of the problem(1 is considered as the starting index).
    round = ((start_s - 1) % n) + 1
    print round


