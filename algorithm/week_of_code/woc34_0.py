#!/bin/python3
"""
One day, Jack was going home by tram. When he got his ticket, he noticed that number on the ticket was not lucky.
A lucky ticket is a six-digit number on the ticket in which sum of the first three digits is equal to the sum of
the last three digits.
For example, number 165912 is lucky because sum of , and .
Since the number on the ticket wasn't lucky, Jack needs your help to find the next lucky ticket number.
For example, if Jack's ticket number is 165901, then the next lucky ticket number is 165903.
Given Jack's current ticket number, find and print the next lucky ticket number.

my solution:
increment digit until find a match, digit set to be 6, short enough to just increment
"""
import sys


def sum_dig(s):
    sum = 0
    for i in range(0, len(s)):
        sum += int(s[i])
    return sum


def is_lucky(x_str):
    upper = x_str[0:3]
    lower = x_str[3:]
    if sum_dig(upper) == sum_dig(lower):
        return True
    else:
        return False


def onceInATram(x):
    if is_lucky(str(x)):
        x += 1
    # Complete this function
    while not is_lucky(str(x)):
        x += 1
    return x

if __name__ == "__main__":
    #x = int(input().strip())
    x = 555555
    #x = 123456
    result = onceInATram(x)
    print(result)
