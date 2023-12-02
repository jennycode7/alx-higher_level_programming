#!/usr/bin/env python3
for i in range(ord('z'), ord('a') - 1, -1):
    char = chr(i)
    if i % 2 == 0:
        print(char.lower(), end='')
    else:
        print(char.upper(), end='')
