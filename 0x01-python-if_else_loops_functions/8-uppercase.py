#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if 'a' <= x <= 'z':
            x = chr(ord(x) - ord('a') + ord('A'))
            continue
        print("{}".format(x), end='')
    print()
