#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for elmnt in r:
            print("{:d}".format(elmnt), end=" ")
        print()
