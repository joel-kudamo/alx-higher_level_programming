#!/usr/bin/python3
from hidden_4 import *
if __name__ == "__main__":
    allfiles = dir()
    for i in range(0, len(allfiles)):
        if allfiles[i][:2] != "__":
            print("{:s}".format(allfiles[i]))
