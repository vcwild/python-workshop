#!/usr/bin/python3

from sys import argv

def handle_arguments(args: list[str]) -> bool:
    """Handles the arguments passed to the program.

    Parameters:
        args: list[str] The list of arguments

    Return:
        bool Returns True if --help was requested, else False
    """
    for arg in args:
        match arg:
            case "--help" | "-h":
                print("This is a help message")
                return 0
            case "--version" | "-v":
                print("This is version 1.0")
                return 1
            case _:
                print("Hello, this is your first program!")
                return 2

    return False

def main() -> None:
    status = handle_arguments(argv)
    exit(status)

if __name__ == "__main__":
    main()
