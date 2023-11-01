#!/usr/bin/python3

x = 'a'
while x <= 'z':
    if x != 'q' and x != 'e':
        print("{}".format((x)), end='')
    x = ord(x) + 1
    x = chr(x)
