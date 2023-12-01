#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if 'a' <= x <= 'z':
            print(chr(ord(x) - ord('a') + ord('A')), end='')
            continue
        print(x, end='')
    print()
