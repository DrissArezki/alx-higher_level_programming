#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ordn = list(a_dictionary.keys())
    list_ordn.sort()
    for i in list_ordn:
        print("{}: {}".format(i, a_dictionary.get(i)))
