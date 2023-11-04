#!/usr/bin/python3


import sys


def main():
    
    x = 0
    if len(sys.argv) > 1:
        for y in sys.argv[1:]:
            x += int(y)

        print("{}".format(x))

    else:
        print("0")


if __name__ == "__main__":
    main()
