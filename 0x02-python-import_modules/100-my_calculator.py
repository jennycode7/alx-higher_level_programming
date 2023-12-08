#!/usr/bin/python3


import sys
import add_0


if __name__ == "__main__":
    def main():
        """
        Main function
        """
        num = len(sys.argv) - 1
        if num != 3:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            exit(1)
        else:
            if sys.argv[2] == '+':
                result = add_0.add(int(sys.argv[1]), int(sys.argv[3]))
                print("{} + {} = {}".format(sys.argv[1], sys.argv[3], result))
            elif sys.argv[2] == '-':
                result = add_0.sub(int(sys.argv[1]), int(sys.argv[3]))
                print("{} - {} = {}".format(sys.argv[1], sys.argv[3], result))
            elif sys.argv[2] == '*':
                result = add_0.mul(int(sys.argv[1]), int(sys.argv[3]))
                print("{} * {} = {}".format(sys.argv[1], sys.argv[3], result))
            elif sys.argv[2] == '/':
                result = add_0.div(int(sys.argv[1]), int(sys.argv[3]))
                print("{} / {} = {}".format(sys.argv[1], sys.argv[3], result))
            else:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)
main()
