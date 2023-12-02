#!/usr/bin/python3
def remove_char_at(str, n):
    ptr = ''
    y = 0
    for x in str:
        if y != n:
            ptr += x
        y += 1
    return ''.join(ptr)
