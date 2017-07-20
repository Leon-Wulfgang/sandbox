#!/bin/python3
"""
https://www.hackerrank.com/contests/w28/challenges/the-great-xor
Given a long integer, , count the number of values of  satisfying the following conditions:

where  and  are long integers and  is the bitwise XOR operator.

You are given  queries, and each query is in the form of a long integer denoting . For each query,
print the total number of values of  satisfying the conditions above on a new line.

2   10
1   01

10  1010
1   0001
----
2   0010
3   0011
----
4   0100
5   0101
6   0110
7   0111

8   1000

"""

'''
q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    # your code goes here
'''

def find_number(x):
    bin_string_x = "{0:b}".format(x)
    length_bin_x = len(bin_string_x)
    one_less = (2 ** (length_bin_x - 1)) - 1
    #print(x, bin_string_x, length_bin_x, one_less, "{0:b}".format(one_less))
    c = 0
    for i in range(0,one_less+1):
        if i ^ x > x:
            c += 1
        #print(i)
    print(c)


find_number(2)
find_number(10)



