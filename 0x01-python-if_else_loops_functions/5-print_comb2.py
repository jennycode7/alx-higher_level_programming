#!/usr/bin/python3
for y in range(0, 100):
    if y == 99:
        print("{:02} ".format(y), end='')
        break
    print("{:02}, ".format(y), end='')
print()
