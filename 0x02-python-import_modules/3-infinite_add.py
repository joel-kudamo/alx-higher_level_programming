#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    addition_int = 0
    for i in range(1, len(argv)):
        addition_int += int(argv[i])
    print("{}".format(addition_int))
