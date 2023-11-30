#!/usr/bin/python3
for y in range(0, 100):
    if y / 10 < y % 10:
        if y == 89:
            print("{:02}".format(y), end='\n')
            break
        print("{:02}, ".format(y), end='')
