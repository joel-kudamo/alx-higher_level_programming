#!/usr/bin/python3

for letter in range(97, 123):  # loop through the ASCII codes from 'a' to 'z' 
    if chr(letter) != 'e' and chr(letter) != 'q':  # check if letter is not 'e' or 'q'
        print("{}".format(chr(letter)),end="")  # print the result
