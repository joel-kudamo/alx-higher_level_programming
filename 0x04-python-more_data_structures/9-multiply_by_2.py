#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_diction = {}
    if a_dictionary:
        for key, value in a_dictionary.items():
            new_diction.update({key: value * 2})
    return new_diction
