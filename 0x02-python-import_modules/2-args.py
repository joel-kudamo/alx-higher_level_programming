#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg_length = len(argv) - 1
    if arg_length < 1:
        print("{} arguments.".format(arg_length))
    elif arg_length == 1:
        print("{} argument:".format(arg_length))
    else:
        print("{} arguments:".format(arg_length))
    for num_of_args in range(arg_length):
        print("{}: {}".format(num_of_args + 1, argv[num_of_args + 1]))
