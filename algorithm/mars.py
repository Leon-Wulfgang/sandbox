#!/bin/python

"""
Sami's spaceship crashed on Mars! She sends sequential SOS messages to Earth for help.

[NASA_Mars_Rover.jpg]

Letters in some of the SOS messages are altered by cosmic radiation during transmission.
Given the signal received by Earth as a string, , determine how many letters of Sami's SOS have been changed by radiation.

"""

import sys

# the received
S = 'SOSSPSSQSSOR'

# the token of message
msg = 'SOS'

# length of the received message
length = len(S)

# the un-altered message should be
original = msg * (length/3)

# count of diff letters
count = 0

for i in range(0, length):
    if S[i] != original[i]:
        count += 1

print count