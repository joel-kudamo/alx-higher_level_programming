#!/usr/bin/python3

"""Print alphabet in lowercase, not followed by a new line"""
for letter in range(97, 123): # ASCII values from 'a' to 'z'
    print("{}".format(chr(letter)), end="")
