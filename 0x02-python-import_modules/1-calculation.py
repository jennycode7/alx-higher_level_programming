#!/usr/bin/python3

if _name__ == "__man__":
    from add_0 import add, sub, div, mul

a = 10
b = 5

print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
