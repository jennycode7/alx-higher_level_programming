#!/usr/bin/python3


import sys


def main():
    """ for command lne arguments """
    """for  sys """
    num = len(sys.argv) - 1
    y = 1

    if num == 1:
        print("{} argument:".format(num))
    elif num == 0:
        print("{} arguments.".format(num))
    else:
        print("{} arguments:".format(num))

    for str in sys.argv[1:]:
        print("{}: {}".format(y, str))
        y += 1


if __name__ == "__main__":
    """ man entry """

    main()
