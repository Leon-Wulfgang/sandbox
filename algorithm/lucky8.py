#!/bin/python3
"""
https://www.hackerrank.com/contests/w28/challenges/lucky-number-eight
Given an -digit positive integer, count and print the number of multiples of  that can be formed
by concatenating subsequences of the given number's digits, modulo .
Sample Input 0
3
968
Sample Output 0
3
"""
from itertools import combinations

# n = int(input().strip())
# number = input().strip()
# your code goes here


def get_the_thing(current_iter):
    length = len(current_iter)
    count = 0
    for j in range(1, length+1):
        curr_combs = combinations(current_iter, j)
        for d in curr_combs:
            num = int(''.join(list(map(str, list(d)))))
            if num % 8 == 0:
                count += 1
            print(num, num % 8)
    return count

n = 3
number = 800
#number = 968


arr_number = list(map(int, list(str(number))))
'''
count_total = 0
for i in range(len(arr_number)-1, -1, -1):
    current_dig = arr_number[i]
    if current_dig % 8 == 0:
        # do its thing
        current_iter = arr_number[:i]
        count_total += get_the_thing(current_dig, current_iter)
'''
count_total = get_the_thing(arr_number)
print(n, number, arr_number, count_total)

"""
from right to left
if pointer %8, do its appending
else move to left

9
6
8

968
96
8

--

88
8
8
88

--

800
8
0
0
80
80
00
800

"""
