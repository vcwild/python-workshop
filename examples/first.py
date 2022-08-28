#!/usr/bin/python3

from sys import argv

def show_msg():
    print("Hello, this is your first program!")

def show_help(args):
    for arg in args:
        if arg in "--help":
            show_msg()
            return True

    return False

def main():
    ask_for_help = show_help(argv)
    if not ask_for_help:
        print(argv)

if __name__ == "__main__":
    main()
