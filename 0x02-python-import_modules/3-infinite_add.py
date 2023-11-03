#!/usr/bin/python3


import sys


def main():
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])

        print("{}".format(x + y))

    else:
        print("0")


if __name__ == "__main__":
    main()
