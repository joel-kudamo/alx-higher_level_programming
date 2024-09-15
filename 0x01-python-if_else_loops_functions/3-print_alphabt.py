#!/usr/bin/python3

for letter in range(97, 123):  # loop through the ASCII codes from 'a' to 'z'
    if letter != 101 and letter != 113:
        print("{}".format(chr(letter)), end="")  # print the result
