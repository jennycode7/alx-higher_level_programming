#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is not [[]]:
        for row in matrix:
            for x in range(len(row)):
                if x == len(row) - 1:
                    print("{:d}".format(row[x]), end='\n')
                else:
                    print("{:d} ".format(row[x]), end='')
                x += 1
