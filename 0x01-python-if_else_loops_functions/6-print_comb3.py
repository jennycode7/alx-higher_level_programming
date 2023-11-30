#!/usr/bin/python3
for y in range(0, 100):
  if y / 10 < y % 10:
    print("{:02}".format(y), end=' ')
print()
